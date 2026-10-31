#!/usr/bin/env python3
"""Portable local UX record tools. Python >=3.10; standard library only.

Validates the bundled schema subset plus traceability rules. It does not certify
UX, research integrity, accessibility, or the truth of referenced evidence.
No network, subprocesses, credentials, repository mutation, or model calls.
"""
from __future__ import annotations
import argparse
import datetime as dt
import html
import json
import math
from pathlib import Path
import re
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
MAX_BYTES = 5 * 1024 * 1024
ALLOWED_SCHEMA_KEYS = {'$schema','$id','title','type','const','enum','properties','required','additionalProperties','items','minItems','minLength','minimum'}
SUPPORT = {'implementation': {'source','runtime'}, 'visual': {'render'}, 'interaction': {'runtime'}, 'human': {'participant','analytics'}, 'data': {'analytics','runtime'}}


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    with path.open('rb') as file:
        data = file.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError('The file exceeds the 5 MiB limit.')
    def bad_constant(value: str) -> None:
        raise ValueError(f'Non-finite JSON number: {value}')
    return json.loads(data.decode('utf-8-sig'), object_pairs_hook=_pairs, parse_constant=bad_constant)


def _type(value: Any, wanted: str) -> bool:
    if wanted == 'null': return value is None
    if wanted == 'boolean': return type(value) is bool
    if wanted == 'integer': return type(value) is int
    if wanted == 'number': return type(value) is int or (type(value) is float and math.isfinite(value))
    if wanted == 'string': return isinstance(value,str)
    if wanted == 'array': return isinstance(value,list)
    if wanted == 'object': return isinstance(value,dict)
    raise ValueError(f'Unsupported schema type: {wanted}')


def check_schema(schema: dict[str, Any]) -> None:
    """Fail closed: this is a deliberately bounded validator, not general JSON Schema."""
    extra = set(schema) - ALLOWED_SCHEMA_KEYS
    if extra: raise ValueError(f'Unsupported schema keyword: {sorted(extra)}')
    for child in schema.get('properties',{}).values(): check_schema(child)
    if 'items' in schema: check_schema(schema['items'])


def shape_errors(value: Any, schema: dict[str, Any], at: str = '$') -> list[str]:
    errors: list[str] = []
    types = schema.get('type', [])
    if isinstance(types,str): types = [types]
    if types and not any(_type(value,t) for t in types):
        return [f'{at}: invalid type; expected {types}']
    if 'const' in schema and value != schema['const']: errors.append(f'{at}: value differs from the constant')
    if 'enum' in schema and value not in schema['enum']: errors.append(f'{at}: value outside the enum')
    if isinstance(value,str) and len(value.strip()) < schema.get('minLength',0): errors.append(f'{at}: empty text')
    if type(value) in (int,float) and 'minimum' in schema and value < schema['minimum']: errors.append(f'{at}: value below the minimum')
    if isinstance(value,list):
        if len(value)<schema.get('minItems',0): errors.append(f'{at}: missing items')
        for i,v in enumerate(value): errors += shape_errors(v,schema['items'],f'{at}[{i}]')
    if isinstance(value,dict):
        for k in schema.get('required',[]):
            if k not in value: errors.append(f'{at}: missing {k}')
        props = schema.get('properties',{})
        for k,v in value.items():
            if k in props: errors += shape_errors(v,props[k],f'{at}.{k}')
            elif schema.get('additionalProperties') is False: errors.append(f'{at}: unknown field {k}')
    return errors


def _date(value: str) -> bool:
    try:
        return dt.date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def validate(report: Any) -> list[str]:
    schema = load_json(ASSETS/'report.schema.json')
    check_schema(schema)
    errors = shape_errors(report,schema)
    if errors: return errors
    evidence = {e['id']:e for e in report['evidence']}
    principles = {p['id'] for p in load_json(ASSETS/'principles.json')['principles']}
    sources = {s['id'] for s in load_json(ASSETS/'sources.json')['sources']}
    for collection in ['evidence','coverage','findings','metrics','decisions','additional_sources']:
        found: set[str] = set()
        for item in report[collection]:
            if item['id'] in found: errors.append(f'{collection}: duplicate ID {item["id"]}')
            found.add(item['id'])
    for source in report['additional_sources']:
        if source['id'] in sources: errors.append(f'Additional source collides: {source["id"]}')
        sources.add(source['id'])
        if not source['url'].startswith(('https://','http://')): errors.append(f'{source["id"]}: invalid source URL')
        if not _date(source['reviewed_on']): errors.append(f'{source["id"]}: invalid review date')
    if not _date(report['session']['created_on']): errors.append('session.created_on: invalid ISO date')
    for item in report['evidence']:
        if not _date(item['observed_on']): errors.append(f'{item["id"]}: invalid evidence date')
    def refs(item: dict[str,Any],field: str,known: set[str] | dict[str,Any]) -> None:
        for ref in item[field]:
            if ref not in known: errors.append(f'{item["id"]}: unknown reference in {field}: {ref}')
        if len(set(item[field])) != len(item[field]): errors.append(f'{item["id"]}: duplicate references in {field}')
    def supports(item: dict[str,Any], field: str) -> bool:
        kinds = {evidence[r]['kind'] for r in item[field] if r in evidence}
        return bool(kinds & SUPPORT[item['claim_kind']])
    for c in report['coverage']:
        refs(c,'evidence_ids',evidence)
        if c['status'] in ('passed','failed') and not supports(c,'evidence_ids'):
            errors.append(f'{c["id"]}: status {c["status"]} without evidence compatible with {c["claim_kind"]}')
    for f in report['findings']:
        for field in ['evidence_ids','verification_evidence_ids']: refs(f,field,evidence)
        refs(f,'principle_ids',principles); refs(f,'source_ids',sources)
        if f['classification']=='observed' and not supports(f,'evidence_ids'):
            errors.append(f'{f["id"]}: observation without compatible evidence; use inference/hypothesis or provide proof')
        if f['classification']=='inferred' and not f['evidence_ids']:
            errors.append(f'{f["id"]}: inference without starting evidence')
        if f['status'] in ('verified','dismissed'):
            if not f['resolution'].strip(): errors.append(f'{f["id"]}: missing resolution')
            if not supports(f,'verification_evidence_ids'): errors.append(f'{f["id"]}: resolution without compatible proof')
    for m in report['metrics']:
        refs(m,'evidence_ids',evidence)
        if m['status']=='measured':
            kinds={evidence[r]['kind'] for r in m['evidence_ids'] if r in evidence}
            wanted={'participant','analytics'} if m['kind']=='human' else {'runtime','analytics'}
            if not kinds & wanted: errors.append(f'{m["id"]}: measured metric without compatible evidence')
            if m['result'] is None or m['sample_size'] is None: errors.append(f'{m["id"]}: missing result or sample')
            if m['comparison'] and m['baseline'] is None: errors.append(f'{m["id"]}: comparison without baseline')
        elif m['result'] is not None or m['sample_size'] is not None:
            errors.append(f'{m["id"]}: plan with results/sample already declared; separate plan and measurement')
        if m['baseline'] is not None:
            kinds={evidence[r]['kind'] for r in m['evidence_ids'] if r in evidence}
            wanted={'participant','analytics'} if m['kind']=='human' else {'runtime','analytics'}
            if not kinds & wanted: errors.append(f'{m["id"]}: baseline without compatible evidence')
    if report['conclusion']['status']=='verified-in-scope':
        if not any(c['status']=='passed' for c in report['coverage']): errors.append('Verified conclusion without passed coverage')
        if any(c['status'] in ('unknown','failed') for c in report['coverage']): errors.append('Verified conclusion with unknown or failed coverage')
        if any(f['severity'] in ('P0','P1') and f['status'] not in ('verified','dismissed') for f in report['findings']):
            errors.append('Verified conclusion with unresolved P0/P1')
    return errors


def encode(value: Any) -> str:
    return json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n'


def new_output(path: Path) -> Path:
    path=path.expanduser().resolve()
    if path == ROOT or ROOT in path.parents: raise ValueError('Write outside the installable skill folder.')
    path.mkdir(parents=True,exist_ok=False)
    return path


def init_report(project: str, scope: str, mode: str) -> dict[str,Any]:
    return {'schema_version':'1.0','session':{'id':'ux-session','project':project,'scope':scope,'mode':mode,'language':'en','created_on':dt.date.today().isoformat(),'authorized_changes':'To be defined; this scaffold does not grant change authority.','limitations':['No product inspection; complete the evidence before issuing conclusions.']},'conclusion':{'status':'draft','summary':'Initial record; no findings and no product validation.'},'evidence':[],'coverage':[{'id':'C-01','dimension':'Main task','claim_kind':'interaction','scope':scope,'status':'unknown','reason':'Not inspected yet','evidence_ids':[]}],'findings':[],'metrics':[],'decisions':[],'additional_sources':[]}


def render(report: dict[str,Any], out: Path) -> None:
    errors=validate(report)
    if errors: raise ValueError('Invalid record:\n'+'\n'.join(errors))
    dest=new_output(out)
    # One manifest; both views preserve every field, including unknowns and limitations.
    (dest/'report.json').write_text(encode(report),encoding='utf-8')
    md=['# Experience Design — report', '', '> Contract validation, not UX certification. Evidence and limits are part of the result.', '']
    sections=[]
    for name,content in report.items():
        if name=='schema_version': continue
        data=encode(content)
        fence='`'*max(3,max((len(m.group(0))+1 for m in re.finditer(r'`+',data)),default=3))
        md += ['## '+name, '',fence+'json',data.rstrip(),fence,'']
        sections.append(f'<section><h2>{html.escape(name)}</h2><pre>{html.escape(data)}</pre></section>')
    (dest/'report.md').write_text('\n'.join(md),encoding='utf-8')
    document='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Experience Design — report</title><style>body{margin:0 auto;padding:32px;max-width:1050px;font:16px/1.6 system-ui;background:#f6f5f1;color:#202321}h1{font-size:clamp(28px,5vw,52px);letter-spacing:-.04em}h2{font-size:20px}section{border-top:1px solid #b5b8ae;padding:16px 0}pre{font:13px/1.6 ui-monospace,monospace;white-space:pre-wrap;overflow-wrap:anywhere}aside{padding:18px;border:1px solid #b5b8ae}a{color:inherit}@media print{body{padding:0}section{break-inside:avoid}}</style><main><h1>Experience Design</h1><aside>This document keeps the complete record. Contract validity does not certify UX, research, or accessibility.</aside>'''+''.join(sections)+'</main></html>'
    (dest/'report.html').write_text(document,encoding='utf-8')


def doctor() -> dict[str,Any]:
    errors=[]
    cards=load_json(ASSETS/'principles.json')['principles']
    sources=load_json(ASSETS/'sources.json')['sources']
    sids={s['id'] for s in sources}
    if len(sids)!=len(sources): errors.append('Duplicate source IDs')
    if len({c['id'] for c in cards})!=len(cards): errors.append('Duplicate entry IDs')
    for c in cards:
        for field in ['id','title','family','evidence_kind','claim','when','action','avoid','boundary','test']:
            if not isinstance(c.get(field),str) or not c[field].strip(): errors.append(f'{c.get("id")}: invalid field {field}')
        if not c.get('sources'): errors.append(f'{c.get("id")}: no sources')
        for s in c.get('sources',[]):
            if s not in sids: errors.append(f'{c.get("id")}: unknown source {s}')
    check_schema(load_json(ASSETS/'report.schema.json'))
    errors += validate(load_json(ASSETS/'example-report.json'))
    # Check local Markdown links. Fragments are intentionally left to document QA.
    for p in ROOT.rglob('*.md'):
        for ref in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8-sig')):
            if '://' in ref or ref.startswith('#'): continue
            ref=ref.split('#')[0]
            if not (p.parent/ref).exists(): errors.append(f'{p.relative_to(ROOT)}: missing link target {ref}')
    return {'contract_valid':not errors,'principles':len(cards),'sources':len(sources),'errors':errors,'limit':'Does not evaluate agent effectiveness or the UX of a product.'}


def main(argv: list[str] | None=None) -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    sub=ap.add_subparsers(dest='command',required=True)
    p=sub.add_parser('init',help='Create an initial record in a new directory, outside the skill')
    p.add_argument('--out',type=Path,required=True);p.add_argument('--project',required=True);p.add_argument('--scope',required=True)
    p.add_argument('--mode',choices=['assess','design','experiment','verify','apply'],default='assess')
    p=sub.add_parser('validate',help='Validate the contract and claim consistency, not the truth of the evidence');p.add_argument('report',type=Path)
    p=sub.add_parser('render',help='Derive complete JSON, Markdown, and HTML without overwriting');p.add_argument('report',type=Path);p.add_argument('--out',type=Path,required=True)
    p=sub.add_parser('lookup',help='Look up entries by text and/or family');p.add_argument('term',nargs='?',default='');p.add_argument('--family',default='')
    sub.add_parser('doctor',help='Check data integrity and local links')
    args=ap.parse_args(argv)
    try:
        if args.command=='init':
            report=init_report(args.project,args.scope,args.mode)
            errors=validate(report)
            if errors: raise ValueError('\n'.join(errors))
            dest=new_output(args.out)
            (dest/'report.json').write_text(encode(report),encoding='utf-8')
            print(encode({'created':str(dest/'report.json'),'authority':'Does not change the product or grant permissions.'}),end='')
        elif args.command=='validate':
            report=load_json(args.report);errors=validate(report)
            print(encode({'contract_valid':not errors,'errors':errors,'limit':'Structural validity and declared traceability. Does not certify the product or verify the existence/truth of evidence.'}),end='')
            return 1 if errors else 0
        elif args.command=='render':
            render(load_json(args.report),args.out)
            print(encode({'created':str(args.out.resolve()),'files':['report.json','report.md','report.html']}),end='')
        elif args.command=='lookup':
            cards=load_json(ASSETS/'principles.json')['principles']
            selected=[c for c in cards if args.term.casefold() in json.dumps(c,ensure_ascii=False).casefold() and args.family.casefold() in c['family'].casefold()]
            print(encode({'count':len(selected),'principles':selected}),end='')
        elif args.command=='doctor':
            result=doctor();print(encode(result),end='');return 0 if result['contract_valid'] else 1
        return 0
    except (ValueError,OSError,RecursionError) as exc:
        print(encode({'error':str(exc),'changed_product':False}),file=sys.stderr,end='')
        return 2

if __name__=='__main__':
    raise SystemExit(main())

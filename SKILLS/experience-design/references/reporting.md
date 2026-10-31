# Reports and utilities

## One source of truth

When the deliverable requires a durable report, `report.json` is canonical and follows `assets/report.schema.json`. A one-off question can be resolved in chat without creating files. Do not write different conclusions in HTML and Markdown. The helper keeps all fields and limitations; an editorial presentation can be added, but it does not replace the record.

Fields: session/authority; conclusion; evidence; coverage; findings; metrics; decisions; additional sources. Each observation has an ID. Separate severity, confidence, reach, and test. Classify observation/inference/hypothesis. Record the sources of the argument and the product artifacts separately.

`verified-in-scope` only expresses verification of claims declared within a scope; it is not certification, a global absence of defects, or population effectiveness. Do not use it with unknown/failed coverage or open P0/P1 risks. A design can conclude as `proposed` and be correctly delivered.

## Optional helper

Python 3.10 or later; standard library only, with no installs, network, subprocesses, telemetry, or model calls. Resolve `<skill-root>` to the real installed folder. Run `python <skill-root>/scripts/ux.py --help` for the exact interface.

Commands: `init` creates an unknown/draft record; `lookup` filters entries; `validate` checks structure and consistency; `render` generates JSON/Markdown/HTML from the record; `doctor` checks data and links. `init` and `render` require a new output directory outside the skill; they do not overwrite. See `assets/example-report.json` for a synthetic example and `--help` for the exact arguments.

The JSON format uses YYYY-MM-DD dates and rejects duplicate keys, NaN/Infinity, unknown fields, and files larger than 5 MiB. The validator implements only the subset of the included schema; it is not presented as a general JSON Schema validator. It fails if the schema adds unsupported keywords.

## Deliberate limits

It does not check the existence, authenticity, or content of cited artifacts. It does not analyze whether a written observation is true. It does not detect every dark pattern or evaluate a design from code. It does not replace human inspection, product tests, or the ecosystem's canonical validation. A correctly declared reference can still be false: inspect it before making a claim.

The helper prevents some checkable contradictions: passed coverage without compatible evidence, a human observation based only on code or simulation, a measured result without sample/source, a comparison without baseline, unknown references, and a verified verdict with open P0/P1.

The included example is synthetic, with unknown coverage and planned metrics. Do not use its figures or hypotheses as product findings.

# Maintenance and the 2026–2027 horizon

## Stability by layers

Keep the process and contracts separate from standards, vendors, and examples. An entry keeps its ID; its text, source, and application condition can change with evidence. Do not present “2027” as a guarantee about future technology.

Before a decision that depends on a standard, format, client, or capability, consult the current official source and date the result. When there is no network, report the date and scope of what is available. An old article can still be useful; a new one does not gain rigor because of its date.

W3-WCAG22 is the consulted web normative reference. W3-WCAG3 stays under watch, not a conformance gate. SYS-TOKENS is a Community Group specification, not a W3C Recommendation. SYS-SKILLS describes the format; activation policies vary by client and are configured in adapters, not with invented fields in the core.

## Review when something material changes

Review the entry when contradictory evidence appears; the AI contract when actions/permissions change; accessibility when states or modalities change; performance when the journey or architecture changes; the handoff boundaries when the scope changes. Do a periodic review of standards and adapters as a maintenance practice, not as a promised automatic update.

A broken link is an access limitation, not a refutation of the idea. Look for a legitimate copy or the original work and keep provenance. Do not bypass paywalls, invent content, or replace studies with unlabeled commercial summaries.

## Evaluation before promotion

The candidate configures explicit activation in the included adapter to avoid conflicts with neighboring skills. `trigger_queries.json` contains **routing eligibility** cases, not proof of natural invocation with that policy disabled. Before enabling implicit invocation, test a real read of SKILL.md with non-leading prompts in a compatible client.

Compare a baseline without the skill against the candidate using identical inputs in a clean context. Separate development and holdout cases. Do not train to the exact wording of the prompts. Observe correctness, usefulness, overreach, evidence, cost, and regressions. Keep negative results and feedback from real users.

The structural review, the helper tests, and the HTML smoke test can pass while cognitive effectiveness remains unmeasured. Do not turn `candidate` into “final” just because files were generated.

## Publication

The installable distribution is the skill folder, self-contained. Keep historical research, build materials, and ecosystem audits outside it. Do not include secrets, plugin caches, or complete third-party content. Decide the license and the canonical repository with the owner before publishing.

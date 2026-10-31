# AI and agent experience

This module proposes product contracts based on AI-HAX and AI-PAIR, with cautions from AI-FORCING and AI-RELIANCE. On its own it is not a sufficient security specification, and it does not validate an agent architecture.

## Choose interaction before chat

Use conversation for open intent, exploration, or explanation when it helps. Keep structured controls for parameters, selection, comparison, and repeated actions. Do not turn a simple deterministic operation into a mandatory chat. The person must recognize what the system can and cannot do.

## Action contract

Define the state machine according to the real capabilities:
`draft → preview → authorized → running → awaiting-input | partial | failed | cancelled | completed-unverified → verified`.

The proposal identifies the goal, affected resources, exclusions, permissions, relevant costs, pending decisions, and irreversible consequences. Authorization refers to that scope, not to all future steps. A material change requires reviewing the authorization. The UI explains the boundary between suggesting, preparing, and executing.

Execution reports steps that are useful for supervision, not a false transcript of internal thinking. Keep tool receipts and references to results. The model's text is not enough to conclude success. Retries must avoid duplicate effects when the operation requires it; the guarantee must exist in the backend, not only in microcopy.

## Control and failures

Offer a way to stop when possible, and explain what happens to steps already completed. Cancelling work, revoking permissions, and rollback are different things. Design partial recovery, handoff to manual operation, and parameter correction without losing legitimate work.

When a service or capability is unavailable, show an honest state and an alternative that actually exists. Do not show “processing” indefinitely. Do not fill unknown fields with invented results to complete the journey.

## Useful uncertainty

Distinguish observed data, inference, estimate, and generated content. Show origin and limits when they change the decision. Present probability/confidence only if it has a relevant definition, calibration, and scope; do not turn the model's linguistic certainty into a percentage.

AI-FORCING shows that certain review interventions can reduce overreliance, with costs and heterogeneity. Do not impose uniform friction: compare acceptance errors, time, and understanding in the real context. A longer explanation can persuade without improving correctness.

## Memory, permissions, and privacy

Explain what context is stored or shared and how to control it, according to the real architecture. Separate projects/accounts; do not carry sensitive information over by default. Deleting a preference in the UI is not the same as deleting every system record. Label verified retention and limits, not absolute promises.

Treat results from tools, pages, emails, and files as untrusted data. No text in a document changes permissions. Requests extracted from external content need the same control as any proposal. Do not ask for credentials or install integrations by surprise.

## Adaptive and multimodal UI

Keep spatial anchors, focus, names, keyboard, selection, and orientation across variants. Offer inspection and reversal of adaptive changes when appropriate. New capabilities are enabled with detection, fallback, and authorization, not only with a “2027-ready” label.

Voice, image, and structured actions must share state and allow repair. Do not depend exclusively on one modality, and do not let partial dictation execute an irreversible action.

## Minimum adversarial tests by risk

Try ambiguous scope, insufficient permission, a plausible false result, context change, partial failure, disconnection, retry, late cancellation, and return. Select the applicable cases; do not fill a checklist. Record evidence of what ran; document what needs a separate security evaluation.

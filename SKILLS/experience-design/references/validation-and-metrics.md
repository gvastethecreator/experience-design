# UX validation and measurement

## Choose the right level

**Code:** implementation test or static rule. **Browser:** controls and transitions executed in an environment. **Render:** appearance in a declared viewport/state. **Participants:** understanding and observed behavior in a described sample. **Analytics/experiment:** instrumented metrics with an explicit comparison design.

None automatically absorbs the others. A Playwright test that walks through a flow does not prove that a person will discover it. An aesthetic preference does not prove productivity. One observed error does not justify extrapolating prevalence to the whole population.

## Goal, signal, metric

Use RES-HEART to guide the choice, not to force measuring all its dimensions. Our own example: goal “export the correct selection”; signal “the file matches the chosen items”; metric “share of tasks completed without an incorrect export”. Add a work-loss guardrail and a confidence/understanding measure when relevant.

Prefer outcome metrics: correct task, errors, help, justified abandonment, recovery, time to value, and perceived effort. Return or conversion can be relevant, but they must not reward compulsion, hidden costs, or defective consent. Fewer clicks is not success if errors increase.

## Comparison protocol

Fix the question, population, unit of analysis, baseline, variants, method, primary variable, guardrails, and decision criterion before observing results. Keep the task and data equivalent. Counterbalance the order when learning matters. Record exclusions, failures, help, and device conditions.

An A/B test needs reliable instrumentation, appropriate assignment, and sample/precision planning according to the effect of interest and the traffic. Do not invent a universal size. Avoid stopping at the first favorable result. If there is not enough evidence, report the uncertainty; “not significant” does not mean “they are equal”.

Without traffic or budget, a qualitative test can resolve ambiguities and detect harm. Do not turn it into a commercial improvement percentage. If participants are missing, leave the protocol prepared and the result unmeasured.

## AI experience

Measure not only acceptance but also incorrect acceptance, corrections, the ability to detect limits, and recovery of control. Segment by knowledge and risk when appropriate. A more convincing AI can increase satisfaction while worsening decisions; verify both.

## Tests of the skill itself

Distinguish three questions: does it activate where it should? Does it follow a good process? Does it improve results at a reasonable cost? Static fixtures only describe cases. For effectiveness, compare the same model/configuration/task/permissions, with and without the skill, in clean contexts. Keep outputs and traces; evaluate without showing the judge which one is the candidate. Do not include expected answers in the executor's context.

Use core cases, variations, edge cases, and holdout. Record quality, errors, undue scope, time, tokens, and human usefulness. A gain that triples the cost is a tradeoff, not a free success. Do not declare an improvement until that comparison runs. See the maintenance protocol and `evals/evals.json`.

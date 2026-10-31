# Performance and feedback

## Separate clocks

Measure at least what the claim needs: local response to input, first useful state, first useful output, actual completion, and recovery. Streaming, a spinner, or a skeleton does not prove task progress. The interaction can respond quickly while remote work legitimately takes time.

For the web, PERF-INP describes a good-responsiveness threshold of INP ≤200 ms at the 75th percentile of visits. It is not the 75th percentile of all interactions. PERF-VITALS includes LCP and CLS; as a reference, the good thresholds are LCP ≤2.5 s and CLS ≤0.1, measured in their context and segmentation. Verify the current definitions before instrumenting.

Do not reduce UX to these metrics. In editors, audio, video, canvas, or native tasks, continuity, cancellation, and the cost of errors also matter. Doherty's historical figure of 400 ms is not a universal boundary between usable and useless.

## Task budget

Define a realistic target with product, infrastructure, and users; do not invent one after measuring. Explain which part of the time the interface controls and which part depends on the process. Observe distributions and slow cases, not only the average on a powerful machine.

## Proportional feedback

Confirm that the action was received without claiming that it finished. With a real denominator, show count/progress. Without one, report the phase and the available controls. Estimates must be labeled and allow correction. Do not use fake percentages or artificial delays to manufacture confidence.

For long waits: keep the work, allow leaving/returning when supported, and notify only through an agreed channel. On failure, differentiate what did not start, what completed, and what needs a decision. On cancel, explain effects that may already have happened.

## Verification

Reproduce relevant network/device scenarios: slowdown, failures, and repetition. Record the measurement conditions. Synthetic tests detect technical regressions; perceived speed and journey success need adequate evidence. Do not publish a percentage gain without a comparable baseline.

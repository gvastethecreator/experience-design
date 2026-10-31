# Inclusive contract

## Standards and scope

Web reference baseline consulted on 2026-09-05: WCAG 2.2. Identify the applicable level and criteria from W3-WCAG22; these notes do not replace the normative text and are not a complete audit. The legally required level depends on the product and the jurisdiction; verify it specifically when needed.

Distinguish 2.5.8 AA (24×24 CSS px or its exceptions, including spacing) from 2.5.5 AAA (44×44 and exceptions). 2.4.11 AA prevents fully hidden focus; do not confuse it with enhanced requirements. 2.5.7 AA requires a pointer alternative without dragging where applicable: **a keyboard shortcut alone is not enough for that criterion**. See W3-TARGET, W3-FOCUS, and the standard.

Authentication, redundant entry, and consistent help need a specific review. Do not block pasting passwords or using password managers without a conforming reason and alternative. Verify the text and exceptions of the relevant criterion.

## Tests per task

Check name, role, state, and semantic relationships; focus order and restoration; use without a mouse; visible focus; identified errors; alternatives to gestures; relevant reading and zoom/reflow. Review dynamic content and status announcements without interrupting unnecessarily. Do not confuse visual order with accessible order.

A scanner provides bounded findings, not a conformance statement. Run manual checks in relevant states. If no screen reader is used, state that limitation. Do not simulate its result from ARIA attributes. Prefer suitable native HTML before adding redundant semantics.

## Access contexts

Long data, RTL, text enlargement, contrast, high-contrast mode, reduced motion, keyboard, touch, assistive technology, and slow network are included according to audience, changed behavior, and risk. Do not require every Cartesian combination for a minimal fix, and do not omit a core modality for convenience.

In canvas, visualizations, games, or editors, do not assume that the graphic representation is enough: define which tasks need a structured alternative and how selection, name, and state stay in sync. In audio/video or voice, plan alternatives suited to the information and the operation.

## Cognition

W3-COGA provides complementary guidance on understanding and use; it is a group note, not a WCAG certification. Apply clear language, context preservation, help, and recovery as verifiable hypotheses. Include relevant people in the research; do not build a synthetic “disabled persona” as a substitute.

## Horizon

WCAG 3 is still an incomplete draft according to W3-WCAG3. Keep it under watch; do not mark its proposals as current obligations or promise a timeline for 2027. Date each consultation and record changes that affect tests or contracts.

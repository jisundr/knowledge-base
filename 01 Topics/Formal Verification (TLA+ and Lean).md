---
type: topic
tags: [ai-engineering, verification, formal-methods, tla-plus, lean]
---

# Formal Verification (TLA+ and Lean)

Using mathematical models and proofs to show that a system's design invariants always hold, reserved for critical logic where edge-case bugs are costly.

- **TLA+**: specify a design and model-check it across all interleavings. SpaceXSI used it to check multi-device notification in its custom virtualization library, removing subtle rendering flicker.
- **Lean**: a proof assistant for machine-checked proofs.

Part of the top verification tier in the [[Agent Verification Stack]]; its output (a proof) is a reviewable artifact, which suits the "review artifacts, not code" approach.

## To research

- TLA+ and Lean in depth (from the source's follow-up notes).

## Related

- [[Statecharts and State Machines]]
- [[Inverse Pyramid of Constraints]]

## Sources

- [[All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI]]

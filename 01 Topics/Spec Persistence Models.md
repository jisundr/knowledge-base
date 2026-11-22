---
type: topic
tags: [sdlc, documentation, spec-driven-development]
---

# Spec Persistence Models

Four conventions for what happens to a feature's `spec.md` after delivery. Pick one explicitly as a team; task lists and proof logs are cleared under all four.

| Model | What happens | Best fit | Watch out for |
| --- | --- | --- | --- |
| **Flow-back** | Discoveries during coding are reconciled back into spec, plan, and tasks | Small, fast, collaborative teams | Silent drift when code changes without the spec |
| **Flow-forward** | Shipped spec folders are frozen; changes get a new folder that links back | Regulated or audit-heavy domains | Context spread over many folders |
| **Living spec** | `spec.md` is the permanent contract; change it first, then regenerate code, plan, tests | Stable platform APIs and domain boundaries | Losing low-level notes when derived files are regenerated |
| **Constitution-only** | Specs are retired after shipping; rules move to code and tests, principles to `constitution.md` | Fast product teams wanting a lean repo | Losing intent if no ADR captures the why |

Part of the [[Spec Exit Strategy]].

## Related

- [[Spec-Driven Development]]
- [[Architecture Decision Record (ADR)]]

## Sources

- [[20261122133225 Spec-Driven Development Exit Strategies - What to Retain, Merge, and Discard|Spec-Driven Development Exit Strategies - What to Retain, Merge, and Discard]]

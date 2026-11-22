---
type: topic
tags: [sdlc, documentation, verification, architecture]
---

# Durable Facts in Native Homes

Move each lasting system rule out of prose and into the artifact that enforces it, so CI fails when it breaks. A failing test halts a deploy; a stale paragraph in `docs/specs/` does not.

| Fact | Native home |
| --- | --- |
| API shapes and contracts | OpenAPI / AsyncAPI schemas, contract tests |
| Data invariants | Migrations, column constraints, domain validation |
| Security and authorization | Access policies, static analysis rules, allow/deny tests |
| Architectural boundaries | Module boundaries, dependency linting, architecture tests |
| Reliability expectations | SLOs, telemetry metrics, alert rules |
| Rationale and trade-offs | [[Architecture Decision Record (ADR)]] (the one non-executable home) |

Same idea as the [[Inverse Pyramid of Constraints]]: prefer deterministic enforcement over natural-language rules.

## Related

- [[Spec Exit Strategy]]
- [[Categorical Elimination of Anti-Patterns]]
- [[Agent Verification Stack]]

## Sources

- [[20261122133225 Spec-Driven Development Exit Strategies - What to Retain, Merge, and Discard|Spec-Driven Development Exit Strategies - What to Retain, Merge, and Discard]]

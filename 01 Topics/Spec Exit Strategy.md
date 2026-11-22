---
type: topic
tags: [ai-engineering, sdlc, documentation, spec-driven-development]
---

# Spec Exit Strategy

A deliberate plan for what happens to spec artifacts once a feature ships: what to keep, what to move into code, and what to delete. Without one, a [[Spec-Driven Development]] repo grows a "shadow codebase" of stale Markdown that drifts from the real system and wastes agent context.

Core principle: **code becomes the fact; specs are for the delta.** A spec earns its place while work is in flight, by fixing scope, trade-offs, and acceptance criteria for the gap between today and next. After shipping, most of it is scaffolding.

## Post-ship protocol

Run on every feature before merge, as a PR checklist item:

1. **Verify** the code against the acceptance evidence in the spec.
2. **Record** load-bearing decisions as an [[Architecture Decision Record (ADR)]]; skip if there were none.
3. **Promote** durable rules into executable homes; see [[Durable Facts in Native Homes]].
4. **Apply the retention policy** for the team's chosen [[Spec Persistence Models|persistence model]]: delete, freeze, or reconcile the spec, and always clear task lists and proof logs.

The failure it prevents is **decision documentation theater**: piles of prose that look like knowledge but no longer match the code. Terms are in [[SDLC Documentation Glossary]].

## Related

- [[Design Document Types]]
- [[Context Engineering]]
- [[Inverse Pyramid of Constraints]]

## Sources

- [[20261122133225 Spec-Driven Development Exit Strategies - What to Retain, Merge, and Discard|Spec-Driven Development Exit Strategies - What to Retain, Merge, and Discard]]

---
type: topic
tags: [ai-engineering, ai-agents, cost, automation]
---

# Agent Script Migration

Move repetitive, rule-based steps out of the model and into deterministic scripts. Every model call costs tokens on every run; a script costs almost nothing and gives the same result each time. Keep model calls for steps that need judgment or unstructured text reasoning.

In practice: once a bot routine is stable, find the steps whose logic never changes and replace them with code the bot calls, for example the `scripts/` folder of an [[Agent Skills|agent skill]].

## Related

- [[Agent Skills]]
- [[Inverse Pyramid of Constraints]]
- [[AI Control Plane]]
- [[LLM Routing]]

## Sources

- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

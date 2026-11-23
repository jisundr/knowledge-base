---
type: topic
tags: [ai-engineering, ai-agents, agent-design, governance]
---

# Agent Anti-Jobs

An explicit list, in the bot's onboarding prompt, of actions it is forbidden to take. Examples: "never send an external email without human approval", "never issue a refund over $100".

Anti-jobs mark the edge of a bot's scope. Enforce the high-stakes ones outside the prompt too, with tool permissions, [[Human-in-the-Loop Approval Gates]], and [[Deterministic Guardrail Policies]]; a prompt rule is a request, not a control (see [[Inverse Pyramid of Constraints]]).

## Related

- [[Agent Design Foundation]]
- [[Categorical Elimination of Anti-Patterns]]
- [[AI Work Autonomy Spectrum]]

## Sources

- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

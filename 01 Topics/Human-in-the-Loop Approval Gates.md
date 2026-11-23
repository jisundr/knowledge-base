---
type: topic
tags: [ai-engineering, ai-agents, governance, hitl]
---

# Human-in-the-Loop Approval Gates

A durable pause in an agent run that waits for a human to approve before a high-stakes action: changing a record, deleting data, spending money, or contacting outsiders. The request goes out through Slack, Teams, or a webhook, and the run resumes when someone answers.

Pair gates with an **append-only, event-sourced audit trail** so every reasoning step and approval can be replayed months later for a compliance audit.

## Related

- [[AI Work Autonomy Spectrum]]
- [[Agent Anti-Jobs]]
- [[AI Control Plane]]
- [[Request-Level Evidence Capture]]

## Sources

- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

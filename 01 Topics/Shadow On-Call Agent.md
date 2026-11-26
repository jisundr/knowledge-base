---
type: topic
tags: [incident-management, ai-agents, operations, on-call]
---

# Shadow On-Call Agent

An agent that receives every page before the human on-call engineer does.

1. **Noise gate**: it decides whether the alert is noise or real. Noise is dropped, so nobody is woken up for it.
2. **Head start**: if real, the page escalates to a human, and meanwhile the agent investigates logs and recent deploys and drafts a fix, often ready by the time the engineer is looking.

The human still owns the incident; the agent saves interrupt time and gives the responder a starting point. Same split as [[AI-Assisted Incident Investigation]]: AI does the legwork, humans decide.

## Related

- [[Blameless Post-Incident Review (PIR)]]
- [[Domain-Specialized Agent Fleet]]
- [[AI Work Autonomy Spectrum]]

## Sources

- [[20261126155209 How Anthropic Builds Software with AI Agents|How Anthropic Builds Software with AI Agents]]

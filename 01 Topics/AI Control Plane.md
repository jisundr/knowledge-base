---
type: topic
tags: [ai-engineering, ai-agents, governance, observability]
---

# AI Control Plane

A central layer that runs and governs a fleet of production agents: who may do what, what each agent did, and what it cost. It closes the *observability gap*: uptime monitoring says a service is up, but not that an agent gave a fluent wrong answer or burned money in a tool-call loop.

Three pillars:

1. **Observability**: see [[Four-Layer AI Observability]].
2. **Human approval and audit**: see [[Human-in-the-Loop Approval Gates]].
3. **Cost control**: see [[Agent Script Migration]].

Enterprise platforms ship it built in (the lesson names Boomi Agentstudio and Microsoft Copilot Studio among others); with code-first frameworks you build it yourself. See [[Agent Framework Altitude Tiers]].

## Related

- [[Domain-Specialized Agent Fleet]]
- [[Deterministic Guardrail Policies]]
- [[AI Evaluation System Pillars]]
- [[Request-Level Evidence Capture]]

## Sources

- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

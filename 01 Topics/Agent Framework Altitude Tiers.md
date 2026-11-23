---
type: topic
tags: [ai-engineering, ai-agents, frameworks, architecture]
---

# Agent Framework Altitude Tiers

Agent tools differ less by "best" than by altitude: how much of the stack they hand you.

| Tier | Examples | You get | You still build |
| --- | --- | --- | --- |
| 1. Low-level primitives | LangGraph, LlamaIndex Workflows, Pydantic AI | Graph engines, state, typed contracts, checkpoints | Governance, audit, dashboards, approval queues |
| 2. Developer frameworks | CrewAI, AutoGen, OpenAI Agents SDK, MetaGPT | Roles, tasks, crews, handoffs; fast prototyping | Hardening for SOC 2, HIPAA, data boundaries |
| 3. Enterprise platforms | Boomi Agentstudio, Microsoft Copilot Studio | Full runtime plus [[AI Control Plane]]: observability, audit logs, model routing, dev-test-prod releases | Little; you trade control of the loop internals |

Deciding question: do we want to spend engineering quarters building a control plane, or run the business on one?

## Related

- [[AI Control Plane]]
- [[Multi-Agent Orchestration Patterns]]
- [[Model and Harness Separation]]
- [[Harness Engineering]]

## Sources

- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

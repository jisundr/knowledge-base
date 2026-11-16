---
type: topic
tags: [ai-engineering, ai-agents]
---

# AI Agents and Tool Use

Moves AI systems from answering static questions to actively performing actions.

- A standard **workflow** has fixed steps (A -> B -> C).
- An **agent** dynamically chooses its next action, runs external tools, observes the results, and iterates through decision loops.

## Production use cases

- Analytical agents that query corporate databases and visualize complex datasets on demand.
- Developer acceleration: tools that help engineering teams ship production code faster.

## Multi-agent orchestration

An orchestrator agent routes tasks to specialist agents (requirements, testing, security, observability, etc.), each defined as a plain Markdown profile and connected to tools via [[Model Context Protocol (MCP)]]. See [[Agentic SDLC]].

## Related

- [[Retrieval-Augmented Generation (RAG)]]
- [[Agentic SDLC]]
- [[Model Context Protocol (MCP)]]
- [[Containerization and Orchestration]]
- [[Context Engineering]]
- [[Agent Memory]]
- [[AI Engineer Skill Stack]] (Tier 2)

## Sources

- [[Essential Skills for Becoming an AI Engineer - RAG, AI Agents & More]]
- [[17 agents, one SDLC - How Levi Strauss reimagined development on GitHub]]
- [[Lamis Mukta - Learning while you sleep - Beyond memory to dreaming - AI Native DevCon June 2026]]

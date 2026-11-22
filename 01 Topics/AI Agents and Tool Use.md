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

## Skills instead of more agents

Anthropic's thesis, now backed by wide adoption of the open standard: stop building a new custom agent per domain, and give one general-purpose agent [[Agent Skills]]. Domain know-how moves into skill folders; the agent loop is built once. Custom agents remain useful where you need isolated context, permissions, or product integration, so many teams frame it as agents *with* skills.

## Related

- [[Retrieval-Augmented Generation (RAG)]]
- [[Agentic SDLC]]
- [[Model Context Protocol (MCP)]]
- [[Containerization and Orchestration]]
- [[Context Engineering]]
- [[Agent Memory]]
- [[Agent Skills]]
- [[AI Engineer Skill Stack]] (Tier 2)

## Sources

- [[20261114221948 Essential Skills for Becoming an AI Engineer - RAG, AI Agents & More|Essential Skills for Becoming an AI Engineer - RAG, AI Agents & More]]
- [[20261115112636 17 agents, one SDLC - How Levi Strauss reimagined development on GitHub|17 agents, one SDLC - How Levi Strauss reimagined development on GitHub]]
- [[20261116203029 Lamis Mukta - Learning while you sleep - Beyond memory to dreaming - AI Native DevCon June 2026|Lamis Mukta - Learning while you sleep - Beyond memory to dreaming - AI Native DevCon June 2026]]
- [[20261122181902 Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks|Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks]]

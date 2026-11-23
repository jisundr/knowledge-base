---
type: topic
tags: [ai-engineering, ai-agents, agent-design]
---

# Agent Design Foundation

The four parts you define before a bot goes live. Treat it like onboarding an intern: goals, tools, and explicit limits.

- **Goal and task**: the end objective and the sub-goals that reach it.
- **Instructions**: rules for how the model reads inputs and picks tools.
- **Personality and voice**: traits (creativity, engagement, clarity, confidence) plus a tone (professional, friendly, instructional).
- **Tools and connectors**: REST APIs, data queries, or [[Model Context Protocol (MCP)]] servers.

## Onboarding rules

- State what the bot must never do: see [[Agent Anti-Jobs]].
- Have the bot write repeated procedures down as [[Agent Skills]], versioned in git.
- Back prompts with [[Deterministic Guardrail Policies]]; prompts alone are not a safety control.

## Related

- [[Domain-Specialized Agent Fleet]]
- [[AI Agents and Tool Use]]
- [[Context Engineering]]

## Sources

- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

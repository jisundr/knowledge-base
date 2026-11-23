---
type: topic
tags: [ai-engineering, ai-agents, mcp]
---

# Model Context Protocol (MCP)

A standard adapter layer that lets agents use external systems (tickets, docs, telemetry, browsers, design tools). Because tools connect through MCP, swapping an external system does not require rewriting the agent's instructions.

## Example integrations (Levi Strauss)

- **Jira and Confluence**: authoritative record of work, used by the requirements agent.
- **New Relic**: telemetry and alerts, used by the observability agent.
- **Playwright**: headless browser automation, used by testing and performance agents.
- **Figma**: design context pulled into build tasks.

## Related

- [[AI Agents and Tool Use]]
- [[Agentic SDLC]]
- [[Interpretable Context Methodology (ICM)]] (complementary: static context organization vs runtime tool connections)
- [[Agent Design Foundation]]

## Sources

- [[20261115112636 17 agents, one SDLC - How Levi Strauss reimagined development on GitHub|17 agents, one SDLC - How Levi Strauss reimagined development on GitHub]]
- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

---
type: topic
tags: [ai-engineering, ai-agents, sdlc, change-management]
---

# Agentic SDLC

Redesigning the software development lifecycle around AI agents instead of slotting AI tools into a legacy workflow.

Core principle: **agents start on execution, humans make the decision.**

| Role          | Responsibilities                                                                  |
| ------------- | --------------------------------------------------------------------------------- |
| AI does       | Synthesize specs (EARS), draft code, run tests, instrument observability, monitor |
| Human does    | Add context, exercise judgment, manage stakeholders                               |
| Human decides | Prioritize, approve or reject PRs, hold accountability                            |

## Three pillars

1. **Process**: ask "how do we stop the waiting?", not "how do we make human work faster?" (removes handoffs).
2. **Platform**: an orchestrator routes tasks to specialist agents defined as Markdown profiles in `.github/agents/`, connected to external systems through [[Model Context Protocol (MCP)]].
3. **People and governance**: change management, operating rules, enablement.

## Standards built in, not remembered

- **Starter kits**: standard repo templates ship with `agents.md`, Copilot instructions, CI/CD, runbooks and telemetry hooks.
- **Sequential CI quality gates**: testing, accessibility (WCAG 2.2 AA), performance (Core Web Vitals, measured not estimated), security (OWASP Top 10, CVEs, secrets; runs last on the final code), observability.
- On a gate failure, an agentic autofix proposes a labeled commit on the PR for human review.

## Operating rules

1. Human as judgment, agents on execution.
2. Context lives where agents can see it (repos and tickets, not chat).
3. Same bar for agents and humans: identical CI gates.
4. Auditable always: log every agent action and human override.

## Case study: Levi Strauss (Backpocket app)

- Legacy build: 9 months, 12 handoffs across 6 roles, 2 to 4 weeks for user stories, 3 weeks of tail-end QE.
- Agentic build: 17 agents, 2.5 months (72% faster), 51% higher throughput, 54% better PR pass rate, AI-assisted PRs 26% to 69%.
- Enablement: embedded principal AI engineer as player-coach, training on production code, office hours, internal marketplace (24 agents, 19 skills, 15 MCP servers).

## Related

- [[AI Agents and Tool Use]]
- [[AI Engineer Skill Stack]]
- [[Inverse Pyramid of Constraints]]
- [[Agent Verification Stack]]
- [[Autonomous Software Factory]]
- [[Grilling Session]]
- [[Task Graph Backlog]]
- [[AFK Agent Execution]]

## Sources

- [[20261115112636 17 agents, one SDLC - How Levi Strauss reimagined development on GitHub|17 agents, one SDLC - How Levi Strauss reimagined development on GitHub]]
- [[20261115183456 All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI|All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI]]
- [[20261121222850 Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture|Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture]]

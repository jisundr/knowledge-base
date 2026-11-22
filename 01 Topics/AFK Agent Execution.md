---
type: topic
tags: [ai-engineering, ai-agents, automation, orchestration]
---

# AFK Agent Execution

Splitting work into a **human-in-the-loop "day shift"** (grilling, PRD, ticket graph) and an **away-from-keyboard "night shift"** where agents implement unattended.

An orchestrator takes ready tickets from the [[Task Graph Backlog]], spins up sandboxes, and runs implementer sub-agents, each in a fresh [[Smart Zone and Dumb Zone|smart-zone]] context. Named tools: the **Ralph loop** (autonomous execution loop) and **Sandcastle** (orchestration harness).

Two safeguards keep it from producing a "ball of mud":

1. [[Test-Driven Development for Agents]] as the objective feedback loop.
2. [[Deep Modules]] so the codebase is easy for agents to work in.

## Related

- [[Autonomous Software Factory]]
- [[Agentic SDLC]]
- [[Ralph Loop]]
- [[Long-Running Agent Harness]]
- [[AI Work Autonomy Spectrum]]

## Sources

- [[20261121222850 Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture|Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture]]
- [[20261122123529 From Problem-First Discovery to Spec-Driven AI Execution|From Problem-First Discovery to Spec-Driven AI Execution]]
- [[20261122155021 Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern|Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern]]

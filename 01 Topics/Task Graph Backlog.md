---
type: topic
tags: [ai-engineering, ai-agents, planning, orchestration]
---

# Task Graph Backlog

Turning a PRD into a Kanban board of tickets arranged as a **directed acyclic graph (DAG)** with explicit blocking relationships, instead of a rigid multi-phase sequential plan.

Any ticket with no open blockers is ready, so several independent sub-agents can each pick one and work in parallel in their own clean context. Tickets are typically [[Vertical Slices (Tracer Bullets)]].

## Repo-native task stores

The graph can live in the repository instead of an external tracker, so agents query it directly. Examples: Beads (`bd ready` lists unblocked tasks) and backlog.md (Markdown tasks in Git). Tasks usually come from the `tasks.md` of [[Spec-Driven Development]], and a [[Ralph Loop]] works through them.

## Related

- [[AFK Agent Execution]]
- [[Multi-Agent Orchestration Patterns]]
- [[Grilling Session]]
- [[Spec-Driven Development]]
- [[Ralph Loop]]

## Sources

- [[20261121222850 Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture|Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture]]
- [[20261122123529 From Problem-First Discovery to Spec-Driven AI Execution|From Problem-First Discovery to Spec-Driven AI Execution]]

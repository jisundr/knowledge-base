---
type: topic
tags: [ai-engineering, ai-agents, memory]
---

# Agent Memory

Persistent knowledge an agent carries across sessions, typically stored as markdown files in a file system.

- **In-band memory**: the agent reads, writes, and updates memory itself during a live session using memory tools.
- **File system as memory**: standard utilities (`bash`, `grep`) index, search, and edit memory files, avoiding complex custom APIs.

## Limits of in-band memory

- **Split focus**: tokens and attention spent on memory upkeep compete with solving the actual task.
- **Limited visibility**: a single session cannot see systemic patterns across many agents or runs.

These motivate out-of-band curation: [[Dreaming (Agent Memory Consolidation)]]. Running it at fleet scale needs [[Memory Guardrails for Multi-Agent Systems]].

## In long-running loops

In a [[Ralph Loop]], lessons from each session are written to the task tracker or `AGENTS.md` and loaded into the next session's briefing, so a fresh context does not repeat old mistakes.

## Related

- [[Context Engineering]]
- [[Progressive Disclosure]]
- [[AI Agents and Tool Use]]
- [[Ralph Loop]]
- [[Long-Running Agent Harness]]

## Sources

- [[20261116203029 Lamis Mukta - Learning while you sleep - Beyond memory to dreaming - AI Native DevCon June 2026|Lamis Mukta - Learning while you sleep - Beyond memory to dreaming - AI Native DevCon June 2026]]
- [[20261122123529 From Problem-First Discovery to Spec-Driven AI Execution|From Problem-First Discovery to Spec-Driven AI Execution]]

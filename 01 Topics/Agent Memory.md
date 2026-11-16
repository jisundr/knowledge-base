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

## Related

- [[Context Engineering]]
- [[Progressive Disclosure]]
- [[AI Agents and Tool Use]]

## Sources

- [[Lamis Mukta - Learning while you sleep - Beyond memory to dreaming - AI Native DevCon June 2026]]

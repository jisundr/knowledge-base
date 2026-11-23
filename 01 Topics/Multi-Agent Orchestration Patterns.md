---
type: topic
tags: [ai-engineering, ai-agents, evaluation, architecture]
---

# Multi-Agent Orchestration Patterns

How multiple agents are wired together, and what each costs to evaluate (from a financial-document benchmark).

- **Sequential**: fixed chain. Simple and cheap to evaluate, fragile to upstream errors.
- **Parallel**: independent sub-agents then an aggregator. Fast, but needs deduplication and consensus checks.
- **Hierarchical**: lead agent decomposes work and reviews worker output. Best balance of accuracy, cost, and scalability in the benchmark.
- **Reflexive / self-correcting loops**: accurate on isolated reasoning, but latency queueing and token costs compound at scale.

## Metrics to track

- **Task accuracy** (end to end), **tool correctness** (valid calls and arguments), **step efficiency** (optimal vs total steps), **coordination quality** (context preserved across handoffs), **operational scaling** (P95 latency and cost per task under load).

## Related

- [[Implement-Review-Remediate Loop]]
- [[Domain-Specialized Agent Fleet]]
- [[Cloud Agent Fleet vs Local Worktree Orchestrator]]
- [[AI Agents and Tool Use]]
- [[Memory Guardrails for Multi-Agent Systems]]
- [[AI System Evaluation]]
- [[Task Graph Backlog]]
- [[AFK Agent Execution]]

## Sources

- [[20261123172458 Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE|Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE]]

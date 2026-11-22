---
type: topic
tags: [ai-engineering, ai-agents, architecture, orchestration]
---

# Long-Running Agent Harness

The runtime around an AI coding agent that works for hours or days. Plain chat sessions hit three walls:

1. **Context rot**: reasoning degrades as the window fills (see [[Smart Zone and Dumb Zone]]).
2. **Stateless sessions**: each new session starts blank.
3. **Generous self-grading**: the model marks its own work done even when tests fail.

## Three decoupled layers

| Layer | What it is |
| --- | --- |
| **Brain** | The LLM that plans and writes code |
| **Hands** | Ephemeral, isolated execution (containers, Git worktrees) |
| **Session** | Append-only event log of thoughts, tool calls, diffs, and test results, kept outside the context window |

The [[Ralph Loop]] is the usual work loop on top of this harness.

## Related

- [[AFK Agent Execution]]
- [[Containerization and Orchestration]]
- [[Agent Memory]]
- [[Spec-Driven Development]]

## Sources

- [[20261122123529 From Problem-First Discovery to Spec-Driven AI Execution|From Problem-First Discovery to Spec-Driven AI Execution]]

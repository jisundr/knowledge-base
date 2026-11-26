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

## Cloud deployment

Anthropic's Claude Managed Agents applies the same split in the cloud: the harness and session state run on a durable server, sandboxes are created only to run tools or untrusted code and then torn down, and secrets stay outside the sandbox via [[Egress Credential Injection]]. This avoids losing state when a sandbox crashes, slow boots, and secrets inside the environment.

## Related

- [[Egress Credential Injection]]
- [[AFK Agent Execution]]
- [[Containerization and Orchestration]]
- [[Agent Memory]]
- [[Spec-Driven Development]]
- [[Loop Engineering]]: this harness is Level 3 of the loop maturity levels.
- [[Verification Density]]

## Sources

- [[20261122123529 From Problem-First Discovery to Spec-Driven AI Execution|From Problem-First Discovery to Spec-Driven AI Execution]]
- [[20261123164745 Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding|Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding]]
- [[20261126155209 How Anthropic Builds Software with AI Agents|How Anthropic Builds Software with AI Agents]]

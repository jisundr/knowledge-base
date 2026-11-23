---
type: topic
tags: [ai-engineering, ai-agents, orchestration, git]
---

# Git Worktree Isolation for Parallel Agents

Give each parallel agent its own `git worktree`: a separate working directory on its own branch, sharing one repository. Agents can then edit the same codebase at the same time without overwriting each other's files.

- One task = one worktree branched from `main`.
- You can race two agents (e.g. Claude Code and Codex) on the same prompt and keep the better result.
- Branches, commits, and diffs become the handoff medium between agents instead of chat history; see [[Implement-Review-Remediate Loop]].

Doing this by hand means running `git worktree add` per task and juggling terminal tabs; an [[Agent Development Environment (ADE)]] automates it.

## Related

- [[Cloud Agent Fleet vs Local Worktree Orchestrator]]
- [[Loop Engineering]]
- [[Task Graph Backlog]]
- [[Long-Running Agent Harness]]

## Sources

- [[20261123172458 Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE|Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE]]

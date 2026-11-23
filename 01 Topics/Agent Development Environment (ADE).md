---
type: topic
tags: [ai-engineering, ai-agents, orchestration, tooling]
---

# Agent Development Environment (ADE)

A desktop control deck for running a fleet of CLI coding agents, instead of an editor with one assistant. Example: **Orca**, an open-source ADE that runs agents such as Claude Code, Codex, Grok Build, or Hermes locally or over SSH.

## Core capabilities

- **Worktree per task**: see [[Git Worktree Isolation for Parallel Agents]].
- **Visual feedback**: an embedded browser for picking UI elements to send to the agent; see [[Visual Element Annotation for Agents]].
- **Repository rules as context**: agents read `AGENTS.md` / `CLAUDE.md` and the linked issue, so you don't write a handoff file per task. See [[Context Pointers]].
- **Quick commands**: one-click reusable checks (`npm run build`, `dotnet test`) so verification is real, not claimed by the agent. See [[Verification Density]].
- **Rate-limit visibility**: usage per provider account, so you can route tasks to whichever quota has room.

## Caution

ADEs may launch agents with permission-bypass flags (e.g. `--dangerously-skip-permissions`). Keep deploys, production changes, and public posts behind human approval; see [[AI Work Autonomy Spectrum]].

## Related

- [[Cloud Agent Fleet vs Local Worktree Orchestrator]]
- [[Harness Engineering]]
- [[Home Repo Pattern]]

## Sources

- [[20261123172458 Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE|Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE]]

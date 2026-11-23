---
type: topic
tags: [ai-engineering, ai-agents, orchestration, architecture]
---

# Cloud Agent Fleet vs Local Worktree Orchestrator

Two ways to run many coding agents at once, beyond an in-editor copilot.

| | Cloud agent fleet | Local worktree orchestrator |
| --- | --- | --- |
| Example | Grok Bot (with Cursor cloud agents) | Orca, an [[Agent Development Environment (ADE)]] |
| Where it runs | Persistent cloud VM with browser, terminal, filesystem | Your machine or an SSH host |
| Trigger | Webhooks and schedules (GitHub, Sentry, Slack, Linear) | You start tasks from a control deck |
| Isolation | Delegates coding to separate cloud agents | One [[Git Worktree Isolation for Parallel Agents|Git worktree]] per agent |
| Models | Vendor's platform | Bring your own CLI agents and subscriptions |
| Runs while you're away | Yes, always on | Only while the host runs |

Choose the cloud fleet for event-driven, unattended work (see [[Domain-Specialized Agent Fleet]]). Choose the local orchestrator for parallel work you steer yourself.

## Related

- [[AI Work Autonomy Spectrum]]
- [[Autonomous Software Factory]]
- [[AFK Agent Execution]]
- [[Multi-Agent Orchestration Patterns]]

## Sources

- [[20261123172458 Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE|Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE]]

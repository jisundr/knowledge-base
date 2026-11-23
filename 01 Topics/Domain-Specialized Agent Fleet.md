---
type: topic
tags: [ai-engineering, ai-agents, orchestration, automation]
---

# Domain-Specialized Agent Fleet

Run many narrow bots instead of one generalist. Each bot owns a domain (iOS UI, desktop CI, infra root-cause analysis) and carries its own memory, guidelines, and [[Agent Skills|skills]]. Narrow scope keeps context sharp.

Rule of thumb: a small fleet of specialized bots, not a crowd. Give each bot one job, clear boundaries, and limited tool access.

## Common bot categories

- **Communication and triage**: inbox triage (urgency, sentiment, draft replies for approval); scheduled daily briefing.
- **Knowledge and research**: read-only research synthesis; contract and compliance review that flags risky clauses for counsel.
- **Operations and support**: IT troubleshooting (diagnose, remediate, or escalate); HR and recruiting assistant; finance reconciliation that flags ledger variances.

Design each one with the [[Agent Design Foundation]] and govern the fleet through an [[AI Control Plane]].

## Operating patterns

- **Manager bots delegate**: a bot turns a Slack or GitHub issue into a spec, starts a cloud coding agent, and watches its progress and proofs.
- **Shared tracker loop**: bots update a tracker (e.g. a Notion database) on a schedule, chase failing CI and security findings, auto-merge high-confidence low-risk changes, and escalate the rest to humans.
- **Ops bot**: a manager bot holds regular 1:1s with the engineering bots to reinforce playbooks, run postmortems on past mistakes, and onboard new bots. See [[Agent Memory]].
- **Nightly audits**: off-hours routines sweep for dead code, security issues, bundle size, and i18n gaps, leaving a queue of PRs by morning.
- **Urgent steering**: for P0 fixes, a routine checks agent traces every few minutes and unblocks stalled runs.

## Related

- [[Cloud Agent Fleet vs Local Worktree Orchestrator]]
- [[Autonomous Software Factory]]
- [[AFK Agent Execution]]
- [[Multi-Agent Orchestration Patterns]]
- [[Loop Engineering]]
- [[Agent Design Foundation]]
- [[AI Control Plane]]

## Sources

- [[20261123172458 Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE|Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE]]
- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

---
type: playbook
status: draft
tags: [playbook, ai-agents, orchestration, automation, bots]
---

# Playbook - Using Bots

Use when work should start from events or schedules and run while nobody is at the keyboard: issues, CI failures, alerts, nightly chores. Outcome: a fleet of narrow, always-on bots that turn events into reviewed PRs, merge only what you allowed, and hand everything else to a human. Pattern: [[Domain-Specialized Agent Fleet]] on the cloud side of [[Cloud Agent Fleet vs Local Worktree Orchestrator]] (e.g. Grok Bot with cloud coding agents).

## Trigger

- The same kind of task keeps arriving and runs clean in [[05 Running Parallel Agents|parallel local runs]] without steering.
- A recurring chore (failing CI, dead code, security findings, dependency bumps, i18n gaps) should run on a schedule.
- Issues from GitHub, Sentry, Slack, or Linear wait too long for a human to start them.

## Principles applied

- **One domain per bot**: each bot owns a narrow area (iOS UI, desktop CI, infra) with its own memory, guidelines, and [[Agent Skills|skills]]. Narrow scope keeps context sharp.
- **Bots manage, cloud agents code**: the bot writes the spec, starts a coding agent, and checks its proof. It does not edit code in its own long-lived context.
- **Earn autonomy**: a bot starts by opening PRs for human review. Auto-merge comes later, per change type, after a clean record ([[AI Work Autonomy Spectrum]]).
- **Same bar for bots and humans**: bot PRs pass [[04 Running Quality Gates]] and the [[Implement-Review-Remediate Loop]], one fix round, then a human.

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | React to events, write specs, start and watch coding agents, review proof, update the tracker, run scheduled audits, run bot postmortems |
| Human does | Define bot domains and memory, write routines, review escalations and the morning PR queue |
| Human decides | Which bot exists, which change types each bot may auto-merge, approval of high-risk actions |

## Steps

| # | Step | Owner (AI / Human / Decision) | Done when |
| --- | --- | --- | --- |
| 1 | Pick one domain with frequent, well-tested work | Decision | Domain, owner, and success measure written down |
| 2 | Create the bot: guidelines, memory file, skills, and the repos and tools it may touch | Human | Bot answers a sample request inside its domain only |
| 3 | Connect triggers: webhooks (GitHub, Sentry, Slack, Linear) and schedules | Human | A test event reaches the bot |
| 4 | Set the approval list: deploys, production data, auth, money, and any external post or message | Decision | The bot pauses on each listed action |
| 5 | Set up the shared tracker (e.g. a database of tasks, PRs, and status) | AI | Every bot task has a row |
| 6 | Run in PR-only mode: bot writes the spec, starts a coding agent, checks proof, opens a PR | AI | PRs land in the human review queue ([[05 Reviewing and Merging a PR]]) |
| 7 | Review the record after a few weeks: revert rate, review findings, escalations | Human | Per-change-type stats exist |
| 8 | Allow auto-merge for change types with a clean record and strong checks | Decision | Allowed types listed in the bot's config |
| 9 | Add routines from the table below, one at a time | Human | Each routine has an owner bot, trigger, and output |
| 10 | Run bot reviews: postmortems on bot mistakes, update guidelines and memory | AI | Each mistake has a fix: a new check or a memory entry |
| 11 | Add the next domain bot only when the first runs clean | Decision | New bot goes back to step 1 |

## Routines

| Routine | Trigger | Output |
| --- | --- | --- |
| Issue to PR | Webhook from GitHub, Sentry, Slack, or Linear | Spec written by the domain bot, coding agent run, PR with proof |
| Tracker sweep | Regular schedule (e.g. every 30 minutes) | Tracker updated, failing CI chased, allowed fixes merged, the rest flagged |
| Nightly audit | Off-hours schedule | PRs for dead code, security, bundle size, i18n; reviewed next morning |
| P0 watch | Every few minutes during an urgent fix | Stalled runs restarted or unblocked, human told |
| Bot review | Daily or weekly, run by an ops bot | Postmortems on bot mistakes, updated playbooks and memory, onboarding for new bots |

## Gates

1. Every bot PR passed the quality gates as exit codes.
2. At most one remediation round; anything beyond went to a human.
3. Auto-merged PRs match a change type approved for that bot.
4. Every approval-gated action has a recorded human approval.
5. No bot acted outside its domain.

## Audit trail

- Tracker row per task: trigger, bot, coding agent run, PR, checks, merge decision and the rule that allowed it.
- Bot review notes: mistake, cause, and the check or memory entry added.
- Nightly audit PR list, with what was merged and what was closed.

## Pitfalls

- **Generalist bot**: one bot for every domain loses focus and context. Split by domain.
- **Auto-merge from day one**: no record to justify it. Start PR-only.
- **Bots talking to the outside world**: Slack, X, or email posts without approval. Put them on the approval list.
- **Morning PR flood**: nightly audits produce more PRs than people can review, so they get rubber-stamped ([[Cognitive Debt in Agentic Coding]]). Cap PRs per routine.
- **Lessons only in memory**: a bot repeats a mistake that a check could block. Prefer a deterministic check ([[Inverse Pyramid of Constraints]]), then memory ([[Agent Memory]]).
- **No one owns the bot**: guidelines go stale. Each bot has a named human owner.

## Escalation

- A bot's revert rate rises: remove auto-merge for that change type and return to PR-only.
- A routine keeps escalating: the work is not routine. Move it back to [[05 Running Parallel Agents]] or [[03 Building a Task]].
- A bot breaks a security or approval rule: pause the bot, run a [[07 Running a Post-Incident Review|post-incident review]].

## Related

- [[Domain-Specialized Agent Fleet]]
- [[Cloud Agent Fleet vs Local Worktree Orchestrator]]
- [[Implement-Review-Remediate Loop]]
- [[Autonomous Software Factory]]
- [[AFK Agent Execution]]
- [[AI Work Autonomy Spectrum]]
- [[05 Running Parallel Agents]]
- [[04 Running an Agent Loop]]
- [[Playbook Template]]

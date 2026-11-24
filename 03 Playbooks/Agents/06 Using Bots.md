---
type: playbook
status: draft
tags: [playbook, ai-agents, orchestration, automation, bots, governance]
---

# Playbook - Using Bots

Use when work should start from events or schedules and run while nobody is at the keyboard: issues, CI failures, alerts, nightly chores. Outcome: a fleet of narrow, always-on bots that turn events into reviewed PRs, merge only what you allowed, and hand everything else to a human. Pattern: [[Domain-Specialized Agent Fleet]] on the cloud side of [[Cloud Agent Fleet vs Local Worktree Orchestrator]] (e.g. Grok Bot with cloud coding agents), governed through an [[AI Control Plane]].

## Trigger

- The same kind of task keeps arriving and runs clean in [[05 Running Parallel Agents|parallel local runs]] without steering.
- A recurring chore (failing CI, dead code, security findings, dependency bumps, i18n gaps) should run on a schedule.
- Issues from GitHub, Sentry, Slack, or Linear wait too long for a human to start them.

## Principles applied

- **Small fleet, not a crowd**: a few bots, each with one job, clear boundaries, and only the tools that job needs. Fifty loosely managed bots means unowned access and token bills nobody can explain.
- **One domain per bot**: each bot owns a narrow area (iOS UI, desktop CI, infra) with its own memory, guidelines, and [[Agent Skills|skills]]. Narrow scope keeps context sharp.
- **Bots manage, cloud agents code**: the bot writes the spec, starts a coding agent, and checks its proof. It does not edit code in its own long-lived context.
- **Earn autonomy**: a bot starts by opening PRs for human review. Auto-merge comes later, per change type, after a clean record ([[AI Work Autonomy Spectrum]]).
- **Prompts are not controls**: list each bot's [[Agent Anti-Jobs|anti-jobs]] in its prompt, but enforce the risky ones with tool permissions, [[Human-in-the-Loop Approval Gates]], and [[Deterministic Guardrail Policies]].
- **Script what needs no judgment**: once a routine is stable, move its rule-based steps into scripts and keep model calls for judgment ([[Agent Script Migration]]).
- **Same bar for bots and humans**: bot PRs pass [[04 Running Quality Gates]] and the [[Implement-Review-Remediate Loop]], one fix round, then a human.

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | React to events, write specs, start and watch coding agents, review proof, update the tracker, run scheduled audits, run bot postmortems |
| Human does | Define bot domains, anti-jobs, guardrails, and memory, write routines, review escalations and the morning PR queue |
| Human decides | Which bot exists, the platform tier ([[Agent Framework Altitude Tiers]]), which change types each bot may auto-merge, approval of high-risk actions |

## Steps

| # | Step | Owner (AI / Human / Decision) | Done when |
| --- | --- | --- | --- |
| 1 | Pick one domain with frequent, well-tested work | Decision | Domain, owner, and success measure written down |
| 2 | Create the bot from the [[Agent Design Foundation]] (see Agent profile below): goal, instructions, voice, memory file, skills, and the repos and tools it may touch | Human | Bot answers a sample request inside its domain only, and refuses each anti-job |
| 3 | Connect triggers: webhooks (GitHub, Sentry, Slack, Linear) and schedules | Human | A test event reaches the bot |
| 4 | Set the approval list: deploys, production data, auth, money, record changes, deletes, and any external post or message. Approvals arrive in Slack, Teams, or a webhook and the run waits for them | Decision | The bot pauses on each listed action and resumes after the answer |
| 5 | Add guardrail policies around the model: prompt-injection detection, denied topics, regex scrubbing of secrets and personal data | Human | Test inputs for each policy are blocked or scrubbed |
| 6 | Set up the shared tracker (e.g. a database of tasks, PRs, and status) | AI | Every bot task has a row |
| 7 | Wire observability at all four layers ([[Four-Layer AI Observability]]), with alerts on step count, tool-call loops, and token spend per task | Human | A test run shows up as one trace across application, agent, model, and infrastructure |
| 8 | Run in PR-only mode: bot writes the spec, starts a coding agent, checks proof, opens a PR | AI | PRs land in the human review queue ([[05 Reviewing and Merging a PR]]) |
| 9 | Review the record after a few weeks: revert rate, review findings, escalations | Human | Per-change-type stats exist |
| 10 | Allow auto-merge for change types with a clean record and strong checks | Decision | Allowed types listed in the bot's config |
| 11 | Add routines from the table below, one at a time | Human | Each routine has an owner bot, trigger, and output |
| 12 | Run bot reviews: postmortems on bot mistakes, update guidelines and memory. When you walk a bot through a new workflow, have it write the procedure as a skill (inputs, steps, what a correct result looks like) and review it before it is merged | AI | Each mistake has a fix: a new check, a skill update, or a memory entry |
| 13 | Review cost: find routine steps that never need judgment and move them into scripts | Human | Token spend per routine is flat or falling |
| 14 | Add the next domain bot only when the first runs clean | Decision | New bot goes back to step 1 |

## Routines

| Routine | Trigger | Output |
| --- | --- | --- |
| Issue to PR | Webhook from GitHub, Sentry, Slack, or Linear | Spec written by the domain bot, coding agent run, PR with proof |
| Tracker sweep | Regular schedule (e.g. every 30 minutes) | Tracker updated, failing CI chased, allowed fixes merged, the rest flagged |
| Nightly audit | Off-hours schedule | PRs for dead code, security, bundle size, i18n; reviewed next morning |
| P0 watch | Every few minutes during an urgent fix | Stalled runs restarted or unblocked, human told |
| Daily briefing | Every morning | One summary of tracker changes, open tickets, and overnight PRs for the team |
| Cost review | Weekly | Token spend per bot and routine; steps proposed for script migration |
| Bot review | Daily or weekly, run by an ops bot | Postmortems on bot mistakes, updated playbooks and memory, onboarding for new bots |

## Gates

1. Every bot PR passed the quality gates as exit codes.
2. At most one remediation round; anything beyond went to a human.
3. Auto-merged PRs match a change type approved for that bot.
4. Every approval-gated action has a recorded human approval.
5. No bot acted outside its domain.
6. Guardrail policies ran on every input and output, and none were bypassed.
7. Each task stayed inside its step and token budget.

## Agent profile

Each bot gets a short profile, versioned in git next to its skills ([[Agent Design Foundation]]):

- **Goal and tasks**: the one job, and the sub-tasks it covers.
- **Instructions**: how to read inputs and pick tools.
- **Voice**: tone for anything humans read (e.g. professional, instructional).
- **Tools**: the exact repos, APIs, and [[Model Context Protocol (MCP)|MCP]] servers it may use, read-only where possible.
- **Anti-jobs**: what it must never do, e.g. "never send an external message without approval", "never issue a refund".
- **Guardrails**: which deterministic policies wrap it.
- **Owner**: the named human.

## Audit trail

- Append-only, event-sourced log of every reasoning step, tool call, and approval, kept long enough to replay a run for a compliance audit months later.
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
- **Safety only in the prompt**: "please don't" is not a control. Back anti-jobs with permissions, approval gates, and guardrail policies.
- **Uptime is not health**: the service is up while the bot gives fluent wrong answers or loops on tool calls. Watch the agent layer, not just the host.
- **Model doing script work**: every run pays tokens for steps that never change. Script them.
- **Self-written skills merged unread**: unreviewed self-written skills give no average benefit ([[Agent Skills]]). Review them like code.
- **Wrong altitude**: building a control plane in-house when the business only needs to run bots, or buying a platform when you need control of the loop. Decide with [[Agent Framework Altitude Tiers]].

## Escalation

- A bot's revert rate rises: remove auto-merge for that change type and return to PR-only.
- A routine keeps escalating: the work is not routine. Move it back to [[05 Running Parallel Agents]] or [[03 Building a Task]].
- Token spend or step count spikes: check agent-layer traces for a tool-call loop, pause the routine, add a step or budget limit.
- A bot breaks a security or approval rule: pause the bot, run a [[07 Running a Post-Incident Review|post-incident review]].

## Related

- [[Domain-Specialized Agent Fleet]]
- [[Cloud Agent Fleet vs Local Worktree Orchestrator]]
- [[Implement-Review-Remediate Loop]]
- [[Autonomous Software Factory]]
- [[AFK Agent Execution]]
- [[AI Work Autonomy Spectrum]]
- [[AI Control Plane]]
- [[Agent Design Foundation]]
- [[Agent Anti-Jobs]]
- [[Deterministic Guardrail Policies]]
- [[Human-in-the-Loop Approval Gates]]
- [[Four-Layer AI Observability]]
- [[Agent Script Migration]]
- [[Agent Framework Altitude Tiers]]
- [[05 Running Parallel Agents]]
- [[04 Running an Agent Loop]]
- [[Playbook Template]]
- [[00 Bots Index]]: where each bot's profile lives (start from [[Bot Profile Template]])

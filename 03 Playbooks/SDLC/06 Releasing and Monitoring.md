---
type: playbook
status: draft
tags: [playbook, release, observability, monitoring, agentic-sdlc, kairyn]
---

# Playbook - Releasing and Monitoring

Stage 6 after [[05 Reviewing and Merging a PR]]. Use when a PR is merged. Outcome: the change is released safely, watched against agreed signals, and either confirmed healthy or rolled back, with lessons fed back into the pipeline. Pattern: agents monitor, humans decide ([[Agentic SDLC]]; the Observability Agent in the Levi Strauss platform).

## Trigger

- Review stage is `done` and the PR is merged.

## Principles applied

- **Human as judgment, agents on execution**: agents watch signals and draft reports; a human decides to promote, hold, or roll back.
- **Context lives where agents can see it**: runbooks and dashboards are linked from the repo and the task folder.
- **Measured, never estimated**: "healthy" means real telemetry against stated thresholds.
- **Auditable always**: release, alerts, and rollback decisions are logged.

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Prepare release notes, run the release checklist, watch telemetry, correlate alerts to the change, draft an incident or all-clear summary |
| Human does | Judge ambiguous signals, communicate with stakeholders, handle what the agent cannot see (customer reports) |
| Human decides | Release timing, promote or roll back, declare success |

## Steps

| # | Step | Owner | Done when |
| --- | --- | --- | --- |
| 1 | Draft release notes from `REQUIREMENTS.md` and the merged PR | AI | Notes state what changed, for whom, and known limits; written in ASD-STE100, Level 1 or 2 ([[01 Using ASD-STE100 with Agents]]) |
| 2 | Define success signals and thresholds (error rate, latency, key business metric) and the rollback trigger; for AI features add quality and drift signals ([[Model Drift Detection]]) and confirm request-level evidence is logged ([[Request-Level Evidence Capture]]) | AI draft, Human confirms | Each signal has a number and a source |
| 3 | Run the pre-release checklist: migrations, config and flags, dependencies, rollback path tested | AI | Checklist all ticked |
| 4 | Approve release timing | **Human decides** | Time and approver logged |
| 5 | Release, preferably gradually (flag, canary, or staged rollout) | AI executes, Human watches | Change live for the first slice |
| 6 | Watch the signals through the observation window | AI | Telemetry compared with baseline, anomalies flagged |
| 7 | Promote, hold, or roll back | **Human decides** | Decision and reason logged |
| 8 | Write the outcome summary and any follow-up tasks | AI | Summary on the task, follow-ups filed |
| 9 | Record learnings in `.kairyn/learnings.md` and feed gaps back into earlier playbooks | AI | Each surprise maps to a stage that should have caught it |

## Gates

1. Pre-release checklist complete, rollback path known.
2. Success signals and rollback trigger defined before release, not after.
3. Observation window completed with signals inside thresholds.
4. Human declared the release healthy or rolled it back.

## When signals go bad

1. Stop the rollout. Do not wait for a perfect diagnosis.
2. The agent correlates the alert with the change (deploy time, flag, dependency) and drafts findings.
3. A human decides: roll back, roll forward with a fix, or hold.
4. If rolled forward, the fix goes through the full pipeline again, at least [[04 Running Quality Gates]].
5. Run [[07 Running a Post-Incident Review]]: blameless timeline, contributing factors, owned action items, and the stage that should have caught it.

## kairyn stage sketch

- **Inputs**: `STATE.md`, all earlier stage files, release and monitoring config
- **Output**: `docs/tasks/<date>-<slug>/RELEASE.md` (release notes, signals and thresholds, observation results, decision, follow-ups)
- **Exit criteria**: observation window passed and release declared healthy, or rollback done and logged
- **State update**: `release: done`, set `status: done`, append log line

## Pitfalls

- Defining "healthy" after seeing the data.
- Releasing everyone at once with no rollback path.
- Releasing late on Friday with nobody watching.
- Alert noise: if thresholds page constantly, people stop reading them.
- Skipping the learnings step, so the same miss repeats.

## Escalation

- Customer impact confirmed: follow the incident process and notify stakeholders now, not after the fix; then run [[07 Running a Post-Incident Review]].
- Cannot tell whether the change caused the issue: roll back first, investigate second.
- Missing telemetry for the new behavior: block the release and return to [[04 Running Quality Gates]] (observability gate).

## Related

- [[Agentic SDLC]]
- [[01 Using ASD-STE100 with Agents]]: how the agent writes release notes and incident summaries
- [[07 Running a Post-Incident Review]]: what to do after a rollback or incident
- [[Playbook Template]]

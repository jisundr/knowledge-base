---
type: playbook
status: draft
tags: [playbook, build, agentic-sdlc, kairyn]
---

# Playbook - Building a Task

Stage 3 after [[02 Designing a Solution]]. Use when `DESIGN.md` is approved. Outcome: a pull request whose code and tests satisfy the plan, ready for the quality gates. Pattern: [[Agentic SDLC]] (agents on execution).

## Trigger

- Design stage is `done` and approved.

## Principles applied

- **Same bar for agents and humans**: agent-written code faces the same gates as human code.
- **Auditable always**: commits and `STATE.md` log show what the agent did.
- **Context lives where agents can see it**: follow `agents.md`, `CLAUDE.md`, and repo conventions, not chat memory.
- **Done means green checks, not a claim**: a step is done when its command exits 0, never because the agent says so ([[Verification Density]]).

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Write tests first, implement task by task, run tests locally, keep commits small, update docs |
| Human does | Unblock questions, review direction early on risky tasks |
| Human decides | Whether a deviation from the plan is acceptable |

## Steps

| # | Step | Owner | Done when |
| --- | --- | --- | --- |
| 0 | Pick the autonomy level from the table below | Decision | Level is recorded in `STATE.md` |
| 1 | Create a branch named after the task slug (a git worktree if other sessions run on the same repo) | AI | Branch exists, clean base |
| 2 | For each task in `DESIGN.md`: write the failing test first | AI | Test fails for the right reason |
| 3 | Implement the minimum to pass | AI | Test passes, no unrelated changes |
| 4 | Run the full local suite and linters | AI | All green |
| 5 | Commit per task with a message linking the criterion | AI | One logical change per commit |
| 6 | Log deviations from the plan in `STATE.md` | AI | Every deviation has a reason |
| 7 | Open a PR summarizing criteria met, tests added, deviations | AI | PR description maps criteria to evidence; written in ASD-STE100, Level 1 ([[01 Using ASD-STE100 with Agents]]) |

## Pick the autonomy level

Match autonomy to how well the change is checked, not to how simple it looks ([[AI Work Autonomy Spectrum]]).

| Level | Use when | Requires |
| --- | --- | --- |
| Human-in-the-loop | High-risk or hard-to-undo changes: schema migrations, auth, shared API contracts, data deletion | A human watches the session and approves tool calls |
| AFK ([[AFK Agent Execution]]) | The plan is clear and the gates cover the risk | Sandbox, auto-approved permissions, ends in a PR |
| Factory-triggered ([[Autonomous Software Factory]]) | Routine, well-tested work started by CI failures, schedules, or issues | Strong deterministic gates, including contract checks for cross-repo changes |

If the task touches more than one repo, run it from a home repo ([[03 Setting Up a Home Repo]]).

For AFK or factory-triggered levels, run the work as a loop: check the harness, pick a loop maturity level, set budgets and approval gates ([[04 Running an Agent Loop]]).

## Gates

1. All tasks in `DESIGN.md` are done or explicitly deferred.
2. Local tests and linters pass.
3. No unplanned scope. Extras go to a follow-up task.

## kairyn stage sketch

- **Inputs**: `STATE.md`, `REQUIREMENTS.md`, `DESIGN.md`, `.kairyn/learnings.md`
- **Output**: a PR plus `docs/tasks/<date>-<slug>/BUILD.md` (what was built per task, deviations, how to verify)
- **Exit criteria**: tasks done, local checks green, PR opened
- **State update**: `build: done`, advance `stage` to `gates`, append log line

## Pitfalls

- Scope creep inside the PR.
- Skipping the failing-test step, so tests prove nothing.
- Silent plan deviations.
- Running AFK on a high-risk change because it looked small.
- Pushing through a degraded session: compact or clear instead ([[02 Writing Agent Instruction Files]]).

## Escalation

- The plan turns out wrong: stop, set `status: blocked`, return to design.
- Task is much larger than estimated: split it and tell the decision-maker.

## Related

- [[Agentic SDLC]]
- [[01 Using ASD-STE100 with Agents]]: how the agent writes PR descriptions and commit messages
- [[AI Work Autonomy Spectrum]]
- [[03 Setting Up a Home Repo]]: cross-repo tasks
- [[04 Running an Agent Loop]]: AFK and factory-triggered runs
- [[Verification Density]]
- [[Playbook Template]]

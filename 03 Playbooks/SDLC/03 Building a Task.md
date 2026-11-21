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

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Write tests first, implement task by task, run tests locally, keep commits small, update docs |
| Human does | Unblock questions, review direction early on risky tasks |
| Human decides | Whether a deviation from the plan is acceptable |

## Steps

| # | Step | Owner | Done when |
| --- | --- | --- | --- |
| 1 | Create a branch named after the task slug | AI | Branch exists, clean base |
| 2 | For each task in `DESIGN.md`: write the failing test first | AI | Test fails for the right reason |
| 3 | Implement the minimum to pass | AI | Test passes, no unrelated changes |
| 4 | Run the full local suite and linters | AI | All green |
| 5 | Commit per task with a message linking the criterion | AI | One logical change per commit |
| 6 | Log deviations from the plan in `STATE.md` | AI | Every deviation has a reason |
| 7 | Open a PR summarizing criteria met, tests added, deviations | AI | PR description maps criteria to evidence |

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

## Escalation

- The plan turns out wrong: stop, set `status: blocked`, return to design.
- Task is much larger than estimated: split it and tell the decision-maker.

## Related

- [[Agentic SDLC]]
- [[Playbook Template]]

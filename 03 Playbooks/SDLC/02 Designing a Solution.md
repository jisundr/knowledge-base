---
type: playbook
status: draft
tags: [playbook, design, agentic-sdlc, kairyn]
---

# Playbook - Designing a Solution

Stage 2 after [[01 Handling New Requirements]]. Use when an approved `REQUIREMENTS.md` exists. Outcome: a short, human-approved design and task breakdown that an agent can build from without guessing. Pattern: [[Agentic SDLC]].

## Trigger

- Requirements stage is `done` and approved in `STATE.md`.

## Principles applied

- **Context lives where agents can see it**: design is a file in the task folder, not a whiteboard photo.
- **Human as judgment**: approach and trade-offs are human decisions; agents explore and draft.
- Removes the wait between "requirements approved" and "someone starts".

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Read the repo, find affected code, propose 1 to 3 approaches with trade-offs, draft the task breakdown and test plan |
| Human does | Add architectural context, constraints, and taste |
| Human decides | Pick the approach, approve the plan |

## Steps

| # | Step | Owner | Done when |
| --- | --- | --- | --- |
| 1 | Read `REQUIREMENTS.md` and `.kairyn/learnings.md` | AI | Every acceptance criterion is mapped to code areas |
| 2 | Survey the existing code: reuse candidates, conventions, risky areas | AI | Affected files and modules are listed |
| 3 | Propose options with trade-offs (include "do the smallest thing") | AI | 1 to 3 options, each with cost and risk |
| 4 | Choose the approach | **Human decides** | Choice and reason recorded |
| 5 | Break into small, independently verifiable tasks, ordered by dependency | AI | Each task has a clear done condition |
| 6 | Write the test plan: which criterion is verified by which test | AI | Every acceptance criterion has a test |
| 7 | Note standards impact (a11y, performance, security, observability) | AI | Matches the gates in [[04 Running Quality Gates]] |
| 8 | Approve the plan | **Human decides** | Approval logged in `STATE.md` |

## Gates

1. Every acceptance criterion maps to a task and a test.
2. No task requires a decision that is not already made.
3. Human approval recorded.

## kairyn stage sketch

- **Inputs**: `STATE.md`, `REQUIREMENTS.md`, `.kairyn/learnings.md`
- **Output**: `docs/tasks/<date>-<slug>/DESIGN.md` (chosen approach and why, rejected options, task list, test plan, standards impact)
- **Exit criteria**: criteria-to-tasks-to-tests mapping complete; approach approved
- **State update**: `design: done`, advance `stage` to `build`, append log line

## Pitfalls

- Designing before the requirements are approved.
- Big-bang tasks that cannot be verified alone.
- Unrecorded trade-offs, so the next agent re-litigates them.

## Escalation

- Design contradicts a requirement: send it back to the requirements stage, do not patch silently.
- Approaches differ in cost by an order of magnitude: take options to the decision-maker.

## Related

- [[Agentic SDLC]]
- [[Playbook Template]]

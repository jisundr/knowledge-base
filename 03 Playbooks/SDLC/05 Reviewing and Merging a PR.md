---
type: playbook
status: draft
tags: [playbook, review, agentic-sdlc, kairyn]
---

# Playbook - Reviewing and Merging a PR

Stage 5 after [[04 Running Quality Gates]]. Use when gates are green. Outcome: a human approves or rejects the PR with accountability, and the lessons are recorded. Pattern: "humans make the decision" from [[Agentic SDLC]].

## Trigger

- Gates stage is `done`.

## Principles applied

- **Human as judgment**: approving a PR is a human decision, never delegated.
- **Auditable always**: the approval and any override are recorded.
- Gates handle mechanical checks, so the reviewer spends time on intent, design fit, and risk.

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Summarize the change against the criteria, flag risky areas, list deviations and waivers, draft review notes |
| Human does | Check intent and design fit, read the risky parts, test by hand where it matters |
| Human decides | Approve, request changes, or reject; accountable for the merge |

## Steps

| # | Step | Owner | Done when |
| --- | --- | --- | --- |
| 1 | Produce a review summary: criteria met with evidence, deviations, waivers, risky files | AI | Summary posted on the PR |
| 2 | Review for intent and fit: does this solve the problem in `REQUIREMENTS.md`? | Human | Questions answered |
| 3 | Read the risky parts and any autofix commits | Human | Nothing unread that matters |
| 4 | Approve, request changes, or reject | **Human decides** | Decision and reason on the PR |
| 5 | Address requested changes, re-run affected gates | AI | Gates green again |
| 6 | Merge | Human | PR merged, branch cleaned up |
| 7 | Record learnings in `.kairyn/learnings.md` | AI | Conventions, pitfalls, commands captured |

## Gates

1. All quality gates pass or have recorded waivers.
2. Every acceptance criterion has evidence.
3. A named human approved.

## kairyn stage sketch

- **Inputs**: `STATE.md`, all earlier stage files, the PR
- **Output**: `docs/tasks/<date>-<slug>/REVIEW.md` (summary, decision, who decided, follow-ups)
- **Exit criteria**: PR approved and merged, or rejected with reason
- **State update**: `review: done`, set `status: done` if last stage, append log line

## Pitfalls

- Rubber-stamping because the gates are green.
- Reviewing the diff without reading `REQUIREMENTS.md`.
- Merging with unanswered review questions.

## Escalation

- Review shows the problem was misunderstood: reopen the requirements stage.
- Disagreement between author and reviewer: involve the tech lead.

## Related

- [[06 Releasing and Monitoring]] (next stage)
- [[Agentic SDLC]]
- [[Playbook Template]]

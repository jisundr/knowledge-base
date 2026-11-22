---
type: playbook
status: draft
tags: [playbook, requirements, agentic-sdlc, ears]
---

# Playbook - Handling New Requirements

Use when a ticket, brief, or change request lands and must become something buildable. Outcome: a testable, human-approved spec living in the ticket, with open questions closed or owned. Pattern from [[Agentic SDLC]] (Levi Strauss): the Requirements Agent converts tickets into specs and asks clarifying questions; humans decide.

## Trigger

- A shaped pitch is committed in [[00 Managing the Idea Backlog]].
- A new ticket, brief, or meeting outcome describes new work.
- An existing requirement changes mid-flight.

## Principles applied

- **Context lives where agents can see it**: the ticket (Jira/Confluence), not chat or memory.
- **Human as judgment, agents on execution**: the agent drafts; people supply context and decide.
- **Auditable always**: every clarifying question, answer, and approval is recorded on the ticket.
- Removes the 2 to 4 week story-writing wait and the late rework caused by ambiguity.

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Read the ticket, draft the spec in EARS, flag ambiguity, generate clarifying questions, draft acceptance criteria and test outline |
| Human does | Answer questions, add business context, manage stakeholders, spot what the agent cannot know |
| Human decides | Scope, priority, and sign-off on the spec |

## Steps

| # | Step | Owner | Done when |
| --- | --- | --- | --- |
| 1 | Capture the request in the ticket (paste source material, link recordings and designs) | Human | Everything needed is on the ticket |
| 2 | Restate the problem and who it is for, free of solution language | AI draft, Human confirms | Problem statement stands without mentioning a solution |
| 3 | Detect ambiguity and ask clarifying questions, batched by theme (scope, users, constraints, success criteria, deadline, dependencies) | AI | Every vague term ("fast", "simple") has a question |
| 4 | Answer questions with context and examples | Human | Each question is answered or has an owner and date |
| 5 | Write requirements in EARS form (see below) | AI | Each requirement is one testable sentence |
| 6 | Define scope: in, out, deferred | AI draft, Human decides | Someone could disagree with a specific line |
| 7 | Derive acceptance criteria and non-functional needs (a11y, performance, security, observability) matching the CI gates | AI | QA could test each without asking; written in ASD-STE100, Level 1 ([[01 Using ASD-STE100 with Agents]]) |
| 8 | List assumptions, risks, dependencies, with an owner for each | AI draft, Human validates | No orphaned assumptions |
| 9 | Review and approve the spec | **Human decides** | Written approval on the ticket |
| 10 | Baseline the spec; changes re-enter at step 3 | Human | One source of truth, linked from the ticket |

## EARS cheat sheet

Easy Approach to Requirements Syntax. One sentence per requirement, with a fixed shape:

- **Ubiquitous**: The `<system>` shall `<response>`.
- **Event-driven**: When `<trigger>`, the `<system>` shall `<response>`.
- **State-driven**: While `<state>`, the `<system>` shall `<response>`.
- **Unwanted behavior**: If `<condition>`, then the `<system>` shall `<response>`.
- **Optional feature**: Where `<feature is included>`, the `<system>` shall `<response>`.

Example: *When a stylist saves a look, the app shall show it in their saved list within 2 seconds.*

## Gates

Run in order before the spec moves to build:

1. **Testable**: every requirement maps to at least one acceptance criterion.
2. **Unambiguous**: no unanswered clarifying questions or vague terms.
3. **Standards**: accessibility, performance, security, and observability needs stated (these are what the CI gates will later check).
4. **Approved**: human sign-off recorded. Same bar whether a person or an agent drafted it.

## Run it with kairyn

[kairyn](https://github.com/jisundr/kairyn) ("an agentic SDLC that grows with your repo") is the executable form of this playbook. Its `requirements` stage (stage 1) is the agent profile, so no separate profile is needed.

Setup, once per repo:

```
/plugin marketplace add jisundr/kairyn
/plugin install kairyn@kairyn
/kairyn:init
```

`/kairyn:init` creates `.kairyn/` (stages, templates, learnings), `docs/tasks/`, and `.harness/`, and adds a block to `CLAUDE.md`. `/kairyn:check` verifies doc headers and size budgets.

How the playbook steps map to the stage:

| Playbook step | kairyn requirements stage |
| --- | --- |
| 1 Capture | Request passed as command arguments; task folder `docs/tasks/<YYYY-MM-DD>-<slug>/` and `STATE.md` created |
| 2 Restate the problem | "Restate the request in one paragraph" |
| 3-4 Clarify | Skim the repo first, then ask the user only what the repo cannot answer |
| 6 Scope | In / explicitly out |
| 7 Acceptance criteria | Checklist a reviewer can verify |
| 9 Approve | Exit criteria: every criterion verifiable, no unresolved open questions |
| 10 Baseline | `REQUIREMENTS.md` in the task folder; `STATE.md` marks `requirements: done` and logs it |

Output: `docs/tasks/<YYYY-MM-DD>-<slug>/REQUIREMENTS.md` (problem statement, scope, acceptance criteria, open questions and answers). Lessons about the repo go to `.kairyn/learnings.md`, so each run starts smarter.

Gaps to cover by hand or by extending the stage (via a PR to kairyn, following its "change a stage" workflow):

- EARS phrasing of requirements (step 5)
- Non-functional needs matching the CI gates (step 7)
- Assumptions, risks, dependencies with owners (step 8)
- An explicit human approval line (step 9); the stage currently ends at exit criteria

## Audit trail

- Questions asked, answers received, and by whom (on the ticket).
- Each spec revision, and who approved it.
- Any human override of an agent-drafted requirement, with the reason.

## Pitfalls

- **Letting the agent guess.** Ambiguity must become a question, not an assumption.
- **Chat-only agreements.** If it is not on the ticket, neither agents nor future you can see it.
- **Rubber-stamp approval.** The human decision is the point; read the spec.
- **Building the stated solution.** Ask what problem it solves.
- **Silent scope creep.** Every addition is a change that re-enters at step 3.

## Escalation

- Stakeholders disagree: take both options and trade-offs to the decision-maker.
- Deadline incompatible with scope: present scope/time/cost options.
- Stage keeps producing unusable specs: change the stage file (and add an eval in kairyn) rather than patching outputs by hand.

## Related

- [[Agentic SDLC]]
- [[00 Managing the Idea Backlog]] (previous stage)
- [[02 Designing a Solution]] (next stage)
- [[01 Using ASD-STE100 with Agents]]: how the agent writes acceptance criteria with one meaning
- [[Playbook Template]]
- [kairyn](https://github.com/jisundr/kairyn)

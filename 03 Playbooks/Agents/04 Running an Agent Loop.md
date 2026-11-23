---
type: playbook
status: draft
tags: [playbook, ai-agents, loop-engineering, harness-engineering, verification]
---

# Playbook - Running an Agent Loop

Use when you want an agent to work through a task by itself: a script or orchestrator prompts it, checks the result, and prompts again, instead of a human prompting turn by turn. Outcome: a loop at the right maturity level that stops on objective checks, stays inside a budget, and asks a human at the risky points. Pattern: [[Loop Engineering]] on top of [[Harness Engineering]].

## Trigger

- You keep typing the same follow-up prompt ("fix the failing tests", "now run lint") by hand.
- A task in [[03 Building a Task]] is set to AFK or factory-triggered autonomy.
- A recurring chore (lint debt, dependency bumps, flaky tests) should run on a schedule or a CI event.

## Principles applied

- **Build the harness before the loop**: a loop around weak checks repeats mistakes faster. Context first, then harness, then loop.
- **Never trust self-report**: the loop ends on deterministic signals such as exit code 0, not on the agent saying it is done ([[Verification Density]]).
- **Guides before, sensors after**: steer with instruction files and specs, catch with tests and linters ([[Feedforward Guides and Feedback Sensors]]).
- **Cheap checks first**: computational checks (tests, types, lint) on every pass; inferential checks ([[LLM-as-a-Judge]], AI review) only where no exact check exists.
- **Human as judgment**: approval gates for hard-to-undo actions, and real review of the result ([[Cognitive Debt in Agentic Coding]]).

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Observe state, plan the next step, act, run the checks, reflect on failures, log each pass |
| Human does | Write the exit criteria and the checks, set budgets, read the log and the final diff |
| Human decides | The maturity level, approval of high-risk actions, and whether the result merges |

## Harness readiness check

Do not start a loop until every row is true.

| Layer | Check |
| --- | --- |
| Context | `AGENTS.md` / `CLAUDE.md` is lean and current ([[02 Writing Agent Instruction Files]]) |
| Guides | The task has a spec or acceptance criteria the agent can read |
| Sensors | Tests, type-check, and lint run from one command with a pass/fail exit code |
| Hands | The agent runs in a sandbox or its own Git worktree |
| Memory | A progress file (the "spine") records what each pass did, outside the context window |

## Pick the maturity level

| Level | Shape | Use when | Requires |
| --- | --- | --- | --- |
| 1. Simple loop | One narrow task, a fixed number of passes | Mechanical fixes: lint errors, type errors, a failing test | One check command, max-iteration limit |
| 2. Task decomposition | Plans sub-tasks, edits files, runs integration tests, reflects on failures | A feature with an approved `DESIGN.md` | Level 1, plus integration tests and a task list |
| 3. Multi-day harness | Worktrees, persistent memory, token budget, error recovery, human approval gates | Long-running backlog work ([[Long-Running Agent Harness]], [[Ralph Loop]]) | Level 2, plus budgets, approval gates, and a separate judge |

Start at Level 1. Move up only when the lower level runs clean.

## Steps

| # | Step | Owner (AI / Human / Decision) | Done when |
| --- | --- | --- | --- |
| 1 | Run the harness readiness check | AI | Every row passes, or the gaps are listed |
| 2 | Pick the maturity level | Decision | Level is recorded in the progress file |
| 3 | Write exit criteria as commands that pass or fail | Human | Each criterion maps to a command with an exit code |
| 4 | Set limits: max iterations, token or cost budget, wall-clock timeout | Human | Limits are in the loop config |
| 5 | List actions that need human approval (production migrations, data deletion, auth, shared contracts) | Decision | The loop pauses on each listed action |
| 6 | Run the loop: observe, plan, act, reflect, repeat | AI | Exit criteria pass, or a limit is hit |
| 7 | On a limit hit: stop, write what failed and why to the progress file | AI | A human can pick up from the file alone |
| 8 | Hand the result to [[04 Running Quality Gates]] as a normal PR | AI | PR open with the progress log linked |

## Behavioral evals for the loop

Test the harness itself, not only the final output ([[Behavioral Evaluations]]). Assert on what the agent did:

- Given an ambiguous task, it asks or reads ground truth instead of guessing.
- After it changes build config, it runs local checks before it reports done.
- On a failing check, it reads the error output before it edits code.
- It never edits or skips a test to make the check pass.

Run these on sample tasks when you change the instruction file, the tools, or the model.

## Gates

1. Every exit criterion passed on the last pass, as an exit code, not a claim.
2. No limit was silently exceeded.
3. Every approval-gated action has a recorded human approval.
4. The progress file explains each pass.

## Audit trail

The progress file: one entry per pass with the plan, the actions, the check results, and tokens used. Human approvals record who approved and when.

## Pitfalls

- **Loop before harness**: no tests or lint, so the loop has nothing to stop on.
- **"Are you done?" as the exit**: the model grades itself generously. Use exit codes.
- **No budget**: an unattended loop that cannot pass keeps spending.
- **Gaming the check**: the agent deletes or weakens a test to go green. Protect test files, or review test diffs separately.
- **Jumping to Level 3**: multi-day loops on a repo that cannot run a clean Level 1 loop.
- **Cognitive surrender**: accepting the loop's PR because it passed. Review it as you would any PR ([[05 Reviewing and Merging a PR]]).

## Escalation

- The loop hits its limit twice on the same task: the task or the spec is wrong. Return to [[02 Designing a Solution]].
- You need several loops at once, or a reviewer agent in the loop: use [[05 Running Parallel Agents]] (worktree per task, one remediation round).
- The agent keeps breaking the same rule: turn the rule into a deterministic check, not a longer instruction ([[Inverse Pyramid of Constraints]]).

## Related

- [[Loop Engineering]]
- [[Harness Engineering]]
- [[Feedforward Guides and Feedback Sensors]]
- [[Verification Density]]
- [[Behavioral Evaluations]]
- [[Cognitive Debt in Agentic Coding]]
- [[AFK Agent Execution]]
- [[AI Work Autonomy Spectrum]]
- [[03 Building a Task]]
- [[05 Running Parallel Agents]]
- [[Implement-Review-Remediate Loop]]
- [[Playbook Template]]

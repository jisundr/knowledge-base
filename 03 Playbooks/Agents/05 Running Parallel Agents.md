---
type: playbook
status: draft
tags: [playbook, ai-agents, orchestration, multi-agent, git]
---

# Playbook - Running Parallel Agents

Use when one agent at a time is the bottleneck: you want several agents on separate tasks, or two agents racing on one task, and you steer the work yourself. Outcome: parallel work that does not collide, hands off through Git, stops after one fix round, and leaves risky actions to a human. Pattern: [[Implement-Review-Remediate Loop]] in a local [[Agent Development Environment (ADE)]]. For always-on bots that start work from events and schedules, see [[06 Using Bots]].

## Trigger

- The [[Task Graph Backlog]] has several ready tasks with no dependencies between them.
- You want to compare two agents or models on the same prompt.

## Principles applied

- **Isolate before you parallelize**: one task, one [[Git Worktree Isolation for Parallel Agents|worktree]] (or container). Never two agents in one working directory.
- **Git is the shared state**: agents hand off through branches, commits, and diffs, not chat transcripts.
- **One remediation round, then a human**: stops implementer and reviewer agents from looping forever.
- **Same bar for agents and humans**: every agent PR goes through [[04 Running Quality Gates]] and [[05 Reviewing and Merging a PR]].

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Create worktrees, implement, run checks, review another agent's diff, fix once |
| Human does | Pick tasks to run in parallel, write specs and exit checks, set quotas and permissions, read escalations |
| Human decides | Approval of high-risk actions, which result wins a race, merges |

## Tooling

An ADE such as Orca automates the setup: a worktree per task, repo rules from `AGENTS.md` / `CLAUDE.md`, one-click check commands, usage per model account, and a preview browser. Without one, run `git worktree add` per task and keep one terminal per agent.

## Steps

| # | Step | Owner (AI / Human / Decision) | Done when |
| --- | --- | --- | --- |
| 1 | Choose the tasks to run in parallel: ready, independent, each with a spec or acceptance criteria | Decision | Task list with no shared files or ordering |
| 2 | Run the harness readiness check from [[04 Running an Agent Loop]] | AI | Every row passes |
| 3 | Define the checks as quick commands (build, test, lint) with exit codes | Human | One command per check, same for every agent |
| 4 | Set permissions: list actions that need human approval (deploy, production data, auth, public posts) | Decision | Agents pause on each listed action, even if launched with permission-bypass flags |
| 5 | Check quota across model accounts and route tasks to the account with room | AI | No task starts on an exhausted quota |
| 6 | Implement: one builder agent per task, in its own worktree or container | AI | Branch with commits, local checks green |
| 7 | Verify against a real instance: preview deploy plus smoke and regression tests | AI | Test run attached to the PR |
| 8 | Review: a separate reviewer agent reads the diff, test logs, and visual proof | AI | Findings posted on the PR |
| 9 | Remediate once: the builder fixes the findings, checks re-run | AI | Green and reviewer agrees, or escalated |
| 10 | Escalate if still red or disputed after one round | AI | Human gets the PR, findings, and what was tried |
| 11 | Hand the PR to [[05 Reviewing and Merging a PR]] | Decision | PR in the human review queue |
| 12 | Clean up worktrees and branches | AI | No stale worktrees |

## UI work: point, don't describe

For frontend tasks, attach the element instead of describing it ([[Visual Element Annotation for Agents]]): select it in the preview browser to send its HTML, CSS, selector, and screenshot. Batch annotations, and mark each as a command (do it) or a question (suggest).

## Gates

1. Each task ran in its own worktree or container.
2. Every check passed as an exit code on the final run.
3. At most one remediation round happened; anything beyond that went to a human.
4. Every approval-gated action has a recorded human approval.

## Audit trail

Per task: branch, worktree, agent and model used, check results, reviewer findings, the remediation round, and escalation if any.

## Pitfalls

- **Shared working directory**: two agents overwrite each other's files. Always one worktree per task.
- **Parallel tasks that are not independent**: merge conflicts and contradictory designs. Check the task graph first.
- **Chat as handoff**: long transcripts lose detail and fill context. Hand off with diffs and commits.
- **Endless review ping-pong**: no remediation cap, so tokens burn on minor findings.
- **Agent-claimed verification**: the agent says tests pass. Use the quick commands and read the exit code.
- **Permission bypass by default**: orchestrators may launch agents with flags like `--dangerously-skip-permissions`. Keep the approval list in step 4.
- **Too many PRs to review**: parallel output exceeds human review capacity, which leads to rubber-stamping ([[Cognitive Debt in Agentic Coding]]). Limit concurrent tasks to what you can review.

## Escalation

- A task escalates twice: the spec is wrong. Return to [[02 Designing a Solution]].
- Agents keep colliding on the same files: the tasks are not independent. Re-split them in the task graph.
- The same kind of task keeps coming back and needs no steering: hand it to a bot ([[06 Using Bots]]).

## Related

- [[Implement-Review-Remediate Loop]]
- [[Git Worktree Isolation for Parallel Agents]]
- [[Agent Development Environment (ADE)]]
- [[Cloud Agent Fleet vs Local Worktree Orchestrator]]
- [[Multi-Agent Orchestration Patterns]]
- [[04 Running an Agent Loop]]
- [[06 Using Bots]]
- [[03 Building a Task]]
- [[Playbook Template]]

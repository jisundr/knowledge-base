---
type: topic
tags: [ai-engineering, ai-agents, loop-engineering, orchestration, automation]
---

# Loop Engineering

Writing the orchestration that prompts the agent, instead of prompting it by hand. The loop triggers the agent, splits work, checks results, and carries memory forward. It is the top layer of the stack and only works on a solid [[Harness Engineering|harness]].

## The loop

A state machine that repeats until checks pass or a safety limit is hit:

1. **Observe**: read code state, error logs, test output.
2. **Plan**: break the task down or pick the next tool step.
3. **Act**: edit code, run migrations, write tests.
4. **Reflect**: compare the outcome against verification gates.

Exit on deterministic signals, not on the model saying it is done. See [[Verification Density]].

## Maturity levels

| Level | Shape | Example |
| --- | --- | --- |
| 1. Simple loop | One narrow task, few iterations | Auto-fix lint errors, max 5 passes |
| 2. Task decomposition | Plans sub-tasks, edits files, runs integration tests, reflects on failures | A feature split into steps |
| 3. Autonomous multi-day harness | Isolated Git worktrees, persistent memory file ("the spine"), token budgets, error recovery, human approval gates for risky actions | Unattended runs across days |

Level 3 is what [[Long-Running Agent Harness]] and the [[Ralph Loop]] describe.

## Risks

Unattended loops can burn compute and drift from intent. Guard with budgets, approval gates, [[Behavioral Evaluations]], and human checkpoints against [[Cognitive Debt in Agentic Coding]].

## Related

- [[AFK Agent Execution]]
- [[AI Work Autonomy Spectrum]]
- [[Multi-Agent Orchestration Patterns]]
- [[Self-Verification Loop]]

## Sources

- [[20261123164745 Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding|Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding]]

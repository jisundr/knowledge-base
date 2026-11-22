---
type: topic
tags: [ai-engineering, ai-agents, automation, orchestration]
---

# Ralph Loop

An autonomous loop that keeps a coding agent working across session resets: pick ready work, do it, get it checked, record what was learned, repeat.

## Parts

- **External task graph**: a repo-native task store with blocking dependencies (e.g., Steve Yegge's Beads, `bd`). The agent asks for unblocked work (`bd ready`). See [[Task Graph Backlog]].
- **Claims and leases**: an agent claims a task atomically and holds it with a heartbeat, so two agents never work the same issue.
- **Persistent memory**: lessons go to the tracker or `AGENTS.md` and are loaded into the next session's briefing. See [[Agent Memory]].
- **Evaluator separation**: a separate judge or test harness checks acceptance criteria; on failure it rejects "done" and sends the agent back into the loop. See [[Evaluator Cascade]].

## Related

- [[Long-Running Agent Harness]]
- [[AFK Agent Execution]]
- [[Test-Driven Development for Agents]]

## Sources

- [[20261122123529 From Problem-First Discovery to Spec-Driven AI Execution|From Problem-First Discovery to Spec-Driven AI Execution]]

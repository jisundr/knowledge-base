---
type: topic
tags: [ai-engineering, ai-agents, orchestration, verification]
---

# Implement-Review-Remediate Loop

A multi-agent pipeline pattern with a hard stop on back-and-forth.

1. **Implement**: an orchestrator hands a spec or card to a builder agent in an isolated container or [[Git Worktree Isolation for Parallel Agents|worktree]].
2. **Hand off via Git**: commits, branches, and diffs are the shared state, not long chat transcripts.
3. **Verify**: automated tests run against a real instance (e.g. PR preview deploys plus headless-browser smoke and regression tests).
4. **Review**: a separate reviewer agent reads the diff, test logs, and visual proof.
5. **One-remediation cap**: the implementer gets one fix round. If tests still fail or the reviewer still objects, the pipeline pauses and escalates to a human.

The cap stops reviewer and implementer from looping forever over minor findings and wasting tokens.

## Related

- [[Loop Engineering]]
- [[Verification Density]]
- [[Multi-Agent Orchestration Patterns]]
- [[Self-Verification Loop]]
- [[LLM-as-a-Judge]]
- [[AI Work Autonomy Spectrum]]

## Sources

- [[20261123172458 Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE|Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE]]

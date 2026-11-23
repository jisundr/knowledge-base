---
type: topic
tags: [ai-engineering, ai-agents, verification, loop-engineering]
---

# Verification Density

Anchoring an agent loop in many objective checks rather than in the model's own report of success. The loop never asks "did you finish?"; it ends only on deterministic signals such as the test suite returning exit code 0.

Early autonomous agents failed largely because they trusted self-reports, and models grade their own work generously (see [[Long-Running Agent Harness]]).

## In practice

- Define exit criteria as commands that pass or fail (tests, type-check, lint, build).
- Check often, at each step of the loop, not only at the end.
- Keep the judge separate from the worker (see [[Ralph Loop]] and [[Evaluator Cascade]]).

## Related

- [[Loop Engineering]]
- [[Feedforward Guides and Feedback Sensors]]
- [[Test-Driven Development for Agents]]
- [[Self-Verification Loop]]
- [[Agent Verification Stack]]

## Sources

- [[20261123164745 Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding|Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding]]

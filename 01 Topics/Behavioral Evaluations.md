---
type: topic
tags: [ai-engineering, evaluation, ai-agents, harness-engineering]
---

# Behavioral Evaluations

Evals that assert on an agent's intermediate actions rather than only its final output. They act like unit tests for the harness, where end-to-end benchmarks act like a final exam: the benchmark says pass or fail, the behavioral eval says why. Promoted by Google engineers Taylor Mullen and Christian Gunderman.

## Example assertions

- Given an ambiguous prompt, does the agent check ground truth or ask, instead of guessing?
- When it changes build configuration, does it run local validation before calling the task done?

Assertions like these are checked against the agent's trace of tool calls (see the Trace unit in [[AI System Evaluation]]).

## Related

- [[AI System Evaluation]]
- [[Evaluation Error Analysis Flywheel]]
- [[Harness Engineering]]
- [[Loop Engineering]]

## Sources

- [[20261123164745 Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding|Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding]]

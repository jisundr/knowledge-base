---
type: topic
tags: [ai-engineering, ai-agents, agent-skills, verification]
---

# Self-Verification Loop

A step built into a skill or workflow where the agent checks and revises its own output before showing it to the user. Rule of thumb: the user's first look should be the agent's fourth or fifth internal pass, not its first draft.

## Ways to verify

- **Visual inspection**: render the output (e.g., slides as images), look for cropped or overlapping content, fix, and render again.
- **Deterministic checks**: run tests or validation scripts before calling the task done. See [[Test-Driven Development for Agents]].
- **Critique persona**: a sub-agent with a critical role (e.g., a skeptical buyer) reviews subjective work such as copy, lists friction points, and the agent revises.

Prefer deterministic checks where they exist; use critique personas only where no objective check is possible ([[Inverse Pyramid of Constraints]]).

## Related

- [[Agent Skills]]
- [[Agent Verification Stack]]: the same idea at team and pipeline scale.
- [[LLM-as-a-Judge]]: the risks of model-based critique.
- [[Ralph Loop]]

## Sources

- [[20261122181902 Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks|Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks]]

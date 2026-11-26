---
type: topic
tags: [ai-engineering, ai-agents, harness-engineering, verification]
---

# Feedforward Guides and Feedback Sensors

A way to classify the controls in a [[Harness Engineering|harness]], borrowed from cybernetics (framed by Birgitta Böckeler, Thoughtworks).

- **Feedforward guides** steer the agent *before* it acts: architecture maps, `CLAUDE.md` / `AGENTS.md`, schemas, module templates, specs.
- **Feedback sensors** observe output *after* it acts and return signals the agent can self-correct from: test runners, linters, type-checkers, pre-commit hooks, review sub-agents.

Analogy: guides are the driving manual and road signs; sensors are the rumble strips and speedometer.

## Computational vs inferential

Both kinds of control can run in one of two ways:

| | Computational | Inferential |
| --- | --- | --- |
| Nature | Deterministic, CPU-bound | Probabilistic, LLM-bound |
| Examples | Type-checkers, unit tests, static linters, architecture tests (ArchUnit) | AI code review, [[LLM-as-a-Judge]] |
| Cost and speed | Near zero, milliseconds | Higher cost, slower |
| Good for | Rules that can be stated exactly | Semantic checks, e.g. "does this match the requirement?" |

Prefer computational controls where they exist and keep inferential ones for what cannot be checked exactly. See [[Inverse Pyramid of Constraints]] and [[Evaluator Cascade]].

## Related

- [[Context Pointers]]: a lean way to write feedforward guides.
- [[Self-Verification Loop]]
- [[Verification Density]]
- [[Software Promises]]

## Sources

- [[20261123164745 Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding|Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding]]
- [[20261127074619 Stop Building Software Factories — Architecting Brownfield & Demand Systems|Stop Building Software Factories — Architecting Brownfield & Demand Systems]]

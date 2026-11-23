---
type: topic
tags: [explainability, ai-agents, evaluation]
---

# Model-Based vs Model-Free Explanations

Two ways an agent can explain a decision to a human reviewer, studied in [[After-Action Review for AI (AAR-AI)]] research.

| | Model-Free | Model-Based |
| --- | --- | --- |
| Shows | A "search stump": each available action with one value score | A search tree: predicted future states, opponent or environment responses, heuristic values at the leaves |
| Reviewer can | Disagree with the high-level strategy | Check each predicted state and find the exact wrong step |
| Cost | Easy to read | Higher mental load at first |

## Empirical falsification

The value of a model-based explanation is that it makes the agent's reasoning falsifiable. An assessor can point at a wrong prediction (a mispredicted opponent move, a bad state assessment) and show where the logic broke. Result: better reflection by the reviewer and more precise bug reports, at the cost of more effort.

The same idea applies to LLM agents: a full trace (see the Trace unit in [[AI System Evaluation]]) supports falsification; a bare final answer does not.

## Related

- [[AI Evaluation System Pillars]]: explainability as one pillar.
- [[Behavioral Evaluations]]

## Sources

- [[20261123170538 Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews|Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews]]

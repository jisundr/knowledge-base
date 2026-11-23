---
type: topic
tags: [ai-agents, evaluation, explainability, human-in-the-loop]
---

# After-Action Review for AI (AAR/AI)

A structured debrief, adapted from the U.S. Army's After-Action Review, by Dodge et al. (Oregon State University, ACM TiiS 2021), that lets a domain expert judge an AI agent's sequential decisions. The assessor walks an "inner loop" of four questions at each decision point.

## The inner loop

1. **Expected**: what did I expect the agent to do next?
2. **Actual**: what did it choose, and what state changes followed?
3. **Why**: what does the agent's explanation say about the choice?
4. **Learn**: would I let it make this kind of decision on its own, or does the policy need to change?

Step 4 turns a review into an autonomy decision, which ties AAR/AI to the [[AI Work Autonomy Spectrum]].

## Explanation type matters

How deep the agent's explanation goes decides what the assessor can find. A shallow score list only supports strategy disagreements; a search tree of predicted future states lets the assessor disprove the agent's reasoning. See [[Model-Based vs Model-Free Explanations]].

## Related

- [[Behavioral Evaluations]]: also judge the steps, not only the outcome.
- [[AI System Evaluation]]
- [[Blameless Post-Incident Review (PIR)]]: the same "review what happened and why" shape, for systems and teams.

## Sources

- [[20261123170538 Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews|Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews]]

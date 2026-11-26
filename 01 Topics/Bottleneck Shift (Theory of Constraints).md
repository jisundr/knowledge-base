---
type: topic
tags: [ai-engineering, ai-agents, sdlc, code-review, delivery]
---

# Bottleneck Shift (Theory of Constraints)

Goldratt's **Theory of Constraints** (*The Goal*, 1984): a system's output is limited by a very small number of constraints. Speeding up a step that is not the bottleneck does not make the system faster; work just piles up in front of the next constraint.

Applied to agentic coding: agents made writing code nearly free, so the constraint moved downstream to **code review** and contextual verification. Engineers with agents produce about 8x more code (741% more), but ship features only about 30% faster.

## Why review becomes the constraint

- **Human limits**: reviewer accuracy drops after roughly 450 lines of code per hour (Cisco study), so a 10,000-line agent diff is more than a week of focused review.
- **AI reviewers disagree**: four leading AI reviewers on the same codebase each found real bugs, but no two agreed on any single bug.
- **Tests miss unwritten context**: see [[Mergeability Gap]].

The long-run constraint, once review and operations are automated too, is defining what "good" means: see [[Accidental vs Essential Complexity]].

## Past review: demand

Once production and review are cheap, the next constraint can be demand itself: a glut of software customers did not ask for. See [[Demand Factory]].

## Related

- [[Risk-Classified PR Routing]]
- [[Blast-Radius Code Review]]
- [[Shipped Value Metrics]]
- [[Agent Verification Stack]]
- [[Cognitive Debt in Agentic Coding]]
- [[Agentic SDLC]]
- [[Demand Factory]]

## Sources

- [[20261126153108 AI Writes the Code - The Rise of the Product Engineer|AI Writes the Code - The Rise of the Product Engineer]]
- [[20261126155209 How Anthropic Builds Software with AI Agents|How Anthropic Builds Software with AI Agents]]
- [[20261127074619 Stop Building Software Factories — Architecting Brownfield & Demand Systems|Stop Building Software Factories — Architecting Brownfield & Demand Systems]]

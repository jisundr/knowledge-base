---
type: topic
tags: [code-review, ai-agents, human-in-the-loop, sdlc]
---

# Blast-Radius Code Review

Stop manually reviewing routine agent-written code and spend human review only where a mistake would do the most damage: core architectural boundaries and high-risk security surfaces.

It responds to review becoming the constraint ([[Bottleneck Shift (Theory of Constraints)]]). The rest of the code is covered by team standards written as machine-readable specs and eval rubrics that AI reviewers enforce. The source cites Amazon going back to mandatory senior sign-off after outages caused by agent code that skipped careful human review, a reminder that the high-risk paths still need a person.

Anthropic applies this with [[Risk-Classified PR Routing]]: a classifier sends mechanical PRs to an LLM reviewer and auto-merge, and high-risk PRs to mandatory human review.

## Related

- [[Risk-Classified PR Routing]]
- [[Human-in-the-Loop Approval Gates]]
- [[Agent Verification Stack]]
- [[Inverse Pyramid of Constraints]]
- [[Mergeability Gap]]
- [[Shipped Value Metrics]]

## Sources

- [[20261126153108 AI Writes the Code - The Rise of the Product Engineer|AI Writes the Code - The Rise of the Product Engineer]]
- [[20261126155209 How Anthropic Builds Software with AI Agents|How Anthropic Builds Software with AI Agents]]

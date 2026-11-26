---
type: topic
tags: [ai-engineering, ai-agents, code-review, evaluation]
---

# Mergeability Gap

The difference between how often agent-written pull requests pass their tests and how often maintainers would actually merge them. In a Cognition benchmark, a model passed unit test suites 87% of the time, but maintainers were willing to merge only 54% of those PRs.

The gap exists because unit tests check only explicit assertions. Maintainers also judge unwritten context: code style, architectural side effects, historical design decisions, and external dependencies that live only in people's heads.

Closing it means writing that context down as specs and eval rubrics that machines can check (see [[Spec-Driven Development]] and [[AI System Evaluation]]), and tracking merge-acceptance rate as a metric ([[Shipped Value Metrics]]).

## Related

- [[Bottleneck Shift (Theory of Constraints)]]
- [[Verification Density]]
- [[Durable Facts in Native Homes]]

## Sources

- [[20261126153108 AI Writes the Code - The Rise of the Product Engineer|AI Writes the Code - The Rise of the Product Engineer]]

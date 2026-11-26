---
type: topic
tags: [ai-engineering, ai-agents, human-in-the-loop, code-review]
---

# Cognitive Debt in Agentic Coding

The human-side costs that build up when agent loops write most of the code and people mostly review it.

- **Comprehension debt**: the gap between how much code is in the repo and how much the team actually understands.
- **Intent debt**: lost rationale behind decisions, leaving code that works but drifts from the product's long-term direction. Records such as [[Architecture Decision Record (ADR)]] help keep it.
- **Cognitive surrender**: reviewers stop thinking critically and accept whatever diff the loop produces.

## Mitigations

- Human approval gates at high-risk points (e.g., production migrations).
- Hard verification standards so review starts from evidence (see [[Agent Verification Stack]] and [[Verification Density]]).
- Keep a human "day shift" for planning and review (see [[AFK Agent Execution]]).

## Related

- [[Loop Engineering]]
- [[AI Work Autonomy Spectrum]]
- [[Product-Minded Engineer]]
- [[Bottleneck Shift (Theory of Constraints)]]
- [[Blast-Radius Code Review]]

## Sources

- [[20261123164745 Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding|Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding]]
- [[20261126153108 AI Writes the Code - The Rise of the Product Engineer|AI Writes the Code - The Rise of the Product Engineer]]

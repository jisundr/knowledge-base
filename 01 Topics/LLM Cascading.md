---
type: topic
tags: [ai-engineering, llm-routing, cost-optimization, inference]
---

# LLM Cascading

Post-generation routing: run the prompt on a cheap model first, check the answer, and escalate to a larger model only when the check fails.

1. **Start cheap**: a small, fast model generates an answer.
2. **Evaluate**: [[LLM Evaluation Glossary#Post-hoc quality estimation|post-hoc quality estimation]] scores it (confidence, token log-probabilities, a self-verification pass).
3. **Pass or escalate**: return a good-enough answer; otherwise send the prompt one step up the model ladder.

## Trade-offs

- Judges real output rather than a prediction from the prompt, so it catches hard queries that look easy.
- Escalated queries pay twice in latency and tokens, because models run in sequence.
- Classic cascades follow a fixed small-to-large chain. [[Cascade Routing]] removes that restriction.

Same cheap-first shape as the [[Evaluator Cascade]], applied to generation instead of scoring.

## Related

- [[LLM Routing]]
- [[Cascade Routing]]
- [[LLM Routing in Production]]

## Sources

- [[20261122093737 Smart AI Traffic Control - A Beginner's Guide to LLM Routing and Cascading|Smart AI Traffic Control - A Beginner's Guide to LLM Routing and Cascading]]

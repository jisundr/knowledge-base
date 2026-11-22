---
type: topic
tags: [ai-engineering, caching, cost-optimization, inference, embeddings]
---

# Semantic Caching

A response cache keyed on meaning rather than exact text. The incoming prompt is embedded and compared against previously answered prompts; above a similarity threshold, the stored answer is returned with no model call.

- Placed **in front of** the router: a hit costs neither routing nor generation.
- Matches paraphrases ("How much do I owe?" vs "What is my current balance?"), which exact-match caches miss.
- The similarity threshold is the main tuning knob: too loose returns wrong answers, too strict rarely hits.

Built on [[Embeddings and Vector Search]].

## Related

- [[LLM Routing in Production]]
- [[LLM Routing]]

## Sources

- [[20261122093737 Smart AI Traffic Control - A Beginner's Guide to LLM Routing and Cascading|Smart AI Traffic Control - A Beginner's Guide to LLM Routing and Cascading]]

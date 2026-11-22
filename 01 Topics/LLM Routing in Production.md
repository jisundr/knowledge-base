---
type: topic
tags: [ai-engineering, llm-routing, deployment, reliability]
---

# LLM Routing in Production

Infrastructure rules that keep a model router from erasing its own savings.

1. **Cache before you route**: put [[Semantic Caching]] first, so repeat questions skip routing and generation.
2. **Keep the hot path cheap**: in-memory rules or small embedding classifiers, with dispatch latency in the ~10-20 ms range. A slow router cancels the speed gain of a small model.
3. **Circuit breakers and failover**: on provider outages or `429 Too Many Requests`, trip a breaker and fail over to a backup provider automatically.
4. **Start simple, then learn**: begin with rules plus caching, log real traffic, and train predictive routers only once you have enough preference data.

## Related

- [[LLM Routing]]
- [[LLM Cascading]]
- [[Cascade Routing]]
- [[Containerization and Orchestration]]

## Sources

- [[20261122093737 Smart AI Traffic Control - A Beginner's Guide to LLM Routing and Cascading|Smart AI Traffic Control - A Beginner's Guide to LLM Routing and Cascading]]

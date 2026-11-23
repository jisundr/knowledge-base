---
type: topic
tags: [ai-engineering, ai-agents, observability, operations]
---

# Four-Layer AI Observability

Monitor an agent system at four layers, ideally with OpenTelemetry semantic conventions so traces join up.

| Layer | What to track |
| --- | --- |
| Application | User gateways, microservices, and databases the agent calls |
| Agentic | Reasoning spans, tool calls, context compaction, retrieval relevance, steps per task |
| Model | Time to first token (TTFT), tokens per second, reasoning tokens, prompt-cache hits |
| Infrastructure | CPU/GPU memory, vector store latency, KV cache evictions, container restarts |

The agentic layer is the one classic APM lacks; it catches runaway tool loops and step-count blowups.

## Related

- [[AI Control Plane]]
- [[Request-Level Evidence Capture]]
- [[Prefix Caching]]
- [[Model Drift Detection]]
- [[Multi-Agent Orchestration Patterns]]

## Sources

- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

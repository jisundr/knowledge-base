---
type: topic
tags: [ai-engineering, llm-routing, cost-optimization, inference]
---

# Cascade Routing

A unified framework that merges [[LLM Routing]] and [[LLM Cascading]]: choose the starting model from the prompt, then reroute based on the quality of the answer.

- **Flexible first dispatch**: a hard prompt can go straight to a medium or large model instead of always starting at the smallest (ex-ante estimate).
- **Rerouting, not a fixed chain**: a weak answer moves to whichever candidate model now looks best, using updated post-hoc estimates.
- **Pruning**: skips model steps whose expected quality gain does not justify the cost.

Formalized in the paper *A Unified Approach to Routing and Cascading for LLMs* (Dekoninck, Baader, Vechev). Reported to beat plain routing and threshold cascades on quality-cost benchmarks such as [[LLM Evaluation Glossary#RouterBench|RouterBench]] and [[LLM Evaluation Glossary#SWE-bench|SWE-bench]] (claim from the source lesson; not verified here).

Ex-ante and post-hoc estimation are defined in [[LLM Evaluation Glossary]].

## Related

- [[LLM Routing]]
- [[LLM Cascading]]
- [[LLM Routing in Production]]

## Sources

- [[20261122093737 Smart AI Traffic Control - A Beginner's Guide to LLM Routing and Cascading|Smart AI Traffic Control - A Beginner's Guide to LLM Routing and Cascading]]

---
type: topic
tags: [ai-engineering, llm-routing, cost-optimization, inference]
---

# LLM Routing

Pre-generation routing: inspect each prompt *before* any tokens are generated and send it to the cheapest model that can reliably answer it. Frontier models handle hard reasoning; lightweight models handle simple lookups and summaries.

The router's job is [[LLM Evaluation Glossary#Ex-ante quality estimation|ex-ante quality estimation]]: predict query difficulty from the prompt alone.

## Strategies

| Strategy | How it decides | Strength | Weakness |
| --- | --- | --- | --- |
| Rule-based | Keywords, prompt length, regex | Fast, easy to debug | Brittle to unexpected phrasing |
| Semantic / embedding | Distance from the prompt's vector to known category centroids | Paraphrases land together | Needs labeled example categories |
| Domain classification | Subject area (medical, legal, math) | Sends work to specialist models | Only as good as the taxonomy |
| Predictive / classifier | Model trained on past traffic predicts per-model answer quality, traded off against cost | Optimizes quality per dollar | Needs logged preference data |

Semantic routing reuses [[Embeddings and Vector Search]].

A related axis is routing by **token budget**: send short prompts with short expected answers to high-concurrency serving pools and long ones to deep-capacity pools (see [[LLM Evaluation Glossary#Dual-pool token routing|dual-pool token routing]]).

## Limits

When difficulty cannot be read from the prompt, routing guesses wrong. [[LLM Cascading]] judges the actual answer instead, and [[Cascade Routing]] combines both.

## Related

- [[LLM Cascading]]
- [[Cascade Routing]]
- [[LLM Routing in Production]]
- [[Semantic Caching]]
- [[01 Adding Model Routing]] (playbook)

## Sources

- [[20261122093737 Smart AI Traffic Control - A Beginner's Guide to LLM Routing and Cascading|Smart AI Traffic Control - A Beginner's Guide to LLM Routing and Cascading]]

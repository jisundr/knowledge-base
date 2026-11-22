---
type: topic
tags: [ai-engineering, inference-cost, context-engineering]
---

# Prefix Caching

A provider-side optimization: when consecutive requests start with an identical prefix (system prompt plus early conversation), the provider skips re-processing that block and bills it as cheap **cache tokens**.

Because harnesses re-send the full history every turn ([[Model and Harness Separation]]), a stable prefix is what keeps long sessions affordable.

## What breaks it

Any change early in the context invalidates everything after it:

- Injecting timestamps or other dynamic values into the system prompt.
- Rewriting or reordering early conversation history.

After a break, every later turn pays full input price.

## Related

- [[Semantic Caching]] (application-level cache keyed on meaning, not exact prefix)
- [[Context Engineering]]
- [[LLM Routing in Production]]

## Sources

- [[20261122155021 Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern|Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern]]

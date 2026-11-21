---
type: topic
tags: [ai-engineering, context-engineering, llm-limits]
---

# Smart Zone and Dumb Zone

A model's reasoning quality is not uniform across a session (framing attributed to Dex Horthy of HumanLayer). A fresh context is the **smart zone**; once the window fills, attention degrades and the model enters the **dumb zone**, making careless mistakes.

- Attention cost grows quadratically with token count, so focus drops off around **~100k tokens** (roughly 40% of the window), whatever the advertised limit.
- **Compacting** (summarizing history into a header) leaves low-signal "sediment" that accumulates over time.

## The Memento approach

Treat the agent as resetting to a blank slate each session, and design for it:

- Keep system prompts small.
- Run each tight task in a fresh context window.
- Push exploratory research to **sub-agents** with isolated contexts that return short summaries to the orchestrator.

## Related

- [[Context Engineering]]
- [[Lost in the Middle]]
- [[Ubiquitous Language]]
- [[AFK Agent Execution]]

## Sources

- [[20261121222850 Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture|Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture]]

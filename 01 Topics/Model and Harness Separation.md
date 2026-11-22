---
type: topic
tags: [ai-engineering, ai-agents, llm-fundamentals, context-engineering]
---

# Model and Harness Separation

An AI coding setup has two distinct parts:

- **Model**: frozen parameters (weights) that do one thing, next-token prediction. It cannot read files, run commands, or remember anything on its own.
- **Harness**: the runtime around it (Claude Code, Cursor, Codex CLI). It holds conversation history, executes tool calls, and feeds results back to the model in a loop. Everything that feels "agentic" lives here.

## Models are stateless

Nothing in a session changes the weights. An agent seems to remember only because the harness re-sends the whole history on every provider request. So every turn pays again for everything already in context, which makes context size both a cost and a quality problem.

## Token arithmetic

- **Input tokens**: everything the model reads (system prompt, history, tool results).
- **Output tokens**: what it writes. More compute per token, typically billed at several times the input rate.
- Repeated input is made cheaper by [[Prefix Caching]].

## Related

- [[AI Agents and Tool Use]]
- [[Context Engineering]]
- [[Smart Zone and Dumb Zone]]
- [[Long-Running Agent Harness]]
- [[Agent Memory]]

## Sources

- [[20261122155021 Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern|Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern]]

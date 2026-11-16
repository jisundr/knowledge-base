---
type: topic
tags: [ai-engineering, ai-agents, context-engineering]
---

# Context Engineering

Deliberately managing what goes into an agent's context window so that raw model intelligence compounds instead of being wasted. Model upgrades alone do not compound performance; tailored organizational context acts as a multiplier.

## Evolution of techniques

1. **Static instruction files**: markdown such as `CLAUDE.md` injected at session start. Very effective for steering behavior, but suffers **context bloat** as files grow.
2. **In-band memory tools**: the agent decides when to read, write, and update memory during a session. See [[Agent Memory]].
3. **Skills with progressive disclosure**: load metadata first, full body only when relevant. See [[Progressive Disclosure]].
4. **File systems as memory**: plain `bash`/`grep` over markdown files rather than bespoke APIs. See [[Agent Memory]].
5. **Out-of-band curation**: asynchronous batch review of fleet transcripts. See [[Dreaming (Agent Memory Consolidation)]].

## Related

- [[AI Agents and Tool Use]]
- [[Retrieval-Augmented Generation (RAG)]]
- [[Memory Guardrails for Multi-Agent Systems]]

## Sources

- [[Lamis Mukta - Learning while you sleep - Beyond memory to dreaming - AI Native DevCon June 2026]]

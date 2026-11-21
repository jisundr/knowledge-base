---
type: topic
tags: [ai-engineering, architecture, code-quality]
---

# Deep Modules

Modules that hide a lot of functionality behind a small, simple interface (John Ousterhout, *A Philosophy of Software Design*). The opposite, **shallow modules**, are many tiny files exporting small helpers with tangled dependencies.

Why it matters for agents: bad codebases make bad agents. Shallow modules force the agent through complex dependency graphs; deep modules let humans own the interface boundaries while agents fill in the internals. A skill like `/improve-codebase-architecture` can scan for places to deepen modules.

## Related

- [[Test-Driven Development for Agents]]
- [[AFK Agent Execution]]
- [[Categorical Elimination of Anti-Patterns]]
- [[Ubiquitous Language]]

## Sources

- [[20261121222850 Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture|Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture]]

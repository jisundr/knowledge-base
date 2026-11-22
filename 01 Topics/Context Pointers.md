---
type: topic
tags: [ai-engineering, ai-agents, context-engineering]
---

# Context Pointers

A one-line entry in an always-loaded file (such as `AGENTS.md`) that tells the agent *where* deeper information lives and *when* to read it, instead of including that information directly.

```
- For production releases or rollbacks: read internal/docs/deploy.md first.
```

The pointer costs almost nothing to keep in context; the agent makes a tool call to fetch the full document only when the task needs it. This is [[Progressive Disclosure]] applied to steering files.

## The trap it avoids

Stuffing `AGENTS.md` with full style guides and runbooks. That file is loaded on every turn, so a bloated version permanently eats token headroom and dilutes attention on every request.

## Pointers to pointers

When the pointer list itself grows too long (e.g., hundreds of repositories in a [[Home Repo Pattern]]), group pointers by domain and point to a per-domain file, read only when working in that domain.

## Related

- [[Progressive Disclosure]]
- [[Context Engineering]]
- [[Five-Layer Context Hierarchy]]
- [[Home Repo Pattern]]

## Sources

- [[20261122155021 Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern|Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern]]

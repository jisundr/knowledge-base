---
type: topic
tags: [ai-engineering, ai-agents, context-engineering]
---

# Context Loading Patterns

Four ways to decide *what* enters an agent's context and *when*, so quality holds across long, multi-step sessions. Each one applies [[Progressive Disclosure]].

1. **Index-first loading**: start the agent with an index of available files, not the files. The agent reads the index and asks only for the file the current subtask needs. See [[Progressive Disclosure Depth (Flat vs Hierarchical)]] for evidence that one index level works.
2. **Scout pattern**: a cheap pre-screening run reads the request, works out which resources it needs, and returns a loading manifest. The main agent loads only what is on the manifest.
3. **Phase-based loading**: split work into phases (research, planning, execution, review). Load only what the current phase needs, and clear or compact before the next phase.
4. **Process vs. reference separation**: keep `SKILL.md` to process steps (workflow, decisions, exit criteria). Put raw data, templates, and long reference material in separate files.

## Related

- [[Agent Skills]]
- [[Context Pointers]]: pointers are index-first loading inside `AGENTS.md`.
- [[Five-Layer Context Hierarchy]]: separates reference material from working artifacts in the same way.
- [[Smart Zone and Dumb Zone]]: why phases end with a clear or compact.
- [[Context Engineering]]

## Sources

- [[20261122181902 Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks|Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks]]

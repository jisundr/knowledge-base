---
type: topic
tags: [ai-engineering, ai-agents, context-engineering]
---

# Progressive Disclosure

Loading context in layers: a cheap summary first, the full content only when needed. In agent Skills, the front-matter metadata (a few sentences) is scanned up front and the full skill body is loaded only when relevant. Like pulling one book off a shelf instead of carrying the whole library.

Controls context bloat while keeping deep procedural detail accessible.

## Skill loading stages

In [[Agent Skills]], disclosure runs in stages:

1. **Advertise** (~100 tokens per skill): only `name` and `description` sit in the system prompt at startup, so dozens of installed skills cost little.
2. **Load** (<5,000 tokens recommended): when a request matches a description, the agent reads the full `SKILL.md`.
3. **Read resources** (as needed): files in `references/` or `assets/` are read only at the step that needs them.
4. **Run scripts** (off-context): bundled `scripts/` run, and only their output (e.g., "Validation passed") enters context, not the code.

The open spec names three levels (metadata, instructions, resources); some teaching material splits script execution out as a fourth stage.

How deep to go: one index level is enough; see [[Progressive Disclosure Depth (Flat vs Hierarchical)]].

## In steering files

The same idea keeps `AGENTS.md` lean: replace inline runbooks with [[Context Pointers]], one-line hints the agent follows with a tool call only when the task needs them. In a [[Home Repo Pattern|home repo]], repo pointers can be grouped by domain so the agent reads a domain's list only when working there.

## Related

- [[Context Engineering]]
- [[Agent Memory]]
- [[AI Agents and Tool Use]]
- [[Five-Layer Context Hierarchy]]
- [[Context Pointers]]
- [[Home Repo Pattern]]
- [[Agent Skills]]
- [[Progressive Disclosure Depth (Flat vs Hierarchical)]]
- [[Context Loading Patterns]]

## Sources

- [[20261116203029 Lamis Mukta - Learning while you sleep - Beyond memory to dreaming - AI Native DevCon June 2026|Lamis Mukta - Learning while you sleep - Beyond memory to dreaming - AI Native DevCon June 2026]]
- [[20261120075832 Interpretable Context Methodology|Interpretable Context Methodology]]
- [[20261122155021 Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern|Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern]]
- [[20261122181902 Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks|Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks]]

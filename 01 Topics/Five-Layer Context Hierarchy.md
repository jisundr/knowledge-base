---
type: topic
tags: [ai-engineering, ai-agents, context-engineering]
---

# Five-Layer Context Hierarchy

The context structure used by [[Interpretable Context Methodology (ICM)]], loaded progressively from global identity down to run-specific data.

| Layer | Question | Location | Size |
| --- | --- | --- | --- |
| 0 Global identity | Where am I? | root `CLAUDE.md` / `AGENTS.md` | ~800 tokens |
| 1 Workspace routing | Where do I go? | root `CONTEXT.md` | ~300 tokens |
| 2 Stage contract | What do I do? | stage folder `CONTEXT.md` ([[Stage Contract]]) | 200-500 tokens |
| 3 Reference material ("factory") | What rules apply? | voice guides, design systems, templates | 500-2,000 tokens |
| 4 Working artifacts ("product") | What am I transforming? | raw inputs, prior stage outputs | varies |

Layer 3 is constraints the model internalizes; Layer 4 is data it transforms. Keeping them in separate folders spares the model from sorting rules from data. A stage runs in a 2,000 to 8,000 token window instead of a 40,000+ token monolithic prompt.

An application of [[Progressive Disclosure]] within [[Context Engineering]]; it counters [[Lost in the Middle]].

## Sources

- [[20261120075832 Interpretable Context Methodology|Interpretable Context Methodology]]

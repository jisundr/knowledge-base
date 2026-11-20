---
type: topic
tags: [ai-engineering, ai-agents, workflows]
---

# Stage Contract

The `CONTEXT.md` inside a stage folder in [[Interpretable Context Methodology (ICM)]] (Layer 2 of the [[Five-Layer Context Hierarchy]]). A three-part spec readable by both humans and models:

- **Inputs**: a table of exact file paths and section headers from Layer 3 references and Layer 4 predecessor outputs.
- **Process**: step-by-step instructions, including audit checks or creative checkpoints.
- **Outputs**: target path, filename slug, and format of the artifact.

Because outputs are plain Markdown/JSON on disk, each is an edit surface: a human can revise it before the next stage picks it up. Keep contracts under 80 lines.

## Related

- [[Statecharts and State Machines]]
- [[Context Engineering]]

## Sources

- [[20261120075832 Interpretable Context Methodology|Interpretable Context Methodology]]

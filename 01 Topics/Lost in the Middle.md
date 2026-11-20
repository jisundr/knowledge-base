---
type: topic
tags: [ai-engineering, context-engineering, llm-limits]
---

# Lost in the Middle

The finding that LLMs attend poorly to instructions buried in the centre of a long context window. Stuffing prompts, style guides, and history into one 30,000 to 50,000+ token prompt degrades output quality.

Mitigations: scope context tightly per task, as in the [[Five-Layer Context Hierarchy]], and load it in layers ([[Progressive Disclosure]]). Part of [[Context Engineering]].

## Sources

- [[20261120075832 Interpretable Context Methodology|Interpretable Context Methodology]]

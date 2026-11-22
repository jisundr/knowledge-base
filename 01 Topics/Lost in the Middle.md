---
type: topic
tags: [ai-engineering, context-engineering, llm-limits]
---

# Lost in the Middle

The finding that LLMs attend poorly to instructions buried in the centre of a long context window. Stuffing prompts, style guides, and history into one 30,000 to 50,000+ token prompt degrades output quality.

Accuracy follows a U-shaped curve by position: best for content at the start or end, worst in the middle.

Mitigations: scope context tightly per task, as in the [[Five-Layer Context Hierarchy]], and load it in layers ([[Progressive Disclosure]]). Part of [[Context Engineering]]. See also [[Smart Zone and Dumb Zone]], [[Agent Skills]], and [[Context Loading Patterns]].

## Sources

- [[20261120075832 Interpretable Context Methodology|Interpretable Context Methodology]]
- [[20261122181902 Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks|Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks]]

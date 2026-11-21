---
type: topic
tags: [ai-engineering, ai-agents, requirements, design]
---

# Grilling Session

A planning step where the agent interviews you, one question at a time, down every branch of the design tree before any code is written, until you and the model hold the same **design concept** (an idea from Frederick Brooks' *The Design of Design*). Run with skills such as `/grill-me` or `/grill-with-docs`.

Targets the biggest failure mode in human or AI development: **misalignment**. It replaces "spec-to-code" prompting, where a spec is handed over and the code is ignored; the code stays the thing you must understand.

Output: a shared design concept, a [[Ubiquitous Language]] glossary, and usually a PRD to break into [[Vertical Slices (Tracer Bullets)]].

## Related

- [[Agentic SDLC]]
- [[Task Graph Backlog]]

## Sources

- [[20261121222850 Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture|Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture]]

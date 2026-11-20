---
type: topic
tags: [ai-engineering, ai-agents, context-engineering, workflows]
---

# Interpretable Context Methodology (ICM)

A system-first architecture (Jake Van Clief and David McDermott) that orchestrates AI workflows with **filesystem structure instead of framework code**. A workflow is a tree of numbered stage folders holding plain Markdown; a single agent walks the tree and reads only what each stage needs.

## Principles

- **Folders over frameworks**: the filesystem is the state machine and control surface, replacing code-heavy orchestration (LangChain, AutoGen, CrewAI).
- **LLM as compiler, not chatbot**: each stage runs under a strict [[Stage Contract]] and emits a structured deliverable.
- **One stage, one job**: Unix-pipeline style, e.g. `01_research`, `02_script`, `03_production`.
- **Layered context loading**: a [[Five-Layer Context Hierarchy]] keeps each stage to roughly 2,000 to 8,000 tokens, avoiding [[Lost in the Middle]].
- **Every output is an edit surface**: intermediate files are plain text a human can inspect and edit before the next stage (glass-box observability). Edits tend to be heavy at stage 1, light mid-pipeline, heavy at the final stage.
- **Configure the factory, not the product**: persistent rules (Layer 3) are separated from run-specific data (Layer 4).

## Conventions

- Stage contracts under 80 lines, reference files under 200 lines.
- **Canonical sources pattern**: every fact has one authoritative home; other files point to it.

## Relation to MCP

Complementary: [[Model Context Protocol (MCP)]] handles dynamic tool/data connections at runtime; ICM organizes context statically. A stage contract can tell the agent to use an MCP connection.

## Limits

Not suited to real-time multi-agent loops, high-concurrency multi-tenant workloads, or heavy automated branching. Future directions: semantic debugging via section IDs, and suggesting Layer 3 updates from recurring human edits (edit-source principle).

## Related

- [[Context Engineering]]
- [[Progressive Disclosure]]
- [[Agent Memory]]
- [[Statecharts and State Machines]]

## To research

- Integrating ICM with a second brain / coding agents (Obsidian for memory, Graphify for connections, ICM for direction).

## Sources

- [[20261120075832 Interpretable Context Methodology|Interpretable Context Methodology]]

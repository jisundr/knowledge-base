---
type: topic
tags: [ai-engineering, ai-agents, agent-skills, context-engineering, benchmarks]
---

# Progressive Disclosure Depth (Flat vs Hierarchical)

How many routing levels a skill pack should have when an agent must navigate large documents. The finding from He et al. (arXiv, July 2026), on ∞Bench long-document tasks: **one level is enough**. A deeper second level never helped and sometimes broke accuracy.

## Three ways to package documents

- **Raw**: unindexed text files; the agent greps and reads on its own.
- **Flat**: one skill. Its description is always loaded, and its `SKILL.md` body is a table of contents that indexes chunk files in `references/`.
- **Hierarchical**: every chunk is its own skill under a meta-router, so every chunk description is always loaded.

## Results

- **One book**: flat matched or beat raw under the Pi and Claude Code harnesses, but added nothing under Codex (gpt-5.4-mini), which already greps well. Several gains were within noise. Progressive disclosure buys context management, not raw intelligence.
- **Library (up to 20 books)**: under raw navigation, English open QA fell to 0.26 even with Codex. Flat held it at 0.46, with about half the tokens per question.
- **Hierarchical**: accuracy dropped sharply in some cells (e.g., one multiple-choice run fell from 0.91 flat to 0.64). The paper blames the "always-loaded context tax": every chunk description sits in context all the time.

## Caveats

The authors list limits: one scaling axis, a fixed chunking recipe, gains that vary by task and language, and small samples. Read "one level is enough" as a strong default, not a proven optimum.

## Counter-evidence: choosing among many skills

AgentSkillOS (arXiv, 2026) tested a different problem: picking the right skill from libraries of 200 to 200,000 skills. There, capability trees (a hierarchy) beat flat lists, and the gap grew with library size. So the flat result applies to navigating one corpus behind a single index. For very large skill libraries, some hierarchy may be needed.

## Takeaway

Use one index level. A single table of contents lets the agent pick the right document before it spends its context window. Do not split each chunk into its own always-advertised skill.

## Related

- [[Progressive Disclosure]]
- [[Agent Skills]]
- [[Context Loading Patterns]]: index-first loading is the same idea.
- [[Lost in the Middle]]
- [[Smart Zone and Dumb Zone]]

## Sources

- [[20261122181902 Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks|Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks]]

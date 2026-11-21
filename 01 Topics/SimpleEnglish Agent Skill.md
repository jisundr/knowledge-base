---
type: topic
tags: [ai-agents, agent-skills, writing, controlled-language]
---

# SimpleEnglish Agent Skill

`AminBlg/SimpleEnglish`: an open-source agent skill (Claude Code, Cursor, Codex) that makes models write in an adapted form of [[Simplified Technical English (ASD-STE100)]].

## Skill vs. one-line system prompt

Critics argue a single "Use ASD-STE100" line in a system prompt does the same job. The case for a skill: a formal spec can be adapted to software artifacts and measured.

## Benchmark (author's own, Nov 2026)

- **Linter**: 81.3% fewer STE violations per 100 words, averaged over 9 Claude models x 8 writing tasks (144 generations). An earlier run (6 models, 96 generations, July 2026) reported 72.9%.
- **Tokens**: output tokens dropped on every model, which also cuts latency and cost.
- **Blind judge**: Claude Opus 4.8 compared skill vs. baseline text, in both orders. The skill won 62 of 72 pairs (6 ties, 4 losses).
- **Caveats**: the regex linter undercounts (no passive-voice detection); one generation per cell, so no variance data; a Claude judge scoring Claude output can carry family bias.

## Scope discipline

- **Use it for**: error messages, runbooks, release notes, incident reports, `AGENTS.md` and other agent instruction files.
- **Keep it away from**: marketing copy and blog posts, where emotion and persuasion matter more than one-meaning clarity.

## Related

- [[80% ASD-STE100 Prompting]]
- [[Progressive Disclosure]]: how skills load into context.
- [[Context Engineering]]

## Sources

- [[20261121234637 Mastering AI Output - From Aerospace Standards to Interactive Media|Mastering AI Output - From Aerospace Standards to Interactive Media]]

---
type: topic
tags: [prompting, writing, llm-output]
---

# 80% ASD-STE100 Prompting

A one-line prompt modifier, attributed to Andrej Karpathy: ask the model to follow [[Simplified Technical English (ASD-STE100)]] "about 80% of the way."

The standard's name works as a compressed style guide, because models already know it. One line replaces pages of style instructions. The "80%" softens it: the model drops filler, passive voice, hedging, and run-on sentences but keeps a natural tone instead of strict repair-manual prose.

Example modifier: `Explain [topic]. Follow ASD-STE100 about 80% of the way.`

Typical effect: one long hedged sentence becomes several short, direct ones with fewer words in total.

## Related

- [[Simplified Technical English (ASD-STE100)]]
- [[SimpleEnglish Agent Skill]]: the same idea packaged as an agent skill.
- [[AI Output Ladder]]: this is Tier 1.

## Sources

- [[20261121234637 Mastering AI Output - From Aerospace Standards to Interactive Media|Mastering AI Output - From Aerospace Standards to Interactive Media]]

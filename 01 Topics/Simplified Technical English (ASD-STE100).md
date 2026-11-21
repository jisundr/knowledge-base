---
type: topic
tags: [writing, controlled-language, prompting]
---

# Simplified Technical English (ASD-STE100)

A controlled-language standard from the European aerospace industry (AECMA, now ASD), built so aircraft maintenance instructions have one meaning only, even for readers working under time pressure in a second language.

## Core rules

- **Controlled vocabulary**: about 900 approved words, most fixed to one part of speech and one meaning ("close" is a verb only; the adjective is "near").
- **Length limits**: 20 words per instruction sentence, 25 per descriptive sentence, 6 sentences per paragraph.
- **Grammar**: active voice; no modal verbs such as *should*, *would*, *may*, *might*; no trailing `-ing` phrases.

## Trade-off

Full compliance reads as robotic outside repair procedures. It gives up tone and persuasion for unambiguous comprehension. For LLM prompting, a partial version works better: see [[80% ASD-STE100 Prompting]].

## Related

- [[80% ASD-STE100 Prompting]]
- [[SimpleEnglish Agent Skill]]
- [[Ubiquitous Language]]

## Sources

- [[20261121234637 Mastering AI Output - From Aerospace Standards to Interactive Media|Mastering AI Output - From Aerospace Standards to Interactive Media]]

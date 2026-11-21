---
type: topic
tags: [llm-output, prompting, learning]
---

# AI Output Ladder

Karpathy's four-tier hierarchy of output formats. Each tier is a richer medium than the last, so pick the lowest tier that makes the subject easy to grasp.

| Tier | Format | Prompt shape | Best for |
| --- | --- | --- | --- |
| 1 | Clean text | "Follow ASD-STE100 about 80% of the way." | Quick answers, docs, Q&A |
| 2 | Diagram | "Do not explain in text. Draw a diagram of X." | Architectures, flows, timelines, comparisons |
| 3 | Interactive HTML/JS | "Give me the output in HTML with interactive controls." | Quantitative relationships you want to vary yourself (sliders, calculators, dashboards) |
| 4 | Explainer video | "Create a 3Blue1Brown-style video on X," with AI narration | Deep understanding of abstract or mathematical topics |

The underlying idea: when code is cheap, you can generate [[Disposable Software Artifacts]] for understanding instead of reading text summaries.

## Related

- [[80% ASD-STE100 Prompting]]
- [[Disposable Software Artifacts]]
- [[Statecharts and State Machines]]: a Tier 2 view of behavior.

## Sources

- [[20261121234637 Mastering AI Output - From Aerospace Standards to Interactive Media|Mastering AI Output - From Aerospace Standards to Interactive Media]]

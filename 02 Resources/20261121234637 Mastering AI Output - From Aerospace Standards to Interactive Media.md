---
type: article-note
status: reviewed
created: 2026-11-21
tags: [prompting, llm-output, writing, controlled-language, agent-skills]
source: https://x.com/karpathy/status/2105819303471976479
---

Sources:

* Post: Andrej Karpathy on X - "We'll be spending a lot more time trying to understand the outputs of language models" [link](https://x.com/karpathy/status/2105819303471976479)
* Article: ASD-STE100 for AI Writing — Skill Cuts Slop 72.9% (explainx.ai) [link](https://explainx.ai/blog/asd-ste100-simplified-technical-english-ai-skill-2026)
* Article: ASD-STE100 Prompting: Karpathy's 4 Tricks for Clearer AI Answers [link](https://munderdiffl.in/blog/asd-ste100-prompting/)
* Repo: AminBlg/SimpleEnglish [link](https://github.com/AminBlg/SimpleEnglish)


Have you ever asked an AI model for a simple technical explanation, only to be buried under a mountain of fluff like *"Leveraging our robus architecture, user can seamlessly synchronize..."*? What if an aerospace standard originally written in the 1980s to keep aircraft mechanics from making fatal repair mistakes holds the key to eliminating verbose AI "slop"?

In this step-by-step guide, we will explore how aerospace writing constraints and multi-modal prompting strategies can radically improve how you consume AI outout. By the end of this lesson, you will be able to:

- **Apply** the ASD-STE100 standard (and the "80% rule") to instantly prompt LLMs for short, direct text.
- **Evaluate** the benchmarked performance of controlled-language skills like `AminBlg/SimpleEnglish` across large language models.
- **Implement** Andrej Karpathy's 4-tier output hierarchy to move from text explanations to diagrams, interactive HTML, and custom video explainers.
- **Select** the most effective output format for you specific learning, documentation, or debugging needs.

# The Aerospace Secret to Cutting AI Slop

To understand why AI models often sound so repetitive and hedged, it helps to look at **ASD-STE100** (Simplified Technical English). Originally developed in the early 1980s by European aerospace industry association AECMA (first released in 1986, with Issue 9 released in January 2025), this standard was engineered for a very specific environment: aircraft maintenance. Mechanics operating under intense time pressure and reading in second languages needed instructions that could not be misread.

ASD-STE100 enforces rigorous constraints to ensure signle-meaning clarity:

- **Controlled Vocabulary**: Only about 900 approved words, most restricted to a single part of speech and meaning (for instance, "close" is strictly a verb; the adjective must be written as "near").
- **Strict Length Limits**: Sentences are capped at 20 words for instructions and 25 words for descriptions. Paragraphs cannot exceed six sentences.
- **Grammatical Discipline**: Requires active voice ("Remove the cover" instead of "The cover should be removed") and explicitly bans modal verbs like *should*, *would*, *may*, or *might*, as well as trailing `-ing` verb phrases.

Former OpenAI founding member and Anthropic researcher Andrej Karpathy noted that fronteier LLMs are heavily trained on this standard. Naming it in your prompt acts as a massive shortcut, replacing pages of style instructions with a single line.

However, full ASD-STE100 compliance can be sound robotic because it was design for repair steps rather than general conversation. Karpathy's key trick is to ask for "ASD-STE100, about 80% of the way." This soft constraint strips away fluff, passive voice, and run-on sentences while preserving a natural human tone.

Consider this real-world transformation from Claude Opus 5.5:


| Before (0% STE)                                                                                                                                                                                                                                                         | After (80% ASD-STE100)                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *"Please be aware that prompt caching can be leveraged to significantly reduce costs, as it essentially allows previously processed portions of a prompt to be reused across subsequent requests rather than being reprocessed each time"* (35 words, 1 dense sentence) | *"Prompt caching lowers cost. The model saves processed parts of your prompt. Later requests use the saved parts again. The model does not process them a second time."* (29 words, 4 crisp sentences) |

# Agent Skills vs. System Prompts: The Benchmark Debate

The growing frustration with verbose AI writing led to the release of **AminBlg/SimpleEnglish**, an open-source agent skill designed for tools like Claude Code, Cursor, and Codex. The repo sparked a lively debate on Hacker News: Is an entire agent skill necessary, or is packaging a single system-prompt line just unnecessary cruft?

While critics argued that adding *"Use ASD-STE100"* to a `system_prompt.md` file achieves a similar effect, the benchmark data provided by the skill's creator reveals why formal specs matter. Testing **6 Claude models across 8 writing tasks (96 generations total)** using a regex-based linter demonstrated measurable improvements:

- **72.9% Average Reduction in Style Violations**: Models like Claude Opus 4.7 and 4.6 saw an 82% drop in rule violations per 100 words.
- **Lower Token Consumption**: Across all six tested models, total ouput tokens dropped significantly, proving that enforced clarity also reduces generation latency and API costs.

Rather than claiming full aerospace certification, the value of an agent skills lies in its **iterative adaptiation**. The skill adapts STE rules specifically for software engineering artifacts, such as error messages, runbooks, release notes, incident reports, and `AGENTS.md` system files, where clear instructions prevent real-world missteps.

However, scope discipline is essential: the maintainers explicitly refuse to apply STE to marketing copy or blog posts. Controlled language deliberately trades emotional expression and persuasive nuance for raw, unambiguous comprehension.

# Beyond Plain Text: Karpathy's 4-Tier Output Ladder

Even perfectly written text still requires reading time. To maximize your speed of comprehension, Karpathy introduced a 4-tier hierarchy of output formats, where each step offers a richer medium than the last:

1. **Tier 1: Clean Writing (80% ASD-STE100)**
	- Prompt Modifier: `"Explain [topic]. Follow ASD-STE100 about 80% of the way.`
	- Best for: Quick text responses, documentation updates, and standard Q&A. 
2.  **Tier 2:  Diagrams & Visual Flowcharts**
	- Prompt Modifier: `"Do not explain this in text. Draw a diagram of [process]."`
	- Best for: Visualizing system architectures, login flows, timelines, and comparisons. You trace a visual path instead of parsing dense paragraphs.
3. **Tier 3: Interactive Web Pages (HTML/JS)**
	- Prompt Modifier: `"Give me the output in HTML. Build a [calculator/dashboard] with interactive controls."`
	- Best for: Exploring complex quantitative relationships. Instead of reading a static text output for one specific set of numbers, an HTML page with interactive sliders (such as an investments SIP calculator) lets you dynamically manipulate variables yourself.
4. **Tier 4: Custom Explainer Videos**
	- Prompt Modifier: `"Create a 3b1b style vidoe explainer on [topic]. Use my ElevenLabs API key for audio narration."`
	- Best for: Masterclass-level understanding of complex mathematical or abstract topics. By combining programmatic animations (in the style of Grant Sanderson's 3Blue1Brown channel) with realistic AI narration, you receive a fully bespoke educational video.

The ladder reflects a fundamental shift in modern computing: as AI intelligence and code become abundant, you no longer need to restrict yourself to reading text summaries. You can instantly generate **custom, discardable software artifacts** tailored specifically to help you understand a topic.


# Key Takeaways

- **The 80% Sweet Spot**: Adding *"Follow ASD-STE100 about 80% of the way"* cuts fluff, shortens sentences, and eliminates passive hedging while keeping explanations natural.
- **Measurable Style Improvement**: Agent skills like `AminBlg/SimpleEnglish` reduce style violations by nearly 73% while cutting total output token usage across frontier LLMs.
- **Contextual Scoping**: Apply controlled language to technical docs, error messages, incident reports, and system instructions, but keep it away from creative or marketing copy.
- **The Output Ladder**: Escalate from plain text (Tier 1) to diagrams (Tier 2), interactive HTML apps (Tier 3), and custom 3b1b video explainers (Tier 4) depending on the complexity of the subject.

## See

- See [[Simplified Technical English (ASD-STE100)]]
- See [[80% ASD-STE100 Prompting]]
- See [[SimpleEnglish Agent Skill]]
- See [[AI Output Ladder]]
- See [[Disposable Software Artifacts]]

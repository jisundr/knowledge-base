---
type: topic
tags: [ai-engineering, evaluation, llm]
---

# LLM-as-a-Judge

Using a strong LLM with an explicit rubric to score open-ended output (reasoning quality, RAG faithfulness, agent trajectories). Tier 4 of the [[Evaluator Cascade]].

## Rubric design

- Binary or small-scale rubric with clear criteria per score.
- Require step-by-step reasoning *before* the score.
- Enforce a structured (JSON) output: reasoning, ungrounded claims, score.

## Known biases and mitigations

- **Position bias** (favors the first option): swap response order, use multi-judge panels.
- **Verbosity bias** (favors longer answers): binary rubrics.
- **Self-preference bias** (favors its own model family): judge with a different family.

## Calibrating against humans

- Plain correlation or Krippendorff's alpha can mislead on skewed data such as rare hallucinations. Prefer **Gwet's AC2**.
- **Spearman / Kendall Tau** when ranking matters more than absolute scores.
- Comparing two system configs: **Wilcoxon signed-rank test** with **Benjamini-Hochberg** correction for multiple metrics.

Terms such as G-Eval, QAG, Gwet's AC2, and Wilcoxon are defined in [[LLM Evaluation Glossary]].

## Related

- [[AI System Evaluation]]
- [[Retrieval-Augmented Generation (RAG)]]
- [[Feedforward Guides and Feedback Sensors]]: LLM judges are inferential sensors in a harness.

## Sources

- [[20261123164745 Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding|Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding]]

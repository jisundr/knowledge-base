---
type: topic
tags: [ai-engineering, evaluation, testing]
---

# Evaluator Cascade

Route outputs through scorers ordered from cheap and deterministic to expensive and semantic, instead of relying on one scoring mechanism.

1. **Deterministic code checks**: exact match, regex, JSON schema. Near-zero latency and cost.
2. **Programmatic heuristics**: latency budgets (time to first token), token caps, tool success rates, keyword coverage.
3. **Reference-based / NLI metrics**: lexical overlap (BLEU, ROUGE), embedding similarity (BERTScore), or Natural Language *Inference* models for entailment.
4. **Model-based scorers**: [[LLM-as-a-Judge]] with explicit rubrics.
5. **Human expert review**: ambiguous cases, ground truth, and calibration of the automated judges.

## Trade-offs

- Code checks and lexical overlap are fully deterministic but miss semantics (and penalize valid paraphrase).
- Embeddings are fast but weak on domain shift and negation; NLI struggles with long multi-sentence context.
- LLM judges are flexible but stochastic, slower, and cost tokens.

This mirrors the [[Inverse Pyramid of Constraints]]: deterministic first, natural language last.

Terms such as BLEU, ROUGE, BERTScore, NLI, and TTFT are defined in [[LLM Evaluation Glossary]].

## Related

- [[AI System Evaluation]]
- [[Agent Verification Stack]]
- [[LLM Cascading]] (same cheap-first shape, for generation)

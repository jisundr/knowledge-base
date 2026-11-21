---
type: topic
tags: [ai-engineering, evaluation, datasets]
---

# Evaluation Dataset Design (5 D's)

Dataset quality bounds how far any downstream metric can be trusted. Five properties of a good evaluation dataset:

1. **Demonstrative**: mirrors real production usage (logs, user-reported issues), not synthetic ideals.
2. **Diverse**: covers the whole input space; clustering embeddings (see [[Embeddings and Vector Search]]) helps spot gaps and near-duplicates.
3. **Defined scope**: targeted cases that act as unit tests for individual subsystems, alongside end-to-end cases.
4. **Decontaminated**: kept out of training and fine-tuning data so scores are not inflated; checked via exact-match or perplexity tests.
5. **Dynamic**: updated as features, edge cases, and user behavior change; obsolete queries retired.

Failure modes found in production feed new cases back in; see [[Evaluation Error Analysis Flywheel]].

## Related

- [[AI System Evaluation]]

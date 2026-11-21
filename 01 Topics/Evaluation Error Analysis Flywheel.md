---
type: topic
tags: [ai-engineering, evaluation, observability]
---

# Evaluation Error Analysis Flywheel

Evaluation is a continuous Analyze-Measure-Improve loop, not a one-off test: prompt edits, provider model updates, and user drift keep creating new failure modes.

## Error analysis

- **Open coding**: read roughly 30-50 raw traces and write free-form notes on why each failed.
- **Axial coding**: group notes into a taxonomy (context truncation, tool-argument errors, extrinsic hallucination, temporal confusion).
- **Dataset enrichment**: turn each failure mode into a permanent golden case so it never regresses; see [[Evaluation Dataset Design (5 D's)]].

## Five deployment stages

1. **Development**: sub-second deterministic checks on every commit.
2. **Pre-release red teaming**: adversarial and jailbreak tests, e.g. OWASP Top 10 for LLM Applications.
3. **CI/CD regression gate**: run a versioned golden dataset on each PR; block merge below baseline.
4. **Production monitoring**: score a 5-10% sample of live traffic asynchronously.
5. **Runtime guardrails**: synchronous filters for policy violations and PII leaks.

## Related

- [[AI System Evaluation]]
- [[Evaluator Cascade]]
- [[Agent Verification Stack]]

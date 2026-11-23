---
type: topic
tags: [evaluation, ai-governance, mlops, monitoring]
---

# AI Evaluation System Pillars

Six areas a production AI evaluation system covers so it can show a model is reliable, fair, and debuggable, not just accurate on a test set.

| Pillar | Checks | Typical tools |
| --- | --- | --- |
| Performance | Task metrics | Precision, recall, F1 (classification); MSE (regression); [[LLM Evaluation Glossary#NDCG|NDCG]] (ranking) |
| Robustness | Out-of-distribution data, adversarial perturbations, stress cases | Held-out and perturbed datasets |
| Bias and fairness | Outcomes across demographic groups | [[LLM Evaluation Glossary#Demographic parity|Demographic parity]], [[LLM Evaluation Glossary#Equalized odds|equalized odds]] |
| Explainability | Why a prediction came out as it did | [[LLM Evaluation Glossary#SHAP|SHAP]], [[LLM Evaluation Glossary#LIME|LIME]]; see [[Model-Based vs Model-Free Explanations]] |
| Monitoring | Degradation after deployment | [[Model Drift Detection]] |
| Evidence capture | Exact versions behind a failing request | [[Request-Level Evidence Capture]] |

Run the automatable checks in CI/CD and keep human-in-the-loop review for edge cases. That combination is what makes the system audit-ready.

## Related

- [[AI System Evaluation]]: the LLM-pipeline view (Goldens, Test Cases, Traces).
- [[Evaluator Cascade]]
- [[Evaluation Error Analysis Flywheel]]

## Sources

- [[20261123170538 Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews|Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews]]

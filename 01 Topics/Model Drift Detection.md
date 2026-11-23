---
type: topic
tags: [monitoring, mlops, evaluation, observability]
---

# Model Drift Detection

Watching a deployed model for the slow ways it stops matching the world, before users notice.

## Three kinds of drift

- **Data drift**: the statistical distribution of input features shifts.
- **Concept drift**: the relationship between inputs and the correct output changes, so the same input now deserves a different label.
- **Prediction drift**: the distribution of the model's outputs shifts.

Data drift can occur without concept drift and vice versa; prediction drift is often the first visible symptom of either.

## Detection

Compare a live window against a reference window with a distribution-distance statistic, such as [[LLM Evaluation Glossary#KL divergence|KL divergence]] or the [[LLM Evaluation Glossary#PSI|Population Stability Index (PSI)]], and alert past a threshold.

## Related

- [[AI Evaluation System Pillars]]
- [[Request-Level Evidence Capture]]
- [[Evaluation Error Analysis Flywheel]]

## Sources

- [[20261123170538 Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews|Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews]]

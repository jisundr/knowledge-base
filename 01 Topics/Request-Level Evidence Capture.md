---
type: topic
tags: [observability, incident-management, llm, debugging]
---

# Request-Level Evidence Capture

Logging the exact versioned inputs behind each AI request so a failure can be reproduced and debugged. "The model got weird" is not a bug report.

## What to record per request

- Request ID
- Prompt version
- Retrieval index version (for [[Retrieval-Augmented Generation (RAG)]])
- Tool schema definitions
- Model and policy version

With these, a hallucination, retrieval miss, or tool-parsing error can be traced to the component and version that changed. Without them, a probabilistic failure cannot be separated from noise.

## Related

- [[AI System Evaluation]]: the Trace unit holds the same evidence for test runs.
- [[Model Drift Detection]]
- [[AI Evaluation System Pillars]]
- [[Blameless Post-Incident Review (PIR)]]: the evidence feeds the timeline.

## Sources

- [[20261123170538 Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews|Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews]]

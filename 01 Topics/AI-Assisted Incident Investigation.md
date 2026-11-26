---
type: topic
tags: [incident-management, ai-engineering, safety, compliance, human-in-the-loop]
---

# AI-Assisted Incident Investigation

Using generative AI to do the labor-heavy parts of an incident investigation (capture, drafting, pattern search) while a competent human keeps the analysis, judgment, and sign-off. Applies to both safety (HSE) and IT operations incidents.

## Where AI helps

| Area | What AI does |
| --- | --- |
| Capture | Turns voice notes and witness interviews into time-stamped, searchable, translated transcripts |
| Drafting | Maps unstructured notes into compliance forms (e.g. [[Incident Investigation Glossary#OSHA Form 301|OSHA Form 301]], [[Incident Investigation Glossary#ISO 45001|ISO 45001]]) |
| Causal analysis | Suggests candidate contributing factors from narrative text using [[Incident Investigation Glossary#ICAM|ICAM]] or [[Incident Investigation Glossary#5 Whys|5 Whys]] |
| Pattern detection | Searches historical incidents for correlations across shifts, equipment, weather, or sites |

Claimed effect: 60–80% less drafting time and 2–3× more near-miss reports when voice capture replaces forms. These figures come from a vendor (AI4HSE case studies and customer data), not independent research.

## Boundaries

- **Human sign-off**: expect a competent person to validate and sign every AI-drafted report. This is good practice rather than an explicit rule: OSHA has no guidance prohibiting AI assistance, and ISO 45001 does not prescribe a method.
- **Risk class**: a drafting assistant is plausibly outside the EU AI Act's high-risk list. A system that makes or supports decisions about workers (promotion, termination, task allocation based on behaviour, or monitoring and evaluating performance) is high risk (see [[Incident Investigation Glossary#EU AI Act risk tiers|EU AI Act risk tiers]]). Once AI output feeds judgments about individual workers, the system can move into that class.
- **Privacy**: GDPR requires data minimisation and appropriate security, with encryption named as an example measure. A vendor processing the data may act only on the controller's instructions, so a vendor training its models on your inputs needs your explicit instruction. Check contracts for no retention and no training.
- **Stays human**: final root cause, sensitive interviews, fatality investigations, and accountability judgments.

AI is a productivity multiplier, not the decision-maker. Same pattern as "agents monitor, humans decide" in [[Agentic SDLC]] and the human tiers of the [[AI Work Autonomy Spectrum]].

For live IT incidents, a [[Shadow On-Call Agent]] applies the same split at page time: it filters noise and starts investigating before the human arrives.

## Related

- [[Shadow On-Call Agent]]
- [[Blameless Post-Incident Review (PIR)]]
- [[After-Action Review for AI (AAR-AI)]]
- [[Request-Level Evidence Capture]]

## Sources

- [[20261123170538 Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews|Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews]]
- [[20261126155209 How Anthropic Builds Software with AI Agents|How Anthropic Builds Software with AI Agents]]

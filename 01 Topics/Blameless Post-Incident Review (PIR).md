---
type: topic
tags: [incident-management, sre, postmortem, culture]
---

# Blameless Post-Incident Review (PIR)

A look back after an incident (SRE "postmortem", ITIL "post-incident review") whose goal is to change the system so the same failure does not happen twice. It must be blameless: when reviews assign personal fault, responders hide details, and the organization loses the information it needs.

## Six mechanics

1. **Ask how it made sense at the time**: rebuild each responder's [[Incident Investigation Glossary#Local rationality|local rationality]] from the signals they had.
2. **Treat human error as the start**: error is a symptom of design flaws, missing guardrails, or alert fatigue, not the root cause.
3. **Ban counterfactual language**: no "should have", "failed to", "neglected to"; keep to a factual timeline.
4. **Roles in the narrative, names on actions**: "the on-call engineer" in the timeline; named owners in the action registry.
5. **Independent facilitator**: someone from an adjacent team asks naive questions without it feeling like cross-examination.
6. **Firewall from performance reviews**: PIR content is never cited in employee evaluations.

## Analysis

Trace contributing factors as a branching graph, not a single linear chain to one "root cause". Output is a set of verified action items; see [[PIR Action Items (Prevent, Detect, Mitigate, Learn)]].

## Related

- [[AI-Assisted Incident Investigation]]
- [[After-Action Review for AI (AAR-AI)]]
- [[Request-Level Evidence Capture]]

## Sources

- [[20261123170538 Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews|Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews]]

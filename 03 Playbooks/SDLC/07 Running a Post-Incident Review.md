---
type: playbook
status: draft
tags: [playbook, incident-management, postmortem, sre, agentic-sdlc, kairyn]
---

# Playbook - Running a Post-Incident Review

Stage 7 after [[06 Releasing and Monitoring]]. Use after an incident is resolved (rollback, outage, an AI feature producing bad output, a safety event). Outcome: a blameless review that changes the system, with small, owned action items closed within 30 days. Pattern: agents gather evidence and draft, humans analyze and decide ([[Agentic SDLC]], [[AI-Assisted Incident Investigation]]).

## Trigger

- A rollback or roll-forward fix in [[06 Releasing and Monitoring]] ("When signals go bad").
- Any customer-impacting incident, near miss, or AI failure (hallucination, retrieval miss, tool-call error, drift alert).

## Principles applied

- **Human as judgment, agents on execution**: agents build the timeline and draft the report; humans own causal analysis, accountability, and sign-off.
- **Context lives where agents can see it**: logs, traces, and [[Request-Level Evidence Capture|request-level evidence]] are linked from the incident folder.
- **Measured, never estimated**: every timeline entry has a timestamp and a source; every action item has a closure check.
- **Auditable always**: the review, decisions, and action-item closure are logged. The review is never used in performance evaluations.

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Collect logs, alerts, deploys, chat, and request evidence; draft the timeline; suggest contributing factors; search past incidents for repeats; draft the report |
| Human does | Facilitate (neutral, from an adjacent team); interview responders; build the causal analysis; check AI suggestions against evidence |
| Human decides | Final contributing factors, action items and owners, sign-off, whether the incident class can stay automated |

## Steps

| # | Step | Owner | Done when |
| --- | --- | --- | --- |
| 1 | Open the incident folder; pick a facilitator who was not involved | **Human decides** | Facilitator named, review booked within 5 working days |
| 2 | Collect evidence: alerts, deploys, flags, dashboards, chat, and for AI features the request IDs, prompt version, retrieval index version, tool schemas, model and policy version ([[Request-Level Evidence Capture]]) | AI | Every claim in the draft links to a log, trace, or message |
| 3 | Draft a factual timeline with roles, not names ("the on-call engineer") and no counterfactual language | AI | No "should have", "failed to", "neglected to"; every entry timestamped |
| 4 | Search past incidents for the same pattern (service, change type, time, dependency) | AI | Repeats listed with links, or "none found" |
| 5 | Run the review: for each decision point ask how it made sense at the time ([[Incident Investigation Glossary#Local rationality|local rationality]]); treat human error as the start of the analysis | Human (facilitator) | Each responder's view captured |
| 6 | For AI agent decisions, walk the AAR/AI questions: expected, actual, why (from the trace), and whether it may keep deciding this alone ([[After-Action Review for AI (AAR-AI)]]) | Human, AI supplies traces | Autonomy decision recorded per decision class |
| 7 | Map contributing factors as a branching graph, not one root cause; AI suggestions (e.g. ICAM categories) are inputs only | **Human decides** | Factors agreed, each with evidence |
| 8 | Write action items across Prevent, Detect, Mitigate, Learn ([[PIR Action Items (Prevent, Detect, Mitigate, Learn)]]) | Human, AI drafts | Each item: one named owner, in the main tracker, sized for 30 days |
| 9 | Sign off the report | **Human decides** | Named reviewer signs; AI-drafted sections checked against evidence |
| 10 | Feed gaps back: missing tests to [[04 Running Quality Gates]], missing signals to [[06 Releasing and Monitoring]], drift checks for AI features ([[Model Drift Detection]]), learnings to `.kairyn/learnings.md` | AI | Each factor maps to the stage that should have caught it |
| 11 | 30-day closure review | **Human decides** | Every item closed, or re-scoped with a reason |

## Gates

1. Evidence before analysis: the timeline is complete and sourced before the review meeting.
2. Blameless language check on the draft (no counterfactuals, roles not names in the narrative).
3. Action items balanced: not all Prevent or all Learn; each has an owner and a 30-day size.
4. Human sign-off on the report.
5. 30-day closure review done.

## Agent profile

`.github/agents/incident-reviewer.md`:

- **Role**: evidence collector and drafter, never the decider.
- **Inputs**: incident folder, logs and traces, deploy history, past PIRs.
- **Rules**: cite a source for every timeline entry; flag gaps instead of guessing; use roles not names; no counterfactual words; label causal suggestions "candidate".
- **Output**: `docs/incidents/<date>-<slug>/PIR.md` (timeline, evidence links, candidate factors, draft actions), written in ASD-STE100 ([[01 Using ASD-STE100 with Agents]]).

## Data and compliance

- Minimize personal data in transcripts and logs; keep only what the review needs.
- Use AI vendors that act only on your instructions: no retention, no training on incident data. Check the contract.
- If AI output is used to judge individual workers (performance, discipline, termination), it may become high-risk under the EU AI Act ([[Incident Investigation Glossary#EU AI Act risk tiers|EU AI Act risk tiers]]). Keep the PIR firewalled from performance reviews.
- Sensitive interviews and serious-harm or fatality investigations stay fully human.

## Audit trail

- Evidence sources, timeline versions, attendees, decisions and who made them, sign-off, action-item status at 30 days.

## Pitfalls

- Naming and blaming: responders stop sharing details.
- Stopping at "human error" or one linear 5 Whys chain.
- Vague AI evidence ("the model got weird") with no request IDs or versions.
- Accepting AI-suggested causes without checking them against evidence.
- Action items in the PIR doc instead of the tracker, with no owner, so they never close.
- Review document cited in a performance review.

## Escalation

- Serious harm, safety, or legal exposure: involve safety, legal, and compliance before the review; follow regulatory reporting deadlines.
- Same incident class repeats: escalate to the owning team lead and block related releases until a Prevent item lands.
- AI agent decision judged unsafe in step 6: remove that decision class from autonomous execution until the policy is fixed.

## Related

- [[Blameless Post-Incident Review (PIR)]]
- [[AI-Assisted Incident Investigation]]
- [[AI Evaluation System Pillars]]
- [[Agentic SDLC]]
- [[Playbook Template]]

---
type: topic
tags: [incident-management, sre, postmortem]
---

# PIR Action Items (Prevent, Detect, Mitigate, Learn)

How a [[Blameless Post-Incident Review (PIR)]] turns findings into change that actually lands, instead of a report that gets filed and forgotten.

## Balance across four categories

| Category | Goal | Example |
| --- | --- | --- |
| Prevent | Stop recurrence | Automated config validation |
| Detect | Catch it earlier | Lower alert thresholds |
| Mitigate | Recover faster | Automated rollback scripts |
| Learn | Spread the knowledge | Updated runbooks |

A list that is all "Prevent" or all "Learn" is a sign the analysis stopped early.

## Follow-through rules

- One named owner per item.
- Lives in the team's main task tracker, not in the PIR document.
- Sized to finish within 30 days.
- Formal closure review at 30 days.

## Related

- [[Categorical Elimination of Anti-Patterns]]: a strong form of "Prevent".
- [[Inverse Pyramid of Constraints]]: prefer deterministic checks as prevention.

## Sources

- [[20261123170538 Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews|Mastering AI & IT Incident Investigation - From Automated Root Cause Analysis to Blameless Reviews]]

---
type: topic
tags: [ai-engineering, ai-agents, guardrails, security]
---

# Deterministic Guardrail Policies

Rule-based filters that run around the model, in parallel with it, instead of relying on the system prompt for safety.

Typical policies:

- **Profanity filter** on inputs and outputs.
- **Prompt-injection detection** on user input and retrieved content.
- **Denied topics**: refuse whole subject areas.
- **Custom regex**: scrub or block patterns such as social security or credit card numbers.

They give the same answer every time, so they can be tested and audited, unlike a model told to "be careful".

## Related

- [[Inverse Pyramid of Constraints]]
- [[Agent Anti-Jobs]]
- [[Agent Design Foundation]]
- [[Feedforward Guides and Feedback Sensors]]
- [[AI Control Plane]]

## Sources

- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

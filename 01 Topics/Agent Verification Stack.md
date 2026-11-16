---
type: topic
tags: [ai-engineering, ai-agents, verification, testing, code-review]
---

# Agent Verification Stack

The tiers of automated checking that let humans review *evidence* instead of raw code once agent output scales. In high-velocity teams, over 70% of daily token spend goes to verification, not generation.

## Tiers

- **Runtime verification**: agents run their own code and inspect the UI, e.g., via the Chrome DevTools Protocol. A **Feature Map** (a user-centric sitemap of app features) gives agents and developers a shared vocabulary. Custom CLI driver scripts keep runs predictable and cut token use.
- **Property-based testing**: randomized interaction streams; see [[Property-Based UI Testing]].
- **Formal verification**: model-checking and proofs for critical invariants; see [[Formal Verification (TLA+ and Lean)]].
- **Statechart visualization**: see [[Statecharts and State Machines]].

## Review artifacts

Human review shifts to inspecting execution videos, UI screenshots, state diagrams, and proofs rather than reading diffs.

## Related

- [[Inverse Pyramid of Constraints]]
- [[Autonomous Software Factory]]
- [[Agentic SDLC]]

## Sources

- [[20261115183456 All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI|All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI]]

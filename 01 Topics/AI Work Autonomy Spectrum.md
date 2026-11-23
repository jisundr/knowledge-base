---
type: topic
tags: [ai-engineering, ai-agents, automation, governance]
---

# AI Work Autonomy Spectrum

How much autonomy to give an agent depends on how its work is verified. Common modes, roughly from most to least human oversight:

- **Human-in-the-loop**: the developer watches the session, approves tool calls, and steers mid-turn. Use for high-risk changes such as schema migrations. For otherwise autonomous agents, add [[Human-in-the-Loop Approval Gates]] on high-stakes actions.
- **AFK (away from keyboard)**: the agent runs unattended in a sandbox with auto-approved permissions and ends with a pull request. See [[AFK Agent Execution]].
- **Software factory**: triggers (CI failures, schedules, new issues) start AFK sessions with no human kick-off. See [[Autonomous Software Factory]].
- **Dark factory**: factory agents generate and land code with no human review, relying only on automated verification.

**Vibe coding** sits off this axis: accepting code because it seems to run, without reading the diff. Fine for throwaway prototypes, dangerous in production.

The further right you go, the more you need deterministic checks (types, tests, lints, contract drift detection) in place of human review.

## Related

- [[Implement-Review-Remediate Loop]]
- [[Agent Development Environment (ADE)]]
- [[AFK Agent Execution]]
- [[Autonomous Software Factory]]
- [[Agent Verification Stack]]
- [[Contract-Driven Workspace]]
- [[Disposable Software Artifacts]]
- [[Human-in-the-Loop Approval Gates]]

## Sources

- [[20261122155021 Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern|Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern]]
- [[20261123172458 Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE|Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE]]
- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

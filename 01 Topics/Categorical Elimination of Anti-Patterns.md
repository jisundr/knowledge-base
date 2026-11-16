---
type: topic
tags: [ai-engineering, ai-agents, code-quality, linting, architecture]
---

# Categorical Elimination of Anti-Patterns

Treat the codebase as a garden: agents copy existing patterns, so any workaround or tech debt gets replicated across hundreds of PRs like weeds. When you catch yourself correcting an agent, don't add a prompt rule; make the anti-pattern impossible (or removed) in the codebase. This is the practical application of the [[Inverse Pyramid of Constraints]].

## Tactics from the Grok Bot team

- **Ban a nuanced API**: React's `useEffect` caused misuse and state bugs, so it was banned in product code by lint rule and allowed only inside internal framework APIs.
- **Structural directory boundaries**: separate `electron/renderer` and `electron/main` directories plus a dependency-graph analyzer that bans cross-imports, so heavy main-thread code can't leak into the renderer. Removes the check from human review.
- **Ban comments (about 99%)**: agents used comments to justify hacks (e.g. `setTimeout` / `requestAnimationFrame` patches causing GC spikes). Comments are unenforceable and go stale; banning them forces root-cause fixes. Helpful linter error messages point the agent to the proper structural solution.

## Related

- [[Agent Verification Stack]]
- [[Autonomous Software Factory]]

## Sources

- [[20261115183456 All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI|All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI]]

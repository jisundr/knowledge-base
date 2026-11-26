---
type: topic
tags: [ai-engineering, ai-agents, migration, verification, architecture]
---

# Shadow Traffic Migration

Rewrite a system as a full parallel fork, then prove it equivalent by sending every live request to both versions and comparing results, instead of refactoring piece by piece and reviewing each diff.

## How it works

1. **Thin front door**: a small router takes each inbound request.
2. **Live plus shadow**: the old system serves the response; the new system runs the same request asynchronously as a shadow.
3. **Compare what you are allowed to see**: when privacy rules forbid inspecting payloads, compare state up to a boundary and a cheap proxy on the way out (Anthropic compared token counts returned from inference).
4. **Converge**: each day, have an agent analyze the telemetry differences and drive the mismatch rate toward zero.
5. **Fallback**: the old path stays live as the fallback until cutover.
6. **Parity gate**: while other teams keep shipping on the old stack, a lint or static-analysis rule blocks CI for any new feature that lacks a matching implementation in the new stack.

Anthropic used this to move its Messages API layer from Python to Rust in about five to six months with a small core team, without the team first mastering Rust (see [[Accidental vs Essential Complexity]]). It is the clearest case of "make the output verifiable and you don't need to read every line" ([[Agent Verification Stack]]).

## Related

- [[Categorical Elimination of Anti-Patterns]]: the parity gate is a structural rule, not a reminder.
- [[Verification Density]]
- [[Risk-Classified PR Routing]]

## Sources

- [[20261126155209 How Anthropic Builds Software with AI Agents|How Anthropic Builds Software with AI Agents]]

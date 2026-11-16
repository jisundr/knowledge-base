---
type: topic
tags: [ai-engineering, ai-agents, code-quality, guardrails]
---

# Inverse Pyramid of Constraints

A trust model for agent-written code: enforce quality with hard, deterministic checks first, and treat natural-language instructions as the last resort. It lets a team move from a low-trust setup (humans read every line) to a high-trust one (agents are constrained to do the right thing by default), which is the only way review keeps up when agents open hundreds of PRs a day.

## Layers (strongest first)

1. **Deterministic codebase constraints**: solid API design, architectural refactoring, strict typing. The codebase is the agent's main context, so correct-by-construction code steers generation.
2. **Compilers, linters, static analysis**: strict compiler flags and custom lint rules reject invalid patterns instantly.
3. **Verification**: running the code, property tests, formal proofs; see [[Agent Verification Stack]].
4. **Prose instructions** (`AGENTS.md`, skill files, prompts): soft rules that depend on agent judgment, so least reproducible.

## Why this order

- Code checks are reproducible; prompts are not.
- Each correction you make to an agent should become a constraint lower in the pyramid, not another prompt line; see [[Categorical Elimination of Anti-Patterns]].

## Related

- [[Agentic SDLC]]
- [[AI Agents and Tool Use]]
- [[Autonomous Software Factory]]

## Sources

- [[20261115183456 All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI|All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI]]

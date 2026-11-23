---
type: topic
tags: [ai-engineering, ai-agents, harness-engineering, verification]
---

# Harness Engineering

Designing the software around a model that turns it into a working agent: tools, sandboxes, rules, and checks. Summed up as **Agent = Model + Harness**: the model supplies reasoning, the harness supplies hands, memory, boundaries, and verification. See [[Model and Harness Separation]].

## Where it sits: the three-layer stack

| Layer | Concern |
| --- | --- |
| 1. [[Context Engineering]] | What information enters the context window each turn |
| 2. **Harness Engineering** | How the agent acts in the project: tools, MCP servers, sandboxes, linters, tests, architecture rules |
| 3. [[Loop Engineering]] | Repeatedly triggering the agent, spawning sub-agents, judging output, keeping memory, without turn-by-turn prompting |

Each layer depends on the one below. A loop around a weak harness does not fix errors; it repeats them faster.

## Building blocks

- [[Feedforward Guides and Feedback Sensors]]: steer before the agent acts, check after.
- [[Model Context Protocol (MCP)]]: standard way to give the agent tools.

## Related

- [[Long-Running Agent Harness]]
- [[Inverse Pyramid of Constraints]]
- [[Agent Verification Stack]]
- [[Verification Density]]

## Sources

- [[20261123164745 Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding|Mastering Harness & Loop Engineering - Beyond Single-Prompt AI Coding]]

---
type: topic
tags: [software-engineering, ai-agents, requirements, product-engineering]
---

# Accidental vs Essential Complexity

Fred Brooks' split of software difficulty (*No Silver Bullet*, 1986, collected in *The Mythical Man-Month*):

- **Accidental complexity**: difficulty from tools, syntax, language limits, and environment setup. This is the typing and boilerplate that coding agents have largely collapsed.
- **Essential complexity**: difficulty in the problem itself: real business logic, human requirements, and user needs. Agents cannot remove it.

## Why it matters with agents

"Code is a lossy projection of the specification" (Sean Grove, OpenAI): whoever writes the spec does the real programming. When software is nearly free to make, demand becomes effectively unlimited, and the limit is our ability to define what "good" means.

Example: a scheduling app for a local bakery and one for an auto-parts distributor may look the same to an LLM, but "good" differs with physical operations, staff habits, and business constraints. That context is not in model weights; it has to be drawn out of people by talking to them.

Example: Anthropic's platform team moved its API to Rust without prior Rust experience; Claude wrote the code and explained the borrow checker on demand, so the language's accidental complexity no longer needed months of retraining (see [[Shadow Traffic Migration]]).

## Related

- [[Shadow Traffic Migration]]
- [[Impact-Based Engineering Seniority]]
- [[Product Engineer]]
- [[Problem-First Thinking]]
- [[Spec-Driven Development]]
- [[Bottleneck Shift (Theory of Constraints)]]

## Sources

- [[20261126153108 AI Writes the Code - The Rise of the Product Engineer|AI Writes the Code - The Rise of the Product Engineer]]
- [[20261126155209 How Anthropic Builds Software with AI Agents|How Anthropic Builds Software with AI Agents]]

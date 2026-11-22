---
type: topic
tags: [requirements, writing, sdlc]
---

# EARS Notation

Easy Approach to Requirements Syntax: each requirement is one testable sentence in a fixed shape, so humans and agents read it the same way.

| Pattern | Shape |
| --- | --- |
| Ubiquitous | The `<system>` shall `<response>`. |
| Event-driven | **When** `<trigger>`, the `<system>` shall `<response>`. |
| State-driven | **While** `<state>`, the `<system>` shall `<response>`. |
| Unwanted behavior | **If** `<condition>`, **then** the `<system>` shall `<response>`. |
| Optional feature | **Where** `<feature is included>`, the `<system>` shall `<response>`. |

Example: *If the payment gateway is unreachable, then the system shall queue the transaction and retry up to 3 times.*

Used in the `requirements.md` of [[Spec-Driven Development]] and in [[Agentic SDLC]] spec synthesis.

## Related

- [[Simplified Technical English (ASD-STE100)]]
- [[Ubiquitous Language]]

## Sources

- [[20261122123529 From Problem-First Discovery to Spec-Driven AI Execution|From Problem-First Discovery to Spec-Driven AI Execution]]

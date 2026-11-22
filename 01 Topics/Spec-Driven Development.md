---
type: topic
tags: [ai-engineering, ai-agents, requirements, sdlc]
---

# Spec-Driven Development

Replacing chat prompts and loose tickets with structured Markdown specs committed to the repository, which humans and AI coding agents build from and verify against.

Phases: **Specify → Plan → Tasks → Implement**, then check the result against the spec.

## Spec artifacts

| File | Answers |
| --- | --- |
| `requirements.md` (or `spec.md`) | **What** the feature must do, from the user and business view, in [[EARS Notation]] |
| `design.md` / `plan.md` | **How** it is built: architecture, schema changes, API contracts |
| `tasks.md` | Discrete, trackable implementation steps, runnable in parallel waves |

Tools: Kiro (`.kiro/specs/`), GitHub Spec Kit, Taskmaster AI (parses a PRD into tasks and scores complexity), backlog.md.

The input is a shaped idea ([[Shaping (Shape Up)]]); the tasks feed a [[Task Graph Backlog]].

## After shipping

Specs are scaffolding for the delta, not permanent truth. Decide upfront what is kept, promoted into code, or deleted: see [[Spec Exit Strategy]] and [[Spec Persistence Models]].

## Related

- [[Grilling Session]]
- [[Agentic SDLC]]
- [[Long-Running Agent Harness]]
- [[Spec Exit Strategy]]
- [[Design Document Types]]

## Sources

- [[20261122123529 From Problem-First Discovery to Spec-Driven AI Execution|From Problem-First Discovery to Spec-Driven AI Execution]]
- [[20261122133225 Spec-Driven Development Exit Strategies - What to Retain, Merge, and Discard|Spec-Driven Development Exit Strategies - What to Retain, Merge, and Discard]]

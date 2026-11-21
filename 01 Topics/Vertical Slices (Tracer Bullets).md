---
type: topic
tags: [ai-engineering, sdlc, planning, architecture]
---

# Vertical Slices (Tracer Bullets)

Breaking work into minimal steps that each cut through **every layer** (schema, service logic, UI) end to end, instead of building one layer at a time. Term from *The Pragmatic Programmer* (Dave Thomas and Andy Hunt).

- **Horizontal** plans (all schema, then all API, then all UI) delay integrated feedback to the last phase, so the agent codes blind across isolated layers. Agents drift into this by default.
- **Vertical** slices give immediate proof the pieces work together.

Slices become tickets in a [[Task Graph Backlog]].

## Related

- [[Grilling Session]]
- [[Test-Driven Development for Agents]]

## Sources

- [[20261121222850 Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture|Mastering AI-Powered Software Engineering - From Grilling to Deep Architecture]]

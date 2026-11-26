---
type: topic
tags: [ai-engineering, automation, verification, requirements]
---

# Software Promises

A way to frame requirements for a brownfield factory: each **promise** is a dimension of the product the customer values and you should not regress on. Examples: a feature, the cost and price, a security guarantee, performance.

Promises are encoded into agent loops that run continuously against production telemetry, pushing the system toward a Pareto improvement (faster, cheaper, safer) without trading one promise for another. Unlike human teams with daily and weekly cycles, the loop keeps promises around the clock.

A good standing instruction: **the same, but faster**, then cheaper and safer. Leave "better" out of the factory: it needs intent, judgment, and taste, so it belongs in discovery.

## Amplifier analogy

An audio amplifier needs a feedback leg to keep fidelity; cut it and it amplifies noise. An agent loop without runtime feedback likewise amplifies technical debt, security holes, and clutter. Promises plus telemetry are the feedback leg. See [[Feedforward Guides and Feedback Sensors]].

## Related

- [[Greenfield vs Brownfield Software Factories]]
- [[Autonomous Software Factory]]
- [[Loop Engineering]]
- [[Verification Density]]

## Sources

- [[20261127074619 Stop Building Software Factories — Architecting Brownfield & Demand Systems|Stop Building Software Factories — Architecting Brownfield & Demand Systems]]

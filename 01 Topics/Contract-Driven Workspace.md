---
type: topic
tags: [ai-engineering, ai-agents, multi-repo, verification, governance]
---

# Contract-Driven Workspace

A multi-repo setup where a shared workspace manifest (e.g., `workspace.toml`) declares which repositories depend on which API contracts. When a contract changes, the tooling detects the drift and notifies the dependent repos, whose agents can then update their own code.

## The failure it targets

An agent changes a shared API in isolation (e.g., moving an endpoint from `/v1` to `/v2`). The provider's tests pass, and callers' unit tests pass too because their HTTP calls are mocked. The break shows up only as live 404s, because no one told the callers.

## Comparison (from a vendor benchmark by Nool)

| Setup | Outcome |
| --- | --- |
| One agent in a [[Home Repo Pattern|home repo]] | Updated provider and all callers, ran every suite |
| Separate teams, no shared repo | Silent failure in production |
| Contract-driven workspace | Drift detected on landing; callers notified and fixed |

## Takeaway

A home repo is enough for a solo developer or one unified team. Distributed teams need deterministic cross-repo checks (types, contract tests, drift detection) because steering only reaches sessions you control.

## Related

- [[Home Repo Pattern]]
- [[Agent Verification Stack]]
- [[Inverse Pyramid of Constraints]]
- [[AI Work Autonomy Spectrum]]

## Sources

- [[20261122155021 Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern|Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern]]

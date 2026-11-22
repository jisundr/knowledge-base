---
type: topic
tags: [ai-engineering, ai-agents, context-engineering, multi-repo]
---

# Home Repo Pattern

One dedicated repository that acts as the control plane for all agent sessions across an organization's many repositories (attributed to Matt Pocock). You launch the agent in the home repo, not in an individual project repo.

## Problems it solves

- **Context fragmentation**: an agent started in one repo cannot see the dependent code in another.
- **Configuration drift**: skills and steering files copied into every repo drift apart.
- **Unshared user config**: skills in a global user directory (e.g., `~/.claude/skills`) are outside git, so they are not versioned or shared with the team.

## What it holds

- `AGENTS.md` with [[Context Pointers]] to each child repo: local path, clone URL, and "read its own `AGENTS.md` first".
- Shared, versioned skills and harness settings.
- A central markdown wiki (architecture decisions, APIs).
- Custom CLI tools (databases, issue trackers, chat).

## How it works

1. **Zero-setup cloning**: the agent follows a pointer and clones the repo if it is missing.
2. **Worktree isolation**: parallel sessions on the same child repo each get a git worktree.
3. **Cross-repo sessions**: one session can trace an alert from a logging tool through several services.

## Scaling limit

Works for roughly 20 to 40 repositories. Beyond that, one flat pointer list overloads the agent's initial decision space; split pointers by domain ([[Progressive Disclosure]]).

## Limit on governance

It only steers sessions that run inside it. Distributed teams working in separate clones still need automated checks or a [[Contract-Driven Workspace]] to catch cross-repo breaking changes.

## Related

- [[Context Pointers]]
- [[Context Engineering]]
- [[Contract-Driven Workspace]]
- [[Agent Memory]]

## Sources

- [[20261122155021 Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern|Mastering AI Coding Agents - Context Engineering & The Home Repo Pattern]]

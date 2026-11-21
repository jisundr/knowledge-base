---
type: playbook
status: draft
tags: [playbook, agentic-sdlc]
---

# Playbook - <Situation>

One line: when this applies and the outcome it produces. Pattern: [[Agentic SDLC]] (agents start on execution, humans make the decision).

## Trigger

What event or signal starts this playbook?

## Principles applied

- Which of the four operating rules matter here (human judgment / context where agents can see it / same bar for agents and humans / auditable).
- Which handoff or wait this playbook removes.

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Execution work: drafting, synthesizing, running checks |
| Human does | Adds context, applies judgment, manages stakeholders |
| Human decides | Prioritizes, approves or rejects, holds accountability |

## Steps

| # | Step | Owner (AI / Human / Decision) | Done when |
| --- | --- | --- | --- |
| 1 | ... | AI | ... |

## Gates

Ordered checks that must pass before moving on. Order matters (e.g. security last, so it audits the final result).

1. ...

## Agent profile

Optional. Markdown spec for the agent that runs this playbook (role, inputs, tools/MCP, rules, output format). Lives in `.github/agents/<name>.md` in a repo.

## Audit trail

What gets logged: agent actions, human overrides, decisions and who made them.

## Pitfalls

- Common mistakes and how to avoid them.

## Escalation

Who to involve and when.

## Related

- [[Agentic SDLC]]
- [kairyn](https://github.com/jisundr/kairyn): runnable stages that implement playbooks

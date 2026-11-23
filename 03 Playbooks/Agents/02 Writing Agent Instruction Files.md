---
type: playbook
status: draft
tags: [playbook, ai-agents, context-engineering, steering]
---

# Playbook - Writing Agent Instruction Files

Use when you write or trim an always-loaded instruction file (`AGENTS.md`, `CLAUDE.md`, a system prompt). Outcome: the file is short, holds only rules that apply to every task, and points to deeper docs and skills that the agent loads on demand. Sessions stay in the smart zone and keep the prefix cache warm. Pattern: [[Progressive Disclosure]] with [[Context Pointers]] and [[Agent Skills]], from [[Context Engineering]].

## Trigger

- You create a new repo or a new agent profile.
- `AGENTS.md` / `CLAUDE.md` grows past its size budget, or someone pastes a full style guide or runbook into it.
- The agent ignores a rule that is in the file, or repeats a mistake you already corrected.
- A long session starts to drift: instructions slip, quality drops, cost per turn climbs.

## Principles applied

- **The model is stateless**: the harness re-sends the instruction file and the full history on every request ([[Model and Harness Separation]]). Every line costs tokens and attention on every turn.
- **Point, do not paste**: one line says where a doc lives and when to read it. The agent fetches it only when the task needs it.
- **Skills for repeatable know-how**: the harness shows only a skill's name and description until the task matches ([[Agent Skills]]).
- **Skills, not new agents**: add domain know-how as a skill on the general agent. Build a separate agent only for isolated context, different permissions, or parallel work.
- **Stable prefix**: keep the start of the context the same between requests so [[Prefix Caching]] works.
- **Context lives where agents can see it**: rules live in versioned files, not in chat memory.
- **The file is a feedforward guide**: it steers before the agent acts. Rules that must always hold also need a feedback sensor (test, lint, hook) that checks after ([[Feedforward Guides and Feedback Sensors]]).

## What goes where

| Content | Where it lives | Why |
| --- | --- | --- |
| Rules for every task (build and test commands, hard constraints, glossary pointer) | `AGENTS.md` / `CLAUDE.md` | Loaded every turn, so keep it small |
| Runbooks, style guides, architecture notes, API docs | `docs/` or a wiki, with a pointer in `AGENTS.md` | Read only when the task needs them |
| Repeatable procedures with scripts or templates (migrations, releases) | A skill (`SKILL.md` folder) | Loaded only when triggered |
| Facts about the codebase (types, schema, config) | The code itself ([[Durable Facts in Native Homes]]) | One source of truth, cannot drift |
| Dates, versions, per-run values | Tool calls or the user turn, never the system prompt | Changing values break the prefix cache |

## Writing a skill

Use this when step 4 moves a procedure into a skill.

| Check | Rule |
| --- | --- |
| Folder | `<name>/SKILL.md`, plus `scripts/`, `references/`, `assets/` only when needed |
| `name` | Lowercase letters, digits, hyphens; max 64 chars; no leading, trailing, or double hyphen; same as the folder. On Claude, not `anthropic` or `claude` |
| `description` | Max 1024 chars. Says what the skill does **and** when to use it, in the words a user would type |
| Body | Process steps, decisions, and exit criteria only. Under 500 lines and about 5,000 tokens |
| References | One level deep from `SKILL.md`, one table of contents ([[Progressive Disclosure Depth (Flat vs Hierarchical)]]) |
| Scripts | Save working code in `scripts/` so the agent runs it instead of rewriting it |
| Verification | End with a check the agent runs before it reports done: a test, a validation script, or a render ([[Self-Verification Loop]]) |
| Review | A human reviews skills the agent drafts. Unreviewed self-written skills gave no average benefit in SkillsBench |
| Security | Read every community skill before install. Run scripts in a sandbox |

Keep each skill focused on one job. Several small skills work better than one skill that holds the whole manual.

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Audit the file, sort each section into the table above, draft pointers, move content out, check pointers resolve |
| Human does | Confirm which rules truly apply to every task, review moved content for lost rules |
| Human decides | The size budget, and what stays in the always-loaded file |

## Steps

| # | Step | Owner (AI / Human / Decision) | Done when |
| --- | --- | --- | --- |
| 1 | Measure the file: lines, tokens, number of sections | AI | Size is recorded against the budget |
| 2 | Sort each section with the "What goes where" table | AI | Every section has a target home |
| 3 | Confirm the every-task rules | Decision | The keep list is approved |
| 4 | Move the rest out to docs or skills | AI | Each moved block lives in its new file |
| 5 | Replace each moved block with a one-line pointer: *for <task>: read <path> first* | AI | Pointers name both the trigger and the path |
| 6 | Remove dynamic values (timestamps, run IDs, versions) from the always-loaded file and system prompt | AI | The prefix is identical across runs |
| 7 | Rewrite what is left in ASD-STE100, Level 1 ([[01 Using ASD-STE100 with Agents]]) | AI | Rules pass the checklist |
| 8 | Run sample tasks that need a moved doc, and check the agent follows the pointer | AI | The agent reads the right doc for each task |
| 9 | Review moved content for rules that were dropped or weakened | Human | No rule was lost |

## Pointer format

```text
## Runbooks
- For production releases or rollbacks: read docs/runbooks/deploy.md first.
- For database migrations: use the db-migration skill.
- For UI styling rules: read docs/frontend/style.md.
```

Each line has a **trigger** (when) and a **path** (where). A pointer with no trigger is a list of files, and the agent will not know when to open one.

## Session hygiene

The file is one half. The other half is keeping each session short enough to stay in the [[Smart Zone and Dumb Zone|smart zone]].

| Signal | Action |
| --- | --- |
| Context past about 100k tokens, or the agent repeats a corrected mistake | **Compact**: summarize into a clean state, then continue |
| The task changes, or the agent is confused after compaction | **Clear**: start a fresh session from a handoff file |
| Long tool outputs (logs, big file reads) fill the context | Read ranges, filter output, or run the step in a sub-agent |
| A rule must hold across sessions | Put it in the instruction file or a skill, not in a chat reminder |

Do not re-explain rules in a degraded session. More text adds noise to a crowded context.

## Gates

1. The always-loaded file is within its size budget.
2. Every pointer resolves to a file or skill that exists.
3. No dynamic values in the always-loaded file or system prompt.
4. Sample tasks show the agent reads the right doc through its pointer.
5. Each new skill passes the "Writing a skill" checks, and a sample prompt triggers it.

## Pitfalls

- **Stuffing the file**: a full style guide in `AGENTS.md` costs tokens and attention on every turn, even for tasks that never touch styling.
- **Pointers without triggers**: "see docs/" gives the agent no reason to open anything.
- **Dead pointers**: a renamed doc leaves a pointer to nothing. Check pointers in CI.
- **Timestamps in the system prompt**: one changing value at the top breaks the cache for every later turn.
- **Rewriting early history**: editing or reordering early turns also breaks the cache. Compact forward instead.
- **One skill per chunk**: splitting a manual into many always-advertised skills floods the context with descriptions. Use one skill with an index in `references/`.
- **Vague descriptions**: "Helps with PDFs" gives the agent no trigger. Say what it does and when.
- **Unreviewed self-written skills**: the agent's own skill drafts need a human review before they join the shared set.
- **Unvetted community skills**: they can run code. Read them first.
- **Skills in `~/.claude/skills` only**: outside git, so not versioned or shared. Keep team skills in a repo ([[03 Setting Up a Home Repo]]).

## Escalation

- The agent still ignores a rule after the cleanup: turn it into a deterministic check (lint, test, hook), not a longer instruction ([[Agent Verification Stack]]).
- The file cannot get under budget: split it per directory or domain, with pointers to each part.

## Related

- [[Context Engineering]]
- [[Context Pointers]]
- [[Progressive Disclosure]]
- [[Prefix Caching]]
- [[Model and Harness Separation]]
- [[Smart Zone and Dumb Zone]]
- [[Five-Layer Context Hierarchy]]
- [[01 Using ASD-STE100 with Agents]]
- [[03 Setting Up a Home Repo]]
- [[Agent Skills]]
- [[Context Loading Patterns]]
- [[Self-Verification Loop]]
- [[Feedforward Guides and Feedback Sensors]]
- [[04 Running an Agent Loop]]
- [[Playbook Template]]

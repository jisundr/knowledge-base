---
type: playbook
status: draft
tags: [playbook, ai-agents, context-engineering, multi-repo, governance]
---

# Playbook - Setting Up a Home Repo

Use when agent work spans more than one repository. Outcome: one versioned repo is the control plane for agent sessions. It holds pointers to every child repo, plus shared skills, settings, wiki, and tools. Cross-repo changes have a deterministic check when teams work apart. Pattern: [[Home Repo Pattern]] (Matt Pocock), with [[Contract-Driven Workspace]] checks for distributed teams.

## Trigger

- A feature or incident needs changes in two or more repos, and an agent started in one repo cannot see the others.
- Skills, steering files, or wiki pages are copied into several repos and drift apart.
- Team skills live in `~/.claude/skills`, outside git, so nobody else gets them.

## Principles applied

- **Context lives where agents can see it**: child repos, shared skills, and decisions are one pointer away.
- **One copy, versioned**: shared config lives once, in git, not in every repo.
- **Steering reaches only the sessions you run**: a home repo cannot govern a teammate's separate clone. Back it with deterministic checks.
- **Same bar for agents and humans**: cross-repo changes face the same contract gates as any other change.

## Layout

```text
home-repo/
├── AGENTS.md          # every-task rules + pointers to child repos (or to domain files)
├── repos/             # per-domain pointer files, once you pass ~20-40 repos
├── .claude/skills/    # shared, versioned skills
├── settings.json      # shared harness permissions and tools
├── wiki/              # architecture decisions, API notes
└── tools/             # CLI scripts: DB, issue tracker, chat, logs
```

Child repo pointer:

```text
## Repositories
- Payments API (Go): ~/repos/acme/payments-api. Clone git@github.com:acme/payments-api.git if missing. Read its AGENTS.md before editing.
```

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Inventory repos and copied config, draft pointers, move shared skills and docs in, clone missing repos, create worktrees for parallel sessions |
| Human does | Confirm which config is truly shared, name repo owners, review moved skills |
| Human decides | Whether a home repo fits (team shape), the domain split, and the cross-repo governance level |

## Steps

| # | Step | Owner (AI / Human / Decision) | Done when |
| --- | --- | --- | --- |
| 1 | List the repos agents touch, and every copy of skills, steering files, and wiki pages | AI | Inventory table with duplicates marked |
| 2 | Decide the team shape: one team in one home repo, or distributed teams in separate clones | Decision | Shape is recorded; it sets step 9 |
| 3 | Create the home repo with the layout above | AI | Repo exists and is pushed |
| 4 | Write one pointer per child repo: path, clone URL, "read its `AGENTS.md` first" | AI | Every repo in the inventory has a pointer |
| 5 | Move shared skills from `~/.claude/skills` and repo copies into `.claude/skills/`; delete the copies | AI | One copy of each skill, in git |
| 6 | Move shared docs to `wiki/` and shared CLI scripts to `tools/`, with pointers in `AGENTS.md` | AI | Docs and tools are reachable by pointer ([[02 Writing Agent Instruction Files]]) |
| 7 | Set the worktree rule: parallel sessions on one child repo each get their own git worktree | AI | Rule is in `AGENTS.md`; two sessions run without collision |
| 8 | Past ~20-40 repos, group pointers by domain into `repos/<domain>.md` | AI | `AGENTS.md` lists domains, not every repo |
| 9 | Distributed teams: add cross-repo contract checks (contract tests, type sharing, drift detection) | Decision, then AI | A breaking API change fails a check before callers break |
| 10 | Run a cross-repo task end to end from the home repo | AI | The agent finds, clones, edits, and tests every affected repo |

## Pick the governance level

| Team shape | What is enough |
| --- | --- |
| Solo developer, or one team running all sessions from the home repo | Home repo alone: one session updates provider and callers, then runs every suite |
| Distributed teams in separate clones | Home repo **plus** deterministic cross-repo checks: contract tests, shared types, or a workspace manifest that flags drift and notifies callers ([[Contract-Driven Workspace]]) |
| AFK or factory agents changing shared APIs | Contract checks are mandatory, because no human watches the session ([[AI Work Autonomy Spectrum]]) |

## Gates

1. Every repo agents touch has a pointer that resolves.
2. No duplicate copies of shared skills or steering files remain.
3. `AGENTS.md` stays within its size budget (domain files once it does not).
4. Distributed teams: a deliberate breaking contract change fails a check.

## Pitfalls

- **Flat pointer list at scale**: hundreds of repos in one `AGENTS.md` overload the agent's first decision. Split by domain.
- **Trusting the home repo to govern everyone**: it steers only sessions launched inside it. A teammate's local agent changing `/v1` to `/v2` passes its own tests while callers get live 404s.
- **Mocked HTTP in caller tests**: unit tests pass after a contract break. Add contract tests at the boundary.
- **Leaving old copies behind**: a skill kept in two places drifts again. Delete the copies when you move it.
- **Shared sessions on one checkout**: parallel agents in one working tree collide. Use worktrees.

## Escalation

- A cross-repo change breaks a caller in production: add the missing contract check first, then fix the caller ([[04 Running Quality Gates]]).
- A child repo has no owner or no `AGENTS.md`: ask its team for one before agents edit it.

## Related

- [[Home Repo Pattern]]
- [[Contract-Driven Workspace]]
- [[Context Pointers]]
- [[Progressive Disclosure]]
- [[AI Work Autonomy Spectrum]]
- [[Agent Verification Stack]]
- [[02 Writing Agent Instruction Files]]
- [[Playbook Template]]

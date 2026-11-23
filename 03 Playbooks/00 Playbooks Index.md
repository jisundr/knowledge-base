---
type: index
tags: [index, playbook]
---

# Playbooks Index

Action-oriented guides: *what do I do when X happens?* Topics (`01 Topics`) explain concepts; playbooks tell you the steps. Copy [[Playbook Template]] to start a new one.

## SDLC (`SDLC/`)

The stages of an agentic SDLC ([[Agentic SDLC]], Levi Strauss pattern), each drafted so it can become a stage in [kairyn](https://github.com/jisundr/kairyn). Agents start on execution, humans make the decision.

0. [[00 Managing the Idea Backlog]]: raw idea to shaped, committed pitch; prune the rest.
1. [[01 Handling New Requirements]]: request to approved spec. (kairyn: implemented as `requirements`)
2. [[02 Designing a Solution]]: approved spec to approved plan and task list.
3. [[03 Building a Task]]: plan to PR, tests first.
4. [[04 Running Quality Gates]]: ordered CI gates with agentic autofix.
5. [[05 Reviewing and Merging a PR]]: human decision, merge, learnings.
6. [[06 Releasing and Monitoring]]: gradual release, watch signals, promote or roll back.
7. [[07 Running a Post-Incident Review]]: blameless review, AAR/AI for agent decisions, owned 30-day action items.

## Agents (`Agents/`)

How to set up and steer agents, across every SDLC stage.

1. [[01 Using ASD-STE100 with Agents]]: make agents write short, direct text with one meaning; pick a strictness level, wire it in, measure it.
2. [[02 Writing Agent Instruction Files]]: keep `AGENTS.md` / `CLAUDE.md` lean with context pointers and skills, write skills that pass the spec and review checks, keep the prefix cache warm, compact or clear degraded sessions.
3. [[03 Setting Up a Home Repo]]: one control repo for multi-repo agent work; add contract checks when teams work apart.
4. [[04 Running an Agent Loop]]: check the harness first, pick a loop maturity level, stop on exit codes, cap the budget, gate risky actions.
5. [[05 Running Parallel Agents]]: one worktree per task, Git handoffs, one remediation round then a human.
6. [[06 Using Bots]]: domain bots started by events and schedules; PR-only first, auto-merge per change type once earned.

## Inference (`Inference/`)

How to serve model requests at the right cost, latency, and quality.

1. [[01 Adding Model Routing]]: add caching, routing, and cascading in stages, each measured against a quality bar.

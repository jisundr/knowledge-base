---
type: article-note
status: reviewed
created: 2026-11-22
tags: [ai-agents, context-engineering, harness, prefix-caching, progressive-disclosure, multi-repo, home-repo]
---

Sources:

* Video: The Home Repo: The effortless multi-repo agent setup (Matt Pocock) [link](https://www.youtube.com/watch?v=hWe-j78vNpc)
* Article: The Home Repo Pattern (AI Hero) [link](https://www.aihero.dev/the-home-repo-pattern)
* Article: Home Repo (AI Coding Dictionary, AI Hero) [link](https://www.aihero.dev/ai-coding-dictionary/home-repo)
* Repo: mattpocock/dictionary-of-ai-coding (GitHub) [link](https://github.com/mattpocock/dictionary-of-ai-coding)
* Article: Home Repo vs Nool Workspace for AI Agents: We Ran Both (Nool) [link](https://www.nool.dev/blog/home-repo-vs-nool-workspace)
* Discussion: Starting/Running Claude Code @ Home while out? How do you do it? (r/ClaudeCode) [link](https://www.reddit.com/r/ClaudeCode/comments/1xxxt8q/startingrunning_claude_code_home_while_out_how_do/)

What if the reason your AI coding agent keeps forgetting project rules, inventing non-existent methods, or breaking downstream microservices isn't because the AI is inherently broken but because we've been feeding it bad context architecture?

In this lesson, you will go under the hood of AI coding systems to understand their raw mechanics, master context management, and learn how to implement the **Home Repo Pattern** to seamlessly orchestrate agents across dozen of repositories.

Here is what you will master in this lesson:

- **Analyze the mechanical separation** between stateless AI models, execution harnesses, and context windows.
- **Diagnose critical failure modes** such as attention degradation, sycophancy, and contextual hallucinations.
- **Implement effective steering** using system prompts, skills, context pointers, and progressive disclosure.
- **Architect and deploy a Home Repo** to centralize steering files, custom tooling, and multi-repository management.
- **Evaluate governance strategies** by comparing central Home Repo workflows against contract-driven workspace architectures.

# Mechanics of AI Coding: Models, Harness and Context

To get predictable results from an AI coding setup, you must first separate the **model** from the **harness**.

A **model** (like Claude 3.5 Sonnet or GPT-4o) is simply a frozen set of billions of numbers called **parameters** or weights. On its own, a model cannot read your files, execute terminal commands, or remember what you asked two minutes ago. It does exactly one thing: **next-token prediction**. It receives a sequence of fragments called **tokens**, performs a massive statistical calculation over its parameters, and predicts the next token in the sequence.

Everything that feels like an active "agent", reading files, running test suites, looping until a bug is fixed is orchestrated by the **harness** (such as Claude Code, Cursor, or Codex CLI). The harness holds the conversation history, executes tool requests, and feeds results back into the model in a continuous loop.

## The Stateless Reality & Token Arithmetic

The fundamental truth of large language models is that they are **stateless**. Nothing you do inside a coding session changes the model's frozen parameters. When an agent seems to "remember" a conversation, it is because the harness re-sends the entire conversation history on every single **model provider request**.

Because every request re-sends everything, context management becomes both a cost and quality issue:

- **Input Tokens vs. Output Tokens**: Input tokens represent everything the model reads (system prompt, session history, tool results). Output tokens are what the model writes. Output tokens take more compute and are typically billed at roughly five times the rate of input tokens.
- **Prefix Caching**: Model providers lower input costs using a **prefix cache**. If consecutive requests share an exact matching prefix (system prompt + early conversation), the provider skips re-processing that block and bills those tokens as cheap **cache tokens**. However, if a harness dynamically mutates early conversation history or injects timestamps into the system prompt, the cache breaks, and every subsequent turn incurs full input costs.

## Attention Budget & The Smart Zone

Inside the model, every token pays attention to every other token in the context window. For $N$ tokens in context, the model evaluates on the order of $N^2$ **attention relationships**. 

Because each token has a fixed **attention budget**, expanding the context window forces that budget to spread across more competitors. As a session accumulates verbose command outputs and long file reads, signal-to-noise ratio drops, a phenomenon known as **attention degradation**.

This leads directly to the **Smart Zone vs. Dumb Zone** phenomenon:
- **Smart Zone**: Early in session (under ~100k tokens), the model is focused, follows instructions sharply, and recalls loaded details accurately.
- **Dumb Zone**: As history bloats (commonly past 125k~150k tokens), instructions slip, the model repeats previously corrected mistakes, and **faithfulness hallucinations** spike.

When an agent degrades in the dumb zone, adding more text to re-explain the instructions only adds noise to a crowded room. The cure is to shrink the context through **clearing** (starting fresh) or **compaction** (summarizing history into a clean state).

# Steering and Memory: Tools, Skills, and AGENTS.md

Since the model is stateless, how do we reliably steer agent across sessions without burning through our context budget?

## The Steering Hierarchy: System Prompts and AGENTS.md

When a session opens, the harness prepends a **system prompt**, standing instructions defining who the agent is, what tools it can call, and how it should behave. Right alongside it, harnesses load project-level configuration files like **AGENTS.md**.

However, there is a common trap: **stuffing `AGENTS.md` with full style guides and runbooks**. Because `AGENTS.md` is loaded on every single turn, a bloated file permanently consumes token headroom and dilutes the model's attention budget on every request.

## Progressive Disclosure & Context Pointers

To keep the always loaded layer lean, high-performing agent setups use **progressive disclosure**, borrowed from UI design. Instead of dumping full documentation into context up front, you provide **context pointers**.

A context pointer is a single line that tells agent where to find deeper information when a specific task arises:

```
## Operational Runbooks
- For production releases or rollbacks: read internal/docs/deploy.md first.
- For UI component styling rules: consult the frontend-skills package.
```

The agent reads the small pointer up front (spending almost zero tokens) and only executes a **tool call** to fetch the full documentation if the current task calls for it.

## Modular Capabilities with Skills

A **skill** is an open standard (`agentskills.io`) for packaging reusable capabilities into a folder containing a `SKILL.md` file, optional execution scripts, and reference templates.

By default, the harness only exposes the skill's name and high-level description to the agent. When a user asks the agent to perform a matching task (e.g., "run a database migration"), the agent triggers the skill and pulls the full instructions into the context window. This gives the agent deep specialized knowledge on demand without cluttering general sessions.

# The Home Repo Pattern: Scaling Agents Across Codebases

Most real-world engineering organization don't live in a single repository. They operate across dozens of microservices, a storefront web app, a payment API, an admin dashboard, and background workers.

This structure creates a severe setup bottlenect for AI coding agents:

1. **Context Fragmentation**: An agent started inside `storefront` only sees `storefront`. If a feature requires modifying `payment-api`, the agent is blind to the dependent code.
2. **Configuration Drift**: Teams try to solve this by copying custom skills, steering files, and project wikis into every repository. Quickly, these copies drift apart.
3. **User Directory Redundancy**: Storing skills in a gloabl user directory (`~/.claude/skills`) makes them invisible to git, preventing team-wide sharing of versioning.

## The Solution: The Home Repo Pattern

Popularized by developer Matt Pocock, the **Home Repo Pattern** establishes **one dedicated repository** that acts as the central control plane for all your agent sessions.

Instead of starting your AI agent inside an individual project repository, you launch your agent session inside the **Home Repo**.

```
my-home-repo/
├── AGENTS.md            # Contains context pointers to all organization repos
├── .claude/skills/      # Shared, versioned private skills
├── wiki/                # Central Markdown LLM wiki (architecture decisions, APIs)
├── settings.json        # Shared harness permissions & tools
└── tools/               # Custom CLI scripts (Slack, DBs, GitHub integrations)
```

Inside the Home Repo's `AGENTS.md`, you define simple navigation pointers to your child repositories on disk:

```
## Organization Repositories
- Storefront (Next.js app): ~/repos/acme/storefront. Clone from git@github.com:acme/storefront.git if missing.
- Payments API (Go service): ~/repos/acme/payments-api. Read its AGENTS.md before editing.
- Admin Dashboard: ~/repos/acme/admin-dashboard.
```

## How It Operates Mechanically

1. **Zero-Setup Cloning**: When you ask an agent in the Home Repo to work on `Payments API`, it follows the path in `AGENTS.md`. If the folder doesn't exist on your machine yet, the agent automatically clones it.
2. **Git Worktree Isolation**: If you run multiple concurrent agent sessions on the same target reposistory, the agent creates a **git worktree** inside that child repository, allowing paralled feature branches without collisions.
3. **Centralized Tooling & LLM Wiki**: The Home Repo becomes a central node housing custom CLI tools (interfacing with databases, issue trackers, or Slack) and an organization-wide LLM wiki. An agent can read an alert from a custom logging tool, across both `storefront` and `payment-api` in one session.

## Scaling Limits & Progressive Disclosure

The Home Repo pattern effortlessly for **20 to 40 repositories**. Beyond that (e.g., hundreds of repos), putting every pointer into a single `AGENTS.md` file overloads the agent's initial decision space.

To scale further, apply progressive disclosure to repo pointers by domain:

```
## Repositories by Domain
- Billing Services (invoices, payments, tax): see repos/billing.md
- Customer Portals (web, mobile): see repos/portals.md
- Internal Infrastructure: see repos/infra.md
```

The agent reads `repos/billing.md` only when working on payment-related tasks.

# Multi-Repo Governance: Home Repo vs Contract Workspaces 

Operating agents across multiple repositories introduces critical questions around governance and safety. How do we ensure agent changes don't break downstream systems?

## The Spectrum of AI Work Patterns 

How much autonomy you grant an agent depends on how you structure verification:

- **Human-in-the-Loop**: The developer actively watches the session, approving tool calls and steering the agent mid-turn. Essential for high-risk changes like schema migrations.
- **AFK (Away From Keyboard)**: The agent runs unattended in a isolated **sandbox** (a container or restricted shell) with auto-approved permissions, finishing its work as a Pull Request for later review.
- **Software Factory**: Automated triggers (CI failures, cron schedules, new Github issues) launch AFK agent sessions automatically without human intervention.
- **Vibe Coding**: Accepting an agent's code based purely on superficial execution without inspecting the diff, acceptable for throwaway prototypes, dangerous for production systems.
- **Dark Factory**: A codebase where software factory agents continuously generate and land code without any human review, relying entirely on automated verification.

## The Cross-Repository Breaking Change Challenge

What happens when an agent changesa shared API contract across multiple repositories?

An empherical benchmark study conducted by *Nool* evaluated an API refactoring task: moving `billing-api` from `POST /v1/charges` to `/v2/charges` across dependent applications (`checkout-web`, `mobile-app`, `usage-reports`).

The study revealed a sharp contrast between architectural patterns:

| Scenario                                     | Execution Mechanism                                                                                   | Outcome                                                                                                                                                                                                  |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Single Developer + Home Repo**             | One agent launched from a Home Repo with cross-repo pointers in `AGENTS.md`                           | **Success**: The agent updated `billing-api`, navigated to all three caller repos, updated their endpoints, ran all test suites, and verified live traffic.                                              |
| **Distributed Teammatest (No Central Repo)** | A developer on the `billing-api` team asks their local agent to make the changes in isolation.        | **Silent Failure**: `billing-api` tests passed. Callers' unit tests passed (because HTTP calls were mocked). However, live integration failed with 404s because caller teams were never notified.        |
| **Contract-Driven Workspace (Nool)**         | Repositories defined in a join workspace manifest (`workspace.toml`) detailing contract dependencies. | **Governed Recovery**: Landing the API change automatically detected contract drift and dispatched `Breaking` notices to caller repos.  Caller agents ingested these notices and self-healed their code. |

## Key Takeaways for Multi-Repo Architecture

- **For Solopreneurs & Unified Teams**: The **Home Repo Pattern** is lightweight, free, and highly effective. A single session can manage changes across all repos cleanry.
- **For Distributed Enterprise Teams**: A Home Repo only steers sessions that execute inside it. When independent team works in separate repo clones, complement your agent steering with **automated checks** (type-checkers, linters, contract testing) or workspace tools that detect breaking contract drift when code lands.

# Key Takeaways 

- **Models are Stateless:** Agents don't "remember" across sessions; harnesses re-send history on every request. Keep input lean to protect your prefix cache and token budget.
- **Beware Attention Degradation:** Long sessions dilute instruction following as the context fills. Clear or compact history when moving into the "dumb zone."
- **Use Progressive Disclosure:** Avoid stuffing large style guides into `AGENTS.md`. Keep always-loaded files short and use **context pointers** and **skills** to load deep knowledge on demand.
- **Adopt the Home Repo Pattern:** Centralize shared skills, steering rules, custom tooling, and multi-repo pointers in a single git repository. Run your sessions from the Home Repo to operate across all project repos without configuration duplication.
- **Layer Verification for High Autonomy:** To run agents AFK or in a Software Factory, enforce deterministic automated checks (types, tests, lints) and automated contract drift tracking.

# Topics

- See [[Model and Harness Separation]]
- See [[Prefix Caching]]
- See [[Smart Zone and Dumb Zone]]
- See [[Progressive Disclosure]]
- See [[Context Pointers]]
- See [[Context Engineering]]
- See [[Home Repo Pattern]]
- See [[Contract-Driven Workspace]]
- See [[AI Work Autonomy Spectrum]]
- See [[AFK Agent Execution]]
- See [[Autonomous Software Factory]]
- See [[Agent Verification Stack]]

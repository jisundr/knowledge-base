---
type: article-note
status: reviewed
created: 2026-11-22
tags: [ai-agents, agent-skills, progressive-disclosure, context-engineering, verification, benchmarks]
source: https://www.youtube.com/watch?v=HIRDzMtuWFk
---

Sources:

* Video: Anthropic Engineer Explains: What to Build Instead of AI Agents [link](https://www.youtube.com/watch?v=HIRDzMtuWFk)
* Docs: Agent Skills (Claude Platform Docs) [link](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
* Docs: Agent Skills (Microsoft Learn) [link](https://learn.microsoft.com/en-us/agent-framework/agents/skills)
* Article: What are Agent Skills? (Google Cloud) [link](https://cloud.google.com/discover/ai-agent-skills)
* Paper: Is Progressive Disclosure All You Need for Long-Context Agents? (arXiv) [link](https://arxiv.org/html/2607.17598v1)
* Article: Progressive Disclosure in AI Agents: How to Load Context Without Killing Output Quality (MindStudio) [link](https://www.mindstudio.ai/blog/progressive-disclosure-ai-agents-context-management)
* Spec: Agent Skills Specification (agentskills.io) [link](https://agentskills.io/specification)
* Talk: Don't Build Agents, Build Skills Instead (Barry Zhang and Mahesh Murag, AI Engineer Code 2025) [link](https://www.ai.engineer/talks/agent-skills)
* Article: Donating Agent Skills to the Agentic AI Foundation (Anthropic) [link](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)
* Article: Agent Skills Work, But the Research Shows Most Teams Are Building Them Wrong (O'Reilly Radar) [link](https://oreilly.com/radar/agent-skills-work-but-the-research-shows-most-teams-are-building-them-wrong)
* Article: Agent skills look great in benchmarks but fall apart under realistic conditions (The Decoder) [link](https://the-decoder.com/agent-skills-look-great-in-benchmarks-but-fall-apart-under-realistic-conditions-researchers-find/)

What if the key to building smarter, more reliable AI agents isn't expanding their context windows, but actually feeding them *less* information at startup?

In this lesson, you will master the open specification for **Agent Skills**, a modular, filesystem-based framework that replaces bloated, monolithic system prompts with lightweight, on-demand capabilities. Through real-world technical architecture, practical authoring guidelines, and empirical research benchmarks, you will learn how to build specialized AI agents that stay fast, cost-effective, and highly accurate.

**Learning Objectives**:

- **Explain** the architecture of Agent Skills and why modular skills outperform traditional monolithic system prompts.
- **Implement** the 4-stage progressive discolsure lifecycle (*Advertise*, *Load*, *Read*, *Run*) to prevent context rot.
- **Author** production-ready `SKILL.md` packages with correct YAML metadata, structured resources, and executable scripts.
- **Apply** advanced context engineering patterns, including Index-First loading, Scout pre-screening, and self-verification loops.
- **Analyze** empirical research comparing raw document navigation, flat disclosure, and hierarchical routing across multi-document datasets.

# The Evolution from Monolithic Prompts to Module Agent Skills

In the early days of agent development, the standard approach to giving an AI specialized knowledge was straightforward: stuff everything into the system prompt. API schemas, corporate compliance policies, style guides, edge-case rules, and historical examples were pre-loaded into every single turn of the conversation.

While this felt thorough, it created a severe failure mode know as **context rot**. As an LLM's working memory fills up, its attention degrades non-linearly. Instructions buried tens of thousands of tokens deep get overlooked or contradicted, a phenomenon known as *inverted U failure pattern* or *"lost in the middle."* Furthermore, pre-loading massive prompt context burns millions of tokens unnecessarily, driving up API costs and response latency.

To understand the solution, consider a helpful mental model: **your LLM is like a smartphone**.

- The **model** is the hardware processor.
- The **agent runtime** is the operating system.
- **Agent Skills** are the individual apps you install.

You wouldn't launch every installed application on your phone into RAM simultaneously just to send a text message. Similarly, general-purpose agents (such as Claude Code, Gemini Platform, or Microsoft Agent Framework) don't need every domain rule loaded upfront. Instead, they run a lightweight general runtime and pull in modular **Agent Skills** only when a specific job demands them.

**Key advantages of Agent Skills:**

- **Token Efficiency**: Only metadata (~100 token per skill) occupies initlal context. 
- **Interoperability**: Based on an open specification (`agentskills.io`), skills work across Anthropic, Google Cloud, Microsoft Agent Framework, VS Code, Cursor, and custom CLI harnesses.
- **Version Control**: Skills exist as clean filesystem directories tracked directly in Git.
- **Deterministic Execution**: Skills offload heavy calculations and file manipulations to pre-written scripts, preventing LLM math hallucinations.

# Mechanics of Progressive Disclosure: The 4-Stage Lifecycle

At the heart of the Agent Skills specification is **progressive disclosure**, a design principle borrowed from the user experience (UX) engineering. Instead of presenting all information upfront, progressive disclosure reveals context in dynamic layers only as the current task requires it.

Agent Frameworks implement progressive disclosure across a structured **4-stage lifecycle**:

1. **Stage 1: Advertise (~100 tokens per skill)**: At startup, the agent loads only the lightweight YAML frontmatter (`name` and `description`) of every available skill into its system prompt. The full instructions stay dormant on disk. This minimal footprint allows you to install dozen of skills without incurring context penalties.
2. **Stage 2: Load (< 5,000 tokens recommended)**: When a user prompt matches a skill's description, the agent triggers the skill. It issues a file read command (such as `load_skill` or `cat /mnt/skills/pdf/SKILL.md`) to pull the main instruction into active memory.
3. **Stage 3: Read Resources (Loaded as Needed)**: If `SKILL.md` references detailed external guides, database schemas, or API docs (e.g., `refernces/FORMS.md`), the agent reads those specific files only when executing that step.
4. **Stage 4: Run Scripts (Executed Off-Context)**: When deterministic tasks (like data validation or slide rendering) are required, the agent calls `run_skill_script` to run executable Python or Bash scripts bundled in `scripts/`. Crucially, the script code itself never enters the context window, only the script's output (e.g., *"Validation Passed"*) is returned to the model.

**Security & Govenance Controls**: Because skills can execute code, safety is paramount. All skill tools (`load_skill`, `read_skill_resource`, `run_skill_script`) enforce approval policies by default. Read-only tools can be safely auto-approved via rules, while script execution should run inside sandboxed container environments with restricted network access.

# Authoring Agent Skills: SKILL.md, Bundled Assets, and Best Practices

Creating an Agent Skill is as simple as creating a directory with a standardized layout. Let's inspect the required architecture of a production-grade skill.

**Standard Directory Structure**:

```
expense-report/
├── SKILL.md                          # Mandatory core file
├── scripts/
│   └── validate.py                   # Executable scripts
├── references/
│   └── POLICY_FAQ.md                 # On-demand reference docs
└── assets/
    └── expense-template.md           # Templates and static resources
```

**The SKILL.md Specification**: Every skill must contain a `SKILL.md` file beginning with strict YAML frontmatter, followed by Markdown instructions:

```
---
name: expense-report
description: File and validate employee expense reports against company policy. Use when asked about expense submissions, reimbursement rules, or spending limits.
compatibility: Requires python3 and pdfplumber
---
# Expense Report Workflow
1. Review submission against reimbursement rules in references/POLICY_FAQ.md.
2. Run scripts/validate.py to inspect uploaded receipts.
```

**Strict Field Requirements**:

- `name`: Max 64 characters. Must contain only lowercase letters, numbers, and hypens. Must match the parent directory name. Cannot contain reserved words like `anthropic` or `claude`.
- `description`: Max 1024 characters. Non-empty. Must explicitly state **what** the skill does and **when** the agent should trigger it. Include triggering keywords a user would naturally say.
- **Markdown Body**: Keep main `SKILL.md` instructions under 500 lines. Focus on clear procedural steps, decision trees, and explicit exit criteria. Move long reference manuals into `references/`.

**The DRY (Don't Repeat Yourself) Principle in AI Skills**: Anthropic and Microsoft engineers noticed that LLMs frequently waste thousands of tokens rewriting identical Python scripts from scratch on every run (e.g., wring script code to format PowerPoint slides). The DRY principle dictates that once an LLM generates a script that works, you should save that file into `scripts/` as permanent tool for its future self. Future runs simply execute the proven scripts.

# Advanced Context Engineering & Self-Verification Patterns

Beyond basic file organization, production agent systems utilize advanced context engineering patterns to maintain output quality across long, multi-step sessions.

**Four Core Context Management Patterns**:

1. **Index-First Loading**: Instead of loading full reference files upfront, give the agent a structured index describing available resources. The agent inspects the index and selectively requests only the specific file needed for the active subtask.
2. **The Scout Pattern**: Send a lightweight pre-screening prompt ahead of the primary agent run. The "Scout" analyzes incoming user requests, identifies exact resource dependencies, and generates a minimal loading manifest for the primary worker agent.
3. **Phase-Based Context Loading**: Divide complex tasks into distinct phases (*Research -> Planning -> Execution -> Review*). Scope context strictly to the active phase, and clear or compact working memory before transitioning to the next phase.
4. **Script/Process Separation**: Keep `SKILL.md` focused strictly on process logic and workflow steps. Do not embed raw data, templates or heavy reference code inside the main instruction body.

**Baking in Quality: Self-Verification Loop**

A critical flaw in naive AI workflows is returning an agent's first draft directly to the user. High0-reliability skills incorporate automated **verification loops** before final output delivery. 

**How to build Verification into a Skill**:

- **Visual Inspection**: For slide generation skills, instruct the skill to render slides as images, inspect the visual layout, correct cropped text, and re-render.
- **Deterministic Testing**: For coding or data skills, require the agent to run validation scripts or unit tests before calling the task complete.
- **Personal Critique**: For subjective tasks (like copy or marketing strategy), instruct sub-agents (e.g., a *Skeptical Buyer personal*) to review the draft, identify friction points, and apply revisions automatically.

Rule of thumb: *Your user's first look at an agent's output should be the agent's fourth or fifth internal pass*.

# Empirical Benchmarks: Single-Book Reasoning vs. Library Scale

While progressive disclosure sounds intuitively powerful, how does it hold up under rigorous scientific benchmarking? A landmark controlled study (*"Is Progressive Disclosure All You Need for Long-Context Agents?"*) evaluated agent skill packaging across **∞Bench** long-document reasoning tasks.

The study evaluated three distinct document access strategies:

- **Raw Navigation (`raw`)**: Handling the agent unindexed raw text files and letting it search or grep on its own.
- **Flat Disclosure (`flat`)**: A single `SKILL.md` whose root description gatest access to an internal table of contents indexing chunk files in `references/`.
- **Hierarchical Disclosure (`hierarchical`)**: A deep tree where every document chunk is its own skill with an always-loaded child description under a meta-router.

**Key Empirical Discoveries**:

1. **Single-Book Scale (~100,000+ Tokens)**:
	- On a single book, `flat` disclosure improves performance for weaker navigation harnesses (such as Pi or Claude Code),
	- However, for highly capable navigators (like Codex on GPT-5.4), `flat` disclosure add little accuracy benefit because the bare model already natively greps for entity names effectively. **Progresive disclosure buys context management, not raw intelligence**.
2. **Library Scale (10 to 20 Books)**:
	- As corpus size scales to multi-book library, `raw` **document navigation completely collapses** (English Open QA accuracy drops from ~66% down to 25%). The bare agent gets lost traversing raw files.
	- `flat` **disclosure rescues performance**, holding accuracy at ~46% while **cutting token consumption by ~50%**. A single-level pre-cut index allows the agent to commit to the target document before burning context window capacity.
3. **The Depth Paradox (Why Hierarchical Disclosure Fails):**
    - Counterintuitively, pushing progressive disclosure deeper into a multi-tiered hierarchy (`hierarchical`) **degrades or breaks accuracy**.
    - Why? Because forcing every chunk's description to remain always-loaded in context floods the top-level router with metadata tokens. This context clutter causes context rot at the routing level. **A single flat level of progressive disclosure is optimal!**

# Key Takeaways 
- **Avoid Context Rot:** Pre-loading massive context dilutes attention and degrades LLM instruction-following. Agent Skills keep working context lean by loading information on demand.
- **Master the 4-Stage Lifecycle:** Skills operate via _Advertise_ (~100 token metadata footprint), _Load_ (instructions pulled on trigger), _Read_ (supplemental references loaded as needed), and _Run_ (scripts executed in sandboxes off-context).
- **Adhere to SKILL.md Standards:** Frontmatter requires a strict `name` (lowercase, hyphens, max 64 chars) and a clear `description` (max 1024 chars stating _what_ it does and _when_ to trigger). Keep instruction bodies under 500 lines.
- **Follow the DRY Principle:** Save proven, working Python or Bash scripts inside `scripts/` so agents don't waste tokens repeatedly rewriting code from scratch.
- **Incorporate Verification Loops:** Ensure skills evaluate their own work (via automated test runs, visual image inspections, or critique personas) before returning final answers.
- **Keep Routing Flat:** Benchmark research proves that single-level `flat` disclosure prevents reasoning collapse at library scale without causing the context rot associated with deep `hierarchical` routing trees.

# Topics

- See [[Agent Skills]]
- See [[Progressive Disclosure]]
- See [[Progressive Disclosure Depth (Flat vs Hierarchical)]]
- See [[Context Loading Patterns]]
- See [[Self-Verification Loop]]
- See [[Lost in the Middle]]
- See [[Context Engineering]]
- See [[AI Agents and Tool Use]]

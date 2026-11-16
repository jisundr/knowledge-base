---
type: video-note
status: reviewed
created: 2026-11-15
tags: [ai-engineering, ai-agents, memory]
source: https://www.youtube.com/watch?v=tTcxVv8HHNw
---

Source: https://www.youtube.com/watch?v=tTcxVv8HHNw
Notebook: https://notebook.google.com/notebook/fd631981-debe-47b7-b8d4-aa7f45526fda

Lamis Mukta from Anthropic explores context engineering and introduces the concept of "**dreaming**" as a way to enhance AI agent memory and performance. She explains that while raw model intelligence is powerful, compounding that intelligence requires effective management.

# The Evolution of Context Engineering: From Files to Autonomous Tools

The evolution of context engineering over the past year has moved from static file injections to fully autonomous, multi-agent memory architecture through several distinct milestones:

- **Claude MD Files**: Context engineering began by injecting simple markdown files (such as  `CLAUDE.md`files launched with Claude Code) into the start of an agent's context window. These Markdown instructions were unreasonably effective at steering agent behavior, communicating codebase structure, and setting user preferences. However, faced severe **context bloat** as instruction files grew longer over time.
- **Autonomous In-Band Memory Tools**: To move beyond static instructions, developers gave memory tools that allowed agents to autonomously decide when to read, write, and update memories during an active session (in-band). It established autonomy in memory management, giving agents control over saving and retrieving relevant details during a task.
- **Skills & Progressive Disclosure**: To handle complex procedural workflows without overflowing context, Anthropic introduced skills to address context bloat using **progressive disclosure**. Agents scan high-level front-matter metadata (a few sentences at the top of a skill file) and only load the complete body into context when relevant. This operates like pulling a specific book off a bookshelf when needed rather than carrying every book in the conversation.
- **File Systems as Memory**: Rather than building overly complex custom APIs, agents use standard utilities like `bash` and `grep` to index, search, and edit markdown memory files.

# Scaling Memory to Production: Engineering Guardrails

Building autonomous file-system memory for a single agent in the demo is straightforward, but scaling the same system to a large-scale enterprise environment introduces severe operational challenges. Here are the four primary issues encountered in real-world deployments:

- **Race Condition**: Multiple agents attempting to update the exact same memory file simultaneously.
- **Contamination and Poisoning**: A single confused agent writing incorrect data to organization-wide instructions, spreading errors to all other agents.
- **Stale Context**: Outdated preferences lingering long past their relevance.
- **Human-Agent Friction**: Unclear tracking when humans and agents edit shared files together.

Solving these problems required incorporating traditional and strict software engineering principles:
- **Versioning**: Storing version history and transcript context so updates can be audited or rolled back.
- **Concurrency**: Using hashing checks before commits to prevent agents from overwriting concurrent memory updates.
- **Layered Permissioning**: Restricting write permissions so standard agents can read only the top-level organizational knowledge, while keeping local scratchpads fully editable.
- **Portability**: The memory system should expose clean, standardized APIs, ensuring curated domain context remains accessible across different product interfaces and toolchains.

# The Concept of Dreaming

While in-band memory (within a session) is useful. it still hits tow fundamental bottlenecks:
- **Split Focus and Token Resources**: An agent tasked with solving a complex coding bug faces a difficult trade-off: how many tokens and cognitive cycles should it spend fixing the code versus updating memory notes for future sessions?
- **Limited Visibility Scope**: An agent operating inside a single session window cannot see systemic patterns. If twenty different agents fail at the exact same task in the exact same way across an enterprise, no individual agent has enough context to detect the trend.

Anthropic introduces an asynchronous, out-of-band batch process called **Dreaming**.

## How does the Dreaming process work?

Dreaming runs asynchronously in batch mode during off-peak hours using dedicated token allocation. An **orchestrator agent** collects recent session transcripts, tool execution logs, and metadata across the agent fleet. This orchestrator spawns specialized **sub-agents** to analyze the transcripts against the current memory store, pinpointing systemic failures or missing information. The orchestrator synthesizes findings and proposes concrete memory changes. Crucially, it provides human operators with prevalence statistics and transcript excerpts justifying why a context file should be added, modified, or deleted.

## Real-World Dreaming Fixes
- **Missing Knowledge**: Spotting that every agent failed a domain question because the memory store lacked key background context, then automatically adding the missing guide.
- **Broken Tool Instructions**: Noticing agents consistently misusing a tool parameter (e.g., passing angle values in radians instead of degrees) and updating tool instructions.
- **Formatting Compliance**: Detecting fleet-wide stylistic errors ( e.g., excessive use of em dashes) and adding explicit organizational style rules.

# Key Takeaways
- **Context Multiples Intelligence**: Model updates alone do not compound performance; tailored organizational context acts as an intelligence multiplier.
- **Progressive Disclosure Controls Bloat**: Loading metadata headers first (as seen in Skills) prevents context window overload while preserving access to deep procedural details.
- **Production Demands Mechanical Guardrails**: Multi-agent architectures require optimistic locking via hashing, transcript-linked versioning, and strict read/write permission tiers to prevent context corruption. 
- **Dreaming Enables True Fleet Learning**: Out-of-band dreaming decouples task execution from memory curation, leveraging dedicated token budgets to analyze cross-session transcripts, prune stale notes, and update global context asynchronously.

# Multimillion Dollar Questions
- Given this level of context engineering optimization, how can I implement this on my own?

# Notes
- Learn Concurrency Control using Hashing
- Research existing implementations of Dreaming 
# Topics

See [[Context Engineering]], [[Agent Memory]], [[Progressive Disclosure]], [[Memory Guardrails for Multi-Agent Systems]], [[Dreaming (Agent Memory Consolidation)]], [[AI Agents and Tool Use]]

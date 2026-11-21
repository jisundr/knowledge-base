---
type: video-note
status: reviewed
created: 2026-11-21
tags: [ai-engineering, ai-agents, context-engineering, sdlc, architecture]
source: https://www.youtube.com/watch?v=-QFHIoCo-Ko
---

Sources:

* Video: Full Walkthrough: Workflow for AI Coding — Matt Pocock [link](https://www.youtube.com/watch?v=-QFHIoCo-Ko)
* Repo: mattpocock/skills [link](https://github.com/mattpocock/skills)


What if the secret to building high-quality software with AI isn't learning a brand-new framework, but doubling down on 20-year-old software engineering principles? While many developers attempt "vibe coding" or naive spec-to-code prompting only to watch their LLMs get hopelessly confused, elite engineers treat AI context windows with the discipline of system architecture.

By mastering a structured workflow designed specifically around Large Language Models actually work, you can delegate tedious implementation while retaining total architectural control. In this lesson, you will learn to:

- **Analyze** LLM context constraints to keep AI agents operating strictly within their high-cognition "smart zone."
- **Execute** grilling sessions to build shared design concepts and domain glossaries that eliminate prompt misalignment.
- **Deconstruct** product requirements into vertical slices and tracer bullets structured as parallelizable task graphs.
- **Implement** test-driven feedback loops and deep module architecture to prevent codebase entropy during automated coding runs.

# Navigating LLM Constraints: The Smart Zone and the Memento Effect

Working with an Large Language Model (LLM) is a bit like working with the protagonist of the film *Memento*, the agent continually resets back to its base state, oblivious to what happened five conversation ago unless it is explicitly recorded. Furthermore, as Dex Horthy of Human Layer identifed, LLMs do not maintain uniform intelligence throughout long sessions. They operate in two distinct cognitive realms: the **Smart Zone** and the **Dumb Zone**.

When you begin a fresh conversation, the model is in its Smart Zone. The attention relationship between tokens are unstrained. Because attention calculation scales quadratically with token count, think of how adding teams to a sports league quadratically increase the total number of matches, the model starts losing focus around **100k tokens** (or roughly 40% of its context window), regardless of whether its advertised limit is 200k or 1 million tokens. Beyond this threshold, attention degrades and the model enters the Dumb Zone, where it starts making careless errors and stupid decisions.

To combat this degradation, developers often rely on **compacting** (summarizing prior chat history into a persistent header). However, compacting leaves behind "sediment", residual, low-signal noise that pollutes context over time. A far superior pattern is embracing the Memento effect: keeping system prompts tiny, executing tight tasks in fresh context windows, and delegating exploratory research to **sub-agents** with isolated context windows that return concise summaries to the orchestrator.

# Aligning Intent through Relentless Grilling and Shared Vocabulary

The most catastropic failure mode in software development, whether working with humans or AI is **misalignment**. A popular trend known as "spec-to-code" suggests writing a specification document, passing it to an AI, and ignoring the underlying code. However, this fails in practice because code is your ultimate battleground, and you must maintain a deep understanding of its structure and mechanics.

Instead of guessing what you want or generating premature code, an AI agent should engage you in **grilling session** using skills like `/grill-me` or `/grill-with-docs`. Inspired by Frederick Brooks' *The Design of Design*, grilling forces the AI to relentlessly interview you, one question at a time, down every branch of the design tree until both you and the model reach a shared **design concept**.

This process also establishes a **ubiquitous language**, a core tenet of Eric Evan's *Domain-Driven Design*. By building a project `GLOSSARY.md`, you replace verbose, multi-sentence explanations with precise project jargon (for instance, replacing *"making a lesson real in the file system"* with *"materialization cascade"*). This concision pays off across every subsequent session by conserving precious smart zone tokens and making codebase navigation effortless for the agent.

# Structuring the Journey: Vertical Slices and Task Graphs

Once a grilling session resolves your design concept into a Product Requirements Document (PRD), you must map out how the AI will navigate from the idea to the implementation. Left to its own  devices, AI tends to code **horizontally**, building the entire database schema in phase one, the API layer in phase two, and the user interface in phase three.

Horizonatal coding is a trap. As highlighted in *The Pragmatic Programmer* by Dave Thomas and Andy Hunt, horizontal steps delay feedback loops until the final phase, leaving the AI coding blind across isolated layers. The solution is dividing the work into **tracer bullets** or **vertical slices**. A vertical slice touches every layer of the architecture, database schema, service logic, and UI display, in a single, minimal implementation step. This provides immediate, integrated feedback on whether the system actually works together end-to-end.

Furthermore, rather than arranging tasks in a rigid, sequential multi-phase plan, elite workflows convert PRDs into **Kanban board of tickets** formatted as a Directed Acyclic Graph (DAG). By explicitly marking blocking relationships between tracer-bullet tasks, you enable multiple independent AI sub-agents to grab non-blocking tickets and work in parallel without context pollution.

# Automated Execution, Test-Driven Feedback, and Deep Architecture

With a clear DAG backlog established, the workflow transitions from **Human-in-the-Loop** planning (the "day shift") to **Away-From-Keyboard (AFK)** execution (the "night shift"). Using autonomous execution loops like the **Ralph loop** or orchestration harnesses like **Sand Castle**, an orchestrator picks up ready tickets, spins up sandboxed environments, and runs implementer sub-agents in fresh, smart-zone context windows.

For AFK execution to succeed without producing software entropy (what Kent Beck calls "the ball of mud"), two safeguards are mandatory:

1. **Test-Driven Development (`/tdd`)**: The agent must follow a strict red-green-refactor cycle, writing a failing test first before touching implementation code. This provides an objective, automated feedback loop that prevents the AI from cheating or hallucinating success.
2. **Deep Modules**: Draing from John Ousterhout's *A Philosophy of Software Design*, bad codebases make bad agents. Shallow modules (tiny files exporting small helper functions with messy interdependencies) force agents to navigate complex dependency graphs. In contrast, **deep modules** conceal massive functionality behind a simple, clean interface.

By running skills like `/improve-codebase-architecture`, you can scan your codebase for opportunities to deepen modules.  Deep modules allow developers to design and enforce high-level interface boundaries while delegating messy internal implementation entirely to AI agents.


# Key Takeaways

- **Protect the Smart Zone**: Keep system prompts minimal, clear context frequently to stay under ~100k tokens, and delegate heavy context-gathering tasks to isolated sub-agents.
- **Grill Before Coding**: Use skills like `/grill-me` and maintain a `GLOSSARY.md` to establish a shared design concept and eliminate prompt misalignment before writing code.
- **Slide Vertically**: Avoid horizontal layer-by-layer implementation: break tasks into tracer bullets that touch all laters end-to-end for immediate feedback.
- **Build Deep Modules**: Prevent software entropy by design deep architectural boudaries with simple interfaces, allowing AI to safely handle inner implementation via strict TDD loops.

## See

- See [[Smart Zone and Dumb Zone]]
- See [[Grilling Session]]
- See [[Ubiquitous Language]]
- See [[Vertical Slices (Tracer Bullets)]]
- See [[Task Graph Backlog]]
- See [[AFK Agent Execution]]
- See [[Test-Driven Development for Agents]]
- See [[Deep Modules]]
- See [[Context Engineering]]
- See [[Agentic SDLC]]
- See [[Lost in the Middle]]
- See [[Multi-Agent Orchestration Patterns]]
- See [[Autonomous Software Factory]]

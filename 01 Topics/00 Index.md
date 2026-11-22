---
type: index
tags: [index]
---

# Topics Index

Every note in `01 Topics`, grouped by category. Start with [[AI Engineer Skill Stack]] for the learning path.

## Foundations

- [[AI Engineer Skill Stack]]: the tiered skill map for an AI engineer; hub for most topics below.

## Retrieval

- [[Embeddings and Vector Search]]: text as vectors so search matches meaning, not keywords.
- [[Retrieval-Augmented Generation (RAG)]]: grounding model answers in retrieved source data.

## Agents and Tools

- [[AI Agents and Tool Use]]: systems that act, not just answer.
- [[Model Context Protocol (MCP)]]: standard adapter layer between agents and external systems.

## Context Engineering

- [[Context Engineering]]: deliberately managing what goes into an agent's context window.
- [[Progressive Disclosure]]: load a cheap summary first, full content only when needed.
- [[Lost in the Middle]]: models attend poorly to instructions buried mid-context.
- [[Smart Zone and Dumb Zone]]: quality drops past ~100k tokens; work in fresh contexts.
- [[Model and Harness Separation]]: stateless model, agentic behavior lives in the harness loop.
- [[Prefix Caching]]: stable context prefixes are billed as cheap cache tokens.
- [[Context Pointers]]: one-line hints in `AGENTS.md` instead of inline runbooks.
- [[Home Repo Pattern]]: one control-plane repo for agent sessions across many repos.
  - [[Contract-Driven Workspace]]: manifest-declared contracts that flag cross-repo breaking changes.
- [[Interpretable Context Methodology (ICM)]]: filesystem structure instead of framework code.
  - [[Five-Layer Context Hierarchy]]: ICM's layers, loaded from global to run-specific.
  - [[Stage Contract]]: the per-stage `CONTEXT.md` spec.

## Agent Memory

- [[Agent Memory]]: persistent knowledge carried across sessions.
- [[Dreaming (Agent Memory Consolidation)]]: async batch review that proposes memory updates.
- [[Memory Guardrails for Multi-Agent Systems]]: engineering controls for shared memory at scale.

## Code Quality and Verification

- [[Inverse Pyramid of Constraints]]: deterministic checks first, natural-language rules last.
- [[Categorical Elimination of Anti-Patterns]]: ban a pattern class instead of fixing instances.
- [[Agent Verification Stack]]: tiers of automated checks so humans review evidence, not code.
  - [[Property-Based UI Testing]]: randomized interactions asserting invariants.
  - [[Statecharts and State Machines]]: review behavior as states and transitions.
  - [[Formal Verification (TLA+ and Lean)]]: proofs of design invariants for critical logic.
- [[Test-Driven Development for Agents]]: red-green-refactor as the agent's objective feedback loop.
- [[Deep Modules]]: simple interfaces over large functionality so agents work safely inside.

## Evaluation

- [[AI System Evaluation]]: judge the whole pipeline, using Goldens, Test Cases, and Traces.
  - [[Evaluation Dataset Design (5 D's)]]: what makes an eval dataset trustworthy.
  - [[Evaluator Cascade]]: deterministic checks first, LLM and human review last.
  - [[LLM-as-a-Judge]]: rubric-based scoring, biases, and calibration.
  - [[Evaluation Error Analysis Flywheel]]: open/axial coding and five deployment stages.
  - [[Multi-Agent Orchestration Patterns]]: sequential, parallel, hierarchical, reflexive.
  - [[LLM Evaluation Tooling]]: DeepEval, Promptfoo, Langfuse, and peers.
  - [[LLM Evaluation Glossary]]: definitions for benchmark, scorer, and statistics terms.

## Process and Automation

- [[Agentic SDLC]]: redesigning the lifecycle around agents.
- [[Autonomous Software Factory]]: deterministic boundaries plus verification for high-velocity output.
- [[AI Work Autonomy Spectrum]]: human-in-the-loop, AFK, software factory, dark factory.
- [[Long-Running Agent Harness]]: brain, hands, and session layers for multi-hour agent work.
  - [[Ralph Loop]]: pick ready task, build, get judged, record lessons, repeat.

## AI-Assisted Design and Planning

- [[Grilling Session]]: the agent interviews you until you share a design concept.
- [[Ubiquitous Language]]: a project `GLOSSARY.md` of precise shared terms.
- [[Vertical Slices (Tracer Bullets)]]: end-to-end slices through every layer, not layer by layer.
- [[Task Graph Backlog]]: tickets as a DAG so sub-agents work in parallel.
- [[Spec-Driven Development]]: requirements, design, and tasks as Markdown specs in the repo.
  - [[EARS Notation]]: one testable sentence per requirement, in a fixed shape.
  - [[Spec Exit Strategy]]: what to keep, promote into code, or delete after a feature ships.
    - [[Spec Persistence Models]]: flow-back, flow-forward, living spec, constitution-only.
    - [[Durable Facts in Native Homes]]: move lasting rules into schemas, tests, and policies.
- [[Design Document Types]]: PRD, RFC, spec, and ADR, by the question each answers.
- [[Architecture Decision Record (ADR)]]: immutable record of one load-bearing decision.
- [[SDLC Documentation Glossary]]: change brief, constitution.md, Nygard format, MADR.
- [[AFK Agent Execution]]: human "day shift" planning, unattended "night shift" implementation.

## Product Discovery and Shaping

- [[Problem-First Thinking]]: start from the customer problem, not the feature.
- [[Product Trio]]: PM, designer, and tech lead own discovery together.
- [[Four Big Product Risks]]: value, usability, feasibility, viability.
- [[Product-Minded Engineer]]: engineers who engage with the why, not just the ticket.
- [[Shaping (Shape Up)]]: bound a raw idea with an appetite before building.
- [[Product Discovery Glossary]]: appetite, breadboarding, fat-marker sketch, and peers.

## AI Output and Communication

- [[AI Output Ladder]]: four tiers of output, from clean text to diagrams, interactive HTML, and video.
  - [[Simplified Technical English (ASD-STE100)]]: aerospace controlled language for one-meaning text.
  - [[80% ASD-STE100 Prompting]]: one-line prompt modifier for short, direct output.
  - [[SimpleEnglish Agent Skill]]: STE packaged as a benchmarked agent skill, scoped to technical docs.
  - [[Disposable Software Artifacts]]: single-use generated tools for understanding a topic.

## Model Routing and Inference Cost

- [[LLM Routing]]: pick the cheapest capable model from the prompt, before generation.
- [[LLM Cascading]]: start on a cheap model, escalate when the answer fails a check.
- [[Cascade Routing]]: flexible first dispatch plus quality-based rerouting.
- [[Semantic Caching]]: return stored answers for semantically matching prompts.
- [[LLM Routing in Production]]: cache first, fast hot path, circuit breakers, start simple.

## Deployment and Operations

- [[Containerization and Orchestration]]: Docker and Kubernetes for reliable agent execution.

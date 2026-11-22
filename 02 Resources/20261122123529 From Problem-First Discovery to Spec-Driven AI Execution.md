---
type: article-note
status: reviewed
created: 2026-11-22
tags: [product-discovery, shape-up, spec-driven-development, ears, ai-agents, long-running-agents]
---

Sources:

* Article: The Trap of Solution-First Thinking (caines.ca) [link](https://caines.ca/posts/2019-02-24-the-trap-of-solution-first-thinking/)
* Article: Product managers need a problem-first mindset (Product-Led Alliance) [link](https://www.productledalliance.com/product-managers-need-a-problem-first-mindset/)
* Article: Discovery - Delivery (Silicon Valley Product Group) [link](https://www.svpg.com/discovery-delivery/)
* Article: Opportunity Solution Trees: Visualize Your Discovery to Stay Aligned and Drive Outcomes (Product Talk) [link](https://www.producttalk.org/opportunity-solution-trees/)
* Article: How “The Product Gap” Has Already Doomed Your Transformation To Failure (Michael Goitein) [link](https://michaelgoitein.com/how-the-product-gap-has-already-doomed-your-transformation-to-failure/)
* Article: The Product-Minded Software Engineer (The Pragmatic Engineer) [link](https://blog.pragmaticengineer.com/the-product-minded-engineer/)
* Article: Best Practices for Product Managers to Collaborate Effectively with Engineering Teams [link](https://swecareer.substack.com/p/building-stronger-bridges-best-practices)
* Article: Product Owner Anti-Patterns — An Introduction [link](https://handsonagile.substack.com/p/product-owner-anti-patterns-an-introduction)
* Article: Product Ownership Anti-Patterns: How To Avoid Them (Platinum Edge) [link](https://platinumedge.com/common-product-ownership-anti-patterns-and-how-to-avoid-them)
* Book: Shape Up: Stop Running in Circles and Ship Work that Matters (Basecamp) [link](https://basecamp.com/shapeup)
* Book chapter: Find the Elements (Shape Up) [link](https://basecamp.com/shapeup/1.3-chapter-04)
* Book chapter: Write the Pitch (Shape Up) [link](https://basecamp.com/shapeup/1.5-chapter-06)
* Article: Upstream & Discovery Kanban (Kanban Tool) [link](https://kanbantool.com/kanban-guide/upstream-discovery-kanban)
* Article: Kiro Specs: Requirements, Design, Tasks, EARS Notation [link](https://kirotutorial.com/concepts/specs/)
* Article: Spec-Driven Development with GitHub Spec Kit: A Practical Guide (SaM Solutions) [link](https://sam-solutions.com/blog/spec-driven-development-github-spec-kit/)
* Article: Taskmaster AI: Structured task management for AI agents, CLI-first (Hamster) [link](https://tryhamster.com/research/taskmaster)
* Article: Transform Project Management with Git and AI: backlog.md (DEV Community) [link](https://dev.to/thedavestack/transform-project-management-with-git-and-ai-backlogmd-28d0)
* Video: Beads Crash Course: Steve Yegge's Issue Tracker for Coding Agents [link](https://www.youtube.com/watch?v=ztZdTOhkxKs)
* Docs: Assign and delegate issues (Linear Docs) [link](https://linear.app/docs/assigning-issues)
* Docs: Using the Copilot Coding Agent (GitHub Copilot Learning Hub) [link](https://awesome-copilot.github.com/learning-hub/using-copilot-coding-agent/)
* Article: Open-source Coding Agents in your GitHub, Fixing your Issues (OpenHands) [link](https://www.openhands.dev/blog/open-source-coding-agents-in-your-github-fixing-your-issues)
* Article: Long-running Agents (Addy Osmani) [link](https://addyosmani.com/blog/long-running-agents/)
* Repository: wiggumdev/ralph: Ralph Wiggum agentic loop TUI (GitHub) [link](https://github.com/wiggumdev/ralph)

What if 60% of the software features your team built this year didn't actually solve a customer problem, and your new AI coding agent just built them twice as fast?

Speeding up the delivery of the wrong solution is the single fastest way to accumulate technical debt and waste engineering capital. To build software that truly matters in the age of AI, teams must combine continuous product discovery with structured, spec-driven execution.

In this lesson, you will learn how to: 

- **Identify and eliminate** solution-first anti-patterns across product management and software engineering workflows.
- **Formulate** bounded solution concepts using high-abstraction shaping techniques like breadboarding and fat-marker sketches.
- **Structure** clear technical specification using EARS (Easy Approach to Requirements Syntax) notation and multi-file spec workflows.
- **Architect** durable runtime harness for long-running AI agents using decoupled state layers and repository-native task graphs.

# The Solution-First Trap and the Product Trio

The most pervasive failure in modern software development is **product myopia**: falling in love with a feature or UI mockup before validating the underlying customer pain. A solution-first team asks, *"What should we build?* while a problem-first team asks, *"What customer problem are we solving, why does it matter and how will we know the pain decreased?*

When teams jump straight to solutions, friction becomes silent. In product-led environments, users rarely file tickets when they hit confusing onboarding or broken flows: they simply close the tab. Customer adapt by creating workarounds, such as maintaining side spreadsheets or manually exporting data. These workarounds are not user quirks; they are load product signals indicating unaddressed pain points.

To manage risk effectively, cross-functional teams should organize as a **Product Trio**, combining three essential perspectives:

- **Product Manager**: Accountable for business viability and value creation.
- **Product Designer (UX)**: Accountable for usability and workflow ergonomics.
- **Tech Lead / Architect**: Accountable for technical feasibility and architectural integrity.

Together, the Product Trio continuously evaluates Marty Cagan's **Four Big Risks**:

1. **Value Risk**: Will the customer choose to use or buy this?
2. **Usability Risk**: Can the user figure out how to navigate it?
3. **Feasibility Risk**: Can our engineering team build it within our constraints?
4. **Business Viability Risk**: Does this solution work for our legal, financial, and operation constraints?
Failing to involve engineers in product discovery leads to classical Product Owner anti-patterns, such as acting as "feature commandant" who pastes unshaped stakeholder demands directly into Jira. Empowered, **product-minded engineers** actively engage with the "why," evaluate technical and product trade-offs upfront, and help shape low-effort alternatives that deliver equivalent customer impact.

# Shaping the Work Before Building

Before committing engineering cycles or assigning tasks to AI agents, work must be **shaped**. Shaping makes an abstract project idea concrete while leaving enough space for designers and developers to exercise creativity during implementation.

Key principles from the *Shape Up* methodology include:

- **Setting an Appetite, Not an Estimate**: Instead of asking developers how long a raw idea will take, leadership defines an **appetite**, the maximum time budget the team is willing to spend (e.g., a 2-week small batch or a 6-week big batch). Scope is then hammered to fit the fixed time window.
- **Breadboarding**: A prototyping technique borrowed from electrical engineering that maps user flows at a high level of abstraction using three basic elements:
	- **Places**: Navigable spaces (e.g., screens, modals and pages).
	- **Affordances**: Actions the user can take (e.g., buttons, fields, copy).
	- **Connection Lines**: Wire pathways showing how affordances move the user from place to place.
- **Fat-Marker Sketches**: Visual layouts drawn with deliberately thick strokes (or wide digital brushes) so that adding fine details is impossible. This prevents teams from getting bogged down in pixel alignment or UI styling too early.
- **De-risking Rabbit Holes**: Identifying hidden technical complexities, third-party API limits, or edge cases during shaping, and explicitly declaring non-essential elements as **No-Gos** out of bounds.

By outputting bounded elements rather than rigid wireframes, shaping establishes clear boundaries for the project without creating a rigid assembly line.

# Spec-Driven Development: Machine-Readable Requirements

Once work is shaped, how do we hand it off to human developers or AI coding agents without losing context or intent? **Spec-Driven Development (SDD)** replaces informal chat prompts and loose tickets with formal, structured Markdown contracts committed directly to the codebase.

Instead of issuing one-off instructions to AI agents, SDD framework into explicit phases: **Specify -> Plan -> Tasks -> Implement -> Converge**.

A complete feature spec typically lives inside `.kiro/specs/` or `.github/` and consists of three core artifacts:
- `requirements.md`: Defines **what** the feature must do from a user and business perspective.
- `design.md` or `plan.md`: Outlines **how** the system will be built, specifying architecture, schema modifications, and API contracts.
- `tasks.md`: Breaks down implementation into discrete, trackable steps that can be executed in parallel waves.

To ensure requirements are unambiguous and programmatically testable, SDD utilizes **EARS (Easy Approach to Requirements Syntax)** notation:

- **Normal Behavior (WHEN)**: *When the user submits an invoice with valid data, THE SYSTEM SHALL calculate tax and store the record.*
- **Error State (IF / THEN)**: *IF the payment gateway is unreachable, THEN THE SYSTEM SHALL queue the transaction and retry up to 3 times.*
- **State Constraints (WHILE)**: *WHILE a data export is in progress. THE SYSTEM SHALL disable the submit button and display a loading indicator.*

Tools such as **Kiro**, **Github Spec Kit**, **Taskmaster AI (`tm parse-prd`, `tm analyze-complexity`)**, and **backlog.md** read these structured specs, run automated clarity analysis, and execute implementation tasks while verifying outcomes against initial requirements.

# Architecting Long-Running AI Coding Agents

When delegating multi-hour or multi-day tasks to autonomous AI coding agents (such as Claude Code, OpenHands, or Kiro), standard chat interfaces hit three fundamental walls:

1. **Context Rot**: Model reasoning degrades steady as token context window fill up.
2. **Stateless Sessions**: New session shifts start completely blank without built-in disk persistence.
3. **Generous Self-Grading**: Model reliably grade their own work as "complete" even when tests fail or requirements are missing.

To overcome these walls, modern agent harnesses decouple system responsibilities into three distinct layers:

- **The Brain**: The LLM reasoner responsible for planning and generating code.
- **The Hands**: Ephemeral, isolated execution environments (such as Docker containers or Git worktrees) where code runs and build occur.
- **The Session**: An append-only external event log of all thoughts, tool calls, diffs, and test results stored outside the context window.

To keep autonomous agents focused over extended runs, team employ the **Ralph Loop** pattern:

- **External Task Graph**: A repository-native database (such as Steve Yegge's **Beads** `bd`, built on Dolt) maintains task states and explicitly blocking dependences. The agent queries `bd ready` to discover actional work.
- **State-Locking & Leases**: Agents claim tasks via compare-and-swap operations with heartbeat leases, preventing multiple agents from working on the same issue.
- **Persistent Memory**: Lessons learned during a shift are logged via `bd remember` or `AGENTS.md` and injected into the agent's context briefing (`bd prime`) as session start.
- **Evaluator Separation**: A dedicated **Judge** or automated test harness validates acceptance criteria. If test fail, the harness rejects completion and pushes the agent back into the loop.

# Key Takeaways

- **Adopt a Problem-First Mindset**: Prioritize root customer problems over shiny feature ideas. Rely on the Product Trio (PM, UX, Tech Lead) to continuously mitigate Value, Usability, Feasibility and Viability risks.
- **Shape Before You Build**: Define an appetite (fixed time, variable scope) and sketch user flows at high level of abstraction using breadboarding and fat-marker sketches.
- **Structure Specifications via SDD**: Use machine-readable specs (`requirements.md`, `plan.md`, `tasks.md`) formulated with EARS notation (`WHEN`, `IF/THEN`, `WHILE`) to establish testable contracts for human and AI builders.
- **Orchestrate Long-Running Agents**: Decouple model reasoning from sandboxed execution and append-only session storage. Use external tasks graphs (`bd ready`) and separate evaluator loops to keep AI agents aligned across session resets.

## See

- See [[Problem-First Thinking]]
- See [[Product Trio]]
- See [[Four Big Product Risks]]
- See [[Product-Minded Engineer]]
- See [[Shaping (Shape Up)]]
- See [[Product Discovery Glossary]]
- See [[Spec-Driven Development]]
- See [[EARS Notation]]
- See [[Long-Running Agent Harness]]
- See [[Ralph Loop]]
- See [[Task Graph Backlog]]
- See [[Agent Memory]]
- See [[Smart Zone and Dumb Zone]]
- See [[AFK Agent Execution]]
- See [[Agentic SDLC]]
- See [[Grilling Session]]

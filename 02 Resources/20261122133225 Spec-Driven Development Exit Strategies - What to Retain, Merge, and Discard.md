---
type: article-note
status: reviewed
created: 2026-11-22
tags: [spec-driven-development, documentation, adr, sdlc]
---

Sources:

* Article: Spec-Driven Development Needs an Exit Strategy (The Main Thread) [link](https://www.the-main-thread.com/p/spec-driven-development-exit-strategy)
* Article: Spec-Driven Development: What Should Survive After Shipping? (DEV Community) [link](https://dev.to/myfear/spec-driven-development-what-should-survive-after-shipping-32fc)
* Docs: How to persist specifications after delivery (Spec Kit Documentation) [link](https://github.github.com/spec-kit/how-to/persisting-specs.html)
* Guide: The Spec-Driven Development (SDD) Playbook (Liatrio Labs) [link](https://liatrio-labs.github.io/spec-driven-workflow/)
* Discussion: How are you maintaining spec document as it evolves? (r/SpecDrivenDevelopment) [link](https://www.reddit.com/r/SpecDrivenDevelopment/comments/1sfda8o/how_are_you_maintaining_spec_document_as_it/)
* Article: Architecture Decision Record (Martin Fowler) [link](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html)
* Article: Context Anchoring (Martin Fowler) [link](https://martinfowler.com/articles/reduce-friction-ai/context-anchoring.html)
* Article: Scaling the Practice of Architecture, Conversationally (Martin Fowler) [link](https://martinfowler.com/articles/scaling-architecture-conversationally.html)
* Article: A Debt-Aware Approach to Architectural Decision Records [link](https://hartiga.de/it-architecture/architectural-decision-records/)
* Article: Architecture Decision Records: Templates and Operational Patterns for Teams That Actually Maintain Them (Hidekazu Konishi) [link](https://hidekazu-konishi.com/entry/architecture_decision_records_templates_and_operations.html)
* Article: ADRs as a Team Habit: The Fastest Path to Better Engineering Decisions (DEV Community) [link](https://dev.to/maximeshr/adrs-as-a-team-habit-the-fastest-path-to-better-engineering-decisions-2b2m)
* Article: Architecture decision records: capture the why behind security choices (Safeguard.sh) [link](https://safeguard.sh/resources/blog/architecture-decision-records-for-security-choices)
* Article: ADR vs RFC: When to Use Each (and How to Find Them Later) (Moai) [link](https://askmoai.com/blogs/adr-vs-rfc)
* Article: How to Make Architecture Decisions: RFCs, ADRs, and Getting Everyone Aligned (ITNEXT) [link](https://itnext.io/how-to-make-architecture-decisions-rfcs-adrs-and-getting-everyone-aligned-ab82e5384d2f)
* Article: How to Write Specs, RFCs and ADRs (JustSteveKing) [link](https://www.juststeveking.com/articles/how-to-write-specs-rfcs-and-adrs/)
* Article: PRD vs ADR vs RFC: The Documents Every Engineer Should Know [link](https://aridanemartin.dev/blog/prd-adr-rfc-decision-documents/)
* Report: Enterprise architecture playbook (Thoughtworks) [link](https://www.thoughtworks.com/content/dam/thoughtworks/documents/report/thoughtworks-enterprise-architecture-playbook.pdf)
* Guide: Guide to the Standard for Retention of Project Documentation (Engineers and Geoscientists BC) [link](https://www.egbc.ca/getmedia/114e91a9-402e-4ab6-af2e-b7b84b3a2fcb/EGBC-QMG-Retention-of-Docs.pdf)
* Paper: Software Release Documentation for Production Deployment (Cross-Disciplinary Knowledge Systems) [link](https://cross-disciplinaryknowledgesystems.com/index.php/cdks/article/download/37/38/74)
* Guide: Systems Engineering for ITS - Retirement/Replacement (FHWA Operations) [link](https://ops.fhwa.dot.gov/seits/sections/section3/3_3_13.html)

# Spec-Driven Development Exit Strategies - What to Retain, Merge, and Discard

Imagine opening a software repository six months after your engineering team enthusiastically adopted Spec-Driven Development (SDD), only to discover a chaotic shadow codebase: hundreds of decaying Markdown files, outdated task lists, and contradictory design notes describing features that were refactored months ago. When AI coding assistants and human developers generate natural-language documentation at lightning speed, how do you prevent your specifications from becoming a bloated, unmaintainable second codebase?

To master Spec-Driven Development, writing the initial prompt or feature brief is only half the battle, you also need a clear **exit strategy**. In this lesson, we will explore best practices for deciding what artifacts to retain, merge into technical homes, or safely discard once your code ships to production.

After completing this lesson, you will be able to:

- **Distinguish** between short lived delivery scaffolding and permanent architectural artifacts.
- **Map** durable system facts to their authoritative native homes, such as code, tests, schemas, and Architectural Decision Records (ADRs).
- **Evaluate** the four post-delivery spec persistence models (Flow-Back, Flow-Forward, Living-Spec, and Constitution-Only).
- **Execute** a disciplined post-ship exit strategy protocol to clean active context while preserving essential raionale.

# The Spec-Driven Dilemma: Delivery Scaffolding vs. Permanent Memory

When teams start using AI agents and spec-driven workflows, a common anti-pattern quickly emerges: treating every temporary Markdown file generated during feature development as permanent system documentation. Before long, simple pull requests generate research notes, task lists, verification logs, and low-level designs. If every stage is kept indefinitely, the the team enters what software architects call **Decision Documentation Theater**, a state where the repository accumulates massive amounts of natural-language prose that drifts out of sync with actual code execution.

To solve this, we must understand the core principle articulated by mode engineering leaders: **code becomes the fact, while specs are for the delta**. A feature specification (or change brief) earns its keep by defining the gap between what exists today and what should exist next. Its primary job is to lock down scope, highlight trade-offs, and establish acceptance criteria *while work is in flight*.

Too keep our documentation lean and trustworthy, we must separate documents by the specific questions they answer:

- **PRD (Product Requirements Document)**: Answers *what* we are building and *why* from a product perspective. It defines user problems, goals, non-goals, and success metrics. It remains frozen once committed.
- **RFC (Request for Comments)**: Answer *how* we should solve a complex or cross-cutting problem. It explores multiple proposals, trade-offs, and rejected options before a decision is finalized.
- **Spec / Change Brief**: Answers *what exactl this single piece of work does* and how we verify completion. It acts as temporary process scaffolding during the implementation loop.
- **ADR (Architecture Decision Record)**: Answers *what single architectural choice was decided, and what did it costs?* It is an immutable, numbered record stored in the repository that lasts forever (until superseded by a new ADR).

Once code is merged and verified in production, the temporary implementation scaffolding, such as granular task lists (`tasks.md`), prompt files, and proof logs has fulfilled its purpose. Holding onto long, details planning files permanently in active developer context only creates friction and consumes valuable AI context window space.

# Promoting Durable Facts to Their Native Homes

If most of a feature specification should expire after shipping, what happens to the critical rules, constraints, and business logic established during development? The secret to a clean exit strategy is **promoting durable facts to their native, executable artifacts** rather than keeping them locked in Markdown text.

Software engineering already provides robust, tool-supported homes for system truths. Executable artifacts like database constraints, OpenAPI definitions and unit tests participate actively in continuous integration (CI) pipelines. A broken schema validation check or a failing unit test immediately halts deployment: a stale paragraph in a forgotten `docs/specs/` folder does not.

When a feature ships, review your change brief and migrate surviving obligations into their natural homes:

- **API Shapes & Contracts**: Migrate to **OpenAPI / AsyncAPI schemas** and contract tests.
- **Data Invariants**: Encode directly into **database migration scripts**, column constraints, and domain validation logic.
- **Security & Authorization Rules**: Define in **access control policies**, static analysis rules, and automated allow/deny integration tests.
- **Architectural Boundaries**: Enforce through **module boundaries**, dependency linting, and architecture tests.
- **Reliability Expectations**: Configure as **Service Level Objectives (SLOs)**, telemetry metrics, alerting rules.
- **Architectural Rationale & Trade-offs**: Capture in a short, dedicated **Architecture Decision Record (ADR)**.

By transferring system rules into automated checks and code, you ensure that the running application acts as the ultimate source of truth, while non-executable architectural raionale is preserved in clean, immutable ADRs.

# Four Models of Post-Delivery Spec Persistence

While temporary process scaffolding (like task checklists and verification proofs) should always be cleaned up, team must decide how to handle the core feature specification file (`spec.md`). Frameworks like Spec Kit outline **four distinct persistence models**, allowing teams to choose an explicitly strategy that matches their team size, compliance needs, and risk profile.

1. **Flow-Back Spec (Editable & Reconciled)**: Accepted discoveries made during coding flow back into the original `spec.md`, `plan.md`, and `tasks.md`. The team reconciles all artifacts so they remain accurate reflections of the delivered system.
	- *Best fit:* Small, highly collaborative teams iterating quickly. 
	- *Watch out for:* Silent divergence if implementation details are updated without updating the primary spec.
2. **Flow-Forward Spec (Immutable Audit Trail)**: Completed feature directories are treated as frozen historical records. When requirements change later, the team never edits the old spec in place: instead, they create a new feature directory (`0002-update-user-billing/`) that cross-links to the original.
	- *Best fit:* Regulated industries, financial systems, or teams requiring strict audit trails.
	- *Watch out for:* Context fragmentation across dozen of directories.
3. **Living Spec (Spec as Contract)**: The `spec.md` is retained as the permanent human-edited contract for a module or subsystem. If behavior changes, developers update `spec.md` first, then regenerate or rewrite implementation code, plans, and tests.
	- *Best fit:* Core platform APIs and highly stable domain boundaries.
	- *Watch out for:* Losing lower-level implementation notes when derived artifacts are regenerated.
4. **Constitution-Only (Spec-First & Retired)**: Feature specs are used strictly for delivery scaffolding and retired from active repository version control upon shipping. Enduring system rules are promoted to native artifacts (code, tests, schemas) and project-wide principles live in an overarching `constitution.md`.
	- *Best fit:* Fast-moving product engineering teams wanting minimal repo clutter.
	- *Watch out for:* Losing high-level intent if business rationale is deleted without creating an ADR.

# The Life Cycle Pipeline: From Ideation to Retirement

To bring all these concepts together into a seamless team habit, engineering teams should institute a standardized **post-shipping exit protocol**. Instead of leaving artifact retention to individual developer preference, follow this four-step pipeline whenever a feature branch is ready to merge:

## Step 1: Verify Code against Acceptance Evidence

Before archiving anything, run the acceptance checks defined in your change brief. Ensure that automated tests exercise the exact boundaries and contracts specified during the planning phase.

## Step 2: Extract & Write ADRs for Load-Bearing Decisions

Ask: *Did this feature introduces an expensive trade-off, a new library, or departure from estrablished patterns?* If yes, write a short, focused ADR using the Nygard or MADR format (e.g., `ADR-0014: Store Session State in Postgres). Store it in `docs/adr/`. If no major architectural trade-offs were made, skip this step.

## Step 3: Promote System Invariants to Native Artifacts

Confirm that all API shapes, database constraints, and validation logic live in executable schemas and test suites rather than unmaintained Markdown text.
# Step 4: Execute the Retention Policy (Archive or Retire)

Depending on your team's chosen persistence model:

- **Constitution-Only**: Delete or externalize temporary feature folders (`docs/specs/01-feature/`), ensuring active AI context remains clean.
- **Flow-Forward**: Update status front-matter to `Accepted`, lock the files, and update the master index (`docs/specs/index.md`).
- **Flow-Backed / Living Spec**: Reconcile `spec.md` with final production behavior and clear out temporary task/proof files.

By embedding this exit protocol into your pull request checklist, you keep your repository focused, maintain AI token efficiency, and preserve architectural context for years to come.

# Key Takeaways

- **Specs are for the Delta**: Code and production runtime represent the ultimate behavior of your system; change briefs exists to guide and verify the immediate delta being built.
- **Promote Facts to Native Homes**: Do not maintain natural-language prose for facts that can be enforced by database constraints, OpenAPI schemas, access policies, or automated tests.
- **ADRs Preserve Nationale** Use immutable Architecture Decision Records (`docs/adr/`) exclusively for significant, hard-to-reverse trade-offs and structural choices.
- **Choose an Explicit Persistence Model**: Adopt a clear team convention, Flow-Back, Flow-Forward, Living Spec, or Constitution-Only to govern how `spec.md` files are handled post-release.
- **Automate the Exit Protocol**: Make artifact promotion, ADR extraction, and temporary context cleanup a mandatory checkpoint in your team's pull request process.

## See

- See [[Spec Exit Strategy]]
- See [[Spec Persistence Models]]
- See [[Durable Facts in Native Homes]]
- See [[Architecture Decision Record (ADR)]]
- See [[Design Document Types]]
- See [[SDLC Documentation Glossary]]
- See [[Spec-Driven Development]]
- See [[Inverse Pyramid of Constraints]]

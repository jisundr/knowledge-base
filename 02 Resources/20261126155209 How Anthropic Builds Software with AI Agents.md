---
type: video-note
status: reviewed
created: 2026-11-26
source: https://www.youtube.com/watch?v=9oNvKMd7xJo
tags: [ai-engineering, ai-agents, code-review, verification, incident-management, hiring, career, sdlc]
---

Sources:

* Video: How Anthropic builds software in 2026 with Katelyn Lesse - The Pragmatic Engineer [link](https://www.youtube.com/watch?v=9oNvKMd7xJo)


What happens when a small team of engineers rewrote an entire enterprise API layer—serving every single token coming from Claude—from Python to Rust in just five months, without deeply reading 80% of the agent-written code? Welcome to the frontier of AI-native software engineering inside Anthropic.

In this lesson, you will explore how software development paradigms shift when code generation costs approach zero, and AI agents handle heavy lifting. By the end of this lesson, you will be able to:

- **Analyze** why Anthropic migrated its core platform API from Python to Rust to overcome critical CPU performance bottlenecks.
- **Explain** the concept of "verifiable outputs" and how automated shadow traffic testing replaces traditional manual line-by-line code reviews.
- **Examine** how AI agents alter daily operations, from automated on-call triage to product managers deploying production features.
- **Evaluate** the shift in engineering identity, the phasing out of algorithmic coding interviews, and updated metrics for engineering seniority.

# Rebuilding the Core API: From Python Monolith to Rust

To understand how modern software is built inside Anthropic, we must first look at their foundational layer: the **Messages API**. Every token served by Claude runs through this central pipeline—handling authentication, authorization, tokenization, billing, sandboxing, and safety safeguards before reaching underlying hardware chips (GPUs and TPUs).

## The Historical Context: Python as a Research Bridge

Anthropic originally operated purely as an AI research lab. Research scientists predominantly used Python for framework compatibility (e.g., PyTorch, TensorFlow). When a small team set out to build the initial public API three years ago, choosing Python was pragmatic. It allowed research, infrastructure, and early product teams to collaborate seamlessly within a single Python monolith running in a single cloud region.

## The Crisis: The CPU Bottleneck

As public adoption exploded—spiked by events like running a Super Bowl commercial—request volumes surged dramatically. The platform team encountered a classic scaling dilemma compounded by modern cloud constraints:

- **Stateful Streaming Chats:** Unlike traditional short-lived HTTP REST requests, Claude API streams responses, holding client connections open for extended durations while maintaining conversation state across turns.
- **Single-Threaded Limitations:** Python’s single-threaded nature consumed disproportionate CPU capacity.
- **Horizontal Scaling Limits:** In traditional web engineering, CPU is treated as an infinitely autoscaling resource. Anthropic reached a point where cloud providers physically could not supply enough CPU instances in targeted regions to keep up with single-threaded Python processing.

## Language Selection: Why Rust?

While Go was adopted for smaller microservices to balance developer experience with efficiency, the team needed maximum performance for the core API path. Rust offered C++ level performance and bare-metal efficiency while maintaining compile-time memory safety.

Crucially, the team lacked deep prior Rust experience. In traditional software engineering, switching an entire team to Rust would require months of developer retraining on concepts like the **borrow checker**. However, because Claude could generate valid Rust code and explain syntax on demand, the team could adopt Rust without upfront language mastery.

## The "Great Leap" Shadowing Strategy

Instead of slowly refactoring individual microservices, a senior engineer proposed standing up a parallel Rust codebase as a complete fork of the API layer within a single codebase:

1. **Thin Front Door:** A lightweight Python router received inbound API requests.
2. **Shadow Execution:** The router sent the live request to the Python system while asynchronously executing a shadow request through the new Rust system.
3. **Privacy-Preserving Verification:** Anthropic’s strict data privacy policies prevent engineers from inspecting customer prompt or completion payloads. To verify system equivalence without viewing raw data, the team verified matching states up to the inference boundary and verified identical output **token counts** returning from inference.
4. **Iterative Convergence:** Day by day, engineers prompted Claude to analyze telemetry differences and drive discrepancy rates between Python and Rust down to zero.
5. **Fallback Safety:** The live Python system served as a fallback mechanism if Rust threw an unexpected error, allowing a smooth cutover in just 5 to 6 months.

# Verification over Code Reviews: Rethinking Quality Assurance

The transition to AI-generated code forces a fundamental rethink of quality assurance. When coding agents generate thousands of lines of code in seconds, human code review becomes the ultimate system bottleneck.

## Verifiable Workflows vs. Manual Review

Anthropic operates on a central principle: **If you can make an output verifiable, you do not need to read every line of code.** Engineers on the platform team estimated that for **80% of pull requests (PRs)** opened by agents, they did not deeply inspect the underlying lines of code.

- **The 80% Unread Rule:** For standard features, refactors, or mechanical changes, engineers rely on automated verification gates—such as shadow testing, integration test suites, static analysis, and deterministic sandboxes.
- **The 20% Deep Dive:** Engineers reserve line-by-line inspection for subtle logic edge cases, complex security boundaries, or when shadow metrics indicate unexpected behavior.

## Classifier-Driven Pull Request Management

Rather than applying a uniform peer-review requirement to every code submission, Anthropic uses automated AI classifiers to evaluate PR risk and assign review routing:

- **Mechanical Changes:** Low-risk updates (e.g., SDK version bumps, schema synchronizations) are evaluated by an automated LLM reviewer. If static gates pass, the PR merges directly into main without human intervention.
- **High-Risk Changes:** Core architectural modifications or security-sensitive updates trigger mandatory human review requirements.

## Preventing Architectural Divergence

During the migration, external feature teams continued developing new capabilities on the legacy Python monolith. To prevent the Rust shadow layer from falling behind, the platform acceleration team introduced automated static analysis rules. Any new feature added to the Python system automatically blocked CI pipelines unless a corresponding Rust implementation was included, enforcing dual-stack parity until the Python layer was decommissioned.

# Operationalizing AI: Ephemeral Sandboxes, Ambient On-Call, and PM Deployments

Beyond code generation, AI agents alter operational infrastructure, incident management, and functional team boundaries.

## Cloud-Managed Agent Architecture

Deploying long-running agents in cloud environments presents severe engineering hurdles: sandbox crashes destroy agent state, boot times introduce latency, secret storage inside environments creates security risks, and background processes strain CPU limits.

To power products like Claude Code, Anthropic re-architected their agent platform from first principles:

- **Durable State Servers:** The agent harness runs on a persistent, resilient server storing session state.
- **Ephemeral Sandboxes:** Sandboxes are spawned strictly on demand to execute tools or untrusted code, then immediately torn down.
- **Egress Proxying:** Sensitive API keys and credentials are stored securely in centralized vaults outside the sandbox. When an agent calls an external tool, an egress proxy injects credentials _just-in-time_ as traffic leaves the sandbox environment, preventing credential leakages.
- **Resource Efficiency:** This decoupled architecture reduced average CPU utilization by two-thirds compared to running whole agents inside dedicated cloud virtual machines.

## Automated Incident Management: Shadow On-Call

On-call rotations for high-throughput APIs are notoriously stressful. Anthropic implemented an ambient **Shadow On-Call Agent** to sit in front of human engineers during incident pages:

1. **Noise Filtering:** When an alert triggers, the AI agent evaluates telemetric context to determine if the page is a false positive. If classified as noise, the page is suppressed, protecting engineers from fatigue.
2. **Root Cause Analysis:** If genuine, the agent immediately analyzes system logs, traces recent deployments, identifies the root cause, and opens a proposed fix PR before the paged engineer opens their laptop.

## Cross-Functional Boundary Blurring

With agents handling syntax and implementation details, non-engineering roles can push production software directly. For example, a Product Manager at Anthropic built and deployed a complete diagnostic dashboard for prompt caching hit rates inside the Developer Console. Using Claude in Slack to generate front-end and back-end logic, the PM brought the feature from concept to production independently, while traditional software engineers provided high-level architectural oversight.

# Redefining Hiring, Seniority, and the Identity of Software Engineering

The rise of agentic software development fundamentally changes what companies look for when hiring and evaluating software engineers.

## Phasing Out the LeetCode Coding Interview

Anthropic became one of the first major technology companies to phase out traditional algorithmic coding interviews (Data Structures and Algorithms / DSA) across product and platform teams.

In historical hiring loops, candidates were eliminated if they struggled with syntax or manual memory allocation under pressure. However, internal data showed candidates who failed manual coding evaluations frequently excelled in system design, trade-off analysis, and project execution. Because engineers no longer spend their days manually typing syntax, algorithmic whiteboarding yields minimal predictive signal for job performance.

In its place, Anthropic tests **agent-driven evaluations**, assessing how effectively candidates evaluate agent-written architecture designs, debug agent-generated PRs, and direct agents to complete complex projects.

## The Shift in Seniority and Metrics

Team structures remain concentrated in standard **"two-pizza teams"** (5 to 10 engineers) to preserve system context and maintain clear on-call ownership. However, team composition skews significantly more senior.

Historically, seniority was tied to effort duration (e.g., "led a 2-year infrastructure migration"). When agents collapse a two-year rewrite into five months, seniority metrics pivot exclusively to:

- **Quantifiable System Impact:** Reduction in CPU footprints, latency improvements, incident prevention, and cost savings.
- **Cross-Team Alignment:** Managing technical dependencies across research, inference, and product organizations.
- **Architectural Boundary Setting:** Designing safe guardrails, security proxies, and verification loops.

## Overcoming the Engineer Identity Crisis

Engineers who defined their professional identity by manual keyboard typing ("click-clacking") face an identity crisis in an AI-first world. However, domain expertise in security, network protocols, operating systems, and distributed systems architecture is more critical than ever.

AI agents cannot autonomously solve ambitious real-world problems—such as drug discovery workflows or financial compliance automation—without robust underlying infrastructure, identity systems, and safety guardrails engineered by humans.

# Key Takeaways

- **Verification Over Code Review:** Automated shadow testing and metric matching allow engineering teams to safely merge up to 80% of agent-opened pull requests without manual line-by-line code reviews.
- **Performance-Driven Rewrites:** Using AI agents as pair programmers eliminates the learning curve of strict languages like Rust, enabling dramatic reductions in CPU bottlenecks and cloud infrastructure costs.
- **Operational Automation:** Ambient agents reduce operational friction by filtering on-call pages, proposing incident hotfixes, and allowing non-engineers to deploy high-quality production features.
- **Modern Hiring Paradigms:** Algorithmic whiteboarding interviews are being replaced by agentic evaluations, shifting engineering value toward system design, domain specialization (e.g., security, infrastructure), and business impact.

# Additional Context from the Source

- **Speaker**: Katelyn Lesse, head of engineering for the Claude Platform at Anthropic; interviewed on The Pragmatic Engineer. Her team owns the API that serves every Claude token and the infrastructure behind Claude Code and Claude Desktop.
- **Code written by the model**: asked for a figure, she estimated about 75% of the work is the model writing the code, with understanding exact syntax mattering less.
- **Other languages**: some newer services are built in Go; Rust was chosen for the core API path.
- **Cloud agents product**: the durable-server and ephemeral-sandbox design is the platform behind Claude Managed Agents, built so people can fire off Claude Code runs in the cloud rather than only on a laptop.
- **Day-to-day work**: engineers are mostly in Slack, working with Claude alongside humans.
- **Unverified in the video**: the "reduced average CPU utilization by two-thirds" figure for the sandbox architecture was not found in the transcript; treat it as unconfirmed.

See [[Shadow Traffic Migration]], [[Risk-Classified PR Routing]], [[Egress Credential Injection]], [[Shadow On-Call Agent]], [[Agent-Driven Technical Interviews]], [[Impact-Based Engineering Seniority]], [[Agent Verification Stack]], [[Blast-Radius Code Review]], [[Bottleneck Shift (Theory of Constraints)]], [[Long-Running Agent Harness]], [[AI-Assisted Incident Investigation]], [[Product Engineer]], [[Accidental vs Essential Complexity]], [[Shipped Value Metrics]]

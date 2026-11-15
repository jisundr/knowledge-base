---
type: video-note
status: reviewed
created: 2026-11-15
tags: [ai-engineering, ai-agents, sdlc, mcp, github-copilot, change-management]
source: https://www.youtube.com/watch?v=-GpxKKgoWWg
---

Source: https://www.youtube.com/watch?v=-GpxKKgoWWg
Notebook: https://notebook.google.com/notebook/c0337480-0337-4f97-b40b-8538a654ca9a

# Levi Strauss Agentic Software Development

See [[Agentic SDLC]].

Jenny Patchin from Levi Strauss & Co shares how they reimagined their entire process around AI capabilities rather than simply slotting AI tools into existing legacy workflows. Using their store stylist app (Backpocket) as the pilot project, they transformed their process across three core pillars: **Process**, **Platform**, and **People/Governance** 

# 1st Pillar: Rewiring the Process & Core Principles

## Background

Before Levi Strauss & Co. introduced AI agents into their flagship retail stylist app, Backpocket, they mapped their development workflow on a board covered in sticky notes representing pain points. The legacy app took 9 months to build and was burdened by 12 manual handoffs across 6 distinct roles. Writing user stories alone took 2 to 4 weeks, while quality engineering (QE) and regression testing added another 3 weeks at the very end of the pipeline.

To break this bottleneck, the team stopped asking, "How do we make human work faster?" and instead asked, "How do we stop the waiting?"

They addressed this by adapting the classic McKenzie framework around one foundational principle: **Agents start on execution, and humans make the decision**.

## Division of Labor

Levi Strauss established a clear division of labor:
- **AI does**: Synthesizes specs using EARS (Easy Approach to Requirements Syntax), drafts code, runs tests, instruments observability, and monitors.
- **Human does**: Adds context, exercises judgment, and manages stakeholders.
- **Human decides**: Prioritizes, approves or rejects pull requests (PRs), and holds ultimate accountability

# The Platform Architecture and 17-Agent Orchestration

See [[AI Agents and Tool Use]] (multi-agent orchestration).

Levi has engineered a modular platform powered by 17 specialized AI agents. They used what developers already use in their daily work, such as VS Code and the GitHub Copilot CLI.

At the core of this system is an **Orchestrator Agent** running on the **GitHub Copilot Cloud** Agent engine, which routes incoming tasks to specialized agents based on plain-text markdown profiles:
- **Requirements Agent**: Converts incoming user tickets into clear, testable feature specifications. Crucially, it asks clarifying questions whenever it detects ambiguous details, preventing costly rework later.
- **Testing Agent**: Automatically writes and executes end-to-end tests using Playwright.
- **Observability Agent**: Instruments telemetry and sets up system monitoring.
- **Security, Accessibility, Code Review, and Performance Agents**: Specialized reviewers auditing code against strict organizational standards.

## Markdown Profiles

Every agent is defined as a simple Markdown file (e.g., `requirements-agent.md`) located inside the repository's `.github/agents/` directory. Because instructions are written in plain text, any engineer can inspect, audit, or submit a Pull Request (PR) to refine an agent's behavior.

## Model Context Protocol (MCP) Integration

Details in [[Model Context Protocol (MCP)]].

To interact with external software ecosystems, agents utilize MCP integrations:
* **Jira & Confluence**: Used by the Requirements Agent as the authoritative record of work.
* **New Relic**: Used by the Observability Agent for telemetry data and real-time alerts.
* **Playwright**: Used by Testing and Performance Agents for headless browser automation.
* **Figma**: Used to pull design context directly into build tasks.
Because tools connect via MCP adapters, swapping out an external system never requires rewriting the agent's core instructions.

## Standards Built-in Starter Kits and CI Quality Gates

Organizational standards for security or accessibility only work if developers remember to apply them. Levi's eliminated this risk by making "the right path the easy path," building standards directly into repository starter kits and automated Continuous Integration (CI) gates.

### Repository Starter Kits

Levi's established 10 standard repository starter kits (covering stacks like TypeScript and Swift). Every new repository generated from these kits includes pre-configured `agents.md` files. Copilot instructions, CI/CD pipelines, runbooks, and telemetry hooks from day one.

### Sequential CI Quality Gates

When code changes are submitted, specialist agents run through a standardized chain of CI quality gates:
1. **Testing**: Validates business logic and regression suites.
2. **Accessibility**: Automated checking for WCAG 2.2 AA compliance in a headless browser via Playwright.
3. **Performance**: Measures real-world execution metrics against **Core Web Vitals** (always measured, never estimated).
4. **Security**: Scans for OWASP Top 10 vulnerabilities, CVEs, and secret leaks. Security always runs last, so it audits the final code incorporating all prior agent fixes.
5. **Observability**: Automatically injects missing instrumentation to ensure full visibility in New Relic.

If a gate fails, **Copilot Agentic Autofix** investigates the break, generates a targeted fix, and attaches it as a labeled commit to the PR for human review. For legacy codebases, an assessment agent analyzes existing repositories against starter kit templates and drafts a PR to automatically upgrade aging repos to baseline standards.

# Culture, Change Management and Measured Results

Building technology is often simple compared to the human challenge of **change management**. As research highlights, high-performing engineers often struggle most with AI transformations because adopting agentic workflows requires unlearning hard-earned habits that previously drove their success.

To build organizational trust and guide developers through this transition, Levi's established clear operational guardrails and support mechanisms:

## Four Core Operating Rules

1. **Human as judgment, agents on execution**: Remind teams that routine work belongs to agents, while taste, judgment, and critical decision-making belong to people.
2. **Context lives where agents can see it**: Repositories and Jira tickets are durable context; ephemeral chat messages are not.
3. **The same bar for agents and humans**: Every line of code, whether written by a person or an agent, must pass identical CI quality gates.
4. **Auditable always**: Every agent action and human override is logged for full transparency.

## Enablement Strategy

Levi's supported their engineering teams by sending pre-workshop research on agentic SDLCs, embedding a Principal AI Engineer as a player-coach directly inside team standups, running hands-on training using production code bases, hosting regular Developer Velocity Office Hours, and launching an Internal AI Marketplace featuring 24 rated agents, 19 skills, and 15 MCP servers available with one click.

## Measured Outcomes

By pairing structural process changes with targeted change management. Levi's achieved dramatic improvements across key operational metrics:
 - **72% faster delivery time**: The new backpocket applications launched in **2.5 months**, compared to 9 months for the legacy version.
 - **51% increase in throughput**: Developer output surges immediately, avoiding the expected initial adaptation slowdown.
 - **54% improvement in PR pass rates**: Demonstrating that velocity gains occurred alongside measurable improvements in software quality.
 - **AI PR adoption jump**: AI-assisted PR involvement expanded from 26% to 69% over the two-and-a-half-month rollout.

# Key Takeaways
- **Reimagine the process first**: Do not place a new AI motor inside an old, friction-filled factory workflow.
- **Decouple execution from decision-making**: Assign heavy execution tasks ("AI Does") to specialized agents while reserving strategic evaluation, prioritization, and final approvals ("Human Decides) for human engineers.
- **Standardize through modular tooling**: Define agent behaviors in plain Markdown files located within repositories, and connect them to enterprise systems using Model Context Protocol (MCP)
- **Embed standards into starter kits and CI gates**: Enforce security, accessibility (WCAG 2.2 AA), performance (Core Web Vitals), and observability automatically using sequential agent CI gates and agentic autofix.
* **Invest heavily in change management**: Guide developer adoption through embedded player-coaches, internal tool marketplaces, clear operating rules, and practical training on real-world codebases.

# Multi-million Dollar Questions
- How can I adopt this in my current company? 
- How can I sell myself as an Applied AI engineer in my organization?
- How can I measure if this is working or not?

# Notes
- Research the McKenzie framework
- Research EARS (Easy Approach to Requirements Syntax)
- Research an applied AI engineer
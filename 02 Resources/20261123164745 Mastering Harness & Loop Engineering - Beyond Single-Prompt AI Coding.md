---
type: article-note
status: reviewed
created: 2026-11-23
source: https://martinfowler.com/articles/harness-engineering.html
tags: [ai-agents, harness-engineering, loop-engineering, context-engineering, verification, evaluation]
---

Sources:

* Article: Anthropic Engineer: Build Loops That Prompt AI, Not Single Prompts (explainx.ai) [link](https://explainx.ai/blog/anthropic-engineer-loops-prompts-ai-coding-harness-engineering-2026)
* Article: Harness engineering for coding agent users (Birgitta Böckeler, martinfowler.com) [link](https://martinfowler.com/articles/harness-engineering.html)
* Article: Loop, Harness, Context Engineering: The Terms Explained (codecentric) [link](https://www.codecentric.de/en/knowledge-hub/blog/loop-harness-context-engineering-explained)
* Article: The Anatomy of Harness Engineering: How to Evaluate, Iterate, and Guard AI Coding Agents (Google Developers Blog) [link](https://developers.googleblog.com/the-anatomy-of-harness-engineering-how-to-evaluate-iterate-and-guard-ai-coding-agents/)
* Article: What is an AI Agent Harness? (Databricks) [link](https://www.databricks.com/blog/ai-harness)
* Article: What is Loop engineering? (CodeRabbit) [link](https://www.coderabbit.ai/blog/loop-engineering)
* Article: What Is Loop Engineering? (IBM) [link](https://www.ibm.com/think/topics/loop-engineering)
* Article: Anthropic says 80% of its new production code is now authored by Claude (VentureBeat) [link](https://venturebeat.com/technology/anthropic-says-80-of-its-new-production-code-is-now-authored-by-claude-how-your-enterprise-can-keep-up)
* Article: Anthropic's Boris Cherny doesn't write code by hand anymore (Fortune) [link](https://fortune.com/2026/06/11/anthropic-claude-boris-cherny-doesnt-write-code-by-hand-anymore/)

What if everything you've learned about writing the perfect prompt for AI coding is already obsolete? In mid-2026, Boris Cherny, Head of Claude Code at Anthropic, dropped a bombshell on the software world: _"I don't prompt Claude anymore. I write loops that prompt Claude."_ By shifting from single, manual prompts to autonomous recursive loops wrapped in robust harness guardrails, Anthropic engineers unlocked an **8x increase in merged lines of code per contributor** (Anthropic's own caveat: likely an overstatement), with AI authoring over **80% of merged production code**. The secret isn't a smarter LLM—it's building the system surrounding the model. Welcome to the era of Harness and Loop Engineering.

In this lesson, you will learn how to:

- **Differentiate** the three foundational layers of autonomous AI systems: Context Engineering, Harness Engineering, and Loop Engineering.
- **Design** a harness using feedforward guides and feedback sensors across computational and inferential controls.
- **Architect** iterative observe-plan-act-reflect loops across three distinct organizational maturity levels.
- **Implement** behavioral evaluations and human-in-the-loop checkpoints to combat comprehension debt and runaway compute costs.

# The Three-Layer Stack: Context, Harness, and Loop

To understand how modern AI development works, we must first clean up the terminology tangle. When developers say "I use AI for coding," they are often mixing up three distinct architectural layers. As software experts from Thoughtworks and codecentric point out, autonomous software engineering relies on a simple core equation: **Agent = Model + Harness**.

Think of a Large Language Model (LLM) as a brilliant engine sitting on a workbench. By itself, it can reason and talk, but it has no hands, no feedback tools, and no workplace boundaries. The surrounding architecture is what turns that engine into a functioning race car. The stack is divided into three clear layers from bottom to top:

- **Layer 1: Context Engineering (The Input Foundation)**: This is the bottom layer. It focuses on curating exactly what information enters the model's context window for a given turn—selecting relevant files, pruning background noise, formatting constraints, and injecting system instructions. If your context wobbles, everything above it fails.
- **Layer 2: Harness Engineering (The Guardrails & Tools)**: The harness is the software infrastructure surrounding the model. It equips the model with hands (tools, sandboxes, MCP servers) and safety mechanisms (linters, test runners, architectural rules). The harness governs _how_ the agent operates within your project.
- **Layer 3: Loop Engineering (The Autonomous Engine)**: Built on top of a solid harness, loop engineering is the orchestration system that repeatedly triggers the agent, spawns helper sub-agents, evaluates output, and manages long-term memory without human turn-by-turn prompting.

Skipping layers is dangerous. A loop running around a poorly constructed harness doesn't solve errors—it just multiplies mistakes at high speed

# Inside the Harness: Guides, Sensors, and the 14% Context Tax

How do you build a harness that gives you real confidence in AI-generated code? Thoughtworks engineer Birgitta Böckeler frames harness design through cybernetic controls: combining **feedforward guides** and **feedback sensors**.

Imagine training a driver. Guides are the driving manual and road signs given _before_ taking the wheel; sensors are the rumble strips and speedometers providing feedback _while_ driving.

- **Feedforward Guides (Steering Control)**: These steer the agent's behavior _before_ it generates code. Examples include your architecture maps, `CLAUDE.md` context files, Zod schemas, and predefined module templates.
- **Feedback Sensors (Self-Correction Control)**: These observe output _after_ the agent acts and produce diagnostic signals for self-correction. High-value sensors include automated test runners, linters, and pre-commit hooks.

Controls are further categorized by how they execute:

- **Computational Controls**: Deterministic, ultra-fast CPU-bound checks like type-checkers, unit tests, and static linters (`ArchUnit`). They cost almost nothing and run in milliseconds.
- **Inferential Controls**: Probabilistic GPU/LLM-bound checks like automated AI code reviews ("LLM as a judge"). They handle semantic reasoning (e.g., checking if code matches product requirements) but cost more and run slower.

**Fixing the 14% Context Tax**: Anthropic's Boris Cherny noted that up to **14% of developer productivity is burned** when LLMs waste turns asking basic questions due to vague context files. Replacing a lazy `CLAUDE.md` file with a structured project context (outlining exact file architectures, styling rules, test commands, and business domain goals) slashes wasted agent cycles by up to 60%!

# The Engine of Autonomy: Building the Steering Loop

Once your harness has tools and sensors, you can step away from manual prompting by wrapping it in an autonomous **Observe-Plan-Act-Reflect** loop.

Instead of asking an agent to "Add user auth" in one giant prompt, a harness loop executes a continuous state machine:

1. **Observe**: Analyzes current codebase state, error logs, and unit test outputs.
2. **Plan**: Deconstructs the task into smaller sub-actions or selects the next tool step.
3. **Act**: Executes code modifications, applies database migrations, or creates test suites.
4. **Reflect**: Evaluates action outcomes against verification gates.
5. **Repeat**: Loops until all criteria pass or a safety threshold is hit.

**Verification Density vs. Generic Autonomy**: Early autonomous agents failed because they relied on self-reporting—asking the model "Did you finish?" Harness engineering anchors loops in **verification density**. The loop never trusts the model's self-assessment; it trusts deterministic exit signals like `exit code 0` from your test suite.

**The Three Maturity Levels of Loop Engineering**:

- **Level 1 (Simple Loop)**: A quick script targeting a single, narrow task (e.g., auto-fixing lint errors over 5 iterations).
- **Level 2 (Task Decomposition)**: A multi-step loop that plans sub-tasks, modifies files, runs integration tests, and reflects on failures.
- **Level 3 (Autonomous Multi-Day Harness)**: Enterprise-grade loops equipped with isolated Git worktrees, persistent memory files ("the spine"), token cost budgets, automated error recovery, and human approval gates for high-risk actions (such as production database migrations).

# Behavioral Evals and Safeguarding Against Cognitive Surrender

As loops run unattended for hours, how do you ensure they stay on course without blowing through your API budget or breaking your architecture? Google Developers staff engineers Taylor Mullen and Christian Gunderman emphasize a crucial shift: moving from end-to-end benchmark scores to **behavioral evaluations**.

End-to-end benchmarks act like final exams—they tell you if an agent passed or failed, but not _why_. Behavioral evals act like unit tests for your harness. They assert on intermediate actions rather than final text strings:

- _When given an ambiguous prompt, does the agent consult ground truth or ask a question rather than guessing?_
- _When modifying build configurations, does it trigger local test validators before completing the task?_

**Human Risks in Autonomous Coding**: Automated loops shift developer friction away from writing code toward reviewing it. Without proper guardrails, engineering teams face significant psychological and architectural risks:

- **Comprehension Debt**: The growing gap between the amount of code in a production repository and the human team's actual mental understanding of it.
- **Intent Debt**: The loss of recorded architectural rationale behind decisions, leaving code that works technically but violates long-term product vision.
- **Cognitive Surrender**: The human tendency to stop critically evaluating agent outputs and passively accept whatever diff the loop produces.

By keeping humans in the loop at strategic approval gates and enforcing hard verification standards, teams harness the speed of AI without sacrificing code quality or team expertise.

# Key Takeaways

- **Agent = Model + Harness**: The underlying LLM supplies reasoning; the outer harness provides tools, memory, sandboxes, and verification rules.
- **Balance Feedforward and Feedback**: Use guides (specs, `CLAUDE.md`, templates) to steer agents before execution, and sensors (tests, linters, review sub-agents) to enable self-correction.
- **Verification Density is Essential**: Never rely on an LLM's self-reported success. Ground loop termination criteria in deterministic signals like passing test suites (`exit code 0`).
- **Protect Against Cognitive Debt**: Maintain human oversight at critical checkpoints to prevent comprehension debt, intent drift, and cognitive surrender.

See [[Harness Engineering]], [[Feedforward Guides and Feedback Sensors]], [[Loop Engineering]], [[Verification Density]], [[Behavioral Evaluations]], [[Cognitive Debt in Agentic Coding]], [[Model and Harness Separation]], [[Context Engineering]], [[Long-Running Agent Harness]], [[Ralph Loop]], [[Self-Verification Loop]], [[AI System Evaluation]], [[LLM-as-a-Judge]]

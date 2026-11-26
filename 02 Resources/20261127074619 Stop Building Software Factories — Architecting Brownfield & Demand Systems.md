---
type: video-note
status: reviewed
created: 2026-11-27
source: https://www.youtube.com/watch?v=1S4hx3wgvBE
tags: [ai-engineering, automation, software-factory, product-discovery, harness-engineering, strategy]
---

Sources:

* Video: Stop Building Software Factories — Justin McCarthy, Diffusion - AI Engineer [link](https://www.youtube.com/watch?v=1S4hx3wgvBE)


What if the biggest mistake in AI engineering today is spending millions of tokens building automated software factories for products customers don't actually want?

As AI capabilities surge, technical leaders are rushing to automate software creation. However, Justin McCarthy, founder and CEO of Diffusion, delivers a provocative warning: industrializing software development before establishing product-market fit only accelerates the production of unwanted features. To capture real value, organizations must pivot away from greenfield automation, deploy brownfield factories to maintain existing promises, and invent **demand factories** that rate-match code output to actual market appetite.

In this lesson, you will learn how to:

- **Distinguish** between greenfield discovery and brownfield factory automation.
- **Explain** how continuous feedback loops maintain software promises without amplifying system noise.
- **Illustrate** the mechanism of self-simplifying factories using the SpaceX Raptor engine analogy.
- **Formulate** a strategy to construct a Demand Factory that expands an organization's brand envelope.

# The Software Factory Trap: Greenfield Discovery vs. Brownfield Automation

The modern concept of the AI software factory emerged when engineers began looping advanced language models like the Claude 4 series with specialized orchestration harnesses. In those early iterations, getting an agent loop to produce stable code required extensive engineering—resembling a duct-taped **Rube Goldberg contraption**. While those complex setups proved that autonomous code generation was possible, they operated at tremendous token expense and required constant human handcrafting.

Today, building autonomous loops has become far easier, prompting many teams to build software factories for every new idea. McCarthy argues that this is a critical strategic error. Subjecting unproven, **greenfield** ideas to an automated factory process is counterproductive because greenfield development is fundamentally about discovery. When you do not yet know what the customer wants, industrializing production simply causes you to build the wrong thing faster, spend too much capital, and generate unnecessary software bloat.

Instead, engineering effort should be directed toward **brownfield factories**. A brownfield environment consists of existing, revenue-generating software where customers actively validate product utility with their dollars and daily usage. In a brownfield codebase, you do not need to invent customer requirements; the runtime data, user interactions, and support tickets provide all the telemetry necessary to stabilize and maintain the system automatically.

# Encoding System Promises & The Feedback Loop Mechanism

To build an effective brownfield factory, developers must reframe software requirements as **promises**. A promise represents a core dimension or guarantee within a product that holds value for the customer. Promises encompass specific functional features, price points, performance targets, latency limits, and security guarantees. In an operational system, you rarely want to regress on an established promise.

Once promises are explicitly defined, they are encoded into automated agent loops. McCarthy compares an operational software factory loop to the classic block diagram of an **audio amplifier**. In electronics, an amplifier takes an input signal, processes it, and relies on a feedback leg to maintain fidelity. If you cut that feedback leg, the system simply amplifies background noise. Similarly, an agentic software loop operating without clear runtime feedback will amplify technical debt, security vulnerabilities, and code clutter.

When tuned correctly with feedback from production runtime telemetry, a brownfield factory operates under the principle of **continuous intelligence**. While human developers work in periodic cycles with daily and weekly seasonality, autonomous agents maintain system promises 24/7. This continuous maintenance focuses on pushing the codebase toward a Pareto equilibrium—making the system faster, cheaper, and safer without trading off overall integrity.

# The Architecture of Simplification: The Raptor Engine Paradigm

A unique phenomenon of building software factories in the AI era is that the systems **self-simplify over time**. In traditional software engineering, adding capabilities inevitably increases architectural complexity. However, because AI software factories rely on underlying foundation models and agent harnesses, advances in model intelligence naturally reduce the amount of scaffolding needed to achieve a result.

To illustrate this dynamic, McCarthy references the evolution of SpaceX's Raptor rocket engine. The initial **Raptor 1** engine was notoriously complex, covered in intricate external tubing, sensors, and fiddly components. It successfully propelled rockets, but required constant maintenance. By applying concentrated intelligence, engineers designed **Raptor 2**, which fit into the exact same external dimensions but delivered significantly higher performance with drastically fewer moving parts.

Software factories follow the exact same evolutionary curve. A factory harness that begins as an intricate web of complex prompts and manual agent handshakes will gradually collapse into shorter prompts and unified model capabilities as foundation models progress. If an engineering team can construct a working brownfield loop today—even if fragile—they can expect smoother, laminar workflow and higher performance in future model iterations without needing to redesign the harness from scratch.

# Aligning Supply with Demand: Constructing the Demand Factory

As brownfield software factories become hyper-efficient, organizations face a new bottleneck: a **glut of software**. Customers rarely want additional UI windows or buttons to click; they want higher gross margins, more customers, and distinct brand differentiation. Simply shipping more code creates excess supply that can spill over and overwhelm change management capacity.

To balance this output, organizations must build a **demand factory**. While a software factory optimizes backend code production, a demand factory uses AI agents to explore the market, synthesize customer intent, and generate commercial demand. Demand factories operate through four main mechanisms:

- **Prioritized Market Inquiry:** Agents formulate and ask targeted questions of the market to identify emerging needs.
- **Continuous Synthesis:** Agents process incoming customer responses, tickets, and feedback overnight, re-ranking market priorities.
- **Automated Experimentation:** Agents schedule pricing elasticity experiments to maximize share of wallet within finite experimental bandwidth.
- **Latency Reduction:** Systems lower response latency for customer requests, encouraging prospects to express broader needs.

Building a demand factory enables an organization to expand its **brand envelope**. Consider a beverage company like Spindrift: moving from sparkling water into caffeinated energy drinks represents a logical expansion of its brand envelope, whereas attempting to sell motor oil breaks it. By using demand factories, technical leaders can identify adjacent product opportunities ("energy drinks"), systematically add new SKUs and product lines, and capture market share before competitors can react.

# Key Takeaways:

- **Stop Industrializing Uncertainty:** Avoid building software factories for greenfield ideas; use discovery-oriented techniques until product-market fit is established.
- **Automate Brownfield Promises:** Encode existing user expectations (security, latency, cost) into closed loops that operate continuously without amplifying system noise.
- **Leverage Model Progression:** Anticipate that factory harnesses will self-simplify over time, adopting a cleaner "Raptor 2" architecture as underlying models improve.
- **Rate-Match Supply with Demand:** Build demand factories to synthesize customer signals, run pricing elasticity experiments, and systematically stretch your brand envelope.

# Additional Context from the Source

- **Speaker**: Justin McCarthy introduces himself in the talk as founder and CEO of Diffusion, a company "diffusing the capabilities of the model into the global economy". Talk published on the AI Engineer channel, 2026-11-26. (Older public listings describe him as co-founder and CTO of StrongDM; the video confirms the Diffusion role.)
- **Origin**: he started building a factory in July 2025 on the Claude 4 series, before GPT-5 and the first Codex harness.
- **Promises he names**: features, cost and price, and security. Performance appears through "faster"; latency is not named as a promise in the talk.
- **The standing instruction**: "the same, but faster", then cheaper and safer, as long as the system stays at a Pareto equilibrium (no trading one for another). "Better" is left out on purpose: it needs intent, judgment, and taste, so it belongs in discovery, not the brownfield factory.
- **Rewrites and backlog**: brownfield factories can also rewrite legacy code, so technical debt and long backlogs start to dry up.
- **Stand one up in a week**: he estimates a brownfield factory over your existing commitments takes about a week to set up.
- **Freedom for greenfield**: the brownfield factory frees time for greenfield work, done with product-market-fit and discovery energy rather than loop rigor.
- **Simplification evidence**: skills are getting shorter and harnesses more general, credited mostly to the models.
- **Demand factory is speculative**: he says he does not really know what a demand factory is yet and that it needs discovery itself. He frames building it as the new job for engineers, who are most fluent with the models: don't wait for sales and marketing. A brownfield factory keeps promises but cannot build the moat.
- **Growth ladder**: demand flow must not overwhelm customers' appetite for change, so you need more customers and more share of wallet, which means more SKUs, organized into product lines, and finally acquiring competitors.
- **First-mover edge**: competitors have the same models, but starting first still gives an edge.
- **Dual-channel messages**: he describes sending messages with a human part and an attached part for the reader's agents; the talk ended with a QR code to technical material for agents.
- **Correction**: the inbox copy said customers want "faster outcomes"; the talk says "more customers". Fixed above.

See [[Greenfield vs Brownfield Software Factories]], [[Software Promises]], [[Self-Simplifying Factory Harnesses]], [[Demand Factory]], [[Autonomous Software Factory]], [[Bottleneck Shift (Theory of Constraints)]], [[Problem-First Thinking]], [[Harness Engineering]], [[Feedforward Guides and Feedback Sensors]]

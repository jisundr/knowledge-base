---
type: article-note
status: reviewed
created: 2026-11-20
tags: [ai-engineering, ai-agents, context-engineering, workflows]
source: https://notebook.google.com/notebook/57347d06-5cee-4bb3-8a0c-d1dd4b0fd43e
---

Notebook: https://notebook.google.com/notebook/57347d06-5cee-4bb3-8a0c-d1dd4b0fd43e

The **Interpretable Context Methodology (ICM)** is a system-first architecture created by Jake Van Clief and David McDermott that replaces complex multi-agent programming frameworks with a straightforward **filesystem structure**. It organizes workflows into numbered folders and plain Markdown files**. ICM allows a single AI agent to navigate progressively through a **five-layered context hierarchy**, dramatically reducing token overhead and preventing performance degradation caused by irrelevant information.

# The Philosophy of ICM: Folder over Frameworks

The ICM philosophy can be summarized in one central idea: **use filesystem structure instead of framework code to orchestrate AI workflows**.

Rather than building complex multi-agent software or writing giant prompts, ICM organizes work into plain-text Markdown files inside a numbered folder tree. A single AI agent navigates this folder hierarchy step by step, reading only specific files it needs at each stage.

## The 6 Pillars of ICM Philosophy

1. **Folders Over Frameworks**: 
	- Traditional agent architectures rely on code-heavy frameworks (such as LangChain, AutoGen, or CrewAI) to manage memory, tools, and message-passing.
	- ICM replaces framework orchestration with a folder hierarchy, letting the filesystem itself serve as the state machine and control surface.
2. **The LLM is a Compiler, Not a Chatbot**
	- ICM treats large language models like **multi-pass compilers** rather than conversational chatbots.
	- Each stage executes under a strict **stage contract** (`CONTEXT.md`) that explicitly defines its inputs, process, and outputs, producing structured deliverables without conversational stuff during execution.
3. **Unix Tradition: "One Stage, One Job"
	- Borrowing principles from Unix pipelines established in the 1970s, multi-step workflows are split into sequential, numbered folders (e.g., `01_research`, `02_script`, `03_production`).
	- A stage that conducts research does not write the script, keeping each step narrowly focused and modular.
4. **Layered Context Loading (Preventing "Lost in the Middle")**
	- Stuffing all prompts, style guides, and conversation history into a single monolithic prompt inflates context to 30,000-50,000+ tokens, causing model performance degradation.
	- ICM organizes context into a **5-layer hierarchy** (Layers 0 though 4), ensuring the AI agent receives a tightly scoped 2,000 - 8,000 token window per stage.
5. **Every Output is an Edit Surface (Glass-Box Transparency)**
	- Because system state exists strictly as files on disk, the output of every stage is a plain Markdown file that a human can open, inspect, edit, or approve before the next run.
	- This provides complete **observability by default**, eliminating the need for complex logging dashboards or opaque "black box" execution loops.
6. **Configure the Factory, Not the Product**
	- ICM separates persistent reference rules (Layer 3: voice guides, design guidelines, brand constraints) from run-specific working data (Layer 4: raw sources, current drafts).
	- You configure the "factory" setup once, and every subsequent run uses that persistent configuration to transform new input into a finished deliverable.

A helpful mental model is to think of an ICM workspace as a physical library. Multi-agent framework approaches often suffer from 'context stuffing', the equivalent of photocopying directory as a small, stable library catalog card. The catalog points the librarian (the LLM) to a specific shelf (a stage folder), where only the relevant books (context files) are pulled for that specific task.

# Navigating the Five-Layer Context Hierarchy

To prevent performance degradation, an AI agent must consume relevant context without being overwhelmed by unnecessary tokens. Research on the 'lost in the middle' phenomenon demonstrates that LLMs attend poorly to instructions buried in the center of long context windows. ICM solves this through its **Five-Layer Hierarchy**, which structures information from global identity down to run-specific artifacts:

- **Layer 0 (Global Identity)**: Stored in a root file like `CLAUDE.md` or `AGENTS.md`, this layer answers *'Where am I?'* It provides top-level identity, folder architecture maps, and global routing rules. It is lightweight (~800 tokens).
- **Layer 1 (Workspace Routing)**: Located in the root `CONTEXT.md`, this layer answers *'Where do I go?'* It maps available stage folders, task categories, and shared resource paths (~300 tokens).
- **Layer 2 (Stage Contract)**: Situated inside each stage folder (e.g., `01_research/CONTEXT.md`), this layer answers *'What do I do?'* It defines the explicit contract of inputs, processes, and output for that specific step (200-500 tokens).
- **Layer 3 (Reference Material / The Factory)**: Persistent reference materials such as voice guides, design systems, formatting rules, and templates. These stay constant across runs, defining how the workspace operates (500-2,000 tokens).
- **Layer 4 (Working Artifacts / The Product)**: Run-specific input data and previous stage outputs. These change with every execution as work moves down the pipeline.

ICM enforces a strict structural distinction between Layer 3 and Layer 4 context. Layer 3 represents the **factory configuration** (rules, brand guidelines, conventions) that the model must internalize as constraints. Layer 4 represents the **product** (raw research, draft scripts) that the model must transform as data. Separating rules from data in distinct folders prevents the model from needing to sort out instructions on its own.

By loading context progressively layer by layer, an agent executing a single stage operates within a tight context frame of 2,000 to 8,000 tokens. This stands in stark contrast to monolithic prompts that stuff 40,000+ tokens of instructions, guidelines, and prior stage outputs into a single prompt, preserving maximum model attention and output quality.

# Building Stage Contracts and Human Edit Surfaces

At the heart of every working ICM stage is the **Stage Contract**, written inside the stage's `CONTEXT.md` file. Each contract follows a simple three-part specification that non-technical users and AI models can easily read:
- **Inputs**: An explicit table mapping exact file paths and section headers from Layer 3 (references) and Layer 4 (predecessor stage outputs).
- **Process**: Step-by-step instructions directing the agent on how to perform the transformation, including audit checks or creative checkpoints.
- **Outputs**: The exact target file path, filename slug, and structural format for the generated artifact.

A core design invariant of ICM is that **every output is and edit surface**. Because every stage writes plain Markdown or JSON to an `output/` directory, the state of the entire system is completely visible on disk. Before stage two reads the output of stage one, a human can open the file in any text editor, tweak the narrative, correct facts or rewrite sections. The agent executing stage two simply picks up whatever text exists in the output folder.

Observations across community practitioners reveal a distinct **U-shaped intervention pattern** during working execution:
- **Heavy Editing at Stage 1**: Creative, direction-setting intervention where human judgement selects angles and narrows scope.
- **Light Editing at Middle Stages**: Constrained execution where established direction and Layer 3 rules guide the agent smoothly.
- **Heavy Editing at the Final Stage**: Quality assurance and alignment debugging, verifying that the final output matches original intentions.
To keep workspaces redable as they grow, ICM enforces key operational conventions: stage contracts must remain under 80 lines, reference files under 200 lines, and all factual rules must adhere to the **canonical sources pattern**, meaning every fact has exactly one authoritative home, with all other files using pointers or relative links rather than copies.

# Practical Workspaces, MCP and Future Trajectories

ICM's folder-based architecture has been deployed across diverse production workflows:
- **Script-to-Animation Pipeline**: A 3-stage workspace transforming raw ideas into structured research (`01_research`), narrative scripts (`02_script`), and Remotion animation specifications (`03_production`).
- **Course Deck Production**: A 5-stage workspace extracting unstructured source material (PDFs, lecture notes) into polished presentation slide decks.
- **Workspace-Builder**: A self-referential 5-stage meta-workspace that interviews a user about a recurring workflow and automatically scaffolds a brand-new, fully compliant ICM workspace directory.

Practioners often ask how ICM relates to Anthropic's **Model Context Protocol (MCP)**. The two protocols operate at different layers and are completely complementary. MCP defines how an AI model connects to external tools, databases, and APIs at runtime. ICM defines how files, stage contracts and context instruction are organized statically across a workflow. An ICM stage contract can explicitly instruct an agent to use an MCP connection to fetch data, combining structured context scoping with dynamic tool integration.

While ICM excels at sequential, reviewable, and repeatable knowledge work, it is not a silver bullet. Real-time multi-agent loops requiring millisecond message passing, high-concurrency multi-tenant workloads, and complex automated branching require dedicated programmatic frameworks.

Looking toward the future, research in ICM focuses on **semantic debugging** and **source integrity tracking**. By embedding lightweight section identifiers into generated artifacts, practitioners will be able to trace an error in a final output directly back to the specific instruction or reference file that produced it. Furthermore, by tracking recurring manual human edit across runs, future systems will suggest permanent source-level updates to Layer 3 reference files - implementing the **edit-source principle** so workspaces continuously improve over time.

# Key Takeaways
- **Structure is Architecture**: Numbered folders replace orchestration code; plain Markdown files carry instructions, state, routing.
- **Five-Layer Scoping**: Scoping active context between 2,000 and 8,000 tokens per stage prevents 'lost in the middle' attention degradation.
- **Factory vs Product**: Layer 3 reference material (the factory) stays constant across runs, while Layer 4 working artifacts (the product) flow dynamically through output directories.
- **Human Edit Surfaces**: Intermediate plain-text files allow humans to review, edit or steer workflow progress seamlessly between stage boundaries.
- **Complementary Ecosystem**: ICM manages static context hierarchy, pairing perfectly with protocols like MCP that manage dynamic tool integration.

# Multi Million Dollar Questions
- How to integrate this on 2nd brain or coding agents?
- Others figured out on how to use ICM on this kind of setup: Obisidian for memory, Graphify for connection and ICM for direction. How can we integrate this on our workflows?

# Topics

See [[Interpretable Context Methodology (ICM)]]
See [[Five-Layer Context Hierarchy]]
See [[Stage Contract]]
See [[Lost in the Middle]]
See [[Context Engineering]]
See [[Progressive Disclosure]]
See [[Model Context Protocol (MCP)]]

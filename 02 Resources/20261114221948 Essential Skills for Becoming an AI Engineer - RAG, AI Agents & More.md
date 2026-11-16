---
type: video-note
status: reviewed
created: 2026-11-14
tags: [ai-engineering, rag, ai-agents, embeddings, devops]
source: https://www.youtube.com/watch?v=XN3xNJvWXsc&t=252s
---

Source: https://www.youtube.com/watch?v=XN3xNJvWXsc&t=252s
Notebook: https://notebook.google.com/notebook/25034987-5050-49ae-b812-575045cb73c6


# AI Engineer vs. Machine Learning Researcher

The primary difference between an ML Researcher and an AI Engineer comes down to whether they are building the underlying models or building applications with existing models.

## ML Researcher

- Focuses on training foundational models and developing new model architectures.
- Publishes research papers about new models and architectures.
- Typically requires deep mathematical knowledge and usually an advanced degree.

## AI Engineer

* Takes existing models, i.e., frontier or open-source models created by researchers, and wires them into working systems that do useful work.
* Produces solutions and products that end-users can actually use, achieved by connecting models to data sources, tools, memory loops, guardrails, and APIs.
* Focuses on practical software engineering and applied AI skills such as Python, Linux/CLIs, RAG, AI agent design, and containerization/deployment rather than theoretical math.


> [!Analogy]
> If ML researchers are the ones building the engine, then AI engineers are the ones building the car

# 3 Tier Skill Stack of Becoming an AI Engineer

See [[AI Engineer Skill Stack]].

## Tier 1: The Foundation

* **Python**: You need to be fluent enough to read code, understand what an AI agent generates, and interact with machine learning libraries (like PyTorch and TensorFlow) that use Python under the hood.
* **Linux, CLIs, and Git**: Understanding Git for version control and project sharing, along with Command Line Interfaces (CLIs) and Linux. AI development tools, agents, and deployments mostly run on these environments.
* **APIs (Application Programming Interfaces)**: Learning how to connect software components, make programmatic calls to models, handle responses, and manage rate limits. Every AI product is built on structured API calls between your application, models, and tools.

Skipping this foundation often forces developers to spend time relearning the basics later when building agents or deploying systems.

## Tier 2: Knowledge Retrieval and Dynamic AI Agents

These skills focus on core applied AI capabilities required for modern AI applications.

* **[[Embeddings and Vector Search]]**: Language models can struggle with simple keyword matching. Vector embeddings solve this by converting text (from PDFs or other formats) into numerical vectors, so systems understand semantic meaning rather than exact word matches. This enables vector databases to search by context and concept similarity (such as recognizing how "Kubernetes" relates to "containers" and "orchestration").  
* **[[Retrieval-Augmented Generation (RAG)]]**: Prevents model hallucinations by feeding relevant, grounded source data (such as internal company policies or legal documents) into the LLM's context window alongside user questions. See RAG Pipeline below.
* **[[AI Agents and Tool Use]]**: Shift AI systems from merely answering static questions to actively performing actions. Unlike a standard linear workflow with fixed steps (A -> B -> C), an AI agent can dynamically choose its next action, run external tools, observe the results, and iterate through decision loops.

## Tier 3: Deployment and Operations

* **[[Containerization and Orchestration]]**: Packaging agents, dependencies, and local model microservices into standardized containers (using tools like Docker and Kubernetes) ensures reliable execution across hybrid cloud infrastructure.
* **Observability**: Tracing model calls, database queries, and tool interactions to understand why an agent made a specific decision, which is essential for transparency and building trust.
* **Monitoring and Security**: Tracking application health, safeguarding the system from a security standpoint, and controlling costs like token bills.

# Top 3 Production AI Use Cases

1. **Enterprise Knowledge RAG**: Internal search engines powering HR desks, legal teams, and customer service chatbots.
2. **Analytical AI Agents**: Agents that query corporate databases and visualize complex datasets on demand.
3. **Developer Acceleration**: AI integration tools that assist engineering teams in deploying production code faster.

# RAG Pipeline

Details in [[Retrieval-Augmented Generation (RAG)]].

1. **Ingestion and Chunking**: Source documents enter the pipeline and are broken down into fixed sizes.
2. **Embedding and Storage**: Text chunks are transformed into vector embeddings and stored in a vector database.
3. **Retrieval**: When a user asks a question, the system retrieves relevant document chunks matching the query's mathematical similarity.
4. **Augmented Prompting**: The retrieved context and the user query are injected into the model's context window.
5. **Grounded Generation**: The model generates a natural language response rooted directly in the factual context.

# Key Takeaways
* Learn the following skills to become an AI engineer
	* **Fundamentals**: Python, Linux, CLIs, and Git
	* **Core AI Engineering**: Embeddings and Vector Search, RAG, and AI Agents and Tool Use.
	* **Production and Deployment**: Kubernetes and Docker for containerization and deployment.

# Notes
* Research Graphify and similar GitHub repos, and identify whether these repos are under embeddings and vector search.
* Research Docker, Kubernetes, and Ray.
* Research and compare Ollama, LMStudio, and vLLM.
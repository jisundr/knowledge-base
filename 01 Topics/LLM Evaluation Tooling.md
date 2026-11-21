---
type: topic
tags: [ai-engineering, evaluation, tools]
---

# LLM Evaluation Tooling

Pick a tool by matching language, architecture, and CI needs.

- **DeepEval / Confident AI**: Python, 50+ metrics (RAG, tool correctness, step efficiency), `pytest` runner.
- **Promptfoo**: CLI-first, declarative YAML for prompt-by-provider matrices and assertions (`contains`, `latency`, `llm-rubric`, `regex`, `factuality`).
- **Langfuse**: tracing, prompt management, PR regression gates via GitHub Actions.
- **Arize Phoenix**: open-source trace capture and RAG evals.
- **Mastra**: TypeScript-native agent framework with built-in evaluators.
- **TruLens**: the RAG Triad (faithfulness, answer relevance, context relevance).
- **RAGAS**: reference-free [[Retrieval-Augmented Generation (RAG)]] metrics.
- **LangSmith**: managed tracing and datasets for LangChain/LangGraph.
- **Cloud evaluators** (Bedrock and peers): managed model-level and judge evals.

A CI regression gate is just a script that scores a golden dataset and exits non-zero below threshold.

## Related

- [[AI System Evaluation]]
- [[Evaluator Cascade]]

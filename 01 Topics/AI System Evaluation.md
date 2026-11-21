---
type: topic
tags: [ai-engineering, evaluation, llm, ai-agents]
---

# AI System Evaluation

Judging an LLM application by how well the whole pipeline solves user tasks, not by how strong the base model is. Non-deterministic outputs break classic unit tests, and an app can return HTTP 200 while completely missing user intent, so uptime monitoring is not quality assurance.

## Model vs system evaluation

- **Model evaluation**: raw capability of a foundation model on academic benchmarks (MMLU for general knowledge, GSM8K for multi-step math, HumanEval for code). Predicts real-world reliability poorly.
- **System evaluation**: end-to-end pipeline: system prompt, [[Retrieval-Augmented Generation (RAG)]] context, tool definitions, orchestration, [[Agent Memory]], guardrails.

## Three universal data units

| Unit | When | Holds |
| --- | --- | --- |
| **Golden** | before execution | input, expected output/outcome, context, constraints, allowed tools |
| **Test Case** | after execution | golden + actual output, retrieved chunks, tool calls, scores |
| **Trace** | after execution | span tree of model calls, tool args, retries, latency, tokens |

The trace is what enables root-cause analysis when a test fails; see [[Evaluation Error Analysis Flywheel]].

## Related

- [[Evaluation Dataset Design (5 D's)]]
- [[Evaluator Cascade]]
- [[LLM-as-a-Judge]]
- [[Multi-Agent Orchestration Patterns]]
- [[LLM Evaluation Tooling]]
- [[AI Agents and Tool Use]]

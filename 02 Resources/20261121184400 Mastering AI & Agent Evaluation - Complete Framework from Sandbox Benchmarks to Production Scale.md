---
type: resource
status: reviewed
created: 2026-11-21
tags: [ai-engineering, evaluation, llm, ai-agents]
---

Sources:

* Paper: A Practical Guide for Evaluating LLMs and LLM-Reliant Systems [link](https://arxiv.org/abs/2506.13023v1)
* Paper: A Survey on Evaluation of Large Language Models [link](https://doi.org/10.1145/3641289)
* Article: AI agent evaluation: frameworks, metrics & testing strategies (Algolia) [link](https://www.algolia.com/blog/ai/ai-agent-evaluation-frameworks-metrics-testing-strategies)
* Article: AI performance engineering: A beginner's guide (Tricentis) [link](https://www.tricentis.com/learn/ai-performance-engineering)
* Paper: Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies [link](https://arxiv.org/abs/2603.22651)
* Article: Evals for AI Engineers (ByteByteGo Newsletter) [link](https://blog.bytebytego.com/p/evals-for-ai-engineers)
* Book: Evals for AI Engineers (O'Reilly) [link](https://www.oreilly.com/library/view/evals-for-ai/9798341660717/)
* Paper: Evaluating Retrieval Augmented Generation: A Comprehensive Review of Evaluation Dimensions, Question Types, and Application (SN Computer Science, 2026) [link](https://doi.org/10.1007/s42979-026-05134-x)
* Article: How to do error analysis for LLM apps (HoneyHive) [link](https://www.honeyhive.ai/learn/error-analysis-llm)
* Article: LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide (Confident AI) [link](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation)
* Article: LLM Evaluation: A Practical Guide for AI Agents, Voice AI, RAG, MCP, and More (DeepEval) [link](https://deepeval.com/blog/ultimate-llm-evaluation-guide)
* Article: LLM Observability: A Developer's Guide (Dash0) [link](https://www.dash0.com/knowledge/llm-observability-developers-guide)
* Article: LLM evaluation: frameworks, metrics, methods, and best practices (Mastra) [link](https://mastra.ai/articles/llm-evaluation)
* Article: LLM regression testing: fail CI before regressions ship (Langfuse) [link](https://langfuse.com/resources/engineering/llm-regression-testing)
* Paper: LLM-as-a-Judge: Rapid Evaluation of Legal Document Recommendation for Retrieval-Augmented Generation [link](https://arxiv.org/abs/2402.10770)
* Paper: Optimizing the role of human evaluation in LLM-based spoken document summarization systems (Interspeech 2024) [link](https://doi.org/10.21437/Interspeech.2024-2268)
* Article: The Definitive Guide to LLM App Evaluation (Arize AI) [link](https://arize.com/blog/llm-evaluation-guide/)
* Article: Top 9 LLM Evaluation Tools in 2026 (Confident AI) [link](https://www.confident-ai.com/knowledge-base/compare/best-llm-evaluation-tools)
* Article: What is the difference between code-based scorers and LLM-as-a-judge scorers for agent evaluations? (Non-Human Identity Management Group) [link](https://nhimg.org/faq/what-is-the-difference-between-code-based-scorers-and-llm-as-a-judge-scorers-for/)
* Article: The complete guide for LLM evaluations in 2026 (Galtea) [link](https://galtea.ai/blog/llm-evaluation-complete-guide)

See [[AI System Evaluation]], [[Evaluation Dataset Design (5 D's)]], [[Evaluator Cascade]], [[LLM-as-a-Judge]], [[Evaluation Error Analysis Flywheel]], [[Multi-Agent Orchestration Patterns]], [[LLM Evaluation Tooling]], [[LLM Evaluation Glossary]]

# The AI Evaluation Paradigm Shift & Core Taxonomy

Evaluating Large Language Model (LLM) applications and autonomous AI agents requires a fundamental departure from classical software engineering protocols. In deterministic software, unit tests assert that specific inputs yield exact, bit-for-bit reproducible outputs. Generative AI systems, by contrast, sample non-deterministic outputs from probability distributions over high-dimensional input spaces. As documented in the developer guide by Dash0, an LLM application can return a standard 200 OK HTTP status code while completely failing to fulfill user intent, rendering traditional infrastructure and uptime monitoring insufficient for AI quality assurance.

A foundation principle established across the evaluation literature, including work by Arize AI, Mastra and Google Research, is the strict separation between **model evaluation** and **system evaluation**:

- **Model Evaluation**: Measures the raw, parametric capabilities of foundation base models (such as GPT-4o, Claude Sonnet 5.5, or Llama 3) across standardized academic benchmarks. These include MMLU for general domain knowledge, GSM8K for multi-step math reasoning, and HumanEval for code synthesis. While academic benchmarks quantify general model capacity, research published by Algolia highlights a stark gap between lab benchmarks and production reality: a March 2026 enterprise survey revealed that while 78% of enterprise engineering teams have AI agent pilots underway, fewer than 15% have successfully deployed agents at scale due to unaddressed execution trajectory failures. 
- **System Evaluation (Task-Level Evaluation)**: Assesses the complete end-to-end software pipeline. This encompasses the system prompt, retrieval-augmented generation (RAG) context windows, tool definitions, multi-step agent orchestration, short/long-term memory stores, and safety guardrails. System evaluation measures how effectively the application solves user tasks under operational constraints.

As detailed in the DeepEval evaluation guide, AI system evaluation operates across three universal data units throughout the application lifecycle.

## The Three Universal Units of LLM Evaluation

To construct robust testing pipelines, engineering teams must distinguish between pre-inference specifications, structured post-inference test objects, and raw runtime telemetry traces.

| Evaluation Unit | Operational Timing | Single-Turn Data Representation                                             | Multi-Turn Agent Representation                                                                 | Primary Architectural Rule                                                                   |
| :-------------- | :----------------- | :-------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| **Golden**      | Pre-Execution      | Input query, reference ground truth, static context, metadata               | Task scenario, expected outcome, user persona profile, permitted tool list                      | Defines the benchmark standard and expected constraints before inference.                    |
| **Test Case**   | Post-Execution     | Golden payload plus actual output, retrieved chunks, tool calls and scores. | Golden payload plus conversation turns, execution trajectory, and metric verdicts               | Structures runtime evidence into a standardized schema for quantitative evaluation.          |
| **Trace**       | Post-Execution    | Span tree of model calls, latency, token usage, and retrieval payloads.     | Hierarchical execution tree detailing agent planning, tool arguments, retries and state shifts. | Preserves the complete, free-form telemetry necessary for deep error analysis and debugging. |
Golden establish the ground-truth baseline before execution occurs. When the application executes against a golden record, it yields a structured test case alongside a telemetry trace. The trace records every intermediate decision, such as vector database lookups, tool parameter extractions, and sub-agent handoffs, enabling developers to perform root-cause analysis when a test fails.

## Adhering to the 5 D's of Evaluation Datasets

As outlined in Google's practical evaluation framework by Ethan Rudd et al., the quality of an evaluation dataset governs the trustworthiness of all downstream metrics. High-quality evaluation datasets must strictly adhere to the five core principles known as the **5 D's**:

1. **Demonstrative of Production Usage**: Dataset queries must mirror real-world user intent, derived from production logs, user-reported issues, and customer satisfaction correlations rather than synthetic ideals.
2. **Diverse**: Prompt distributions must cover the full operational space, evaluated using Locality-Sensitive Hashing (LSH) or embedding-based semantic clustering to prevent over-representing easy queries.
3. **Defined Scope**: Datasets must isolate individual components (e.g., tool-argument extraction vs. final synthesis) in addition to end-to-end pipelines, serving as unit tests for AI subsystems.
4. **Decontaminated**: Evaluation data must be strictly isolated from model training or fine-tuning datasets to avoid artificial metric inflation, verified via exact string matching or perplexity continuation testing.
5. **Dynamic**: Benchmark datasets must evolve over time, regularly updated to reflect new product features, edge cases, and emerging user behaviors while deprecating obsolete queries.

# Multi-Agent & Specialized Architecture Evaluation

Evaluating multi-agent systems introduces architectural complexities far beyond single-prompt or simple RAG applications. When multiple autonomous agents collaborate to solve a task, evaluation pipelines must inspect not only final outputs, but also delegation topologies, message routing, and inter-agent coordination efficiency.

## Architectural Orchestration Trade-offs

Research by Kulkarni et al. (arXiv 2603.22651) benchmarking multi-agent LLM architectures for financial document processing (evaluating thousands of SEC disclosures) provides a comparative breakdown of multi-agent orchestration patterns:

- **Sequential Orchestration**: Agents execute in a fixed linear chain (e.g., Data Extractor -> Financial Analyst -> Summarizer). Simple to evaluate with low overhead, but fragile if an upstream agent introduces errors.
- **Parallel Orchestration**: Independent sub-agents analyze separate document sections concurrentlyly before an aggregator synthesizes results. Offers sub-second execution speeds, but requires robust deduplication and consensus evaluation.
- **Hierarchical Orchestration**: A lead orchestrator agent dynamically decomposes user intent, assigns sub-tasks to specialized worker agents, and reviews intermediate outputs. The financial benchmark demonstrated that hierarchical orchestration provides the optimal balance of accuracy, monetary cost, operational scalability.
- **Reflexive / Self-Correcting Loops**: Agents iteratively critique and refine their own outputs until specific quality criteria are satisfied. While highly accurate for isolated complex reasoning, the research highlights that reflexive loops suffer severe degradation at high operational scale due to exponential latency queueing delays and compounding token costs.

## Multi-Agent Evaluation Metrics Matrix

Evaluating multi-agent workflows requires tracking five specialized performance dimensions:

| Dimension                | Scope         | Key Metric / Metric Formula                                                     | Failure Mode                                            |
| ------------------------ | ------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Task Accuracy**        | End-to-End    | Precision / Recall on extracted attributes vs. ground truth                     | Extrinsic hallucination, invalid data extraction        |
| **Tool Correctness**     | Step-Level    | Ratio of valid tool invocations with correct argument types                    | Schema violation, hallucinated tool parameters          |
| **Step Efficiency**      | Trajectory    | Ratio of essential steps vs. total executed steps (Optimal Steps / Total Steps) | Infinite retry loops, redundant tool calls              |
| **Coordination Quality** | Inter-Agent   | Inter-agent message relevance and context preservation ratio                    | Loss of state across agent handoffs, context truncation |
| **Operational Scaling**  | Infrastructure | P95 latency (ms) and cost per task completion under concurrent load          | Latency degradation in reflexive loops                  |

# The Evaluator Spectrum & Calibration Methodologies

A mature evaluation suite does not rely on single scoring mechanism. Instead, it deploys a tiered cascade of evaluators ranging from instant, zero-cost programmatic checks to natural language LLM judges. As analyzed by Non-Human Identity Management Group and HoneyHive AI, combining deterministic code assertions with model-graded rubrics provides both strict operational enforcement and semantic flexibility.

## The 5-Tier Evaluator Cascade

The evaluation pipeline routes execution outputs through five progressive levels of assessment:

1. **Level 1: Deterministic Code Checks**: Evaluates structural rules, exact string matches, regex patterns, and JSON schema compliance with sub-millisecond execution and zero token cost.
2. **Level 2: Programmatic Heuristics**: Evaluates quantitative operational bounds, such as latency budgets (TTFT), token consumption caps, tool execution success rates, and keyword coverage.
3. **Level 3: Reference-Based & NLI Metrics**: Measures statistical overlap (ROUGE, BERTScore) or applies Natural Language Inference (NLI) models to evaluate logical entailment between statements.
4. **Level 4: Model-Based Scorers (LLM-as-a-Judge)**: Deploys high-capability LLMs to evaluate open-ended quality, reasoning coherence, brand alignment, and complex agent trajectories using explicit rubrics.
5. **Level 5: Human Domain Expert Review**: Incorporates human-in-the-loop review to annotate ambiguous cases, establish ground truth, and continuously calibrate automated judges.

## Comparative Evaluation of Scorer Families

The table below outlines the core trade-offs across major scoring approaches.

| Scorer Family                              | Determinism    | Latency & Cost    | Best Use Case                                                      | Primary Failure Mode / Risk                                    |
| ------------------------------------------ | -------------- | ----------------- | ------------------------------------------------------------------ | -------------------------------------------------------------- |
| **Deterministic Code Checks**              | 100% Fixed     | < 1ms / $0.00     | JSON validation, regex pattern matching, tool argument constraints | Misses semantic nuance and contextual meaning                  |
| **Lexical Overlap (BLEU / ROUGE)** | 100 % Fixed    | < 5ms / $0.00     | Exact string matching, short text summarization                    | Penalizes valid paraphrasing and semantic synonyms.            |
| **Semantic Embeddings (BERTScore)**   | High           | ~ 20ms / Low      | Vector similarity matching against reference text                   | Vulnerable to domain shift and subtle negations.               |
| **NLI Entailment Model**                   | High           | ~ 50ms / Low      | Factual alignment and hallucination detection                      | Struggles with long-form multi-sentence context                |
| **LLM-as-a-Judge (G-Eval/ QAG)**     | Stochastic | 1-3s / Token Cost | Open-ended QA, reasoning quality, RAG faithfulness, agent intent   | Subject to position bias, verbosity bias, and self-preference. |

## Calibrating LLM Judges & Statistical Inter-Rater Reliability

While LLM-as-a-judge scorers scale seamlessly, research published in arXiv studies on legal document RAG systems demonstrates that relying on simple correlation metrics like Krippendorff's alpha can be misleading due to the heavily skewed distributions common in hallucination testing.

To build trustworthy LLM judges, engineering teams should implement the following statistical calibration protocols:

- **Gwet's AC2 Coefficient**: Outperforming Krippendorff's alpha and Cohen's kappa when evaluating skewed binary or ordinal data (such as rare hallucination events), providing a stable agreement score between human raters and LLM judges.
- **Rank Correlation (Spearman & Kendall Tau)**: Used when relative ordering matters more than absolute scores, verifying whether an LLM judge ranks candidate responses in the same order of quality as human domain experts.
- **Non-Parametric System Comparison**: When comparing two competing LLM configurations across evaluation runs, use the **Wilcoxon Signed-Rank Test** paired with **Benjamini-Hochberg corrections** to control false discovery rates across multi-metric evaluations.
- **Mitigating Judge Biases**: To eliminate position bias (favoring the first presented option), verbosity bias (favoring longer responses), and self-preference bias (favoring outputs generated by the same model family), evaluation pipelines should utilize binary pass/fail rubrics, require step-by-step Chain-of-Thought reasoning prior to scoring and swap response order across multi-judge panels.

# Standard Data Specification & Evaluator Formats

Standardizing data specifications across development environments ensures that evaluation benchmarks remain portable across local CLI runners, CI/CD pipelines, and enterprise observability suites.

## Machine-Readable Golden Dataset Format (JSON)

Golden datasets encapsulate the input queries, expected ground truth, static contexts, and metadata needed for repeatable benchmark execution.

```
[
  {
    "id": "gold_rag_001",
    "type": "single_turn_rag",
    "input": {
      "question": "What is the paid annual leave policy for full-time employees?",
      "context": [
        "HR Policy Document 4.2: Full-time employees accrue 20 days of paid annual leave per calendar year. Leave requests exceeding 5 consecutive business days require manager approval."
      ]
    },
    "expected_output": "Full-time employees receive 20 days of paid annual leave per calendar year under HR Policy 4.2.",
    "metadata": {
      "category": "HR_Policy",
      "difficulty": "easy"
    }
  },
  {
    "id": "gold_agent_084",
    "type": "multi_turn_agent",
    "scenario": "Customer requests a refund for order #ORD-9921 which arrived damaged.",
    "user_profile": "Frustrated high-value tier customer.",
    "expected_outcome": "Agent verifies damage proof, executes refund_order tool, and logs incident ticket.",
    "expected_tools": [
      "verify_order_status",
      "process_refund",
      "create_support_ticket"
    ],
    "constraints": [
      "Refund amount must not exceed $500 without supervisor approval.",
      "Must remain empathetic and adhere to brand tone."
    ]
  }
]
```

## Standardized LLM-as-a-Judge Rubric Prompt Template

To ensure judge consistency, model-graded evaluators must enforce structured output schemas (such as JSON formatting) and require explicit reasoning steps prior to score output.

```
You are an expert impartial evaluator assessing the factual correctness and groundedness of an AI response.

[EVALUATION TASK]
Evaluate whether the [ACTUAL OUTPUT] is factually faithful to the [RETRIEVED CONTEXT] and directly answers the [USER QUERY].

[DATA TO EVALUATE]
User Query: {input}
Retrieved Context: {context}
Actual Output: {actual_output}

[SCORING RUBRIC & CRITERIA]
- Score 1.0 (Fully Faithful): Every statement in [ACTUAL OUTPUT] is directly supported by [RETRIEVED CONTEXT]. No ungrounded claims or extraneous details added.
- Score 0.5 (Partially Faithful): The core answer is supported, but contains minor ungrounded details or slight extrapolations.
- Score 0.0 (Unfaithful / Hallucinated): The output directly contradicts [RETRIEVED CONTEXT] or introduces significant ungrounded claims.

[INSTRUCTIONS]
1. Extract all discrete factual assertions made in [ACTUAL OUTPUT].
2. Cross-reference each assertion against [RETRIEVED CONTEXT].
3. Detail any discrepancies or hallucinations in the explanation.
4. Output your final score strictly in JSON format as specified below.

[OUTPUT FORMAT]
{
  "reasoning": "<Step-by-step audit of claims against context>",
  "ungrounded_claims": ["<list of ungrounded statements, if any>"],
  "score": <0.0, 0.5, or 1.0>
}
```

## Declarative Promptfoo CLI Specification (`promptfooconfig.yaml`)

Promptfoo provides a declarative YAML configuration format that enables developers to execute prompt matrix tests, provider benchmarks, and assertion suites from the command line without writing custom evaluation harnesses.

```
# 1. Define prompt templates to compare
prompts:
  - "You are a customer support agent. Answer concisely: {{question}} Context: {{context}}"
  - "You are an AI assistant. Based ONLY on the context: {{context}}, answer: {{question}}"

# 2. Target model providers
providers:
  - openai:gpt-4o
  - anthropic:messages:claude-sonnet-5-5

# 3. Test dataset and assertions
tests:
  - vars:
      question: "What is the return policy window?"
      context: "Customers can return items within 30 days of purchase for a full refund."
    assert:
      # Deterministic string check (Zero token cost)
      - type: contains
        value: "30 days"
      # Latency budget assertion (Milliseconds)
      - type: latency
        threshold: 2000
      # Model-graded semantic check
      - type: llm-rubric
        value: "The response clearly states the 30-day window without introducing outside facts."

  - vars:
      question: "How do I reset my API key?"
      context: "Navigate to Account Settings > Security and click 'Regenerate API Key'."
    assert:
      # Regex pattern check
      - type: regex
        value: "(?i)account settings"
      # Model-graded factual alignment
      - type: factuality
        value: "Navigate to Account Settings > Security and click Regenerate API Key."
```

# Tooling Landscape & Comparative Analysis

The evaluation ecosystem contains specialized tools tailored for different programming languages, architectural patterns, and operational goals. As analyzed in market guides by Confident AI, Mastra, and Langfuse, selecting an evaluation tool requires matching application architecture to tool capabilities.

## Framework & Platform Overview

1. **DeepEval / Confident AI**: The premier open-source evaluation framework in Python. DeepEval includes over 50 research-backed metrics spanning RAG (faithfulness, answer relevancy, context precision/recall), agent trajectories (tool correctness, plan quality, step efficiency), and multi-turn conversations. Confident AI serves as the enterprise cloud platform, providing no-code evaluation workflows for production managers and domain experts.
2. **Promptfoo**: An open-source, CLI-first testing harness configured via declarative YAML. It excels at fast local prompt matrix testing, model provider comparisons, and automated guardrail assertions within CI workflows.
3. **Langfuse**: An open-source LLM engineering platform combining distributed tracing, prompt management, and automated regression testing. It features native GitHub Actions integration (`langfuse/experiment-action`) to execute regression gates on pull requests, failing builds if scores drop below baseline thresholds.
4. **Arize AI / Phoenix**: An enterprise ML observability platform with deep evaluation capabilities. Its open-source library, Phoenix, provides trace capture, RAG evaluation (groundless, QA correctness), and dataset curation for Python workflows.
5. **Mastra**: An open-source TypeScript framework built specifically for Node.js and TypeScript agent developers. It provides native evaluators for tool calling, classification, and multi-turn conversation trajectories, embedding observability directly into TypeScript builds.
6. **TruLens**: An open-source evaluation toolkit optimized for RAG pipelines. It operationalizes the "RAG Triad" (Faithfulness, Answer Relevance, Context Relevance) and utilizes OpenTelemetry tracing for span-level pipeline diagnostics.
7. **RAGAS**: A widely adopted open-source Python library focused specifically on reference-free RAG evaluation metrics, measuring context precision/recall and generator faithfulness.
8. **LangSmith**: A managed SaaS platform by LangChain. It provides end-to-end tracing, dataset versioning, and prompt playground testing, tailored primarily for teams built on the LangChain/LangGraph ecosystem.
9. **Amazon Bedrock & Cloud Evaluators**: Managed evaluation services integrated into AWS, GCP, and Azure. They allow enterprise teams to run model-level benchmarks and custom LLM-as-a-judge evaluations directly within cloud infrastructure.

## Technical Comparison Matrix of Leading Evaluation Tools

The table below outlines technical capabilities across the nine leading evaluation platforms.

| Tool / Framework            | Ecosystem / Language | Primary Strengths                                       | RAG Metric Coverage                               | Agent & Tool Metric Depth                                  | CI/CD Integration Mechanism                    | Deployment & Hosting                             |
| --------------------------- | -------------------- | ------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------ |
| **DeepEval / Confident AI** | Python & TypeScript  | 50+ research-backed metrics; cross-functional UI        | Excellent (Faithfulness, Relevancy, Precision)    | Advanced (Tool Correctness, Plan Quality, Step Efficiency) | `pytest` runner & HTTP triggers                | Open-Source CLI / Cloud / Enterprise Self-Hosted |
| **Promptfoo**               | Node.js / CLI        | Fast, offline declarative YAML testing & red teaming    | Good (Factuality, Semantic Similarity)            | Moderate (Custom JS/Python assertions & latency)           | Native CLI / GitHub Actions                    | Open-Source CLI / Local                          |
| **Langfuse**                | Python, TS, Go, Java | PR regression gates; trace-to-dataset pipeline          | High (Custom judges & code evaluators)            | High (Span-level trajectory scoring)                       | `langfuse/experiment-action` in GitHub Actions | Open-Source / Cloud / Self-Hosted                |
| **Arize AI / Phoenix**      | Python               | High-volume trace observability & span-level evals      | Excellent (Groundedness, QA Correctness)            | Moderate (Iteration counter & step inspection)             | Python test scripts & API triggers             | Open-Source (Phoenix) / Enterprise SaaS          |
| **Mastra**                  | TypeScript           | Native Node.js /TS agent framework with built-in evals  | Good (Context & Answer scoring)                   | High (Tool calling & trajectory rubrics)                   | Vitest / Jest Integration                      | Open-Source / Self-Hosted                        |
| **TruLens**                 | Python               | Diagnostic RAG Triad feedback functions & OpenTelemetry | Excellent (RAG Triad focus)                       | Moderate (Span-level feedback)                             | Pytest runner                                  | Open-Source / Local Dashboard                    |
| **RAGAS**                   | Python               | Reference-less RAG metrics; lightweight library         | Excellent (Context, Precision/Recall/Faithfulness) | Low (Focus is primarily RAG)                               | Pytest scripts                                 | Open-Source / Library                            |
| **LangSmith**               | Python & TypeScript  | Deep LangChain/LangGraph trace visualization            | Good (Built-in RAG evaluators)                    | High (Agent execution graph view)                          | SDK experiment runners                         | Cloud SaaS / Managed Enterprise                  |

# End-to-End Implementation Code Templates

The following runnable code samples demonstrate how to implement automated evaluation suites using Python and DeepEval, alongside a CI/CD regression gate script.

## Sample 1: Python Agent Unit Test Suite (`test_agent_eval.py`)

Using DeepEval's `pytest` integration, this test suite evaluates RAG groundedness, agent tool selection, step efficiency, and custom brand tone against defined thresholds.

```
import pytest 
from deepeval import assert_test 
from deepeval.test_case import LLMTestCase, LLMTestCaseParams 
from deepeval.metrics import ( 
	FaithfulnessMetric, 
	ToolCorrectnessMetric, 
	StepEfficiencyMetric, 
	GEval 
)

# 1. Define reusable evaluators 
@pytest.fixture 
def faithfulness_evaluator(): 
	return FaithfulnessMetric(threshold=0.8, model="gpt-4o")
	
@pytest.fixture
def tool_correctness_evaluator():
	return ToolCorrectnessMetric(threshold=1.0)
	
@pytest.fixture
def step_efficiency_evaluator(): 
	return StepEfficiencyMetric(threshold=0.7, model="gpt-4o")
	
# 2. Test Case: Validate RAG Generator Groundedness 
def test_rag_faithfulness(faithfulness_evaluator): 
	test_case = LLMTestCase(
		input="What is the employee refund limit for travel meals?",
		actual_output="Employees can claim up to $75 per day for meals without receipts.",
		retrieval_context=[ 
			"Expense Policy Sec 3.1: Daily meal allowances are capped at $75 per day. Itemized receipts are optional for expenses under $75." 
		] 
	) 
	assert_test(test_case, [faithfulness_evaluator])
	
# 3. Test Case: Validate Agent Tool Selection & Step Efficiency 
def test_agent_tool_and_efficiency(tool_correctness_evaluator, step_efficiency_evaluator): 
	test_case = LLMTestCase(
		input="Book a flight from NYC to London for tomorrow.",
		actual_output="I have booked flight BA-178 from NYC to London departing tomorrow.",
		expected_tools=["search_flights", "book_flight"], 
		actual_tools=["search_flights", "book_flight"] 
	) 
	# Asserts that exact expected tools were called without redundant steps 
	assert_test(test_case, [tool_correctness_evaluator, step_efficiency_evaluator])
	
# 4. Test Case: Custom G-Eval Metric for Brand Tone
def test_custom_brand_tone():
	tone_metric = GEval( 
		name="Professional Tone", 
		criteria="Determine whether the response maintains a polite, professional, and concise tone.", 
		evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT], 
		threshold=0.8, model="gpt-4o" 
	) 
	test_case = LLMTestCase( 
		input="Your service is terrible and I want my money back!",
		actual_output="I sincerely apologize for your experience. I would be glad to help process your refund immediately." 
	) 
	assert_test(test_case, [tone_metric])

```

## Sample 2: CI/CD Regression Gate Script (`regression_gate.py`)


This standalone Python script executes evaluation experiments over a golden dataset during pull requests. If aggregate accuracy falls below the baseline threshold, it raises an exit code `1` to block CI pipeline merging.

```

import os 
import sys 
import json 
from typing import List, Dict 

# Mock application under test 
def run_support_agent(question: str, context: str) -> str: 
	# Simulates model response generation 
	return f"Based on our policy: {context}, the answer to '{question}' is fully supported." 
	
# Code Evaluator: Deterministic String Containment 
def evaluate_exact_containment(actual_output: str, expected_keyword: str) -> float: 
	return 1.0 if expected_keyword.lower() in actual_output.lower() else 0.0 
	
# CI Regression Gate Entrypoint 
def run_ci_regression_gate(): 
	print("Starting CI Evaluation Regression Gate...") 
	
	# Load Golden Dataset 
	dataset_path = os.path.join(os.path.dirname(__file__), "golden_dataset.json") 
	with open(dataset_path, "r") as f: 
		golden_dataset = json.load(f) 
		
	thresholds = { 
		"min_containment_pass_rate": 0.90, 
		"max_latency_p95_ms": 2500 
	} 
	
	results: List[float] = [] 
	
	for item in golden_dataset: 
		question = item["input"]["question"] 
		context = item["input"]["context"][0] 
		expected_keyword = item.get("expected_keyword", "") 
		
		# Execute application 
		actual_output = run_support_agent(question, context) 
		
		# Score output 
		score = evaluate_exact_containment(actual_output, expected_keyword) 
		results.append(score) 
		
	aggregate_score = sum(results) / len(results) if results else 0.0
	print(f"Regression Gate Results: Pass Rate = {aggregate_score * 100:.1f}% (Threshold = {thresholds['min_containment_pass_rate'] * 100:.1f}%)") 
	
	# Threshold Assertion 
	if aggregate_score < thresholds["min_containment_pass_rate"]:
		print(f"CRITICAL ERROR: Quality regression detected! Score {aggregate_score:.2f} < Threshold {thresholds['min_containment_pass_rate']:.2f}") 
		sys.exit(1) # Fail CI Pipeline 
		
	print("SUCCESS: Regression gate passed. Proceeding with deployment.") 
	sys.exit(0) 
	
if __name__ == "__main__": 
	run_ci_regression_gate()

```

# The Continuous Evaluation Lifecycle & Error Analysis Flywheel

A common engineering failure is treating evaluation as static post-hoc test. In production environments, prompt modifications, model provider updates, and user input drift introduce unseen failure modes.

As advocated by Shreya Shankar and Hamel Husain in Evals for AI Engineers, effective evaluation requires establishing an iterative **Analyze-Measure-Improve Lifecycle**.

## The 5 Stages of Evaluation Deployment

To maintain high quality without slowing development velocity, evaluation checks must be deployed across five distinct operational stages:

1. **Development (Unit Sanity Checks)**: Executed locally on every commit. Consists of sub-second deterministic checks (JSON parsing, regex compliance, status code validation) to catch breaking code errors instantly.
2. **Pre-Release (Adversarial & Red Teaming)**: Stress-test candidate models against adversarial prompts, jailbreak attempts, and security vulnerabilities (such as OWASP Top 10 for LLM Applications) before release approval.
3. **CI/CD Regression Gating**: Automated test runs executed on every pull request using a verson-controlled golden dataset. Merges are blocked if accuracy dropts below baseline thresholds.
4. **Production Monitoring (Online Evaluation)**: Asynchronous sampling of 5% to 10% of live user traffic, scored by automated evaluators (e.g., faithfulness, toxicity, latency) to detect real-world quality drift.
5. **Runtime Guardrails (Synchronous Inline Interceptors)**: Inline safety filters executing in real-time to block policy violations, PII leaks, or harmful outputs before they reach the user.

## Systematic Error Analysis: Open Coding & Axial Coding

Building high-coverage golden dataset begins with qualitative error analysis:

- **Open Coding**: Engineers manually inspect 30 to 50 raw execution traces from production or pilot failures, writing unconstrained notes on the root causes of each failure.
- **Axial Coding**: Notes are grouped into a formal taxonomy of failure modes (e.g., Context Window Truncation, Tool Parameter Extraction Error, Extrinsic Hallucination, Temporal Confusion).
- **Dataset Enrichment**: Each identified failure mode is converted into a permanent test case within the golden dataset, ensuring that resolved bugs never regress in future releases.

By connecting runtime tracing, qualitative error analysis, automated scoring, and CI/CD gates into a continuous loop, engineering teams transform unpredictable AI prototypes into dependable, enterprise-grade software systems


# Key Takeaways

- **Model Evals vs. System Evals**: Academic benchmarks (like MMLU or HumanEval) only test base model capacity and fail to predict real-world reliability. System evaluation must test the end-to-end pipeline, including prompts, RAG context, tool execution, multi-agent orchestration, and safety guardrails.
- **The Three Universal Data Units**: Structured evaluation requires **Golden** (pre-inference benchmark standards), **Test Cases** (structured post-inference execution records), and **Traces** (runtime telemetry for root-cause debugging).
- **The 5 D's of Dataset Quality**: Evaluation datasets must be **Demonstrative** (reflect real production logs). **Diverse** (clustered via embeddings), **Defined Scope** (subsystem unit tests), **Decontaminated** (isolated from model training data), and **Dynamic** (regularly updated).
- **Multi-Agent Orchestration Trade-offs**: Hierarchical orchestration (lead orchestrators directing worker agents) provides the optimal balance of accuracy, cost and scale. **Reflexive/self-correction loops** improve isolated reasoning but degrade quickly under concurrent volume due to exponential latency and compounding token costs.
- **The 5-Tier Evaluator Cascade**: Test outputs through a cost-effective cascade: Deterministic Code Checks (Level 1: JSON schemas, regex) -> Programmatic Heuristics (Level 2: latency/token bounds) -> NLI Entailment (Level 3) -> LLM-as-a-Judge Rubrics (Level 4) -> Human Expert Review (Level 5).
- **Statistical Calibration for LLM Judges**: Standard correlation metrics (like Krippendorff's alpha) fail on heavily skewed hallucination datasets. Use **Gwet's AC2** and **rank correlations (Spearman/Kendall Tau)** to calibrate LLM judges, and **Wilcoxon Signed-Rank Tests** with Benjamini-Hochberg corrections to compare competing system configurations.
- **Continuous Error Analysis Flywheel**: Deploy evaluation checks across five operational stages, Local Dev Unit Tests, Pre-Release Red Teaming, CI/CD PR Gates, Production Monitoring (5-10% traffic sampling), and Inline Safety Guardrails. Inspect failure traces using **Open & Axial Coding** to continuously enrich Golden datasets so resolved bugs never regress.

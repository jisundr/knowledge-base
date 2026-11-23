---
type: topic
tags: [ai-engineering, evaluation, glossary]
---

# LLM Evaluation Glossary

One-line definitions for terms used across the evaluation notes. Link to a term with `[[LLM Evaluation Glossary#Term|Term]]`.

## Benchmarks

### MMLU
Massive Multitask Language Understanding: multiple-choice knowledge test across ~57 subjects.

### GSM8K
~8.5K grade-school math word problems that require multi-step reasoning.

### HumanEval
Code-synthesis benchmark: write a function from a docstring, checked by unit tests.

## Latency and operations

### P95 latency
95th-percentile response time; 95% of requests are faster than this.

### TTFT
Time To First Token: latency until the first streamed token appears.

## Scorers and metrics

### BLEU
Bilingual Evaluation Understudy: n-gram precision against a reference (from translation).

### ROUGE
Recall-Oriented Understudy for Gisting Evaluation: n-gram overlap against a reference (from summarization).

### BERTScore
Similarity of contextual embeddings between output and reference tokens.

### NLI
Natural Language Inference: classifies whether one statement entails, contradicts, or is neutral to another. Used for factual-alignment checks.

### G-Eval
LLM judge that uses chain-of-thought to score against criteria, weighted by token probabilities.

### QAG
Question-Answer Generation: generate close-ended questions from the output, answer them against the source, and score the fraction correct.

### Stochastic
Outputs vary between runs because LLM sampling is probabilistic.

## Dataset methods

### LSH
Locality-Sensitive Hashing: hashes similar items into the same bucket for fast near-duplicate detection. Used, alongside embedding clustering, to check that dataset prompts are diverse.

## Statistics

### Gwet's AC2
Agreement coefficient for ordinal ratings, robust to skewed category prevalence where kappa and Krippendorff's alpha give paradoxically low scores.

### Spearman and Kendall Tau
Rank-correlation coefficients. Kendall counts concordant versus discordant pairs.

### Wilcoxon signed-rank test
Non-parametric paired test for comparing two systems scored on the same items.

### Benjamini-Hochberg
Procedure that controls the false discovery rate across many simultaneous tests.

## Security

### OWASP Top 10 for LLM Applications
OWASP's list of the top LLM security risks (prompt injection, sensitive information disclosure, and so on).

## Routing and inference

### Ex-ante quality estimation
Predicting how well a model will answer from the prompt alone, before generation. The basis of [[LLM Routing]].

### Post-hoc quality estimation
Scoring an answer after it is generated (confidence, log-probabilities, self-checks) to decide whether to escalate. The basis of [[LLM Cascading]].

### vLLM
Open-source, high-throughput LLM inference and serving engine.

### Dual-pool token routing
Splitting serving capacity into a high-concurrency pool for short requests and a deep-capacity pool for long ones, and routing each request by expected token usage.

### RouterBench
Benchmark for comparing LLM routers on answer quality versus cost.

### SWE-bench
Benchmark of real GitHub issues; a model must produce a patch that passes the repository's tests.

## Classical ML metrics and monitoring

### NDCG
Normalized Discounted Cumulative Gain: ranking metric that rewards relevant items placed near the top.

### SHAP
SHapley Additive exPlanations: attributes a prediction to input features using Shapley values from game theory.

### LIME
Local Interpretable Model-agnostic Explanations: fits a simple model around one prediction to explain it locally.

### Demographic parity
Fairness criterion: each group receives the positive outcome at the same rate.

### Equalized odds
Fairness criterion: true-positive and false-positive rates are equal across groups.

### KL divergence
Kullback-Leibler divergence: how much one probability distribution differs from a reference one (asymmetric). Used for drift detection.

### PSI
Population Stability Index: binned, symmetric measure of how much a variable's distribution has shifted between two samples; a common drift alarm.

## Related

- [[Evaluator Cascade]]
- [[LLM-as-a-Judge]]
- [[Evaluation Dataset Design (5 D's)]]
- [[AI System Evaluation]]
- [[LLM Routing]]
- [[Cascade Routing]]
- [[AI Evaluation System Pillars]]
- [[Model Drift Detection]]

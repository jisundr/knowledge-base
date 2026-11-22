---
type: playbook
status: draft
tags: [playbook, llm-routing, cost-optimization, inference, observability]
---

# Playbook - Adding Model Routing

Use when an LLM feature or agent sends every request to one model and you want to cut cost or latency. Outcome: each request goes to the cheapest model that answers it well enough, quality stays at the agreed bar, and the router is measured, not assumed. Pattern: [[LLM Routing]], [[LLM Cascading]], and [[Cascade Routing]], built in the order from [[LLM Routing in Production]].

## Trigger

- Model spend grows faster than traffic, or one frontier model handles all traffic.
- Latency targets fail because simple requests wait on a large model.
- A new, cheaper model becomes available and you want to use it without lowering quality.
- A provider outage or `429 Too Many Requests` takes the feature down.

## Principles applied

- **Build in stages**: add each stage only when the one before it is measured. Do not start with a trained router.
- **Cache before you route**: a cache hit costs no routing and no generation ([[Semantic Caching]]).
- **Quality bar first, savings second**: a route that saves money but fails the eval set is a regression.
- **Keep the hot path cheap**: the routing decision must take much less time than it saves (target: under 20 ms).
- **Measured, never estimated**: savings and quality come from logged traffic and the eval set.
- **Auditable always**: log the route, the reason, and any escalation for each request.

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Analyze traffic, draft rules and categories, run evals per model, run shadow mode, build the cost and quality report |
| Human does | Write the quality bar, review samples of cheap-model answers, check failure cases |
| Human decides | The quality bar, which stages to ship, thresholds, and promote or roll back |

## Stages

Add stages from top to bottom. Stop at the first stage that meets the cost and latency goals.

| Stage | What you add | Add it when |
| --- | --- | --- |
| 0 | Logging and a baseline: model, tokens, cost, latency, and quality score per request | Always, first |
| 1 | Failover: circuit breaker and a backup provider | Always; it protects availability, not cost |
| 2 | [[Semantic Caching]] in front of everything | Many requests repeat or paraphrase earlier ones |
| 3 | Rule-based routing (length, keywords, request type) | Traffic has clear easy and hard classes |
| 4 | Semantic routing (embedding distance to labeled categories) | Rules miss paraphrases, or there are many categories |
| 5 | [[LLM Cascading]]: cheap model first, escalate on a failed check | Difficulty cannot be read from the prompt |
| 6 | Predictive router trained on logged traffic and preference data (e.g. RouteLLM) | You have enough labeled traffic and stages 3-5 leave savings unused |
| 7 | [[Cascade Routing]]: predicted first model plus quality-based rerouting | You run three or more models and need the best quality per dollar |

Token-budget routing (short requests to a high-concurrency pool, long ones to a deep-capacity pool) is a serving-side option. Add it when you host models yourself and long requests block short ones ([[LLM Evaluation Glossary#Dual-pool token routing|dual-pool token routing]]).

## Steps

| # | Step | Owner (AI / Human / Decision) | Done when |
| --- | --- | --- | --- |
| 1 | Log every request for at least one week: prompt class, model, tokens, cost, latency, outcome | AI | The baseline report exists |
| 2 | Write the quality bar: the eval set, the scorer, and the minimum score per request class | Human | Each class has a number ([[AI System Evaluation]]) |
| 3 | Approve the quality bar and the cost and latency goals | **Decision** | Goals and approver are logged |
| 4 | Run the eval set on each candidate model | AI | A quality, cost, and latency table per model and class |
| 5 | Pick the next stage from the Stages table and build it behind a flag | AI | The stage runs in staging and logs its decisions |
| 6 | Run the stage in shadow mode: it decides a route, but production still uses the old model | AI | Predicted savings and the eval score per route are reported |
| 7 | Review a sample of requests that the stage sends to a cheaper model | Human | No class falls below its bar |
| 8 | Set thresholds (cache similarity, cascade confidence, router cutoff) | **Decision** | Thresholds and reasons are recorded in config |
| 9 | Release gradually ([[06 Releasing and Monitoring]]) | AI executes, Human watches | The stage serves a share of live traffic |
| 10 | Promote, hold, or roll back | **Decision** | Decision and reason are logged |
| 11 | Add failures to the eval set, then go back to step 5 for the next stage | AI | The eval set covers every escaped failure |

## Signals to watch

| Signal | Why |
| --- | --- |
| Cost per request and per class | The main goal |
| Quality score per route | Catches silent quality loss on the cheap path |
| Escalation rate (cascades) | A high rate means the cheap model is wrong too often; each escalation pays twice |
| Cache hit rate and wrong-hit rate | A loose threshold returns wrong answers |
| Provider cache-token share | A drop means something broke the prefix cache |
| Routing latency (p95) | A slow router cancels the gain |
| Share of traffic per model | Detects drift when traffic changes |
| Fallback and circuit-breaker trips | Provider health |

## Gates

1. Every route meets the quality bar for its class on the eval set.
2. Shadow mode shows savings at or above the goal.
3. Routing p95 latency is within budget.
4. Failover is tested: a forced provider error switches to the backup.
5. A human has reviewed a sample of cheap-path answers.

## Pitfalls

- **Starting with a trained router**: without logged traffic you have no data to train or check it. Start with rules and a cache.
- **Judging by averages**: the average score can hold while one class fails. Score per class.
- **Cache threshold too loose**: similar wording with a different meaning returns a wrong answer ("cancel my order" and "cancel my subscription").
- **Cascade on every request**: if most requests escalate, use a predictive first dispatch or route those classes straight to the larger model.
- **Self-checks that the small model always passes**: test the cascade check against known failures.
- **Stale routes**: a model update or new traffic changes which model is good enough. Rerun the evals when either changes.
- **Hidden rules**: routing logic in code that nobody can read. Keep rules and thresholds in config.
- **Breaking the prefix cache**: switching models mid-conversation, or putting timestamps and other changing values in the system prompt, makes every later turn pay full input price ([[Prefix Caching]]). Route per conversation, not per turn, for multi-turn agents, and keep the prompt prefix stable.

## Escalation

- A class falls below its bar in production: route that class to the larger model, then investigate.
- Savings stay below the goal after stage 5: check the share of hard traffic before building a trained router.
- A provider fails often: review the backup provider and contract limits with the platform owner.

## Related

- [[LLM Routing]]
- [[LLM Cascading]]
- [[Cascade Routing]]
- [[Semantic Caching]]
- [[Prefix Caching]]
- [[LLM Routing in Production]]
- [[Evaluator Cascade]]
- [[06 Releasing and Monitoring]]
- [[Playbook Template]]

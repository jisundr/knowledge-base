---
type: article-note
status: reviewed
created: 2026-11-23
tags: [incident-management, ai-engineering, evaluation, explainability, monitoring, sre, postmortem]
---

Sources:

* Paper: After-Action Review for AI (AAR/AI) (Dodge et al., ACM TiiS 2021, Oregon State University) [link](https://web.engr.oregonstate.edu/~burnett/Reprints/TIIS21_AARAI-accepted-preprint.pdf)
* Article: AI Incident Investigation: Automating Root Cause Analysis (ai4hse.com) [link](https://ai4hse.com/topics/incident-investigation/ai-incident-investigation)
* Article: Core Components of an AI Evaluation System (Walturn) [link](https://www.walturn.com/insights/core-components-of-an-ai-evaluation-system)
* Article: Post-Incident Review: Best Process and Free Template (Motadata) [link](https://www.motadata.com/blog/post-incident-review)
* Article: Post-Incident Review Template: Blameless PIR & Examples (All Quiet) [link](https://allquiet.app/blog/post-incident-review-template)
* Article: Post-Incident Review Template: Free PIR & Postmortem Examples (Runframe) [link](https://runframe.io/blog/post-incident-review-template)
* Article: The AI Incident Report Template I Actually Use for Wrong Answers and Tool Failures (optyxstack, DEV Community) [link](https://dev.to/optyxstack/the-ai-incident-report-template-i-actually-use-for-wrong-answers-and-tool-failures-174l)
* Article: What Is AI-generated incident report? Definition & Examples (nhimg.org) [link](https://nhimg.org/glossary/ai-generated-incident-report/)

When a critical system fails, or an AI model makes an unexpected misstep, what actually changes ninety days later? Too often, organizations pay for the exact same failure twice because incident reviews devolve into superficial paperwork theater where reports are filed away and forgotten.

To break this cycle, modern teams are pairing AI-driven automation with structured, human-centered evaluation frameworks. By the end of this lesson, you will be able to:

- Identify key operational areas where AI accelerates incident investigations while maintaining compliance and human accountability boundaries.
- Evaluate AI agent decisions using the After-Action Review for AI (AAR/AI) framework to contrast Model-Based and Model-Free explanations.
- Construct a comprehensive AI evaluation and incident reporting system that captures model drift, bias, and request-level diagnostic evidence.
- Execute blameless Post-Incident Reviews (PIRs) that convert system failures into time-bound, verifiable action items.

# The New Frontier: Automating Root Cause Analysis with AI

Imagine an incident investigator stepping onto a site: instead of taking manual notes and spending hours at a desktop drafting administrative forms, they dictate voice notes directly into an AI assistant. Generative AI tools are fundamentally reshaping Health, Safety, and Environment (HSE) as well as IT operations by handling the most labor-intensive phases of investigation.

AI adds immediate productivity value across key operational touchpoints:

- **Voice-to-Text Capture:** Converts field witness interviews into searchable, time-stamped transcripts in minutes, supporting multilingual translation for diverse workforces.
- **Automated Report Drafting:** Maps unstructured notes directly into standard compliance fields like OSHA Form 301 or ISO 45001.
- **ICAM & 5 Whys Frameworks:** Analyzes narrative text to suggest potential contributing factors across organizational, environmental, and individual action categories.
- **Cross-Site Pattern Detection:** Scans historical incident databases to identify hidden correlations across shifts, equipment models, weather conditions, or specific locations.

Early adopters report a **60–80% reduction in drafting time** and a **2–3× increase in near-miss reporting** when voice capture replaces complex paperwork. However, incorporating AI into safety and operational workflows introduces crucial regulatory boundaries.

Regulators such as **OSHA**, the **UK Health and Safety Executive (HSE)**, and **ISO 45001** standards permit AI-assisted reporting provided a competent human investigator validates the output and signs the report. Under the **EU AI Act**, occupational safety AI tools acting as administrative assistants are classified as 'limited risk', but high-risk classifications apply if the AI autonomously makes decisions affecting worker safety or discipline. Furthermore, privacy standards like **GDPR** require strict data minimization, transient processing (ensuring input data is not retained to train vendor models), and robust encryption at rest and in transit.

Crucially, AI acts as a productivity multiplier rather than a decision-maker. Final root-cause analysis, sensitive witness interviews, fatality investigations, and ethical judgments regarding accountability must remain strictly human responsibilities.

# Evaluating AI Decisions: The After-Action Review for AI (AAR/AI)

As AI agents are increasingly entrusted with complex, sequential decision-making—from autonomous vehicles to real-time resource allocation—how do human experts evaluate whether an AI agent is behaving safely and logically?

To solve this, researchers adapted a U.S. Army debriefing method called the **After-Action Review (AAR)** into **AAR/AI**. Designed for domain experts, AAR/AI guides a human assessor through a structured 'inner loop' of questions to systematically evaluate an intelligent agent's rationale:

- **Review what was supposed to happen:** What did the evaluator expect the AI to execute in the next decision point?
- **Identify what actually happened:** What actions did the agent select, and what immediate state changes occurred?
- **Examine why it happened:** Why did the AI choose those actions, based on its underlying explanations?
- **Formalize learning:** Would the evaluator permit the AI to make this category of decisions autonomously in the future, or are specific policy modifications required?

A central discovery of AAR/AI research is that the **type of explanation** provided by the AI profoundly impacts human evaluation and cognitive load. Explanations generally fall into two architectural categories:

**Model-Free Explanations:** These present a simple 'search stump' showing available actions paired with a single numerical value score. While easy to read, Model-Free explanations limit the human assessor to high-level strategy disagreements without revealing _why_ the model assigned those scores.

**Model-Based Explanations:** These expose a deeper search tree displaying predicted future states, opponent/environmental counter-actions, and heuristic evaluation values at leaf nodes.

Model-Based explanations empower human evaluators to perform **empirical falsification**. By inspecting future state projections, assessors can catch specific logic bugs—such as incorrect predictions of opponent moves or flawed state assessments—and disprove the agent's internal reasoning path. Although Model-Based explanations increase initial mental demand, they significantly foster deeper metacognition and higher-quality bug reporting.

# Core Components of a Defensible AI Evaluation System

To ensure AI models operate reliably in production without introducing bias, inaccuracy, or operational risk, engineering teams build dedicated **AI Evaluation Systems**. A robust evaluation architecture extends beyond basic accuracy scores to systematically analyze model health across six core pillars:

- **Quantitative Performance Metrics:** Measuring task-specific efficacy using precision, recall, and F1-score for classification; Mean Squared Error (MSE) for regression; or NDCG for ranking.
- **Robustness & Generalization:** Testing models against out-of-distribution datasets, adversarial input perturbations, and stress scenarios to ensure models do not merely memorize training data.
- **Bias & Fairness Assessments:** Evaluating outcomes across demographic cohorts using metrics like demographic parity and equalized odds to prevent discriminatory automated decisions.
- **Explainability & Interpretability:** Integrating feature importance tools like **SHAP** (Shapley Additive Explanations) and **LIME** (Local Interpretable Model-Agnostic Explanations) to unpack black-box model predictions for end-users and auditors.
- **Continuous Monitoring & Drift Detection:** Tracking model degradation post-deployment. Monitoring tools detect **concept drift** (changing relationships between inputs and output labels), **data drift** (shifts in statistical properties of input features), and **prediction drift** using statistical algorithms like KL Divergence or Population Stability Index (PSI).
- **Request-Level Evidence Capture:** When production AI models fail (e.g., hallucinated outputs, RAG retrieval misses, or tool parsing errors), vague descriptions like 'the model got weird' hinder debugging. Incident logs must capture exact versioned parameters, including request IDs, prompt versions, active retrieval index versions, tool schema definitions, and model policy versions.

By integrating these components into automated Continuous Integration/Continuous Deployment (CI/CD) pipelines while retaining **Human-in-the-Loop (HITL)** oversight for complex edge cases, organizations establish audit-ready AI governance

# Running Blameless Post-Incident Reviews (PIRs) that Work

Whether managing a production outage or analyzing an operational safety breach, the ultimate goal of incident management is ensuring an organization never pays for the exact same failure twice. In Site Reliability Engineering (SRE) and ITIL practices, this lookback is called a **Post-Incident Review (PIR)** or **Incident Postmortem**.

A PIR must be strictly **blameless**. When postmortems assign personal fault, responders naturally conceal critical details, depriving the organization of the exact information required to harden the system.

Putting blameless culture into practice relies on six structural mechanics:

- **Ask how it made sense at the time:** Reconstruct the local rationality of responders based on the information and dashboard signals available during the event.
- **Treat human error as the starting point:** Human error is a symptom of system design flaws, inadequate guardrails, or alert fatigue—not the root cause.
- **Ban counterfactual language:** Avoid accusatory phrases like 'should have', 'failed to', or 'neglected to'. Stick strictly to factual chronologies.
- **Separate narrative roles from action owners:** Refer to 'the on-call engineer' in the timeline narrative, but assign specific named individuals in the action item registry.
- **Maintain an independent facilitator:** Use a neutral facilitator from an adjacent team to ask probing, naive questions without sounding like a cross-examination.
- **Firewall reviews from performance evaluations:** Ensure PIR discussions and documents are never cited in annual employee reviews.

When tracing contributing factors, rely on multi-branching analysis rather than a single linear chain. A complete PIR generates verified action items balanced across four functional categories:

- **Prevent:** Structural changes to stop recurrence (e.g., automated config validation).
- **Detect:** Observability improvements to catch issues earlier (e.g., lowering alert thresholds).
- **Mitigate:** Process enhancements to speed up recovery (e.g., automated rollback scripts).
- **Learn:** Knowledge sharing across teams (e.g., publishing updated runbooks).

To ensure follow-through, every action item must have a single named owner, live in the team's primary task tracker, be sized for completion within 30 days, and undergo a formal 30-day closure review.

# Key Takeaways:

- **AI is an Assistant, Not an Auditor:** AI drastically cuts report drafting time and surfaces hidden patterns, but regulatory frameworks (OSHA, ISO 45001, EU AI Act) require competent human sign-off and strict data privacy compliance.
- **Model-Based Explanations Enable Falsification:** Evaluating AI agents with search-tree explanations (AAR/AI) allows assessors to inspect predicted future states, catch underlying logic errors, and audit model reasoning.
- **Comprehensive AI Governance Requires Continuous Monitoring:** Robust AI evaluation demands tracking performance metrics, testing for demographic bias, applying SHAP/LIME interpretability, and monitoring for concept and data drift.
- **Specific Request-Level Evidence is Mandatory:** Debugging probabilistic AI failures requires logging versioned parameters, including prompt versions, retrieval index states, tool schemas, and request IDs.
- **Blameless PIRs Change Systems, Not People:** Effective postmortems ban counterfactual language, explore multi-branch contributing factors, and track small, time-bound action items across Prevent, Detect, Mitigate, and Learn categories.

See [[AI-Assisted Incident Investigation]], [[After-Action Review for AI (AAR-AI)]], [[Model-Based vs Model-Free Explanations]], [[AI Evaluation System Pillars]], [[Model Drift Detection]], [[Request-Level Evidence Capture]], [[Blameless Post-Incident Review (PIR)]], [[PIR Action Items (Prevent, Detect, Mitigate, Learn)]], [[Incident Investigation Glossary]], [[LLM Evaluation Glossary]], [[AI System Evaluation]]

---
type: topic
tags: [ai-engineering, ai-agents, frontend, context-engineering]
---

# Visual Element Annotation for Agents

Point at UI instead of describing it. In a browser next to the code, you click an element on the running app and the tool attaches its HTML, computed CSS, selector, and a screenshot to the agent prompt.

- Removes ambiguity like "the button on the right" by giving the agent exact structural targets.
- Annotations can be queued and sent as one batch, each marked as a **command** (do this) or a **question** (suggest an improvement).

Orca calls this Design Mode with Element Select; see [[Agent Development Environment (ADE)]].

## Related

- [[Context Engineering]]
- [[Agent Verification Stack]]

## Sources

- [[20261123172458 Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE|Mastering AI Agent Orchestration - Building Software Factories with Grok Bot and Orca ADE]]

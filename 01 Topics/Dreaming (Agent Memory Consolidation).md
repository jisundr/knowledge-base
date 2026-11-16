---
type: topic
tags: [ai-engineering, ai-agents, memory]
---

# Dreaming (Agent Memory Consolidation)

An asynchronous, out-of-band batch process that reviews agent fleet activity and proposes updates to the shared memory store. Decouples task execution from memory curation.

## How it works

- Runs off-peak with a dedicated token budget.
- An **orchestrator agent** gathers recent session transcripts, tool logs, and metadata.
- It spawns **sub-agents** to analyze transcripts against the current memory store and find systemic failures or gaps.
- It synthesizes findings into concrete add/modify/delete proposals, with prevalence stats and transcript excerpts so a human can approve.

## Example fixes

- Missing domain knowledge: add the guide every agent lacked.
- Misused tool parameter (e.g., radians vs. degrees): fix tool instructions.
- Fleet-wide style errors (e.g., overusing em dashes): add explicit style rules.

## Why

Fixes in-band limits (split focus, narrow visibility) described in [[Agent Memory]], and enables pruning stale notes. Writes should be protected by [[Memory Guardrails for Multi-Agent Systems]].

## Related

- [[Context Engineering]]
- [[AI Agents and Tool Use]]

## Sources

- [[Lamis Mukta - Learning while you sleep - Beyond memory to dreaming - AI Native DevCon June 2026]]

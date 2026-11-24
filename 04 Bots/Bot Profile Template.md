---
type: bot
status: draft
tags: [bot, template]
owner: <name>
---

# Bot - <Name>

One line: the single job this bot does and where it runs. Profile follows [[06 Using Bots]] (Agent profile) and [[Agent Design Foundation]].

**Owner**: named human who reviews its output and keeps this file current.

**How to start it**: the trigger or the exact prompt that starts a run.

## Goal and tasks

The one job, then the sub-tasks in order.

## Instructions

How the bot reads inputs, picks tools, and reports. Numbered steps.

## Voice

Tone for anything a human reads.

## Tools

Exact repos, APIs, and [[Model Context Protocol (MCP)|MCP]] servers it may use. Read-only where possible.

## Anti-jobs

What it must never do ([[Agent Anti-Jobs]]).

## Guardrails

Controls that enforce the anti-jobs outside the model ([[Deterministic Guardrail Policies]], [[Human-in-the-Loop Approval Gates]]). A prompt alone is not a control.

## Autonomy level

Where it sits on the [[AI Work Autonomy Spectrum]]. Start at PR-only. Record which change types may auto-merge, with the evidence.

## Escalate to the owner

Conditions that stop the run and go to a human.

## Related

- [[06 Using Bots]]

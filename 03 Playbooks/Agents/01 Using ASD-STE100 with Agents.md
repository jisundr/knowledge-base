---
type: playbook
status: draft
tags: [playbook, ai-agents, controlled-language, prompting]
---

# Playbook - Using ASD-STE100 with Agents

Use when you set up an agent, or a stage in an agentic pipeline, that produces text. Outcome: the agent writes short, direct text with one meaning, at the lowest strictness that does the job, and you can check that it does. Pattern: [[Simplified Technical English (ASD-STE100)]], applied partly ([[80% ASD-STE100 Prompting]]) or through a skill ([[SimpleEnglish Agent Skill]]).

## Trigger

- You add a new agent or a new agent profile (`.github/agents/<name>.md`, a kairyn stage, a sub-agent).
- You write or update an agent instruction file (`AGENTS.md`, `CLAUDE.md`, a skill, a system prompt).
- An agent's output is too long, hedged, or uses different words for the same thing.

## What it applies to

| Agent text | Why one meaning matters |
| --- | --- |
| **Output the agent writes**: error messages, runbooks, release notes, incident summaries, acceptance criteria, PR descriptions, commit messages | A person or another agent acts on it |
| **Handoffs between agents**: stage outputs such as `REQUIREMENTS.md`, `DESIGN.md`, `BUILD.md` | The next agent reads it as its input; vague text becomes a wrong action |
| **Instructions the agent reads**: `AGENTS.md`, `CLAUDE.md`, skills, agent profiles | Short, direct rules leave less room for the model to guess |

Do **not** turn it on for agents that write marketing copy, blog posts, or other text where tone and persuasion matter more than one meaning.

## Principles applied

- **Name the standard, do not restate it**: models already know ASD-STE100, so one line replaces pages of style rules.
- **One word, one meaning**: the agent uses the same term for the same concept every time ([[Ubiquitous Language]]).
- **Lowest strictness that works**: full compliance reads as robotic. Go stricter only when a wrong reading is costly.
- **Same bar for every agent**: set the level in config, not in each prompt.
- **Measured, never assumed**: check agent output with a linter or an evaluator, not by feel.

## Pick a strictness level

| Level | How you wire it in | Use for |
| --- | --- | --- |
| 0 | Nothing | Agents that write marketing or persuasive text |
| 1 | One line in the system prompt or instruction file: "Follow ASD-STE100 about 80% of the way." | Most agents: chat answers, PR descriptions, release notes, stage handoffs |
| 2 | Load an agent skill (e.g. `AminBlg/SimpleEnglish`) | Agents that produce one text type often: error messages, runbooks, instruction files |
| 3 | Full ASD-STE100 (approved vocabulary, hard length limits) in the agent profile | Agents that write safety-critical or step-by-step procedures |

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Write output at the configured level, self-check against the checklist, report remaining violations |
| Human does | Sample agent output and read for lost meaning, nuance, or wrong terms |
| Human decides | The level for each agent, and whether to change it after measurement |

## Steps

| # | Step | Owner (AI / Human / Decision) | Done when |
| --- | --- | --- | --- |
| 1 | List the agent's text outputs and who reads each (a person or another agent) | Human | Each output is classified, or the agent is Level 0 |
| 2 | Pick the level for the agent | Decision | Level is recorded in the agent profile |
| 3 | Wire it in: add the line to the system prompt or instruction file, or load the skill | Human | The config change is committed |
| 4 | Rewrite the agent's own instruction file in ASD-STE100 (Level 1) | AI | Instructions pass the checklist |
| 5 | Run the agent on sample tasks and check output against the checklist (linter or LLM evaluator) | AI | Violations are counted per 100 words |
| 6 | Sample the output for lost meaning | Human | No dropped conditions, limits, or real uncertainty |
| 7 | Add the checklist to the agent's eval set so regressions show up | AI | Check runs with the other evals |

## Checklist (agent output must pass)

Use this as a linter spec or an evaluator rubric.

- [ ] Sentences: at most 20 words for an instruction, 25 for a description.
- [ ] Paragraphs: at most 6 sentences.
- [ ] Active voice. The actor is named.
- [ ] One instruction per sentence. Steps are numbered.
- [ ] No hedges (*should*, *would*, *might*, *may*). Instructions are direct, or the condition is stated: "If X, do Y."
- [ ] No trailing `-ing` phrases.
- [ ] Same term for the same concept, matching the project glossary.
- [ ] No filler ("in order to", "it is important to note that", "basically").

## Config snippets

System prompt or `AGENTS.md` / `CLAUDE.md` (Level 1):

```text
Write all output in ASD-STE100, about 80% of the way.
Use the terms in the project glossary. Do not use synonyms for them.
```

Agent profile for an error-message or runbook agent (Level 2):

```text
Load the SimpleEnglish skill.
Error messages: say what failed, why, and the one action the user must do next.
Runbook steps: numbered, one action per step, active voice, max 20 words per step.
```

Stage handoff (e.g. a kairyn stage output):

```text
Write <STAGE>.md in ASD-STE100, about 80% of the way. The next agent reads this file as its only input.
```

## Measure it

When you turn on a level for an agent, run a sample of tasks with and without it:

1. **Violations per 100 words** from a linter. Regex linters undercount (they often miss passive voice), so treat the number as a floor.
2. **Output tokens**: shorter output also cuts cost and latency.
3. **Blind pairwise judge**: show both versions in both orders and ask which is clearer. Use a judge from a different model family if you can (see [[LLM-as-a-Judge]]).

## Gates

1. The agent's level is recorded in its profile.
2. Sample output passes the checklist, or each remaining violation has a reason.
3. A human confirms no meaning was lost on a sample (Level 2 and up, or any agent whose output a customer reads).

## Where it plugs into the SDLC playbooks

- [[01 Handling New Requirements]]: the requirements agent writes acceptance criteria (Level 1).
- [[03 Building a Task]]: the build agent writes PR descriptions and commit messages (Level 1).
- [[06 Releasing and Monitoring]]: the release agent writes release notes and incident summaries (Level 1 or 2).
- Every stage: handoff files and agent profiles in `.github/agents/*.md` (Level 1).

## Pitfalls

- **Turning it on everywhere**: an agent that writes blog posts or sales emails reads cold under strict STE.
- **Losing real uncertainty**: the agent removes "may" and turns "this may fail on Windows" into a false fact. The rule is: keep it as a condition ("This can fail on Windows. If it fails, do X.").
- **Synonym drift**: the agent swaps "deploy" for "release" or "ship". Give it the glossary.
- **Trusting the linter alone**: a low score does not prove the output is correct. A human still samples for meaning.
- **Per-prompt copies**: pasting the rule into every prompt drifts. Set it once in the instruction file or agent profile.

## Escalation

- Output keeps failing the meaning check: the agent's input is unclear. Fix the upstream spec, design, or handoff first.
- The level feels wrong for an agent: measure again, then change it in the profile with a recorded reason.

## Related

- [[Simplified Technical English (ASD-STE100)]]
- [[80% ASD-STE100 Prompting]]
- [[SimpleEnglish Agent Skill]]
- [[AI Output Ladder]]: ASD-STE100 is Tier 1 (clean text).
- [[Context Engineering]]
- [[Ubiquitous Language]]
- [[Playbook Template]]

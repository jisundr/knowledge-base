---
type: topic
tags: [ai-engineering, ai-agents, agent-skills, context-engineering]
---

# Agent Skills

A skill is a folder that gives a general-purpose agent one specialized capability. It holds instructions, metadata, and optional scripts and reference files. Skills replace one large system prompt with small capabilities that load on demand. The format is an open specification (agentskills.io) that Anthropic, Microsoft Agent Framework, Google Cloud, and several coding agents support.

## Build skills, not agents

The thesis of Anthropic's Barry Zhang and Mahesh Murag ("Don't Build Agents, Build Skills Instead", AI Engineer Code 2025): stop building a new custom agent for each domain. Run **one general-purpose agent** and give it **skills** for each domain. The gap is expertise, not intelligence.

- **One loop to maintain**: the agent loop, tools, and harness are built once; domain know-how lives in skill folders.
- **Composable**: one agent can combine several skills in a single task.
- **Cheap to add**: a new capability is a folder of Markdown and scripts, not a new agent with its own prompt, tools, and deployment.
- **Shareable and versioned**: skills sit in git and work across agents that support the open spec.

### Evidence that it is a trend

- Anthropic published the standard in December 2025 and donated it to the Agentic AI Foundation (Linux Foundation) in October 2026. By then, Anthropic says, more than 70 agent platforms had integrated it, including ChatGPT, Cursor, GitHub Copilot, and VS Code, with 1 million skills published and nearly 280 million installs. These are Anthropic's own figures.

### Caveats

- **Not "skills instead of agents" everywhere**: many practitioners frame it as *agents with skills*. Separate agents still make sense for isolated context, different permissions or autonomy settings, parallel work ([[Multi-Agent Orchestration Patterns]]), or tight product integration.
- **Quality varies**: in SkillsBench (84 tasks, 11 domains), curated skills raised the average pass rate by 16.2 points, but self-generated skills gave no average benefit. Gains ranged from 4.5 points in software engineering to about 52 in healthcare. Small, focused skills beat long documentation.
- **Realistic conditions**: a study of about 34,000 real-world skills reported that skills barely helped in realistic settings, and weaker models did worse with them (reported by The Decoder; paper not checked).
- **Security**: one study found that 26.1% of 31,132 community skills had at least one exploitable vulnerability.

Mental model: the model is the processor, the agent runtime is the operating system, and skills are the apps. You do not open every app to send one text message.

## Folder layout

```
expense-report/
├── SKILL.md        # required: frontmatter + instructions
├── scripts/        # executable code; only its output enters context
├── references/     # docs read on demand (e.g., FORMS.md)
└── assets/         # templates, images, data files
```

Keep file references **one level deep** from `SKILL.md`. Do not build chains of references to references.

## SKILL.md frontmatter (open spec)

| Field | Required | Rule |
| --- | --- | --- |
| `name` | yes | 1-64 chars, lowercase letters, digits, hyphens. No leading or trailing hyphen, no `--`. Must match the folder name. |
| `description` | yes | 1-1024 chars. Says **what** the skill does and **when** to use it, with the words a user would actually type. |
| `license` | no | License name or a bundled license file. |
| `compatibility` | no | 1-500 chars. Only for real environment needs (e.g., "Requires python3"). |
| `metadata` | no | String-to-string map. |
| `allowed-tools` | no | Experimental. Space-separated pre-approved tools; support varies by agent. |

**Platform extras**: the Claude platform also bans the reserved words `anthropic` and `claude` in `name`. That rule is Claude's, not the open spec's.

## Size budget

- Metadata: about 100 tokens per skill, always loaded.
- Body: under 5,000 tokens recommended; the open spec also says under 500 lines.
- Move long manuals into `references/`.

## Scripts as reusable tools (DRY)

Agents tend to rewrite the same script on every run, which wastes tokens and invites errors. Once a script works, save it in `scripts/` and have the skill call it. Deterministic code also avoids LLM math and formatting errors.

## Learning from corrections

When you correct the agent during a task, write the fix into the skill (instructions or a script), so the next run starts from the corrected version. Review these changes yourself: SkillsBench found that skills the model writes for itself, without review, give no average benefit.

A related habit: after you walk a bot through a new workflow, ask it to write the procedure up as a skill (inputs, steps, what a correct result looks like) and store it in a private git repo, so the bot stays consistent. The same review rule applies.

## Security

Skills can run code. Keep tool approvals on by default: auto-approve read-only actions if needed, but run scripts in a sandbox with restricted network access. Only install skills from sources you trust, and read a community skill before you install it.

## Related

- [[Progressive Disclosure]]: how skills load in stages.
- [[Progressive Disclosure Depth (Flat vs Hierarchical)]]
- [[Context Loading Patterns]]
- [[Self-Verification Loop]]
- [[Context Pointers]]
- [[Context Engineering]]
- [[SimpleEnglish Agent Skill]]: an example skill with a benchmark.
- [[Home Repo Pattern]]: where to version shared skills.
- [[Agent Design Foundation]]
- [[Agent Script Migration]]

## Sources

- [[20261122181902 Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks|Mastering Agent Skills & Progressive Disclosure -Architecture, Patterns, and Benchmarks]]
- [[20261123181254 Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance|Mastering the AI Bot Fleet - Design, Workflow Integration, and Enterprise Governance]]

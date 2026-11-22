---
type: playbook
status: draft
tags: [playbook, agentic-sdlc, product-discovery, shaping, backlog]
---

# Playbook - Managing the Idea Backlog

Stage 0, before [[01 Handling New Requirements]]. Use for raw ideas and requests that are not yet work: a stakeholder ask, a meeting outcome, a workaround someone noticed, a "we should…" from an engineer or an agent. Outcome: each idea is either dropped, parked with a review date, or shaped into a bounded pitch that a human commits to and hands to stage 1. Pattern: [[Agentic SDLC]] (agents start on execution, humans make the decision).

The team owns this stage even when the product function is weak: engineers act as [[Product-Minded Engineer|product-minded engineers]] and turn solution-shaped requests back into problems before anything is built.

## Trigger

- A new idea or request arrives from anywhere (chat, meeting, ticket, support, an agent's finding).
- The weekly triage slot comes round.
- An idea's review date passes.

## Principles applied

- **The backlog holds options, not commitments.** Nothing in it is promised. Work becomes committed only at step 8, by a human.
- **Problem first.** An idea enters as whatever was said, but leaves as a problem with evidence ([[Problem-First Thinking]]). Agents never build from a solution-only request.
- **Shape before you build.** Fix the appetite, then cut scope to fit ([[Shaping (Shape Up)]]).
- **Context lives where agents can see it.** One record per idea, in the tracker's triage inbox or in the repo (`docs/ideas/`), not in chat.
- **Human as judgment.** Agents capture, deduplicate, research, and draft. Humans triage, set appetite, and commit.
- **Auditable.** Every keep, park, drop, and commit decision is recorded on the idea with who made it.
- Removes the two failure modes of a raw backlog: the endless list nobody reads, and the "feature commandant" pipe that sends unshaped asks straight to build.

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Capture verbatim, deduplicate and cluster, draft problem statements, search the repo and tracker for evidence and rabbit holes, draft pitches, flag stale ideas |
| Human does | Supply context, talk to requesters, sketch the solution at fat-marker level, check the [[Four Big Product Risks]] |
| Human decides | Keep, park, or drop; the appetite; whether to commit a shaped pitch |

The deciding humans are ideally a [[Product Trio]]. Without a PM, the tech lead and one engineer take the product seat for the decision and record who did.

## Idea record

The minimum fields. Keep it one short file or ticket per idea.

| Field | Content |
| --- | --- |
| Title | Short, problem-flavoured if possible |
| Raw request | Verbatim, unedited, with a link to where it came from |
| Requester and date | Who asked, when |
| Problem | Who has what pain, and how we would know it decreased |
| Evidence | Workarounds, tickets, metrics, quotes; links to duplicates merged in |
| Status | `inbox` → `triaged` → `shaping` → `shaped` → `committed`, or `parked` / `dropped` |
| Appetite | Small batch or big batch (set at step 5) |
| Review by | Date after which a parked idea is dropped unless renewed |

## Steps

| # | Step | Owner | Done when |
| --- | --- | --- | --- |
| 1 | **Capture** the idea verbatim with its source and requester | AI or Human | Record exists with status `inbox` |
| 2 | **Deduplicate and cluster**: link to similar ideas and existing work, merge evidence | AI | Duplicates merged; related ideas linked |
| 3 | **Reframe as a problem**: who hurts, why it matters, what evidence exists, and how we would know it improved | AI draft, Human confirms | Problem statement stands without naming a solution |
| 4 | **Triage**: keep, park (set a review date), or drop (record why) | **Human decides** | No idea in `inbox` older than one triage cycle |
| 5 | **Set the appetite**: the most time this idea is worth | **Human decides** | Appetite recorded; it is a budget, not an estimate |
| 6 | **Shape**: rough elements at breadboard and fat-marker level; agent searches the code for feasibility and rabbit holes; list no-gos | Human, with AI research | Elements fit the appetite; rabbit holes resolved or cut |
| 7 | **Write the pitch**: problem, appetite, solution elements, rabbit holes, no-gos, risks with owners | AI draft, Human edits | Someone outside the shaping session could understand it |
| 8 | **Commit**: choose which shaped pitches to take on next | **Human decides** | Pitch handed to [[01 Handling New Requirements]] as its request; status `committed` |
| 9 | **Prune**: flag parked ideas past their review date | AI flags, **Human decides** | Each flagged idea renewed with a new date or dropped |

Steps 1 to 3 run continuously. Steps 4, 8, and 9 run in a fixed triage slot (for example weekly), so decisions are batched and visible. Steps 5 to 7 run only for ideas that were kept.

## Gates

Before a pitch is committed (step 8):

1. **Problem first**: the pitch states a problem and evidence, not only a solution.
2. **Risks covered**: value, usability, feasibility, and viability each addressed or given an owner.
3. **Bounded**: appetite set; rabbit holes and no-gos listed.
4. **Decided**: commitment recorded with who decided. Same bar whether a person or an agent drafted the pitch.

## Agent profile

Sketch for an `idea-triager` agent (`.github/agents/idea-triager.md` in a repo, or a kairyn stage later):

- **Role**: keep the idea backlog clean and ready for human decisions. Never decide priority, appetite, or commitment.
- **Inputs**: new idea records, the existing backlog, the repo, and the tracker.
- **Does**: steps 1 to 3, research for step 6, the draft for step 7, flags for step 9.
- **Output**: updated idea records and a short triage digest for the human slot: new ideas, proposed merges, draft problem statements, stale ideas.
- **Rules**: quote the raw request verbatim; mark every inference; ask the requester, not the model, when the problem is unclear.

## Audit trail

- Each status change, with who made it and why (especially drops and commits).
- Merges between ideas, so evidence is not lost.
- The appetite and the pitch version that was committed.

## Pitfalls

- **Backlog as promise list.** Requesters read "in the backlog" as "coming soon". Say "option" and use review dates.
- **Solution-first tickets straight to agents.** Agents build the wrong thing faster. Step 3 is not optional.
- **Over-shaping.** Wireframes and pixel detail at this stage remove room for the builders. Stay at breadboard and fat-marker level.
- **Estimates instead of appetite.** Asking "how long?" invites scope to grow; asking "how much is this worth?" makes scope fit.
- **No expiry.** Without review dates the backlog grows until nobody reads it.
- **Agent deciding priority.** Agents can score and summarise; humans commit.

## Escalation

- An idea is urgent and cannot wait for the triage slot: one deciding human can commit it, and records why.
- A requester disputes a drop: bring the problem statement and evidence to the next triage slot, not the original solution.
- Shaping cannot fit the appetite: cut scope, raise the appetite (human decision), or park the idea.

## Related

- [[Agentic SDLC]]
- [[01 Handling New Requirements]] (next stage)
- [[Problem-First Thinking]]
- [[Shaping (Shape Up)]]
- [[Product Trio]]
- [[Four Big Product Risks]]
- [[Product-Minded Engineer]]
- [[Product Discovery Glossary]]
- [[Grilling Session]]: another way to reach a shared concept before the spec
- [[Playbook Template]]
- [kairyn](https://github.com/jisundr/kairyn): runnable stages that implement playbooks (no stage for this one yet)

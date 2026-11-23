---
type: playbook
status: draft
tags: [playbook, quality, ci, agentic-sdlc, kairyn]
---

# Playbook - Running Quality Gates

Stage 4 after [[03 Building a Task]]. Use when a PR is open. Outcome: the PR passes a fixed, ordered chain of gates, so standards are built in rather than remembered. Pattern: sequential CI quality gates from [[Agentic SDLC]] (Levi Strauss).

## Trigger

- A PR is opened or updated.

## Principles applied

- **Same bar for agents and humans**: identical gates for every PR.
- **Standards built in, not remembered**: gates run automatically.
- **Measured, never estimated**: performance numbers come from real runs.
- **Auditable always**: each gate result is logged on the PR.

## Roles

| Role | Responsibilities |
| --- | --- |
| AI does | Run each gate, report evidence, propose an autofix as a labeled commit on failure |
| Human does | Judge whether a flagged item is a true problem |
| Human decides | Accept an autofix, or waive a gate (with a recorded reason) |

## Steps

Gates run in this order. Security is last so it audits the final code, including fixes from earlier gates.

| # | Gate | What is checked | Done when |
| --- | --- | --- | --- |
| 1 | Testing | Business logic, regression suite, end-to-end tests (e.g. Playwright) | Suite green; each acceptance criterion has a passing test |
| 2 | Contract | For changes to a shared API: contract tests against callers, or drift detection across repos ([[Contract-Driven Workspace]]) | No caller breaks; breaking changes notify every dependent repo |
| 3 | Accessibility | WCAG 2.2 AA in a headless browser | No AA violations |
| 4 | Performance | Core Web Vitals, measured | Metrics within budget |
| 5 | Observability | Telemetry and monitoring present for the new behavior | Missing instrumentation added |
| 6 | Security | OWASP Top 10, known CVEs, leaked secrets | No unresolved findings |

(Levi Strauss ran observability last before security; keep security last whatever else you reorder.)

Within each gate, run computational checks (tests, scanners, linters) before inferential ones (AI review, [[LLM-as-a-Judge]]). Computational checks are cheap, fast, and exact; keep inferential checks for what they cannot judge, such as fit to requirements ([[Feedforward Guides and Feedback Sensors]]).

## On failure

1. The agent investigates the break and writes a targeted fix.
2. The fix lands as a **labeled commit** on the PR, never a force-push.
3. A human reviews the autofix. Re-run the failed gate and every gate after it.

## kairyn stage sketch

- **Inputs**: `STATE.md`, `DESIGN.md`, `BUILD.md`, the PR
- **Output**: `docs/tasks/<date>-<slug>/GATES.md` (result and evidence per gate, autofixes applied, waivers with reasons)
- **Exit criteria**: all gates pass or have a human-recorded waiver
- **State update**: `gates: done`, advance `stage` to `review`, append log line

## Pitfalls

- Running security before the other gates, then auditing stale code.
- Estimating performance instead of measuring it.
- Waiving a gate without a recorded reason.
- Accepting autofixes unread.
- Trusting mocked caller tests: they pass after a contract break, and the failure shows up as live 404s. The contract gate catches it.

## Escalation

- Repeated failures on the same gate: the design may be wrong; go back to [[02 Designing a Solution]].
- A gate is flaky: fix the gate, do not ignore it.

## Related

- [[Agentic SDLC]]
- [[Agent Verification Stack]]
- [[Contract-Driven Workspace]]
- [[03 Setting Up a Home Repo]]
- [[Feedforward Guides and Feedback Sensors]]
- [[Playbook Template]]

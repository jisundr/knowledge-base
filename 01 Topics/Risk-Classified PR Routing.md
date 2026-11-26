---
type: topic
tags: [code-review, ai-agents, sdlc, human-in-the-loop]
---

# Risk-Classified PR Routing

Instead of one peer-review rule for every pull request, a classifier (often an LLM) labels each PR by risk and routes it:

- **Mechanical** (SDK version bumps, schema syncs, routine refactors): an LLM reviewer checks it; if the automated gates pass, it merges without a human.
- **High risk** (core architecture, security boundaries): mandatory human review, and the classifier can say how many humans and from which teams.

At Anthropic's platform team, engineers estimated they did not deeply read about 80% of agent-opened PRs; line-by-line reading is kept for subtle logic, security, or when shadow metrics look wrong. This is the routing mechanism behind [[Blast-Radius Code Review]].

## Related

- [[Bottleneck Shift (Theory of Constraints)]]
- [[Agent Verification Stack]]
- [[Human-in-the-Loop Approval Gates]]
- [[Shadow Traffic Migration]]

## Sources

- [[20261126155209 How Anthropic Builds Software with AI Agents|How Anthropic Builds Software with AI Agents]]

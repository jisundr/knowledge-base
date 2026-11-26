---
type: topic
tags: [ai-agents, security, sandboxing, architecture]
---

# Egress Credential Injection

Keep secrets out of the agent's sandbox entirely. Credentials live in a vault; when the agent calls an external tool, an egress proxy adds the credential just in time as the request leaves the sandbox. A compromised or prompt-injected agent has no key to leak.

Part of Anthropic's cloud agent design (Claude Managed Agents): a durable server holds the harness and session state, sandboxes are spun up only to run tools or untrusted code and then torn down, and the egress proxy handles credentials. See [[Long-Running Agent Harness]] for the brain, hands, and session split.

## Related

- [[Containerization and Orchestration]]
- [[Deterministic Guardrail Policies]]
- [[AI Control Plane]]

## Sources

- [[20261126155209 How Anthropic Builds Software with AI Agents|How Anthropic Builds Software with AI Agents]]

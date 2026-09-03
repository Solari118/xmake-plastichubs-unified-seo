---
name: seo-learning-governor
description: Compare completed SEO actions with 30/60/90-day GSC, GA4, ranking, CTR, and conversion evidence and propose governed workflow improvements without self-modifying agents or skills.
---

# SEO Learning Governor

Use this skill after performance-review evidence exists.

## Workflow

1. Trigger on completed-action-linked 30/60/90-day evidence, a scheduled monthly algorithm review, or a repeated verified false-positive/route failure.
2. Match completed action IDs to observations and separate correlation from causation.
3. Compare outcomes by content form, search intent, source confidence, implementation type, and sample size.
4. Produce `KEEP`, `TEST`, `REVISE`, or `RETIRE` proposals.
5. For any Agent, Skill, threshold, or routing change, create a proposal matching `extensions/agentic-seo/schemas/learning-change-proposal.schema.json`.
6. Include the exact target file, current hash, before/after summary, proposed patch, evidence, regression tests, risk, and rollback point.
7. Stop at `WAITING_FOR_GOVERNANCE_APPROVAL`. Apply nothing until the user explicitly approves that proposal.

Observation logging may be automatic. Prompts, Agents, Skills, routes, thresholds, and live content must never be modified automatically.

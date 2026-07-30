---
name: seo-opportunity-orchestrator
description: Reconcile evidence-backed SEO proposals, expose conflicts, and produce a prioritized candidate action queue without silently changing strategy or writing to canonical project state.
---

# SEO Opportunity Orchestrator

Use this skill for weekly opportunity selection or when multiple SEO agents produce competing recommendations.

## Workflow

1. Accept proposal files that follow `extensions/agentic-seo/schemas/proposal.schema.json`.
2. Reject proposals without provenance, timestamp, confidence, effort, and business value.
3. Deduplicate by brand, target, and action type.
4. Flag conflicting actions for the same target.
5. Rank candidates with transparent inputs; never present the score as predicted traffic.
6. Run `scripts/reconcile_proposals.py <output.json> <proposal.json>...`.
7. Send any search-intent or content-format deviation to `WAITING_FOR_INTENT_APPROVAL`.

Only the approved project router may promote a candidate into canonical execution state. This skill never edits master strategy, articles, skills, or live pages.


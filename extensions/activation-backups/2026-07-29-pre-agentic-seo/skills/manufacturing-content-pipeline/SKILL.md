---
name: manufacturing-content-pipeline
description: Route and execute XMAKE or PlasticHubs manufacturing blog work through Top-10-and-style-aware Plan, Info, article-and-corpus Audit, B2B Image, Final Output with verified internal links, and optional post-publication Performance Review. Use for complete article production, an approved Plan brief, an existing manufacturing article, audit-only work, upstream rollback, article revision, 30/60/90-day content review, or legacy entry points. Detect the latest artifact and enter at its safe stage. Keep standalone image edits and unrelated campaign or service-page packaging requests out of this router.
metadata:
  owner: Lostk
  lifecycle_stage: governed
  maturity_tier: governed
  review_cadence: monthly
---

# Manufacturing Content Pipeline

## Owned Job

Act as the sole top-level router. Coordinate specialist skills without merging their prompts, scratch context, or authority.

## Execution

1. Read `references/migration-boundary.md`, `../../workflows/route-policy.md`, `../../workflows/article-pipeline.yaml`, `../../workflows/handoff-contract.md`, and `../../policies/context-isolation.md`.
2. Classify the request as `full_pipeline`, `phase_only`, `standalone_image`, or `performance_review`, then detect the latest verifiable input artifact.
3. Create a run ID and task envelope using `../../schemas/task-envelope.schema.json`.
4. Insert at the latest safe stage: a supplied article starts at Audit; a supplied approved brief starts at Info; a topic/keyword starts at Plan; an audited article starts at B2B Image or Final Output; a published URL with dated performance data starts at Performance Review.
5. Roll back only when a downstream gate identifies an upstream defect. Audit may return a local or sectional issue to Info, or a strategy/intent/architecture defect to Plan; re-run every affected downstream stage before continuing.
6. Pass only the fields declared in the handoff contract. Keep raw conversation, private research, and scratch notes out of downstream context.
7. Validate the requested output and record one truthful terminal state.
8. When task-relevant, load registered private sources through `../../config/private-resource-sources.yaml` and enforce `../../policies/private-resource-policy.md`. Local use is allowed; package/export requests require a fresh enterprise-knowledge inclusion decision.
9. When the user explicitly requests WeChat Official Account references, run `wechat-manufacturing-research` before Plan research or before an Info revision. First generate a brand-wide or topic-focused query portfolio from service scope, Semrush evidence, live Google language, and the manufacturing ontology; do not require the user to know engineering terms. Store its output as a private auxiliary pack; it does not satisfy or replace the Google Top-10 gate.
10. Require Plan to emit a machine-readable brief and run `../../scripts/validate_plan_gate.py --receipt <run>/plan/plan-gate-receipt.json`. Proceed to Info only when it returns `PASS`. Preserve `WAITING_FOR_INTENT_APPROVAL` as a real terminal wait state rather than treating it as permission to continue.

## Phase Owners

| Stage | Skill | Required artifact |
|---|---|---|
| Plan | `b2b-seo-topic-map-builder` | validated content brief |
| Info | `manufacturing-blog-writer` | article bundle plus writer self-check |
| Audit | `seo-geo-content-auditor` | independent findings and verdict |
| B2B Image | `b2b-machining-image-generator` | visual brief, prompts, and asset records |
| Final Output | `xmake-plastichubs-website-ops` | final article package and truthful QA status |
| Performance Review | `seo-content-performance-review` | 30/60/90-day review and feedback artifact |
| Conditional WeChat research | `wechat-manufacturing-research` | private WeChat reference pack |

## Gates

- User-supplied primary keywords proceed. Agent-proposed primary keywords stop at `WAITING_FOR_KEYWORD_APPROVAL`.
- Missing or blocked required SERP evidence prevents final-labeled article output.
- A new Plan brief requires ten documented Google organic editorial/blog benchmark records or transparent exclusions/substitutions, a selected structure/style reference set, and an executable adaptation map.
- Each of the ten records must contain intent, primary audience, content format, outline, opening, pacing, style, evidence form, commercial intensity, CTA position, strengths, gaps, and ranking hypotheses. A title-only list fails.
- Plan must calculate the dominant intent, audience, and format. Any proposed primary-intent or content-format deviation requires a user-facing proposal and explicit approval. Without approval, stop at `WAITING_FOR_INTENT_APPROVAL`; do not draft, audit, generate images, or package output.
- Plan must evaluate search intent, site authority context, internal links, indexation, keyword difficulty evidence, CTR context, content history, and competing-page strength. Backlink acquisition remains outside this content route.
- Info must execute the selected structure, pacing, evidence form, and high-level style profile. It must not default back to one universal opening, table, DFM, FAQ, RFQ, or CTA sequence.
- Audit must block GREEN when the article materially ignores its reference-adaptation contract, repeats a recent same-brand architecture without query-based justification, lacks a passing Plan gate, or implements an unapproved intent/format change.
- Audit hard failures prevent Image and Final Output.
- Standalone image generation does not inherit article stages.
- Article-linked image generation requires the final audited article. If only an unaudited article is supplied, enter at Audit rather than restarting Plan automatically.
- Word or paginated output requires rendered inspection; otherwise label `Structural QA Only`.
- Performance Review requires a published date plus GSC/GA4 or equivalent dated evidence. Otherwise stop at `WAITING_FOR_PERFORMANCE_DATA`.
- WeChat raw text is research-only unless ownership or permission is recorded. Reject wholesale copying, close translation, distinctive-outline copying, and any attempt to use WeChat solely to evade Google duplicate-content detection.

## Output Contract

Return the route trace, Plan-gate receipt path, Top-10 record count, dominant versus selected intent/format, approval status, artifact paths, per-stage status, unresolved evidence, and terminal state. Never present a writer self-check as an Audit verdict.

## Rollback Boundary

Do not mutate accepted upstream artifacts. A repair creates a successor version and can roll back to the last accepted version. Legacy snapshots under `data/raw/legacy-projects/` are read-only preservation evidence.

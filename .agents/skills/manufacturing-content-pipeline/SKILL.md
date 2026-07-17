---
name: manufacturing-content-pipeline
description: Route and execute XMAKE or PlasticHubs manufacturing blog work through Plan, Info, Audit, B2B Image, and Final Output with phase-isolated context and versioned artifacts. Use for complete article production, an approved Plan brief, an existing manufacturing article, an audit-only manufacturing article request, upstream rollback to Plan or Info, article revision toward publication, or legacy Plan/Info/Audit/article-image entry points. Detect the latest artifact and enter at its safe stage. Keep standalone image edits and unrelated campaign or service-page packaging requests out of this router.
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
2. Classify the request as `full_pipeline`, `phase_only`, or `standalone_image`, then detect the latest verifiable input artifact.
3. Create a run ID and task envelope using `../../schemas/task-envelope.schema.json`.
4. Insert at the latest safe stage: a supplied article starts at Audit; a supplied approved brief starts at Info; a topic/keyword starts at Plan; an audited article starts at B2B Image or Final Output according to the request.
5. Roll back only when a downstream gate identifies an upstream defect. Audit may return a local or sectional issue to Info, or a strategy/intent/architecture defect to Plan; re-run every affected downstream stage before continuing.
6. Pass only the fields declared in the handoff contract. Keep raw conversation, private research, and scratch notes out of downstream context.
7. Validate the requested output and record one truthful terminal state.

## Phase Owners

| Stage | Skill | Required artifact |
|---|---|---|
| Plan | `b2b-seo-topic-map-builder` | validated content brief |
| Info | `manufacturing-blog-writer` | article bundle plus writer self-check |
| Audit | `seo-geo-content-auditor` | independent findings and verdict |
| B2B Image | `b2b-machining-image-generator` | visual brief, prompts, and asset records |
| Final Output | `xmake-plastichubs-website-ops` | final article package and truthful QA status |

## Gates

- User-supplied primary keywords proceed. Agent-proposed primary keywords stop at `WAITING_FOR_KEYWORD_APPROVAL`.
- Missing or blocked required SERP evidence prevents final-labeled article output.
- Audit hard failures prevent Image and Final Output.
- Standalone image generation does not inherit article stages.
- Article-linked image generation requires the final audited article. If only an unaudited article is supplied, enter at Audit rather than restarting Plan automatically.
- Word or paginated output requires rendered inspection; otherwise label `Structural QA Only`.

## Output Contract

Return the route trace, artifact paths, per-stage status, unresolved evidence, and terminal state. Never present a writer self-check as an Audit verdict.

## Rollback Boundary

Do not mutate accepted upstream artifacts. A repair creates a successor version and can roll back to the last accepted version. Legacy snapshots under `data/raw/legacy-projects/` are read-only preservation evidence.

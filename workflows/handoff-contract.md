# Handoff Contract

Every run uses `run_id` and versioned artifacts. Paths below are logical; implementations may use Markdown, JSON, or both when schema fields remain equivalent.

| From | To | Required payload | Explicitly excluded |
|---|---|---|---|
| Orchestrator | Plan | task envelope, approved user constraints, brand evidence pointers | unrelated conversation, downstream scratch |
| Plan | Info | accepted machine-readable Plan brief, passing Plan-gate record, complete Top-10 classifications, resolved SERP access/browser-verification state, explicit approval evidence for any `Best-effort` downgrade, intent/audience/format distributions, dominant and selected routes, explicit approval evidence for any deviation, selected structure/style records, article archetype, adaptation map, site/competition context, verified link deployment, public/private flags | planner chain-of-thought, raw browser session state, copied competitor prose, unresolved verification or permission block, unapproved `Best-effort` downgrade, unapproved alternative intent/format |
| Info | Audit | Plan brief, article version, writer self-check, reference-adaptation record, internal-link manifest, recent-article comparison set, private claim ledger | discarded prose, unrelated drafts |
| Audit | Plan | plan-origin findings, affected fields, evidence gap, required replay | full Audit scratch, image ideas |
| Audit | Info | scoped findings, passages, acceptance criteria, preserved elements | unrelated Plan redesign |
| Audit | B2B Image | Green article, visual brief with at least three distinct section-level visual jobs, brand/text constraints | competitor URLs, private source ledger, audit deliberation |
| B2B Image | Final Output | at least three approved standalone asset files per article, prompts record, placement map, alt text, generation status | failed attempt payloads, unrelated references |
| Audit + Image | Final Output | Green article, metadata, approved images, verified internal-link manifest, output mode | non-public evidence and legacy snapshots |
| Final Output | Performance Review | published URL, publication date, archetype/reference metadata, final link manifest, 30/60/90 schedule | private SERP scratch and unrelated article drafts |
| Performance Review | Plan | intent, competition, cannibalization, CTR, indexation, or archetype findings requiring strategy change | raw analytics exports not needed for planning |
| Performance Review | Info | passages/modules needing title, introduction, structure, answer, CTA, or internal-link revision | unrelated analytics and strategy redesign |

## Version Rule

Accepted artifacts are immutable. Use names such as `plan.v2`, `article.v3`, and `audit.v3`. Every successor records `supersedes`, `created_by_stage`, `reason`, and `input_versions`.

## Contract Mismatch

A missing optional field does not force an upstream restart. A missing field triggers rollback only when Audit shows that it materially changes intent, technical accuracy, evidence safety, brand scope, or final acceptance.

`PLAN_GATE_STATUS=PASS` is mandatory, not optional. `WAITING_FOR_INTENT_APPROVAL`, `WAITING_FOR_USER_BROWSER_VERIFICATION`, and `WAITING_FOR_TOOL_PERMISSION` are not accepted Plan briefs and cannot be handed to Info.

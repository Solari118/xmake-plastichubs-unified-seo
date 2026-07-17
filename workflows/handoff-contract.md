# Handoff Contract

Every run uses `run_id` and versioned artifacts. Paths below are logical; implementations may use Markdown, JSON, or both when schema fields remain equivalent.

| From | To | Required payload | Explicitly excluded |
|---|---|---|---|
| Orchestrator | Plan | task envelope, approved user constraints, brand evidence pointers | unrelated conversation, downstream scratch |
| Plan | Info | accepted Plan brief, benchmark status, source pointers, public/private flags | planner chain-of-thought, raw browser session state |
| Info | Audit | Plan brief, article version, writer self-check, private claim ledger | discarded prose, unrelated drafts |
| Audit | Plan | plan-origin findings, affected fields, evidence gap, required replay | full Audit scratch, image ideas |
| Audit | Info | scoped findings, passages, acceptance criteria, preserved elements | unrelated Plan redesign |
| Audit | B2B Image | Green article, visual brief, brand/text constraints | competitor URLs, private source ledger, audit deliberation |
| B2B Image | Final Output | asset files, prompts record, placement map, alt text, generation status | failed attempt payloads, unrelated references |
| Audit + Image | Final Output | Green article, metadata, approved images, output mode | non-public evidence and legacy snapshots |

## Version Rule

Accepted artifacts are immutable. Use names such as `plan.v2`, `article.v3`, and `audit.v3`. Every successor records `supersedes`, `created_by_stage`, `reason`, and `input_versions`.

## Contract Mismatch

A missing optional field does not force an upstream restart. A missing field triggers rollback only when Audit shows that it materially changes intent, technical accuracy, evidence safety, brand scope, or final acceptance.


# Unified Manufacturing Content Project

Mandatory: all user-facing responses are bilingual, Chinese first and English second. Keep code, commands, URLs, paths, formulas, quoted labels, and IDs unchanged when translation would reduce precision.

## Canonical Route

Start every non-trivial manufacturing content task with:

`Route: Manufacturing Content Pipeline > Plan (Top-10 + Structure/Style Route) → Info → Audit (Article + Corpus) → B2B Image → Final Output + Internal Links [→ Performance Review after publication] | Stage: [stage] | Deliverable: [mode]`

Use `skills/manufacturing-content-pipeline/SKILL.md` as the only top-level article router. Specialist skills own their phases and must not absorb another phase's role.

## Entry-Point Behavior

- A complete article, blog, revision-to-publication, or content-package request defaults to the full ordered pipeline.
- A request received from any legacy Plan, Info, Audit, or B2B Image workspace must route here first.
- A user may explicitly request a phase-only task. Run only that phase after checking its prerequisites and label the terminal state accurately.
- A standalone image generation or retouch request remains B2B Image-only. An article-linked image request requires the audited article and visual brief.
- Never skip directly to final packaging without an Audit artifact. Never call a writer self-check the final Audit verdict.

## Ordered Stages

1. `Plan` — `b2b-seo-topic-map-builder`: live Google Top-10 editorial/blog benchmark, per-page intent/audience/format/structure/style records, distribution synthesis, site and competition evidence, selected single- or multi-source structure/style references, article archetype, primary service, verified internal-link plan, and evidence boundary. If exact Google positions cannot be collected because Google presents a verification challenge, open the exact query in the in-app browser and stop at `WAITING_FOR_USER_BROWSER_VERIFICATION`; if browser/tool access is permission- or sandbox-blocked, report the exact permission needed and stop at `WAITING_FOR_TOOL_PERMISSION`. Never silently downgrade to `Best-effort`. Run `scripts/validate_plan_gate.py` against the machine-readable brief before Info. When the user says `对微信公众号相关关键词文章进行参考` or an equivalent explicit request, first run `wechat-manufacturing-research` as a private supplemental research route.
2. `Info` — `manufacturing-blog-writer`: original article that executes the selected reference structure, pacing, and high-level style profile without copying expression. Do not replace the selected pattern with a universal house outline.
3. `Audit` — `seo-geo-content-auditor`: independent hard gates, reference-adaptation check, cross-article similarity check, findings, verdict, and bounded revision request.
4. `B2B Image` — `b2b-machining-image-generator`: visual brief and independent article assets from the audited article.
5. `Final Output` — `xmake-plastichubs-website-ops` plus the appropriate document workflow: final article package, metadata, image placement, alt text, verified same-brand internal links, WordPress and/or verified Word output.
6. `Performance Review` — `seo-content-performance-review`: post-publication 30/60/90-day GSC/GA4 review, archetype performance comparison, and evidence-backed feedback to Plan or Info. Run only after publication data exists or the user requests monitoring.

Conditional auxiliary route: `WeChat Research` — `wechat-manufacturing-research`, owned by `agents/wechat-research.md`, runs only on an explicit WeChat-reference request and hands a private research pack to Plan or Info.

Governed SEO auxiliary routes:

- `seo-run-health-check` runs before scheduled, multi-agent, or post-deployment executions.
- `seo-data-foundation` normalizes GSC, GA4, Semrush, sitemap, PageSpeed, and live SERP evidence. Missing or stale critical evidence stops at `WAITING_FOR_FRESH_DATA`.
- `seo-technical-preflight` runs before `CREATE`, `UPDATE`, or `CONSOLIDATE` decisions and existing-URL optimization. It is read-only; live changes stop at `WAITING_FOR_LIVE_CHANGE_APPROVAL`.
- `seo-opportunity-orchestrator` reconciles campaign or weekly proposals. It is optional for one user-supplied keyword and never replaces the Top-10 Plan gate.
- `seo-learning-governor` receives completed-action-linked 30/60/90-day evidence. It proposes changes only; Agent, Skill, threshold, or route mutation stops at `WAITING_FOR_GOVERNANCE_APPROVAL`.
- Local JSON/CSV/Excel and project artifacts remain canonical. Slack and Google Sheets are optional non-blocking collaboration outputs.
- Local keyword databases are historical/supporting evidence. When a decision depends on current demand, ranking, CTR, cannibalization, or competition, request refreshed evidence if GSC/GA4 is older than 7 days, Semrush is older than 30 days, or the live SERP was not collected in the current run; stop at `WAITING_FOR_FRESH_DATA`.
- `seo-backlink-intelligence` and `seo-link-outreach` are installed but inactive. They may not run or enter the article route until the user explicitly says `激活外链skill` and approves activation. Even after activation, third-party contact stops at `WAITING_FOR_EXTERNAL_OUTREACH_APPROVAL`.

WeChat Research must not expect the user to supply engineering terminology. It must build a brand-correct service universe, load relevant Semrush evidence when available, inspect live Google query language, and expand across process, material, mechanism/defect, tolerance/quality, finishing, DFM, inspection, application, cost, and sourcing before searching WeChat. XMAKE is metal-and-plastic manufacturing; PlasticHubs is the complete supported plastic-processing portfolio, not plastic CNC alone.

Audit may return work to Info for targeted repair. Re-audit the revised artifact before B2B Image. The default automated repair loop is limited to two cycles; unresolved hard failures end in `BLOCKED` or `REVISION_REQUIRED`.

## Artifact And Context Isolation

- The orchestrator owns the route state. Phase agents receive only the current task envelope, their declared inputs, and approved references.
- Store phase artifacts under one run ID. Do not pass the whole conversation, another phase's scratch notes, or unfiltered private research into a downstream phase.
- Treat handoff artifacts as immutable. Corrections create a versioned successor and preserve provenance.
- Keep public content separate from `Internal — Not for Publication` evidence ledgers.
- `data/raw/legacy-projects/` is preservation evidence, not an executable knowledge source. Do not load it unless migration diagnosis explicitly requires it.
- Follow `policies/context-isolation.md`, `workflows/handoff-contract.md`, and the JSON schemas in `schemas/`.

## Evidence And Brand Gates

- One public brand per artifact: XMAKE or PlasticHubs.
- Never expose RapidDirect, supplier identities, competitor URLs, or private source notes in publishable content.
- PlasticHubs remains plastic-manufacturing-focused. Exact figures, standards, certifications, guarantees, legal or regulated claims require applicable support.
- Public links default to the selected brand's domain. External research stays private unless explicitly approved.
- Never invent search volume, rankings, tolerances, material values, lead time, cost savings, capacity, or certification scope.
- Except for backlink acquisition, Plan must evaluate search intent, site authority context, verified internal-link opportunities, indexation/canonical risk, keyword difficulty evidence, CTR context, content history/cannibalization, and competing-page strength. Mark unavailable metrics as `missing evidence`; do not fabricate them.
- The Top-10 benchmark is not complete until Plan selects one or more reference pages and records how their structure, pacing, evidence form, and high-level writing style will be adapted in Info.
- Plan must also preserve a selected-reference shape fingerprint: H1/H2/H3 hierarchy and reader jobs, title-to-section alignment, opening answer point, narrative order, section-count and section-length pattern, heading grammar, paragraph cadence, evidence/list/table use and placement, FAQ/CTA placement, ending form, comprehension load, English naturalness, and AI-pattern risks. Top-10 coverage points alone are not a valid style handoff.
- Count the dominant intent, primary audience, and content format from the ten per-page records. If the proposed primary intent or content format differs from the observed dominant route, show the user a compact alternative-angle proposal with expected gain, ranking risk, audience effect, and measurement plan. Stop at `WAITING_FOR_INTENT_APPROVAL`; do not enter Info until the user explicitly approves. Differentiation inside the dominant intent does not require approval.
- A title-only Top-10 list, unclassified result, non-editorial page without transparent exclusion/substitution, mismatched distribution, or unapproved intent/format deviation fails the Plan gate. No downstream stage may infer approval or repair the omission silently.
- When exact Google Top-10 evidence is required, `Best-effort` may pass only after the user explicitly approves that downgrade and the brief records the approval evidence. A Google verification challenge must first open the exact query in the in-app browser and wait for the user; a tool or sandbox permission block must identify the exact permission required. Neither condition may be disguised as an ordinary `Best-effort` benchmark.
- Every article run must preserve and report `plan-gate-receipt.json` with the Top-10 record count, intent/audience/format distributions, dominant and selected routes, approval status, and gate result. This is the user's execution evidence; a narrative claim that the route ran is insufficient.
- The legacy engineering-control guide remains an allowed `ARTICLE_ARCHETYPE`; it must be selected explicitly from SERP/reference evidence and may not silently become the project-wide house structure.
- WeChat research supplements but never replaces the Google Top-10. Public WeChat pages may supply private topic leads, shop-floor mechanisms, terminology, or counterexamples; do not translate, paraphrase-launder, or republish third-party articles. Verify technical claims independently and keep raw captures private.
- Every public Blog must contain (1) a visible, topic-specific FAQ and (2) a visible CTA with a selected-brand action, useful input request, and direct same-brand URL. Their question count, question source, placement, answer form, CTA heading, CTA position, and wording must follow the query and selected reference route rather than one fixed ending. Tables, RFQ modules, failure modes, answer-first blocks, SPEAR openings, DFM, and conclusions remain conditional.
- Audit must route upstream defects before Final Output: intent, reference selection, format, archetype, or rhythm defects return to Plan; article execution, hierarchy, title alignment, opening answer timing, English, complexity, FAQ, CTA, or corpus-diversity defects return to Info. Repair and re-run Audit; no RED artifact may advance.
- Treat every path in `config/private-resource-sources.yaml` as an approved private source for this project and `XMAKE-PlasticHubs-SEO-Blueprint`. Local copies are allowed; follow `policies/private-resource-policy.md`.
- For source images carrying APEX or TIGER marks, replace every visible mark with the selected target brand's approved XMAKE or PlasticHubs logo/wordmark before public use. Images without source marks still require a material, non-technical edit; pixel-identical reuse is forbidden.
- Engineering/process files in `企业知识（保密）` may support article facts and data. Business/management material is conditional backup evidence. Never expose private paths or unrelated confidential content publicly.
- On every package/export/deployment request, ask afresh whether `企业知识（保密）` should be included. Without an explicit yes for that packaging run, exclude it. This gate does not prohibit local copies.

## Completion Truth

Valid terminal states are `COMPLETED`, `PHASE_COMPLETED`, `WAITING_FOR_KEYWORD_APPROVAL`, `WAITING_FOR_INTENT_APPROVAL`, `WAITING_FOR_USER_BROWSER_VERIFICATION`, `WAITING_FOR_TOOL_PERMISSION`, `WAITING_FOR_FRESH_DATA`, `WAITING_FOR_LIVE_CHANGE_APPROVAL`, `WAITING_FOR_GOVERNANCE_APPROVAL`, `WAITING_FOR_PERFORMANCE_DATA`, `REVISION_REQUIRED`, and `BLOCKED`.

`COMPLETED` requires all requested artifacts, a passing final Audit, truthful image-generation status, and the requested final-output QA. If `.docx` or paginated rendering cannot be visually inspected, use `Structural QA Only` and do not claim Word-ready status.

## Canonical And Compatibility Policy

- Canonical skills live in `skills/`.
- Discovery mirrors live in `.agents/skills/` and `.codex/skills/`; update them only through `scripts/sync_mirrors.py`.
- Legacy workspaces contain adapters to this root and retain their former instructions as `AGENTS.legacy.md`.
- Run `python scripts/validate_project.py` before release or after changing routing, contracts, adapters, or mirrors.

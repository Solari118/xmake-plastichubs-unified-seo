---
name: b2b-seo-topic-map-builder
description: Build writer-ready XMAKE or PlasticHubs SEO/GEO briefs from keyword evidence, a live Google Top-10 editorial/blog benchmark, site and competition context, explicit single- or multi-source structure/style reference selection, article-archetype routing, verified internal-link deployment, and originality controls. Use for a topic or primary keyword, keyword filling, competitor-content analysis, content architecture, GEO answer planning, content clusters, or topic maps. Do not draft articles or issue final Audit verdicts.
---

# B2B SEO/GEO Content Planner

## Owned Job

Convert a manufacturing topic and primary keyword into a complete brief that the Info writer can execute and the Audit reviewer can evaluate. Keep the work strategic; do not draft article body copy.

At activation, report `Route: Plan > b2b-seo-topic-map-builder`, the current stage, and requested deliverable mode in one concise bilingual line.

## Core Workflow

1. Confirm or infer `BRAND`, `TOPIC`, `PRIMARY_SERVICE`, and `PRIMARY_KEYWORD`. Ask only if brand or primary-service ambiguity creates a service-scope risk.
2. Read [Company Assets](references/company-assets.md), [Content Brief Contract](references/content-brief-contract.md), [SEO/GEO Planning Rules](references/seo-geo-planning-rules.md), and [Top-10 SERP And Reference Selection Workflow](references/serp-top-ten-workflow.md).
3. Search the project for relevant XMAKE, PlasticHubs, AI Prompt Data, Info, Roundup, technical, and process knowledge files. Load only relevant sources.
   When the user explicitly requests WeChat Official Account references, require `wechat-query-portfolio.md` and `wechat-reference-pack.md`. Check brand/service coverage, Semrush provenance, Google-language provenance, technical-dimension diversity, source quality, and novelty leads. Keep both artifacts separate from the Google benchmark.
4. Classify content type, primary and secondary intent, decision stage, target market, and conversion goal.
5. Run the live Google Top-10 organic editorial/blog benchmark before finalizing the brief. Preserve observed results and transparent substitutions. When Google presents a verification challenge or exact positions cannot be confirmed, open the exact query in the in-app browser. Ask the user to complete the visible verification and stop at `WAITING_FOR_USER_BROWSER_VERIFICATION`; resume the same query only after the user confirms completion. If the browser or search tool is blocked by a permission or sandbox boundary, name the exact permission needed and stop at `WAITING_FOR_TOOL_PERMISSION`. Do not silently substitute another engine, API result set, or `Best-effort` pack. For every page record intent, primary audience, content format, outline, opening, pacing, style, evidence form, commercial intensity, CTA position, strengths, gaps, and ranking hypotheses. A title-only list is incomplete.
6. Calculate `SERP_INTENT_DISTRIBUTION`, `SERP_AUDIENCE_DISTRIBUTION`, and `SERP_FORMAT_DISTRIBUTION` from the ten records, then name `DOMINANT_SERP_INTENT`, `DOMINANT_AUDIENCE`, and `DOMINANT_CONTENT_FORMAT`. Do not infer one persona for the whole query before counting the pages.
7. Build the keyword/query map: primary keyword, secondary candidates, natural query variants, buyer modifiers, questions, and entities. Never invent volume, CPC, difficulty, or live rankings.
8. Evaluate `SITE_AUTHORITY_CONTEXT`, `SITE_CONTENT_HISTORY`, `INDEXATION_AND_CANONICAL_RISK`, `KEYWORD_DIFFICULTY_CONTEXT`, `CTR_CONTEXT`, `COMPETITOR_PAGE_STRENGTH`, and the verified same-brand internal-link inventory. Backlink acquisition is excluded because it is governed separately by the user.
9. Select one or more Top-10 pages as structure/style references. Record `STRUCTURE_REFERENCE_MODE`, `PRIMARY_STRUCTURE_REFERENCE`, `SECONDARY_PATTERN_REFERENCES`, `STRUCTURE_ADAPTATION_MAP`, `STYLE_PROFILE`, `REFERENCE_SHAPE_FINGERPRINT`, and `ARTICLE_RHYTHM_ROUTE`. Capture H1/H2/H3 hierarchy and reader jobs, title-to-section alignment, opening answer point, narrative sequence, H2 count or range, section-length distribution, heading grammar, paragraph cadence, evidence density, list/table use and placement, FAQ/CTA placement, ending form, comprehension load, English naturalness, and AI-pattern risks. Reference selection must affect the Info article, not remain background research.
   WeChat sources may contribute a separately labeled `WECHAT_REFERENCE_ADAPTATION` for questions, evidence forms, shop-floor mechanisms, or counterexamples. They must not replace the selected Google structure/style reference contract.
10. Set `SELECTED_PRIMARY_INTENT`, `SELECTED_CONTENT_FORMAT`, and `SELECTED_CONTENT_ANGLE`. If either intent or format differs from the observed dominant route, prepare `INTENT_CHANGE_PROPOSAL` with reason, expected gain, ranking risk, audience effect, and measurement plan. Show it to the user and stop at `WAITING_FOR_INTENT_APPROVAL`. Continue only after recording explicit approval evidence; never treat silence or a general request for variety as approval.
11. Choose `ARTICLE_ARCHETYPE` from diagnostic, comparison, failure investigation, material experiment, procurement guide, cost decision, case-led analysis, technical encyclopedia, engineering decision guide, engineering-control guide, or a justified custom type. Keep it consistent with `SELECTED_CONTENT_FORMAT`. Preserve the former engineering-control structure as one valid option; never select it merely because it is familiar.
12. Define the persona's technical goal, information void, failure risk, and required information gain.
13. Define `INTENT_COMPLETION_CRITERIA`, `OPENING_MODE`, `SECTION_ROLE_MAP`, `SECTION_REFERENCE_MAP`, `MANDATORY_MODULES`, `OPTIONAL_MODULES`, `MODULES_TO_OMIT`, and `CROSS_SERVICE_LINK_PLAN`. Build every planned public H2—including FAQ and CTA—from observable selected-Top-10 behavior. For each H2 record its original planned heading, `sequence_index`, `sequence_reason`, `heading_scope_mode`, Top-10 result positions and URLs, reference heading pattern, information order, reader question, mandatory first-paragraph answer, included and excluded scope, adaptation note, and originality guard. Use `multi-topic-umbrella` when one H2 governs several distinct H3 topics; do not place a narrow negative comparison over a broad catalog. Do not reduce this to an abstract label such as `capability` or `decision section`. For every Blog, put `FAQ` and `CTA` in `MANDATORY_MODULES`, populate `FAQ_PLAN`, and populate `CTA`. If any core H2 follows FAQ, list it in `substantive_sections_after_faq`, set `allow_substantive_sections_after_faq=true`, and preserve a Top-10-supported placement rationale; otherwise require `false` and an empty list. Do not force a table, RFQ, failure-mode module, SPEAR opening, DFM, conclusion, or fixed FAQ/CTA position.
14. Carry forward user-set `MIN_WORD_COUNT`, `READABILITY_TARGET`, `DELIVERABLE_MODE`, `PREVIEW_FORMAT`, `WORD_STYLE_REFERENCE`, `REVISION_SCOPE`, and `SOURCE_ELEMENTS_TO_PRESERVE` without turning them into universal defaults.
15. Select `COMMERCIAL_BRIDGE_MODE`: `none`, `soft`, or `explicit`. Match its intensity and placement to the selected structure and intent.
16. Build the GEO answer plan: direct-answer targets, fan-out questions, evidence requirements, quotable facts, and entity disambiguation. Treat these as content-quality tactics, not guaranteed ranking factors.
17. Produce `INTERNAL_LINK_DEPLOYMENT` with live same-brand URL, target relationship, contextual anchor, planned section, and link validation status. Do not append a service catalog.
18. Recommend a differentiated architecture that adapts the selected reference structure/style at a high level without copying prose, distinctive headings, proprietary examples, unique tables, or a near-duplicate outline.
19. Save a machine-readable Plan brief conforming to `../../schemas/plan-brief.schema.json`, run `../../scripts/validate_plan_gate.py --receipt <run>/plan/plan-gate-receipt.json`, and record `PLAN_GATE_STATUS`. The receipt must expose the Top-10 count, SERP access state, browser-verification state, downgrade approval, distributions, dominant and selected routes, and approval state so the user can verify execution. Hand off only on `PASS`.
20. Run [Brief Quality Checklist](evals/brief-quality-checklist.md) before handoff.

## Brand And Evidence Boundary

- Published copy and writer-facing brand language must mention only XMAKE or PlasticHubs, according to `BRAND`.
- RapidDirect data may be used internally as shared-supply-chain evidence. Do not expose the RapidDirect name in public copy, metadata, CTAs, or commercial hooks.
- Shared data does not need public source attribution to RapidDirect. It must still be relevant to the selected brand, applicable to the service scope, and supported by the project knowledge base.
- PlasticHubs remains plastic-manufacturing-first. XMAKE may cover the broader verified manufacturing scope.
- Ordinary XMAKE manufacturing, finishing, self-operated factory, owned-equipment, engineering, inspection, and supply-chain capability are project-approved defaults. Lack of independently searchable Chinese factory or supplier records does not invalidate those general capability statements.
- Do not invent or generalize exact figures, standards, tolerances, guarantees, or certification scope.

## Reference Adaptation And Conditional Modules

- Borrow structure and high-level style only from the explicitly selected Top-10 reference set. A single reference is allowed when it best fits the query; multiple references are allowed when their functions combine coherently.
- `STYLE_PROFILE` may describe opening mode, narrative stance, pacing, paragraph rhythm, evidence density, example usage, transition behavior, technical tone, and ending form. Do not request imitation of an identifiable author's distinctive expression.
- `REFERENCE_SHAPE_FINGERPRINT` must retain observable form rather than vague adjectives. Include H1/H2/H3 hierarchy, the exact logic order and reader job of each level, the point at which the opening resolves primary intent, title-to-section alignment, section count/range, relative section lengths, heading grammar, paragraph-length distribution, evidence/list/table behavior and placement, FAQ/CTA position, ending form, reading complexity, English naturalness, and AI-template signals.
- `ARTICLE_RHYTHM_ROUTE` must state which selected reference controls the dominant rhythm and which secondary references contribute only bounded modules. Do not average all ten results into one house cadence.
- `STRUCTURE_ADAPTATION_MAP` must map each borrowed function to an original article module and state the new information gain.
- `SECTION_REFERENCE_MAP` is the executable H2 handoff. Follow the selected Top-10 pages' reader-facing hierarchy, heading function, information order, answer timing, and table/list location where useful; write original headings and prose. Every referenced URL must belong to `TOP_TEN_SERP_RESULTS`.
- Treat FAQ as a question-cleanup module, not an automatic interruption point. Default to completing the core narrative before FAQ. A core section after FAQ is allowed only when the selected reference structure provides a clear reader benefit and the brief records the exact exception, affected headings, rationale, and supporting Top-10 URL.
- A consequence-led opening, definition opening, diagnostic scenario, result-first answer, case opening, question opening, or specification opening may be selected when supported by intent and reference evidence.
- Every Blog requires a visible FAQ and CTA. Build FAQ questions from Top-10 gaps, PAA when available, query variants, buyer objections, or unresolved technical decisions; plan 3–6 questions that do not merely repeat body sections. Define a topic-specific FAQ heading and vary placement and answer form according to intent.
- Every Blog requires a visible CTA. Define a topic-specific heading or callout, selected-brand action, useful inputs, reader value, placement, and direct same-brand URL. `COMMERCIAL_BRIDGE_MODE=none` still requires a neutral action CTA; it only removes supplier-model contrast.
- Tables, RFQ checklists, DFM, failure modes, calculators, diagrams, conclusions, and the exact FAQ/CTA placement remain conditional. Record why each included module helps and explicitly omit habitual modules that do not.
- For comparison content, use shared decision dimensions only when the query is genuinely comparative.
- Keep public paragraphs readable, but do not force identical paragraph length or cadence across articles.
- Do not impose one H2 count, one 1,600-word band, one three-sentence paragraph cap, or one supplier-input ending across sibling articles.
- Use factory-direct or broker contrast only under `soft` or `explicit` mode and only when relevant.
- Treat legacy prompt figures, including `20-40%`, `30%`, `20,000㎡`, `3-day`, machine counts, certifications, and AI-engine claims, as prohibited until current target-brand evidence verifies the exact scope.

## Anti-AI Gate

Reject these public-language patterns: `delve`, `embark`, `craft`, `unlock`, `discover`, `utilize`, `dive deep`, `unveil`, `harness`, `elucidate`, `game-changer`, `skyrocket`, `revolutionize`, `disruptive`, `groundbreaking`, `cutting-edge`, `remarkable`, `powerful`, `world-class`, `shed light`, `imagine`, `realm`, `tapestry`, `illuminate`, `navigating`, `landscape`, `ever-evolving`, `testament`, `you're not alone`, `in a world where`, `pivotal`, `intricate`, `hence`, `furthermore`, `however`, `moreover`, `in summary`, `in conclusion`, and `in closing`.
- Keep third-party names, URLs, competitor links, and external attribution inside the internal brief, SERP pack, or source notes marked `Internal — Not for Publication`. Public-content requirements must default to selected-brand internal links only.
- Never prescribe an outbound link for SEO, GEO, citation readiness, or authority signaling. Exceptional public outbound links require explicit approval and commercial/SEO review; compensated placements require `rel="sponsored"` or `rel="nofollow"`.

## Commercial Bridge Modes

- `none`: no broker comparison; use for neutral or standards-led content when commercial contrast would reduce usefulness.
- `soft`: one contextual factory-direct implication, buyer-risk note, or CTA; default for informational engineering blogs.
- `explicit`: visible comparison of supplier transparency, accountability, quotation flow, or routing risk; use for sourcing and commercial-investigation content.

Never invent markup percentages, savings percentages, or universal speed advantages.

## Default Blueprint Output

```markdown
## 1. Target Persona Deep-Dive
## 2. Search Intent And Decision Context
## 3. Google Top-10 SERP And Competing-Page Benchmark
## 4. Keyword And Query Map
## 5. Site Authority, Content History, Indexation, CTR, KD, And Internal Links
## 6. Selected Structure/Style References And Article Archetype
## 7. Structure Adaptation, Module Selection, And Information Gain
## 8. GEO Answer Plan And Commercial Bridge
## 9. Evidence And Publishing Requirements
## 10. Ready-to-Copy Project Inputs
```

The last section must use the exact field names in [Content Brief Contract](references/content-brief-contract.md). Populate secondary keywords and query variants as strategic candidates when no validated keyword dataset is supplied, and label validation status accurately.

## Topic-Map Workflow

Use this only for campaign-level topic maps, clusters, pillar/supporting architecture, CSV, or HTML reports.

Read in order:

1. `references/input-format.md`
2. `references/prompt-01-industry-knowledge-map.md`
3. `references/prompt-02-customer-intent-map.md`
4. `references/prompt-03-topic-map-builder.md`
5. `references/prompt-04-pillar-supporting-pages.md`
6. `references/prompt-05-final-report-generator.md`

Use `assets/topic_map_columns.csv` as the exact CSV contract. Markdown is the editable source of truth; HTML is presentation only.

## Boundaries

- Live browsing is mandatory before a brief is marked ready for final article production. For exploratory brainstorming, a provisional non-SERP brief is allowed only when labeled `Blocked` or `Provisional`.
- `SERP_ACCESS_STATUS=google-verification-required` requires opening the in-app browser and `PLAN_GATE_STATUS=WAITING_FOR_USER_BROWSER_VERIFICATION`. `SERP_ACCESS_STATUS=tool-permission-required` requires a precise permission request and `PLAN_GATE_STATUS=WAITING_FOR_TOOL_PERMISSION`.
- `SERP_BENCHMARK_STATUS=Best-effort` may pass only with `SERP_ACCESS_STATUS=best-effort-approved`, `BEST_EFFORT_DOWNGRADE_APPROVAL=approved`, and explicit approval evidence. Silence, impatience, or a general instruction to continue is not downgrade approval.
- A Top-10 pack that only summarizes content topics but does not select and map executable structure/style references is incomplete.
- A Top-10 pack that lists titles without complete per-page classifications is incomplete.
- A different angle within the dominant intent and format is allowed. Changing the primary intent or governing content format is not: pause for explicit user approval and state the ranking and audience tradeoff first.
- Use observed organic positions only. Exclude ads and clearly document intent-mismatched, inaccessible, duplicate, or substituted results.
- Do not describe ranking hypotheses as proven causes.
- Do not copy competitor prose, distinctive headings, examples, tables, or a single competitor's full outline.
- Do not copy, closely translate, or paraphrase-launder WeChat prose, distinctive headings, cases, tables, images, or a full outline. Treat WeChat technical claims as leads requiring independent verification.
- Mark unvalidated keyword candidates and SERP assumptions explicitly.
- Do not draft article body copy, perform line editing, or issue a publish verdict.
- Do not create a commercial section merely to satisfy a template.
- Do not prescribe a universal word count; scope follows decision complexity and information completeness.

## Final Gate

Confirm that the brief is bilingual when project instructions apply, all ten benchmark records or substitutions exist, selected references visibly control the archetype and adaptation map, required site/competition factors are evaluated, links are verified, habitual modules are explicitly included or omitted, the selected brand is clean, RapidDirect is absent from public variables, and user-set constraints are preserved.

---
name: seo-geo-content-auditor
description: Audit XMAKE or PlasticHubs articles against a Plan brief, live Google Top-10 benchmark, selected structure/style references, article archetype, adaptation map, recent same-brand corpus, evidence, and verified internal links. Use for final quality verdicts, reference-adaptation checks, cross-article similarity checks, revision actions, red/yellow/green status, or pre-publication audits. Do not create upstream strategy or draft a new article from scratch.
---

# SEO/GEO Content Auditor

## Owned Job

Decide whether a draft is ready, needs targeted revision, or requires substantial rework. Audit against the Plan brief and source evidence rather than a generic article template.

At activation, report `Route: Audit > seo-geo-content-auditor`, the audit/revision stage, and requested deliverable mode in one concise bilingual line.

## Workflow

1. Read [Content Brief Contract](references/content-brief-contract.md), [Audit Rubric](references/audit-rubric.md), [SERP Benchmark Review Rules](references/serp-benchmark-review-rules.md), and the supplied brief.
2. Identify public brand, content type, `PRIMARY_SERVICE`, primary intent, primary keyword, `CROSS_SERVICE_LINK_PLAN`, and `COMMERCIAL_BRIDGE_MODE`.
3. Validate the Top-10 environment, SERP access state, browser-verification state, explicit approval evidence for any `Best-effort` downgrade, all required fields in each of the ten result records, exclusions/substitutions, intent/audience/format distributions, dominant classifications, selected intent/format/angle, approval evidence when divergent, `PLAN_GATE_STATUS=PASS`, selected reference set, archetype, adaptation map, style profile, reference shape fingerprint, article rhythm route, module list, site/competition context, verified internal-link plan, differentiation, and originality guardrails.
4. Compare the draft against all ten results and the selected reference set for intent fit, structure/style execution, essential coverage, gap closure, information gain, and derivative-copy risk.
5. Test every `INTENT_COMPLETION_CRITERIA` item and locate the early core answer.
6. Compare the article with `STRUCTURE_ADAPTATION_MAP`, `SECTION_REFERENCE_MAP`, `STYLE_PROFILE`, `MANDATORY_MODULES`, `MODULES_TO_OMIT`, and `SECTION_ROLE_MAP`. For every actual H2, separately record the reader question implied by the heading, the first-paragraph answer, the full-section answer, and the selected Top-10 structure pattern. Do not accept an abstract role label as evidence.
7. Run the cross-article similarity check against the declared recent same-brand comparison set. Compare H1/H2/H3 hierarchy, title alignment, opening answer timing, semantic section roles and narrative order, H2 count, section-length distribution, heading grammar, paragraph cadence, evidence/list/table form and placement, comprehension load, English naturalness, AI-pattern signals, FAQ position/question pattern, CTA position/wording, ending form, and media logic. Exact-heading or n-gram differences alone do not pass this gate.
8. Create `section-alignment-audit.json` as the independent Audit-stage evidence, then run `scripts/validate_heading_content_alignment.py <article.md> <section-alignment-audit.json>`, `scripts/validate_blog_conversion_modules.py`, `scripts/validate_blog_narrative_quality.py <plan.json> <article.md>`, and `scripts/validate_blog_corpus_similarity.py`. The H2 audit must cover every H2 in order and quote evidence that exists in the first paragraph and section body. Any missing record, evidence mismatch, semantic `FAIL`, forbidden tone hit, unapproved FAQ interruption, or H2 scope failure is a hard failure; a narrative checklist or aggregate score cannot override it.
9. When a WeChat reference pack exists, audit its query portfolio first: correct brand scope, service coverage, Semrush/Google provenance, technical-dimension diversity, and noise exclusions. Then compare the draft with selected source functions and available private excerpts. Fail for a single-literal-query search without justified scope, close translation, paragraph-by-paragraph paraphrase, distinctive-outline copying, copied cases/tables/images, or unverified WeChat technical claims.
10. Check task-specific readability, minimum length, and artifact-delivery requirements when supplied.
11. Check `REVISION_SCOPE` and `SOURCE_ELEMENTS_TO_PRESERVE`; require the smallest correction scope that resolves the defect.
12. Run hard gates before assigning points.
13. Score all eight rubric dimensions with evidence from the draft, selected reference contract, recent corpus, and benchmark.
14. List findings first, ordered `Blocker`, `High`, `Medium`, then `Low`.
15. Quote the smallest exact passage needed to identify each problem and provide a specific correction.
16. Preserve good sections. Produce a replacement outline only for Red status or when structure is the main Yellow-status defect.
17. Use [Audit Report Template](templates/audit-report-template.md) for the final bilingual report.

## Hard Gates

Any hard-gate failure forces Red status regardless of numerical score:

- RapidDirect appears in public copy, metadata, CTA, headings, image text, schema, or publishable notes.
- A third-party brand name, third-party URL, competitor link, `Source:` label, or external-research attribution appears in public copy without explicit approval.
- Public brand is mixed, wrong, or absent when the brief identifies one brand.
- PlasticHubs is assigned an unsupported non-plastic direct service.
- A material claim, citation, standard, certification, metric, tolerance, guarantee, safety statement, or competitor fact is fabricated or materially wrong.
- A critical claim cannot be traced because required evidence is missing and publication would create material technical, legal, or commercial risk.
- The article contradicts the primary user intent or promotes a service unrelated to the topic.
- `SERP_RESEARCH_REQUIRED=Yes` but the Top-10 benchmark is missing, has fewer than ten analyzed editorial/blog records without transparent substitutions, is `Blocked`, materially incomplete, or falsely labeled `Validated`.
- Google verification or tool-permission access remains unresolved, `Best-effort` was used without explicit user downgrade approval and evidence, or either wait state was bypassed.
- The Top-10 pack is title-only, any page lacks the required intent/audience/format/structure/style analysis, declared distributions do not match the ten records, or `PLAN_GATE_STATUS` is not `PASS`.
- The selected primary intent or content format differs from the observed dominant route without explicit user approval evidence. General requests for originality or variety are not approval for a specific intent shift.
- Required structure/style references, archetype, adaptation map, style profile, or module selection are absent.
- `REFERENCE_SHAPE_FINGERPRINT` or `ARTICLE_RHYTHM_ROUTE` is absent, vague, or not visibly executed.
- The article materially ignores the selected reference contract and substitutes a habitual universal house outline.
- `SECTION_REFERENCE_MAP` is absent, vague, cites pages outside the Top-10 pack, or is not visibly executed.
- `section-alignment-audit.json` is missing, was produced as an Info self-check, does not cover every actual H2 in order, contains evidence not found in the article, or fails `validate_heading_content_alignment.py`.
- Any H2 promises a different question, scope, object, or decision from the answer in its first paragraph or full section.
- A core section appears after FAQ without the explicit Plan exception, named affected headings, placement rationale, and Top-10 support required by `FAQ_PLAN`.
- A narrow negative-comparison H2 governs three or more distinct H3 topics, or a multi-topic section lacks the planned `multi-topic-umbrella`/comparison scope contract.
- `validate_blog_narrative_quality.py` reports a forbidden tone term, FAQ-flow defect, or H2-scope defect.
- The article repeats a recent same-brand semantic section sequence or rhythm profile without query/reference justification, even when headings and exact phrases differ.
- A final Blog lacks a clearly labeled, topic-specific FAQ with at least three useful non-duplicate answers.
- A final Blog lacks a visible action-led CTA, selected-brand next step, useful input request, or direct same-brand URL. A generic `contact us` sentence does not satisfy this gate.
- The final article copies or closely paraphrases competitor language, distinctive headings, proprietary examples, unique tables, or one competitor's full outline.
- A final-labeled artifact ignores an explicit user minimum length, readability target, or required delivery format.

Ordinary XMAKE manufacturing, finishing, self-operated factory, owned-equipment, engineering, inspection, and supply-chain capability are project-approved defaults and are not hard failures solely because independent Chinese registry evidence is unavailable. Exact figures, certifications, legal qualifications, regulated work, guarantees, and safety-critical claims remain evidence-controlled.

## Scoring

Use the 20-point rubric in [Audit Rubric](references/audit-rubric.md).

- `GREEN`: 19-20, no hard fail, publishable after ordinary human approval.
- `YELLOW`: 15-18, no hard fail, targeted revision required.
- `RED`: 0-14 or any hard fail, substantial rework required.

Do not inflate scores. Explain every deduction. A reasonable qualifier is not a trust failure; false certainty is.

## Commercial Mode Review

- `none`: broker contrast should be absent; forced sales comparison is a defect.
- `soft`: expect limited contextual relevance, usually integrated into a technical or CTA section.
- `explicit`: expect a clear, factual sourcing-model comparison tied to buyer criteria.

Do not require or reward invented markup percentages, savings percentages, universal speed claims, or competitor attacks.

## SEO/GEO Review

- Evaluate topic clarity, query coverage, entity coverage, intent satisfaction, and internal-link relevance.
- Do not require the exact keyword in a fixed set of positions.
- Check direct answers, conditions, limitations, internally sourceable facts, private evidence traceability, information gain, and useful subquestion coverage.
- Keep external sources and competitor URLs in the private brief, SERP pack, audit evidence, or claim ledger marked `Internal — Not for Publication`. Do not reward public third-party links or attribution.
- Require public links to default to the selected brand's own domain. Any exceptional outbound link needs explicit approval and commercial/SEO review; paid placements must be qualified with `rel="sponsored"` or `rel="nofollow"`.
- Check that metadata and structured-data recommendations match visible content.
- Do not require special AI files or promise generative-engine citations.
- Compare against the complete Top-10 benchmark. Verify that the approved primary or multi-reference adaptation is visible, the remaining results were used for validation and gap detection, and the draft is neither a stitched summary nor a derivative copy.
- Treat ranking explanations only as hypotheses and reject unsupported causal claims.

## Reference Adaptation, Corpus Diversity, And Tone Review

- Check whether the opening mode, pacing, evidence density, transitions, tone, and ending execute `STYLE_PROFILE`. Do not impose SPEAR, definition-first, or answer-first forms when Plan selected another mode.
- For comparison content, map every core H2 to shared buyer criteria and confirm both options remain visible. A long one-sided section is acceptable only when it states how that detail changes the comparison.
- Require FAQ and CTA for every Blog. Check answer-first blocks, tables, RFQs, DFM, failure modes, and conclusions only when selected by the brief.
- Reject mechanical cadence or fragmented logic, but do not require identical paragraph length.
- Reject fewer than three FAQ questions, duplicate FAQ answers, questions already answered verbatim in the body, generic topic-free FAQ headings, and cross-article reuse of the same question set without query evidence.
- Require a visible topic-specific CTA heading or callout, a concrete selected-brand action, useful inputs or next step, reader value, and direct same-brand URL. CTA position and wording must follow the brief and differ from recent sibling articles when intent allows.
- Check every H2 for a distinct reader job. A decision matrix and later “when to choose” sections should be consolidated when they repeat the same criteria.
- Treat slogans and compressed metaphors as failed headings when a reader cannot predict the section's subject and decision. Route an execution-level heading/body mismatch to Info; route a defective Top-10-derived section map to Plan.
- Compare the recent corpus for repeated opening, H2 order, evidence modules, CTA placement, and image logic. Unjustified high similarity prevents GREEN and returns the defect to Plan or Info.
- Specifically test for the recurring `explanation → cautions → supplier inputs` sequence, similar H2 counts, uniform section lengths, and near-identical CTA endings. Treat these as structural similarity even when labels differ.
- Confirm that the engineering-control guide remains available but appears only when explicitly selected by Plan; do not penalize it merely for being an older approved archetype.
- Route upstream defects deterministically: wrong intent, reference selection, format, archetype, or rhythm contract returns to Plan; weak execution, hierarchy, English, complexity, FAQ, CTA, or corpus diversity returns to Info. After repair, replay every affected downstream stage and re-run Audit. No RED article may enter Final Output.
- Confirm that selected reference functions were adapted without copying distinctive expression, proprietary examples, unique tables, or a near-duplicate outline.
- Replace generic `Quick Answer`, `Fast Guide`, or `Rapid Decision` headings when they add no task meaning; do not penalize a factual discussion of speed.
- When `READABILITY_TARGET` exists, evaluate the English against it and check that technical terms are defined before use. When `MIN_WORD_COUNT` exists, verify the final word count without rewarding padding.
- Run a literal Tone Check for: `delve`, `embark`, `craft`, `crafting`, `unlock`, `discover`, `utilize`, `utilizing`, `dive deep`, `unveil`, `harness`, `elucidate`, `enlightening`, `esteemed`, `game-changer`, `skyrocket`, `revolutionize`, `disruptive`, `groundbreaking`, `cutting-edge`, `remarkable`, `powerful`, `world-class`, `real-world`, `shed light`, `imagine`, `realm`, `abyss`, `tapestry`, `illuminate`, `glimpse into`, `navigating`, `landscape`, `stark`, `testament`, `bustling`, `opened up`, `ever-evolving`, `you're not alone`, `in a world where`, `it remains to be seen`, `pivotal`, `intricate`, `hence`, `furthermore`, `however`, `moreover`, `in summary`, `in conclusion`, and `in closing`.
- Do not restore or reward RapidDirect public references, mixed brands, or unverified legacy metrics. Accurate qualifiers remain acceptable when process variability is real.

## Output Boundary

- Audit and prescribe; do not silently replace the entire article.
- If a section is sound, write `No change needed.`
- Proposed text must not introduce new unsupported claims.
- Proposed public text must not introduce third-party names, URLs, citations, or attribution. If a claim needs external attribution, remove or qualify it, use approved brand-owned evidence, or mark it `Needs approval`.
- Output Chinese first, English second.
- For paginated preview or Word delivery, verify the artifact rather than only the chat text. Render and inspect pages when supported; otherwise state that only structural QA was completed.
- Persist approved corrections to the artifact and do not claim Word-ready status when font, punctuation, tables, links, or page breaks were not visually checked.
- Do not recommend a full rewrite when local or sectional repair can restore intent, accuracy, comparison logic, tone, or readability. Record why any scope expansion is necessary.

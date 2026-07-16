---
name: seo-geo-content-auditor
description: Audit XMAKE or PlasticHubs manufacturing articles and blogs against a Plan content brief and live Top-5 SERP benchmark using hard brand, factual, benchmark-completeness, and originality gates; a 20-point SEO/GEO quality rubric; natural keyword review; commercial-bridge mode checks; information-gain comparison; structural-diversity checks; and publishing-readiness checks. Use for final quality verdicts, revision actions, red/yellow/green status, or pre-publication audits. Do not use to create the upstream strategy brief or draft a new article from scratch.
---

# SEO/GEO Content Auditor

## Owned Job

Decide whether a draft is ready, needs targeted revision, or requires substantial rework. Audit against the Plan brief and source evidence rather than a generic article template.

At activation, report `Route: Audit > seo-geo-content-auditor`, the audit/revision stage, and requested deliverable mode in one concise bilingual line.

## Workflow

1. Read [Content Brief Contract](references/content-brief-contract.md), [Audit Rubric](references/audit-rubric.md), [SERP Benchmark Review Rules](references/serp-benchmark-review-rules.md), and the supplied brief.
2. Identify public brand, content type, primary intent, primary keyword, and `COMMERCIAL_BRIDGE_MODE`.
3. Validate the Top-5 benchmark environment, five result records, exclusions/substitutions, status, ranking hypotheses, gaps, borrowable patterns, differentiation requirements, and originality guardrails.
4. Compare the draft against the benchmark for intent fit, essential coverage, gap closure, original information gain, and derivative-structure risk.
5. Test every `INTENT_COMPLETION_CRITERIA` item and locate the early core answer.
6. Compare the H2s with `SECTION_ROLE_MAP`; flag overlapping reader jobs and repeated selection logic.
7. Check task-specific readability, minimum length, and artifact-delivery requirements when supplied.
8. Check `REVISION_SCOPE` and `SOURCE_ELEMENTS_TO_PRESERVE`; require the smallest correction scope that resolves the defect.
9. Run hard gates before assigning points.
10. Score all eight rubric dimensions with evidence from the draft and benchmark.
11. List findings first, ordered `Blocker`, `High`, `Medium`, then `Low`.
12. Quote the smallest exact passage needed to identify each problem and provide a specific correction.
13. Preserve good sections. Produce a replacement outline only for Red status or when structure is the main Yellow-status defect.
14. Use [Audit Report Template](templates/audit-report-template.md) for the final bilingual report.

## Hard Gates

Any hard-gate failure forces Red status regardless of numerical score:

- Plastichubs/xmake appears in public copy, metadata, CTA, headings, image text, schema, or publishable notes.
- A third-party brand name, third-party URL, competitor link, `Source:` label, or external-research attribution appears in public copy without explicit approval.
- Public brand is mixed, wrong, or absent when the brief identifies one brand.
- PlasticHubs is assigned an unsupported non-plastic direct service.
- A material claim, citation, standard, certification, metric, tolerance, guarantee, safety statement, or competitor fact is fabricated or materially wrong.
- A critical claim cannot be traced because required evidence is missing and publication would create material technical, legal, or commercial risk.
- The article contradicts the primary user intent or promotes a service unrelated to the topic.
- `SERP_RESEARCH_REQUIRED=Yes` but the benchmark is missing, `Blocked`, materially incomplete, or falsely labeled `Validated`.
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
- Compare against the five benchmark pages. Reward useful pattern adaptation and gap closure; penalize stitched summaries and derivative structure.
- Treat ranking explanations only as hypotheses and reject unsupported causal claims.

## SPEAR, Comparison, And Tone Review

- Check for a 3-5 sentence SPEAR opening built around a specific engineering or sourcing consequence. Deduct heavily for definition-first or generic setup.
- For comparison content, map every core H2 to shared buyer criteria and confirm both options remain visible. A long one-sided section is acceptable only when it states how that detail changes the comparison.
- Check that the answer-first block helps the reader decide and does not rely on unsupported universal rules.
- Check DFM as concrete risk control, not as a generic marketing label.
- Enforce no more than three sentences per public paragraph while rejecting mechanical cadence or fragmented logic.
- Reject duplicate FAQ answers.
- Check every H2 for a distinct reader job. A decision matrix and later “when to choose” sections should be consolidated when they repeat the same criteria.
- Replace generic `Quick Answer`, `Fast Guide`, or `Rapid Decision` headings when they add no task meaning; do not penalize a factual discussion of speed.
- When `READABILITY_TARGET` exists, evaluate the English against it and check that technical terms are defined before use. When `MIN_WORD_COUNT` exists, verify the final word count without rewarding padding.
- Run a literal Tone Check for: `delve`, `embark`, `craft`, `crafting`, `unlock`, `discover`, `utilize`, `utilizing`, `dive deep`, `unveil`, `harness`, `elucidate`, `enlightening`, `esteemed`, `game-changer`, `skyrocket`, `revolutionize`, `disruptive`, `groundbreaking`, `cutting-edge`, `remarkable`, `powerful`, `world-class`, `real-world`, `shed light`, `imagine`, `realm`, `abyss`, `tapestry`, `illuminate`, `glimpse into`, `navigating`, `landscape`, `stark`, `testament`, `bustling`, `opened up`, `ever-evolving`, `you're not alone`, `in a world where`, `it remains to be seen`, `pivotal`, `intricate`, `hence`, `furthermore`, `however`, `moreover`, `in summary`, `in conclusion`, and `in closing`.
- Do not restore or reward Plastichubs/xmake public references, mixed brands, or unverified legacy metrics. Accurate qualifiers remain acceptable when process variability is real.

## Output Boundary

- Audit and prescribe; do not silently replace the entire article.
- If a section is sound, write `No change needed.`
- Proposed text must not introduce new unsupported claims.
- Proposed public text must not introduce third-party names, URLs, citations, or attribution. If a claim needs external attribution, remove or qualify it, use approved brand-owned evidence, or mark it `Needs approval`.
- Output Chinese first, English second.
- For paginated preview or Word delivery, verify the artifact rather than only the chat text. Render and inspect pages when supported; otherwise state that only structural QA was completed.
- Persist approved corrections to the artifact and do not claim Word-ready status when font, punctuation, tables, links, or page breaks were not visually checked.
- Do not recommend a full rewrite when local or sectional repair can restore intent, accuracy, comparison logic, tone, or readability. Record why any scope expansion is necessary.

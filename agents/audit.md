# Audit Agent

Owner: `seo-geo-content-auditor`

Start here when the user supplies an article. Audit the available artifact first; do not force a new Plan run merely because a formal brief is missing.

Classify defects by origin:

- `audit_local`: correction can be made in audit notes without article revision.
- `info_rollback`: prose, technical explanation, structure execution, tone, link placement, or metadata deviates from an otherwise valid strategy.
- `plan_rollback`: search intent, primary service, keyword, audience, outline logic, evidence plan, comparison dimensions, or commercial mode is defective or absent and materially changes the article.
- `blocked`: user authority, regulated evidence, brand choice, or required approval is missing.

Only Green or an explicitly accepted equivalent may continue to B2B Image.

GREEN also requires a complete Top-10 reference contract, faithful high-level structure/style adaptation, justified module selection, a visible topic-specific FAQ, a visible actionable CTA with a direct same-brand URL, verified internal links, and a cross-article similarity result showing that the draft does not repeat a recent same-brand house pattern without query evidence.

GREEN also requires a complete independent `section-alignment-audit.json`. Compare every actual H2, in order, against `SECTION_REFERENCE_MAP`; state the heading-implied reader question, first-paragraph answer, full-section answer, and Top-10 structure pattern. Run `scripts/validate_heading_content_alignment.py`; missing evidence or any semantic `FAIL` blocks GREEN.

Run `scripts/validate_blog_narrative_quality.py` with the accepted Plan and exact article. Treat a tone or execution failure as `info_rollback`; treat a defective Plan sequence/scope contract as `plan_rollback`.

Do not treat zero identical H2s or zero exact phrase overlap as proof of diversity. Compare semantic section roles, section-count/length distribution, heading grammar, paragraph cadence, evidence pattern, FAQ construction, CTA position/wording, and ending form against `REFERENCE_SHAPE_FINGERPRINT` and the recent corpus.

Treat missing per-page Top-10 analysis, mismatched intent/audience/format distributions, a non-passing Plan gate, an unapproved intent/format deviation, a missing FAQ, or a missing/non-actionable CTA as hard failures. Audit cannot retroactively approve the planner's alternative or issue GREEN.

Also hard-fail an unresolved Google verification/tool-permission state or a `Best-effort` benchmark without explicit user downgrade approval evidence.

If intent, Top-10 classification, selected reference, article format, archetype, or rhythm contract is defective, return to Plan and replay Info plus Audit. If execution, heading hierarchy, title alignment, opening answer timing, English, comprehension load, FAQ, CTA, or corpus diversity is defective, return to Info and re-run Audit. RED cannot advance to Final Output.

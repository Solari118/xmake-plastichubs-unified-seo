---
name: seo-content-performance-review
description: Review published XMAKE or PlasticHubs articles at 30, 60, or 90 days using dated Google Search Console, GA4, Semrush, indexation, internal-link, article-archetype, and reference-mode evidence. Use for post-publication SEO performance diagnosis, query and CTR analysis, content-history or cannibalization review, archetype comparison, refresh decisions, and evidence-backed rollback to Plan, Info, or Final Output. Do not manage backlink outreach or invent unavailable analytics.
---

# SEO Content Performance Review

## Owned Job

Determine whether a published article's intent, archetype, structure/style reference choice, content execution, metadata, internal links, indexation, or conversion path needs revision.

At activation, report `Route: Performance Review > seo-content-performance-review`, review day, evidence status, and deliverable in one concise bilingual line.

## Workflow

1. Read [Performance Review Contract](references/performance-review-contract.md).
2. Require the published URL, publication date, final Plan/Info metadata, article archetype, structure-reference mode, and internal-link manifest.
3. Load dated GSC, GA4, and available Semrush evidence. Use `Missing evidence` for unavailable metrics.
4. Select the 30-, 60-, or 90-day review branch. Do not judge a new page by a later-stage standard.
5. Evaluate indexation/canonical status, impressions, clicks, CTR relative to position, query coverage, average position, conversions, internal-link behavior, content history, cannibalization, and competing-page movement.
6. Compare results with relevant same-brand articles grouped by article archetype and `single` versus `multi-source` reference mode. Do not compare unrelated intents as if they were equivalent.
7. Diagnose the smallest origin:
   - intent, keyword, archetype, reference selection, competition, or cannibalization → `Plan`;
   - title, introduction, structure execution, evidence, module, CTA, or article answer → `Info`;
   - broken/weak deployed links, canonical, metadata injection, or package defect → `Final Output`;
   - unavailable data → `WAITING_FOR_PERFORMANCE_DATA`.
8. Create a versioned review artifact using `../../schemas/performance-review.schema.json`.

## Gates

- Backlink acquisition and outreach are excluded and remain user-managed.
- Do not claim exact keyword difficulty, authority, CTR cause, conversion cause, or ranking cause without measured evidence.
- Separate facts, hypotheses, and recommended tests.
- Do not rewrite a successful article merely because it differs from the current house style.
- Preserve the selected reference structure/style when it performs; change it only when evidence identifies a specific defect.

## Output Contract

Return:

- review day and data window;
- evidence status and missing inputs;
- metric and query summary;
- indexation, CTR, content, archetype, reference-mode, internal-link, and conversion diagnosis;
- comparison with relevant same-brand articles;
- smallest recommended route and acceptance criteria;
- next review date when applicable.

Use Chinese first and English second. A review without usable dated data stops at `WAITING_FOR_PERFORMANCE_DATA`.


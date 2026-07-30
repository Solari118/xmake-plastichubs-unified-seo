# Google Top-10 SERP And Reference Selection Workflow

## Search Definition

Record the exact keyword, Google locale, language, device assumption, capture date, target content type, and intent.

When Google presents a CAPTCHA, consent wall, unusual-traffic page, or another verification challenge:

1. open the exact query in the in-app browser;
2. preserve the query, locale, language, device assumption, and capture date;
3. ask the user to complete the visible verification;
4. set `SERP_ACCESS_STATUS=google-verification-required`, `USER_BROWSER_VERIFICATION_STATUS=pending`, and `PLAN_GATE_STATUS=WAITING_FOR_USER_BROWSER_VERIFICATION`;
5. resume the same Google query only after the user confirms completion.

When browser/search access is blocked by a permission or sandbox boundary, identify the exact permission or capability required, set `SERP_ACCESS_STATUS=tool-permission-required`, and stop at `WAITING_FOR_TOOL_PERMISSION`.

Do not silently replace either condition with another engine, API-derived rankings, or a `Best-effort` pack. Use `Best-effort` only after the user explicitly approves the downgrade and the brief records `SERP_ACCESS_STATUS=best-effort-approved`, `BEST_EFFORT_DOWNGRADE_APPROVAL=approved`, and the approval evidence.

## Result Set

Capture the first ten relevant non-sponsored organic editorial/blog pages.

- Preserve observed positions.
- Record ads, tools, category pages, duplicates, inaccessible pages, and intent mismatches before substituting.
- When the first ten organic results contain fewer than ten relevant editorial/blog pages, continue downward only to fill the benchmark and label each substitute with its observed position and reason.
- A final-labeled brief requires ten analyzed pages or a transparent `Blocked` status.

## Per-Page Record

Capture:

1. position, title, URL, domain, type, author/date when visible;
2. title/H1 and intent alignment;
3. H1/H2/H3 hierarchy, the reader job at each level, H2/H3 sequence, and information order;
4. opening mode, opening length, and the exact point where the core search need is answered;
5. narrative stance, pacing, section proportions, paragraph rhythm, transitions, technical tone, English naturalness, comprehension load, AI-pattern risks, and ending form;
6. reasoning, examples, entities, conditions, and limitations;
7. evidence, citations, original data, expertise signals, media, tools, internal links, and whether tables/lists are used, what they do, and where they appear;
8. commercial integration and CTA position;
9. strongest elements, weak elements, uncovered needs, and plausible ranking contributors labeled as hypotheses.

Do not infer backlinks, engagement, authority, CTR, or keyword difficulty without measured evidence.

After all ten records are complete, count the intent, primary audience, and content-format classifications. Record the distributions and highest-count classifications. Do not replace this count with an impressionistic persona statement.

## Required Site And Competition Context

Before selecting the new article shape, evaluate:

- dominant and secondary search intent;
- site authority context using available GSC, Semrush, indexed topical coverage, or clearly labeled qualitative evidence;
- existing same-brand pages, content history, cannibalization, canonical and indexation risk;
- keyword difficulty evidence from supplied or connected data;
- CTR context from existing GSC data or SERP title/snippet hypotheses;
- competing-page strength: domain/page relevance, freshness, evidence, tools, media, usability, and information gain;
- verified same-brand internal-link opportunities.

Backlink acquisition is excluded from this workflow.

## Reference Selection

Select one primary structure/style/rhythm controller and zero or more secondary pattern references.

- Use `single` when one page best matches intent and its architecture can be adapted without derivative copying.
- Use `multi-source` when multiple pages contribute compatible functions.
- Select for intent fit, useful structure, pacing, evidence form, style suitability, and adaptation value—not position alone.
- Record what each reference contributes and what must not be copied.
- Do not average the ten pages into a generic house outline. The primary controller supplies the dominant rhythm and macro logic; secondary references may add only named, bounded functions.

## Article Archetype

Choose diagnostic, comparison, failure investigation, material experiment, procurement guide, cost decision, case-led analysis, technical encyclopedia, engineering decision guide, or a justified custom type.

Compare the selected primary intent and governing content format with the dominant classifications. Differentiation within the dominant route may proceed. A different primary intent or governing format requires a compact user proposal covering expected gain, ranking risk, audience effect, and measurement plan. Stop at `WAITING_FOR_INTENT_APPROVAL` until that specific alternative is explicitly approved.

## Adaptation Contract

Produce:

- `STRUCTURE_ADAPTATION_MAP`: reference function → original module → new information gain;
- `STYLE_PROFILE`: high-level opening, stance, pacing, rhythm, evidence density, examples, transitions, tone, ending;
- `REFERENCE_SHAPE_FINGERPRINT`: hierarchy, title alignment, answer timing, narrative order, section proportions, heading grammar, cadence, table/list placement, FAQ/CTA placement, ending, complexity, English naturalness, and AI-pattern risks;
- `ARTICLE_RHYTHM_ROUTE`: primary controller, bounded secondary contributions, rationale, and anti-convergence guard;
- `MANDATORY_MODULES`, `OPTIONAL_MODULES`, `MODULES_TO_OMIT`;
- mandatory `FAQ_PLAN` and visible actionable `CTA` for every Blog;
- verified `INTERNAL_LINK_DEPLOYMENT`.

Borrow functional structure and high-level style characteristics. Do not copy prose, distinctive headings, proprietary cases, unique tables, or an identifiable author's expression.

Save the Plan handoff as machine-readable JSON and run `scripts/validate_plan_gate.py`. A title-only list, incomplete page record, distribution mismatch, unresolved browser verification, unapproved `Best-effort` downgrade, or unapproved intent/format deviation cannot pass.

---
name: xmake-plastichubs-website-ops
description: Produce and package XMAKE or PlasticHubs website pages with brand separation, technical claim control, page-type templates, WordPress-ready blocks, and approved-content publishing metadata. Use for service, surface-finishing, material, industry, solution, hub, FAQ, and approved-draft packaging tasks. Do not use for SEO/GEO content planning, first-draft editorial blog writing, or final content quality audits.
---

# XMAKE/PlasticHubs Website Operations

## Owned Job

Create buyer-facing operational website pages and package approved content for publishing. Strategy briefs belong to the planner; editorial blog drafts belong to the Info writer; final quality verdicts belong to the Audit reviewer.

At activation, report `Route: Website Ops > xmake-plastichubs-website-ops`, the output stage, and requested deliverable in one concise bilingual line.

## Workflow

1. Identify `BRAND`, page type, output stage, deliverable mode, preview format, and source pack.
2. Read [Manufacturing Claims Control](references/manufacturing-claims-control.md), [Delivery And Variation Framework](references/delivery-and-variation-framework.md), and [Internal Link Deployment](references/internal-link-deployment.md), then load only the relevant brand, process, technical, keyword, and template references.
3. Establish process facts and claim boundaries.
4. Create the requested operational page, or package an approved article without changing its editorial argument, selected structure/style, or module choices unless asked.
5. Apply natural keyword/query coverage from [SEO Keyword Rules](references/seo-keyword-rules.md).
6. Run the relevant checks. Do not issue the final cross-project publish verdict.

## Brand And Evidence Boundary

- Public copy must name only XMAKE or PlasticHubs, according to `BRAND`.
- Plastichubs/xmake data may support internal reasoning as shared-supply-chain evidence. Never expose the Plastichubs/xmake name in public copy, metadata, CTAs, source notes intended for publication, or schema fields.
- Keep PlasticHubs focused on plastic CNC machining and supported plastic processes.
- Ordinary XMAKE manufacturing, finishing, self-operated factory, owned-equipment, engineering, inspection, and supply-chain capability are project-approved defaults. Lack of independently searchable Chinese factory or supplier records does not invalidate ordinary capability language.
- Use exact machine counts, areas, addresses, lead times, tolerances, certifications, guarantees, and capacity only when supported by current task inputs, project files, or approved official sources.
- Do not disclose supplier identities, routing relationships, or confidential upstream providers.
- Keep third-party sources and URLs in a private ledger marked `Internal — Not for Publication`. Public copy defaults to same-brand internal links.
- Treat legacy examples such as `20-40%`, `30%`, `20,000㎡`, `3-day`, machine counts, certifications, and AI-engine claims as unverified until current target-brand evidence supports the exact scope.

## Content Diversity And SEO

- Match structure to the page task. For `A vs B` content, keep both options visible under shared buyer criteria; do not package separate mini-guides that lose the comparison.
- Do not require exact-match keywords in a fixed list of positions.
- Use the primary topic naturally in page-defining elements when accurate; cover secondary terms, entities, questions, and buyer language where useful.
- Use a consequence-led opening and an answer-first decision aid for selection content.
- Use tables, FAQ, checklists, diagrams, and tools only when they improve the buyer's decision.
- Keep public paragraphs to three sentences maximum. Include FAQs only when they answer unresolved questions without duplicating the body.
- For batch or sibling pages, create a private variation plan before drafting: selected architecture, hero angle, first decision aid, evidence form, CTA placement, and modules to omit. Do not repeat the same architecture across consecutive pages unless the query requires it.
- Treat the surface-finishing template as a coverage library, not a fixed public outline. Each visible H2 must have a distinct buyer job.

## Output Stages

1. `Bilingual Review Draft`: Chinese first, English second.
2. `Paginated Preview`: create the requested preview format and inspect every page; a link alone is not visual QA.
3. `Publish-ready English`: only after review approval.
4. `WordPress-ready`: inject every approved internal link at its exact contextual location with the verified URL. Provide standard Markdown links and, when HTML is requested, use clickable `<a>` elements with `style="color:#5B9BD5;"`.
5. `Word-ready`: generate only after content approval; create real clickable hyperlink relationships, style internal-link text light blue `#5B9BD5`, and render/inspect fonts, punctuation, tables, headings, links, and page breaks.

Every full article package must contain at least three approved standalone images, each with a contextual placement and alt text. Three concepts, variants, or collage panels do not satisfy this gate.

Every final article package must include an internal-link manifest containing anchor, URL, source section, target relationship, validation status, and injected output formats. Do not deliver link suggestions separately when the user requested deployed links.

For approved blog packaging, use [Blog Article Publishing Template](templates/blog-article-template.md). For service-page Markdown, run `scripts/validate_surface_page.py <page.md>` and resolve errors.

Review Markdown must be readable stacked text with no raw layout HTML. Persist user-requested display and wording corrections to the source artifact. If rendering is unavailable, report structural QA only and do not claim visual verification.

## Non-Goals

- Do not create the upstream SEO/GEO brief.
- Do not draft a new editorial blog article from only a topic and keyword.
- Do not perform the final weighted audit or traffic-light verdict.
- Do not mention Plastichubs/xmake in publishable output.

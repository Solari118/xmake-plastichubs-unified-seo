# AGENTS.md instructions for XMAKE-PlasticHubs Unified SEO System

Mandatory: All responses must be bilingual: Chinese first, English second. Keep code, commands, URLs, file paths, formulas, quoted labels, and IDs unchanged when translation would reduce precision.

Give the result first. Be concise, evidence-aware, and direct. Challenge unsupported claims. Never invent citations, standards, certifications, exact metrics, keyword volumes, search rankings, or company capabilities.

## Unified Route

This project consolidates the previous `文章规划提示词-Plan`, `文章撰写提示词-Info`, and `文章优化提示词2.0-Aduit` projects into one XMAKE/PlasticHubs SEO system.

Start every non-trivial task with one concise bilingual route line:

- `Route: Plan > b2b-seo-topic-map-builder | Stage: Strategy Brief | Deliverable: [mode]`
- `Route: Info > manufacturing-blog-writer | Stage: Drafting/Revision | Deliverable: [mode]`
- `Route: Audit > seo-geo-content-auditor | Stage: Audit/Targeted Revision | Deliverable: [mode]`
- `Route: Website Ops > xmake-plastichubs-website-ops | Stage: [stage] | Deliverable: [mode]`
- `Route: SEO Core > xmake-plastichubs-seo-expert | Stage: Routing/Data Loading | Deliverable: [mode]`

When the user asks for the complete `Plan -> Info -> Audit` chain, run the stages sequentially. Keep each stage's owner, inputs, artifact, and gate visible. Do not claim Info or Audit passed before the actual artifact exists.

## Skill Ownership

- `xmake-plastichubs-seo-expert`: default router and data-loading coordinator for XMAKE/PlasticHubs SEO tasks.
- `seo-content-strategy`: campaign-level keyword research, content planning, topic map use, competitor and content-calendar strategy.
- `b2b-seo-topic-map-builder`: writer-ready Plan briefs, live Top-5 organic SERP benchmark, keyword/query maps, GEO answer plans, commercial-bridge mode, and topic architecture.
- `manufacturing-blog-writer`: Info-stage editorial article and blog drafting from a complete Plan brief.
- `manufacturing-content-writer`: package-provided manufacturing content writing reference; use only when it adds useful process/page writing rules not already covered by `manufacturing-blog-writer`.
- `seo-geo-content-auditor`: final Audit-stage quality verdict, brand/factual gates, SEO/GEO scoring, and targeted revision actions.
- `xmake-plastichubs-website-ops`: service, material, industry, solution, hub, FAQ, WordPress-ready, and approved-content packaging operations.

## Brand And Evidence Rules

- Select one public brand per artifact: XMAKE or PlasticHubs.
- Public copy, metadata, CTA text, headings, image text, schema, and publishable notes must not expose shared upstream supplier identities or legacy brand names.
- PlasticHubs remains plastic-manufacturing-first. XMAKE may use the broader supported manufacturing scope.
- Use project data, user input, official sources, standards, and primary technical evidence. Exact metrics, tolerances, certifications, lead times, guarantees, legal qualifications, and regulated claims require support.
- Keep third-party research, competitor URLs, and external source notes in private sections marked `Internal — Not for Publication` unless the user explicitly approves public attribution.
- Public links default to same-brand, same-domain internal links.

## Keyword Resource Rules

The PlasticHubs keyword source library is preserved at `data/plastichubs/keywords/`.

- Use `PlasticHubs_SEMrush_All_Keywords_Classified_2026-07-10.xlsx` for keyword selection, volume/KD support, content brief evidence, and keyword insertion candidates when relevant.
- Do not treat the workbook as exhaustive or mandatory when better current-task evidence exists.
- Do not use long-tail phrases as primary Semrush seed keywords by default; use them as page-intent or insertion evidence unless explicitly asked otherwise.
- Do not generate seed lists by mechanically appending broad modifiers such as `parts`, `manufacturer`, `supplier`, or `service` without exported-data support.
- Keep brand, claim-control, and source-boundary rules above keyword convenience.

## Planning Rules

For Plan work, use `skills/b2b-seo-topic-map-builder/SKILL.md`.

Minimum inputs: `BRAND`, `TOPIC`, and `PRIMARY_KEYWORD`. Ask only when brand ambiguity creates service-scope risk. Live Top-5 SERP benchmarking is required before marking a brief ready for final article production. If live search cannot be performed, label the brief `Blocked` or `Provisional`.

The final Plan artifact must include every handoff field required by `skills/b2b-seo-topic-map-builder/references/content-brief-contract.md`.

## Writing Rules

For Info work, use `skills/manufacturing-blog-writer/SKILL.md`.

Write from a complete Plan brief. Do not rebuild the upstream strategy when a valid brief exists. Use the declared `COMMERCIAL_BRIDGE_MODE`, satisfy every `INTENT_COMPLETION_CRITERIA`, preserve user-specified delivery constraints, and produce bilingual review drafts Chinese first, English second unless the user asks for approved publish-ready English.

## Audit Rules

For Audit work, use `skills/seo-geo-content-auditor/SKILL.md`.

Apply hard gates before scoring. Findings come first, ordered by severity. Audit against the Plan brief, source evidence, benchmark status, brand scope, and publishing contract. Do not silently rewrite acceptable sections.

## Website Ops Rules

For operational website pages, approved-content packaging, WordPress-ready output, and Word-ready output, use `skills/xmake-plastichubs-website-ops/SKILL.md`.

For Word/PDF/paginated previews, create the artifact and inspect the rendered pages before claiming visual QA. If rendering is unavailable, report structural QA only.

## Anti-AI Language Gate

Do not use or recommend public wording such as `delve`, `embark`, `craft`, `unlock`, `discover`, `utilize`, `dive deep`, `unveil`, `harness`, `game-changer`, `skyrocket`, `revolutionize`, `cutting-edge`, `world-class`, `shed light`, `imagine`, `realm`, `tapestry`, `navigating`, `landscape`, `ever-evolving`, `pivotal`, `intricate`, `hence`, `furthermore`, `moreover`, `in summary`, `in conclusion`, or `in closing`.

## Canonical And Mirror Policy

Canonical active skills live in `skills/`. Discovery mirrors live in `.agents/skills/` and `.codex/skills/`. Update canonical files first, then synchronize mirrors when changing project instructions.

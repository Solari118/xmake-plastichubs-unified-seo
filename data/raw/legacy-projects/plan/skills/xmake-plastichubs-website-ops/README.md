# Xmake-Plastichubs Website Operations Skill

This Codex skill helps generate and audit SEO-ready buyer-facing manufacturing website content for Xmake and Plastichubs.

Current stage: `prototype-baseline`. The package is structured for long-term use, but public production use should wait until real source documents, sample pages, human review, and batch tests are recorded.

It is designed for long-term use across:

- service pages
- surface finishing service pages
- plastic CNC machining pages
- material pages
- industry pages
- solution pages
- blog articles
- FAQ pages
- hub pages
- page audits
- SEO keyword workflows
- WordPress-ready content blocks

## Core Behavior

The skill must identify the page type before writing. It must keep Xmake and Plastichubs positioning separate, control unsupported claims, and include human verification notes when source evidence is missing.

It does not assume access to external documents, websites, previous conversations, uploaded files, or hidden source files. Add project-specific sources into `references/` before asking the skill to rely on them.

## Package Structure

```text
xmake-plastichubs-website-ops-skill/
├── SKILL.md
├── manifest.json
├── README.md
├── agents/
│   └── interface.yaml
├── references/
├── templates/
├── evals/
├── scripts/
└── reports/
```

## Usage

Use this skill when asking Codex to write, revise, or audit manufacturing website content for Xmake or Plastichubs.

Example request:

```text
Use xmake-plastichubs-website-ops to create a Plastichubs Plastic CNC Machining service page.
Brand: Plastichubs
URL: /plastic-cnc-machining/
Primary keyword: plastic CNC machining
Secondary keywords: custom plastic CNC parts, plastic CNC milling, plastic CNC turning
Source notes: [paste verified source material here]
```

Audit example:

```text
Use xmake-plastichubs-website-ops to audit this Xmake surface finishing page.
Page type: Page Audit Report
Brand: Xmake
Source page: [paste current page content]
Goal: identify sections to keep, revise, delete, merge, or move down.
```

## Future Source Workflow

When adding project-specific sources:

1. Use `references/source-ingestion-rules.md` to record source name, path, brand, source type, what it supports, what it cannot support, and claims requiring human verification.
2. Use `templates/project-source-pack-template.md` before generating or auditing a new group of pages.
3. Put brand positioning material in `references/xmake-positioning.md` or `references/plastichubs-positioning.md`.
4. Put manufacturing process notes in the relevant knowledge-base file.
5. Put reusable page structure in `templates/`.
6. Put quality gates in `evals/`.
7. Put review notes and batch decisions in `reports/output-review-log.md`.

For any future batch page project, including surface finishing when requested, add:

- sample service page template or approved reference page
- hub page or parent page when relevant
- target page names
- URLs
- primary keywords
- secondary keywords
- process notes
- capability boundaries

Then generate one sample page first. Review that page before batch-producing the remaining pages.

For specialized surface finishing pages only, use `templates/surface-finishing-input-sheet-template.md` to capture URL, keywords, substrates, process category, source documents, allowed claims, blocked claims, and human verification notes.

## Future Modules

Add future modules only when real reuse appears:

- material pages: expand `templates/material-page-template.md` and add material-specific source notes
- industry pages: expand `templates/industry-page-template.md` with buyer use cases and claim boundaries
- blogs: expand `templates/blog-article-template.md` with editorial rules and citation expectations
- SEO maps: add keyword clustering rules to `references/seo-keyword-rules.md`
- WordPress blocks: expand `templates/wordpress-ready-block-template.md` with block naming and HTML constraints

## Validation

Before relying on this skill for batch output, review:

- `evals/page-quality-checklist.md`
- `evals/seo-checklist.md`
- `evals/technical-accuracy-checklist.md`
- `evals/claim-risk-checklist.md`
- `evals/brand-consistency-checklist.md`

This package is a prototype baseline. It should be validated against real Xmake and Plastichubs source documents, one approved sample page, and human review before public publishing or batch production.

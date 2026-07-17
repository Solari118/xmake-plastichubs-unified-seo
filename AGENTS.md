# Unified Manufacturing Content Project

Mandatory: all user-facing responses are bilingual, Chinese first and English second. Keep code, commands, URLs, paths, formulas, quoted labels, and IDs unchanged when translation would reduce precision.

## Canonical Route

Start every non-trivial manufacturing content task with:

`Route: Manufacturing Content Pipeline > Plan → Info → Audit → B2B Image → Final Output | Stage: [stage] | Deliverable: [mode]`

Use `skills/manufacturing-content-pipeline/SKILL.md` as the only top-level article router. Specialist skills own their phases and must not absorb another phase's role.

## Entry-Point Behavior

- A complete article, blog, revision-to-publication, or content-package request defaults to the full ordered pipeline.
- A request received from any legacy Plan, Info, Audit, or B2B Image workspace must route here first.
- A user may explicitly request a phase-only task. Run only that phase after checking its prerequisites and label the terminal state accurately.
- A standalone image generation or retouch request remains B2B Image-only. An article-linked image request requires the audited article and visual brief.
- Never skip directly to final packaging without an Audit artifact. Never call a writer self-check the final Audit verdict.

## Ordered Stages

1. `Plan` — `b2b-seo-topic-map-builder`: strategy brief, live Top-5 SERP benchmark, primary service, link plan, evidence boundary.
2. `Info` — `manufacturing-blog-writer`: article draft from the accepted Plan artifact.
3. `Audit` — `seo-geo-content-auditor`: independent hard gates, findings, verdict, and bounded revision request.
4. `B2B Image` — `b2b-machining-image-generator`: visual brief and independent article assets from the audited article.
5. `Final Output` — `xmake-plastichubs-website-ops` plus the appropriate document workflow: final article package, metadata, image placement, alt text, WordPress and/or verified Word output.

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

## Completion Truth

Valid terminal states are `COMPLETED`, `PHASE_COMPLETED`, `WAITING_FOR_KEYWORD_APPROVAL`, `REVISION_REQUIRED`, and `BLOCKED`.

`COMPLETED` requires all requested artifacts, a passing final Audit, truthful image-generation status, and the requested final-output QA. If `.docx` or paginated rendering cannot be visually inspected, use `Structural QA Only` and do not claim Word-ready status.

## Canonical And Compatibility Policy

- Canonical skills live in `skills/`.
- Discovery mirrors live in `.agents/skills/` and `.codex/skills/`; update them only through `scripts/sync_mirrors.py`.
- Legacy workspaces contain adapters to this root and retain their former instructions as `AGENTS.legacy.md`.
- Run `python scripts/validate_project.py` before release or after changing routing, contracts, adapters, or mirrors.


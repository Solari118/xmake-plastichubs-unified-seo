---
name: b2b-seo-topic-map-builder
description: Build writer-ready B2B manufacturing SEO/GEO content briefs with live Top-5 organic SERP benchmarking, competitor-article structure analysis, keyword and query maps, audience and intent analysis, controlled Factory-Direct versus broker positioning, differentiation requirements, and pillar/supporting-page topic maps for XMAKE and PlasticHubs. Use when the user supplies a topic and primary keyword, requests a Content Strategy Blueprint, keyword filling, competitor-content analysis, GEO answer planning, content clusters, or CSV/HTML topic maps. Do not use to draft articles or perform final content audits.
---

# B2B SEO/GEO Content Planner

## Owned Job

Convert a manufacturing topic and primary keyword into a complete brief that the Info writer can execute and the Audit reviewer can evaluate. Keep the work strategic; do not draft article body copy.

At activation, report `Route: Plan > b2b-seo-topic-map-builder`, the current stage, and requested deliverable mode in one concise bilingual line.

## Core Workflow

1. Confirm or infer `BRAND`, `TOPIC`, and `PRIMARY_KEYWORD`. Ask only if brand ambiguity creates a service-scope risk.
2. Read [Company Assets](references/company-assets.md), [Content Brief Contract](references/content-brief-contract.md), [SEO/GEO Planning Rules](references/seo-geo-planning-rules.md), and [Top-5 SERP Benchmark Workflow](references/serp-top-five-workflow.md).
3. Search the project for relevant XMAKE, PlasticHubs, AI Prompt Data, Info, Roundup, technical, and process knowledge files. Load only relevant sources.
4. Classify content type, primary and secondary intent, decision stage, target market, and conversion goal.
5. Run the live Top-5 SERP benchmark before finalizing the brief. Record observed positions and URLs, analyze each article, distinguish ranking hypotheses from facts, and derive common strengths, gaps, borrowable patterns, and differentiation requirements.
6. Build the keyword/query map: primary keyword, secondary candidates, natural query variants, buyer modifiers, questions, and entities. Never invent volume, CPC, difficulty, or live rankings.
7. Define the persona's technical goal, information void, failure risk, and required information gain.
8. Define `INTENT_COMPLETION_CRITERIA`, choose `ANSWER_FIRST_FORMAT`, and create a `SECTION_ROLE_MAP` with one distinct reader job per H2. Merge sections that would repeat the same selection logic.
9. Carry forward user-set `MIN_WORD_COUNT`, `READABILITY_TARGET`, `DELIVERABLE_MODE`, `PREVIEW_FORMAT`, `WORD_STYLE_REFERENCE`, `REVISION_SCOPE`, and `SOURCE_ELEMENTS_TO_PRESERVE` without turning them into universal defaults.
10. Select `COMMERCIAL_BRIDGE_MODE`: `none`, `soft`, or `explicit`. Match its intensity to the intent instead of forcing the same broker section into every brief.
11. Build the GEO answer plan: direct-answer targets, fan-out questions, evidence requirements, quotable facts, and entity disambiguation. Treat these as content-quality tactics, not guaranteed ranking factors.
12. Recommend a differentiated architecture that uses useful SERP patterns without copying any one competitor's expression or outline and without exposing competitor names or URLs in public copy.
13. Run [Brief Quality Checklist](evals/brief-quality-checklist.md) before handoff.

## Brand And Evidence Boundary

- Published copy and writer-facing brand language must mention only XMAKE or PlasticHubs, according to `BRAND`.
- RapidDirect data may be used internally as shared-supply-chain evidence. Do not expose the RapidDirect name in public copy, metadata, CTAs, or commercial hooks.
- Shared data does not need public source attribution to RapidDirect. It must still be relevant to the selected brand, applicable to the service scope, and supported by the project knowledge base.
- PlasticHubs remains plastic-manufacturing-first. XMAKE may cover the broader verified manufacturing scope.
- Ordinary XMAKE manufacturing, finishing, self-operated factory, owned-equipment, engineering, inspection, and supply-chain capability are project-approved defaults. Lack of independently searchable Chinese factory or supplier records does not invalidate those general capability statements.
- Do not invent or generalize exact figures, standards, tolerances, guarantees, or certification scope.

## SPEAR And Comparison Blueprint Protocol

- Define a precise senior-engineer or sourcing persona, the part or program they are trying to deliver, and a concrete `3 AM` failure risk.
- Make `COMMERCIAL_HOOK` a one-sentence `SPEAR Hook Concept` that directs a 3-5 sentence consequence-led opening. Do not open with definitions.
- Require an answer-first table or checklist for selection queries.
- For comparison content, set shared `COMPARISON_DIMENSIONS` in the architecture and require every core H2 to compare both options on the same buyer criterion or explicitly state how a one-sided technical detail changes the choice.
- Plan DFM as risk control before quote or production, naming the defect, rework, delay, or acceptance failure it is meant to prevent.
- Keep public paragraphs to three sentences maximum. Use Markdown tables for actual comparative data and verified specifications, not as decoration.
- Plan 5-7 non-duplicative FAQs only when unresolved queries remain.
- Use factory-direct or broker contrast only under `soft` or `explicit` mode and only when relevant to the reader's decision.
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
## 3. Top-5 SERP Benchmark
## 4. Keyword And Query Map
## 5. Information Gain And GEO Answer Plan
## 6. XMAKE/PlasticHubs Commercial Bridge
## 7. Flexible Content Architecture
## 8. Evidence And Publishing Requirements
## 9. Ready-to-Copy Project Inputs
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
- Use observed organic positions only. Exclude ads and clearly document intent-mismatched, inaccessible, duplicate, or substituted results.
- Do not describe ranking hypotheses as proven causes.
- Do not copy competitor prose, distinctive headings, examples, tables, or a single competitor's full outline.
- Mark unvalidated keyword candidates and SERP assumptions explicitly.
- Do not draft article body copy, perform line editing, or issue a publish verdict.
- Do not create a commercial section merely to satisfy a template.
- Do not prescribe a universal word count; scope follows decision complexity and information completeness.

## Final Gate

Confirm that the brief is bilingual when project instructions apply, every required handoff field exists, the selected brand is clean, RapidDirect is absent from public variables, keyword use is non-mechanical, commercial intensity matches the declared mode, intent completion is testable, section roles do not overlap, and user-set readability or delivery constraints are preserved.

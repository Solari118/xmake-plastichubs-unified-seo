# Artifact-Aware Route Policy

## First Principle

Route from the latest artifact that can be verified, not from the workspace name and not automatically from Plan.

## Entry Rules

1. A topic, keyword, or blank-page article request starts at Plan.
2. A complete accepted Plan brief starts at Info.
3. A supplied article starts at Audit, even when it arrived through the Info or B2B legacy entry.
4. A Green audited article starts at B2B Image when visuals are missing, or Final Output when approved visuals already exist.
5. A standalone image or retouch request runs B2B Image only.
6. Explicit phase-only requests stop after the requested phase unless the user asks for downstream completion.
7. A published article with dated GSC/GA4 evidence starts at Performance Review. A review request without usable data stops at `WAITING_FOR_PERFORMANCE_DATA`.

## Audit Rollback Decision

Audit examines the supplied article before requesting upstream work.

- Return to Info when the strategy can remain: technical explanation, prose, redundancy, missing decision rule, comparison execution, tone, metadata, CTA, link placement, or paragraph quality.
- Return to Plan when the article's intent, keyword, audience, primary service, outline logic, evidence requirements, comparison dimensions, brand scope, commercial mode, or SERP differentiation is materially wrong or missing.
- Ask the user only when the missing choice changes brand, legal/regulated scope, primary keyword approval, proprietary facts, or the requested deliverable.

After rollback, replay all affected stages. A Plan repair requires Info and Audit again; an Info repair requires Audit again. Image and Final Output always consume the last Green audited article.

## Plan Evidence Order

After keyword approval, Plan must run in this order:

1. capture Google Top-10 relevant organic editorial/blog results;
2. if Google requires visible verification, open the exact query in the in-app browser and stop at `WAITING_FOR_USER_BROWSER_VERIFICATION`; if tool or sandbox permission blocks access, state the exact permission and stop at `WAITING_FOR_TOOL_PERMISSION`;
3. resume the same query after user verification, or use `Best-effort` only after recording explicit downgrade approval;
4. complete the per-page intent, audience, format, structure, style, pacing, evidence, commercial, strength, gap, and ranking-hypothesis record;
5. calculate dominant intent, audience, and content format from all ten records;
6. evaluate site authority context, indexation/canonical risk, keyword difficulty evidence, CTR context, site content history/cannibalization, internal-link inventory, and competing-page strength;
7. select one or more structure/style references from the Top-10;
8. choose the article archetype and compare the selected intent/format with the dominant route;
9. if either differs, present the alternative-angle tradeoff and stop at `WAITING_FOR_INTENT_APPROVAL` until the user explicitly approves;
10. produce the structure-adaptation map, style profile, module selection, differentiation, and verified link deployment;
11. run the deterministic Plan gate and enter Info only on `PASS`.

Top-10 research without a selected executable structure/style reference is incomplete.

## No Hidden Restart

Do not silently rebuild Plan for every article. Record the Audit finding that justified an upstream rollback and the artifact version that replaced the prior one.

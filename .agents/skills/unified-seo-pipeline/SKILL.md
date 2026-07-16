---
name: unified-seo-pipeline
description: "Route PlasticHubs and XMAKE content requests through SEO Core, Plan, Info, Audit, B2B industrial image generation, and WordPress/Word packaging in one execution. Use when a user provides a keyword, asks for a complete blog package, requests keyword analysis followed by article production, or needs the four formerly separate projects coordinated. Pause only for approval of agent-proposed keywords or for a hard evidence or permission blocker."
---

# Unified SEO Pipeline

## Purpose

Coordinate the complete content production path in one task. This skill is orchestration logic; specialist skills remain the owners of planning, writing, auditing, image generation, and document packaging.

## Decision Tree

1. Identify `BRAND`, `TOPIC`, `PRIMARY_KEYWORD`, output mode, and any user-set constraints.
2. Load `config/live-seo-data-source.yaml`, then load only the brand-relevant data and the current official pages needed for the claim set.
3. For every user-supplied primary keyword, attempt the configured authenticated live keyword source before using the local keyword library. The live lookup is read-only.
4. Record the database, locale, language, device assumption, capture date, source status, and any source limitation. Never infer missing volume, KD, ranking, trend, or SERP-feature values.
5. If the user supplied `PRIMARY_KEYWORD`, set `keyword_gate: bypassed_by_user`.
6. If no primary keyword exists, Plan may propose candidates. Set `terminal_state: WAITING_FOR_KEYWORD_APPROVAL` and stop after the Plan recommendation.
7. If the user asks for keyword analysis but does not ask for article production, return the Plan artifact only unless the user has already requested the complete chain in the same task.
8. For the full chain, execute each stage in order and pass actual artifacts forward.

## Stage Contract

| Stage | Skill | Input | Output | Continue condition |
|---|---|---|---|---|
| 0 | `xmake-plastichubs-seo-expert` | task + brand | route/data selection | brand scope is safe |
| 0.5 | authenticated live SEO source | keyword + market settings | current keyword/SERP evidence | source is available, otherwise apply fallback policy |
| 1 | `b2b-seo-topic-map-builder` | topic + primary keyword | writer-ready Plan brief | keyword gate resolved |
| 2 | `manufacturing-blog-writer` | Plan brief | bilingual review or English article | Plan artifact exists |
| 3 | `seo-geo-content-auditor` | Plan + article + evidence | findings, verdict, revision artifact | no unresolved hard gate |
| 4 | `b2b-machining-image-generator` | final article + visual requirements | independent image files and prompts | image constraints are accurate |
| 5 | `xmake-plastichubs-website-ops` + document workflow | final article + images | WordPress-ready and/or `.docx` | QA status is recorded |

## Approval State Machine

Use these states exactly:

```text
START
  -> KEYWORD_USER_SUPPLIED
  -> PLAN
  -> INFO
  -> AUDIT
  -> ASSET
  -> PACKAGE
  -> COMPLETED

START
  -> KEYWORD_MISSING
  -> PLAN_KEYWORD_PROPOSAL
  -> WAITING_FOR_KEYWORD_APPROVAL
```

Do not ask for approval after `KEYWORD_USER_SUPPLIED`. Do not start `INFO`, `AUDIT`, `ASSET`, or `PACKAGE` from `WAITING_FOR_KEYWORD_APPROVAL`.

## Artifact Requirements

- Live data trace: record `LIVE_DATA_STATUS` as `Validated`, `Degraded`, or `Unavailable`; source name; exact query; database; locale; language; device assumption; capture date; available metrics; and fallback used. Keep browser-session URLs, tokens, account details, and provider credentials out of artifacts.
- Plan: include the full content-brief contract, intent-completion criteria, SERP status, evidence boundary, and keyword decision.
- Info: write from the actual Plan brief; keep Chinese review before English when bilingual review is requested.
- Audit: findings first, hard gates before scoring, and no silent rewrite of acceptable copy.
- Asset: use the B2B machining skill for article visuals; generate separate files when multiple images are requested; no precision-certified drawings or unsupported measured labels.
- Package: include internal metadata, article body, image files, alt text, WordPress copy, and `.docx` when requested. Never expose private competitor research in publishable copy.

## Failure Handling

- `Validated`: live source returned the required current data for the declared query environment.
- `Degraded`: live source was authenticated but only some requested fields were available, or interactive control timed out after a query attempt. Use available values only and supplement from the local library with clear source separation.
- `Unavailable`: no authenticated live source, an expired session, a CAPTCHA, denied access, or a repeat browser-control failure before data could be read. Use the local library only where it contains relevant historic data; otherwise mark keyword metrics unavailable and continue only when the requested deliverable can remain evidence-safe.
- `BLOCKED`: missing evidence, unavailable required tool, unsafe brand ambiguity, or denied permission that prevents the requested artifact.
- `WAITING_FOR_KEYWORD_APPROVAL`: only for agent-proposed primary keywords.
- `COMPLETED`: every requested artifact exists and its QA status is truthful.

## Scheduler Interface

Read `config/article-schedule.yaml` when a task is invoked by a scheduler. The scheduler may supply a fixed keyword or a pre-approved topic queue. A scheduled invocation must not silently approve new keyword candidates.

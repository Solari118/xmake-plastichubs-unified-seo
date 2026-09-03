# SEO/GEO Content Brief Contract

Use these exact field names for the Plan to Info to Audit handoff.

## Required Fields

```text
BRAND:
CONTENT_TYPE:
TARGET_MARKET:
LANGUAGE:
TOPIC:
PRIMARY_SERVICE:
PRIMARY_KEYWORD:
SECONDARY_KEYWORDS:
QUERY_VARIANTS:
KEY_ENTITIES:
AUDIENCE:
PRIMARY_INTENT:
SERP_INTENT_DISTRIBUTION:
DOMINANT_SERP_INTENT:
SERP_AUDIENCE_DISTRIBUTION:
DOMINANT_AUDIENCE:
SERP_FORMAT_DISTRIBUTION:
DOMINANT_CONTENT_FORMAT:
SELECTED_PRIMARY_INTENT:
SELECTED_CONTENT_FORMAT:
SELECTED_CONTENT_ANGLE:
ANGLE_ALIGNMENT_STATUS: aligned | alternative-approved | approval-required
INTENT_CHANGE_PROPOSAL:
USER_INTENT_APPROVAL: not-required | approved | pending
USER_INTENT_APPROVAL_EVIDENCE:
PLAN_GATE_STATUS: PASS | WAITING_FOR_INTENT_APPROVAL | WAITING_FOR_USER_BROWSER_VERIFICATION | WAITING_FOR_TOOL_PERMISSION | BLOCKED
SECONDARY_INTENT:
INTENT_COMPLETION_CRITERIA:
DECISION_STAGE:
TECHNICAL_GOAL:
THREE_AM_PAIN_POINT:
INFORMATION_VOID:
INFORMATION_GAIN:
COMMERCIAL_BRIDGE_MODE: none | soft | explicit
COMMERCIAL_HOOK:
GEO_ANSWER_TARGETS:
OPENING_MODE:
ANSWER_FIRST_FORMAT: # legacy compatibility only; use Not applicable unless an answer-first opening is selected
SECTION_ROLE_MAP:
SECTION_REFERENCE_MAP:
ARTICLE_ARCHETYPE:
STRUCTURE_REFERENCE_MODE: single | multi-source
PRIMARY_STRUCTURE_REFERENCE:
SECONDARY_PATTERN_REFERENCES:
STRUCTURE_ADAPTATION_MAP:
STYLE_PROFILE:
REFERENCE_SHAPE_FINGERPRINT:
ARTICLE_RHYTHM_ROUTE:
MANDATORY_MODULES:
OPTIONAL_MODULES:
MODULES_TO_OMIT:
FAQ_PLAN:
RECENT_ARTICLE_COMPARISON_SET:
EVIDENCE_REQUIREMENTS:
INTERNAL_LINK_TARGETS:
CROSS_SERVICE_LINK_PLAN:
INTERNAL_LINK_INVENTORY:
INTERNAL_LINK_DEPLOYMENT:
LINK_VALIDATION_STATUS:
EXTERNAL_SOURCE_REQUIREMENTS:
CTA:
SCHEMA_TYPE:
TOOL_NEEDED:
READABILITY_TARGET:
MIN_WORD_COUNT:
DELIVERABLE_MODE:
PREVIEW_FORMAT:
WORD_STYLE_REFERENCE:
REVISION_SCOPE: local | sectional | full | Not applicable
SOURCE_ELEMENTS_TO_PRESERVE:
KEYWORD_VALIDATION_STATUS:
KEYWORD_DIFFICULTY_CONTEXT:
SITE_AUTHORITY_CONTEXT:
SITE_CONTENT_HISTORY:
INDEXATION_AND_CANONICAL_RISK:
CTR_CONTEXT:
COMPETITOR_PAGE_STRENGTH:
BACKLINK_SCOPE: Excluded — user-managed
SERP_RESEARCH_REQUIRED: Yes | No
SEARCH_ENGINE:
SEARCH_LOCALE:
SEARCH_LANGUAGE:
SEARCH_DEVICE:
SERP_QUERY:
SERP_CAPTURE_DATE:
SERP_BENCHMARK_STATUS: Validated | Best-effort | Blocked
SERP_ACCESS_STATUS: exact-positions-verified | google-verification-required | tool-permission-required | best-effort-approved | blocked
USER_BROWSER_VERIFICATION_STATUS: not-required | pending | completed
BEST_EFFORT_DOWNGRADE_APPROVAL: not-required | approved | pending
BEST_EFFORT_DOWNGRADE_APPROVAL_EVIDENCE:
TOP_TEN_SERP_RESULTS:
TOP_TEN_COMPLETENESS_STATUS: complete | incomplete | blocked
SERP_EXCLUSIONS_AND_SUBSTITUTIONS:
SERP_RANKING_HYPOTHESES:
SERP_COMMON_STRENGTHS:
SERP_CONTENT_GAPS:
BORROWABLE_PATTERNS:
PATTERNS_TO_AVOID:
DIFFERENTIATION_REQUIREMENTS:
ORIGINALITY_GUARDRAILS:
```

## Optional Publishing Fields

```text
EXISTING_URL:
CANONICAL_URL:
AUTHOR:
REVIEWER:
DATE_PUBLISHED:
DATE_MODIFIED:
FEATURED_IMAGE_REQUIREMENTS:
WECHAT_RESEARCH_STATUS: Not requested | Validated | Best-effort | Thin evidence | Blocked
WECHAT_BRAND_SCOPE:
WECHAT_SERVICE_UNIVERSE:
WECHAT_KEYWORD_EVIDENCE:
WECHAT_QUERY_PORTFOLIO:
WECHAT_DIMENSION_COVERAGE:
WECHAT_REFERENCE_PACK:
WECHAT_SELECTED_SOURCES:
WECHAT_REFERENCE_ADAPTATION:
WECHAT_RIGHTS_STATUS: research-only | owned | permission-confirmed
NOTES:
```

## Value Rules

- Use `Not provided` when the user or source pack has not supplied a value.
- Use `Not applicable` only when the field genuinely does not apply.
- Populate the `WECHAT_*` fields only when the user explicitly requests WeChat Official Account references. Record whether numeric volume/KD comes from Semrush and whether phrases come from live Google or project ontology. The WeChat pack supplements but does not replace `TOP_TEN_SERP_RESULTS`; default rights status is `research-only`.
- `SECONDARY_KEYWORDS` and `QUERY_VARIANTS` may contain planner-derived candidates, but `KEYWORD_VALIDATION_STATUS` must say whether they are user-provided, tool-validated, SERP-validated, or strategic candidates only.
- `COMMERCIAL_HOOK` must name only the selected brand and must match `COMMERCIAL_BRIDGE_MODE`.
- `PRIMARY_SERVICE` must name the main supported service for service-centered content. Use `Not applicable` only for genuinely brand-level, material-only, standards-only, or other non-service-centered topics.
- `CROSS_SERVICE_LINK_PLAN` must name the relationship, placement, same-brand destination, and accurate anchor approach for each cross-service link. Use `None` when no cross-service link improves the reader's task.
- `INTENT_COMPLETION_CRITERIA` must list observable questions or decisions that the article must resolve. Identify which one must be answered in the opening or first core section.
- `OPENING_MODE` must name the selected opening behavior from the reference adaptation, such as diagnostic scene, decision boundary, comparison frame, experiment result, case event, definition, or direct answer.
- `ANSWER_FIRST_FORMAT` is a legacy compatibility field only. Use `table`, `checklist`, `short prose`, `diagnostic flow`, `tool/calculator`, or `Not applicable` only when the selected reference and intent actually require answer-first behavior.
- `SECTION_ROLE_MAP` must assign one distinct reader job to each proposed H2. Merge modules that would repeat the same decision logic.
- `SECTION_REFERENCE_MAP` must define every planned public H2, including FAQ and CTA, with `planned_heading`, `section_kind`, `sequence_index`, `sequence_reason`, `heading_scope_mode`, selected Top-10 result positions and URLs, observed heading patterns and information order, `reader_question`, `first_paragraph_answer_requirement`, `body_scope`, `excluded_scope`, `adaptation_note`, and `originality_guard`. Every URL must belong to `TOP_TEN_SERP_RESULTS`. Abstract labels alone are invalid.
- `ARTICLE_ARCHETYPE` must follow the Top-10 intent and reference evidence rather than rotate randomly.
- `TOP_TEN_SERP_RESULTS` must contain exactly ten complete editorial/blog records. `SERP_INTENT_DISTRIBUTION`, `SERP_AUDIENCE_DISTRIBUTION`, and `SERP_FORMAT_DISTRIBUTION` must be calculated from those records rather than estimated separately.
- `SELECTED_PRIMARY_INTENT` and `SELECTED_CONTENT_FORMAT` may differ from the corresponding dominant classifications only after the user approves a specific `INTENT_CHANGE_PROPOSAL`. A general request for originality is not approval.
- `PLAN_GATE_STATUS=WAITING_FOR_INTENT_APPROVAL` stops the pipeline before Info. Only `PASS` is a valid Plan-to-Info handoff.
- `SERP_ACCESS_STATUS=google-verification-required` requires opening the exact query in the in-app browser and `PLAN_GATE_STATUS=WAITING_FOR_USER_BROWSER_VERIFICATION`. `SERP_ACCESS_STATUS=tool-permission-required` requires a precise permission request and `PLAN_GATE_STATUS=WAITING_FOR_TOOL_PERMISSION`.
- `PRIMARY_STRUCTURE_REFERENCE` and `SECONDARY_PATTERN_REFERENCES` must identify the chosen Top-10 record(s), selection reason, structure contribution, and high-level style contribution.
- `STRUCTURE_ADAPTATION_MAP` must map reference functions to original sections and state the added information gain. It must not authorize copied prose or a near-duplicate distinctive outline.
- `STYLE_PROFILE` must specify opening mode, narrative stance, pacing, paragraph rhythm, evidence density, example usage, transitions, technical tone, and ending form at a high level.
- `REFERENCE_SHAPE_FINGERPRINT` must record the selected reference's observable H1/H2/H3 hierarchy, title-to-section alignment, opening answer point, narrative sequence, section count and proportions, heading grammar, paragraph cadence, evidence density, table/list use and placement, FAQ/CTA position and form, ending form, comprehension load, English naturalness, and AI-pattern risks.
- `ARTICLE_RHYTHM_ROUTE` must name one primary rhythm controller and bound any secondary contributions. It must not average all ten results into a universal house cadence.
- Every Blog must place `FAQ` and `CTA` in `MANDATORY_MODULES`; neither may appear in `MODULES_TO_OMIT`. `FAQ_PLAN` must define 3–6 non-duplicative questions, their sources, heading, placement, answer guard, whether core sections may follow FAQ, the exact affected headings, a placement rationale, and supporting Top-10 URLs. `CTA` must define a topic-specific visible callout, selected-brand action, useful inputs, reader value, verified direct same-brand URL, and variation note. Tables, RFQs, failure modes, DFM, conclusions, and the exact FAQ/CTA position remain conditional.
- `RECENT_ARTICLE_COMPARISON_SET` must identify recent same-brand articles used to check opening, H2 order, evidence form, CTA placement, and image logic. Use the latest relevant set available; do not fabricate unavailable articles.
- `EVIDENCE_REQUIREMENTS` must identify exact claims, standards, statistics, or technical boundaries that need support.
- `READABILITY_TARGET`, `MIN_WORD_COUNT`, `DELIVERABLE_MODE`, `PREVIEW_FORMAT`, and `WORD_STYLE_REFERENCE` must preserve explicit user constraints. Use `Not provided` when absent; do not invent defaults or silently discard a requested artifact format.
- `REVISION_SCOPE` controls change breadth. `SOURCE_ELEMENTS_TO_PRESERVE` records sections, logic, voice, examples, or formatting the user wants retained. A local request must not silently become a full rewrite.
- `SCHEMA_TYPE` is a publishing recommendation such as `BlogPosting`, `Article`, or `Not applicable`; it is not a GEO guarantee.
- `TOP_TEN_SERP_RESULTS` must identify observed position, title, URL, domain, content type, intent fit, outline, opening strategy, pacing, evidence form, high-level style features, strengths, ranking hypotheses, and gaps for each result.
- `SERP_BENCHMARK_STATUS=Validated` requires a search source that exposes the specified locale, language, device, date, and organic positions.
- `SERP_BENCHMARK_STATUS=Best-effort` requires `SERP_ACCESS_STATUS=best-effort-approved`, `BEST_EFFORT_DOWNGRADE_APPROVAL=approved`, and explicit approval evidence. Never infer downgrade approval.
- `SERP_RANKING_HYPOTHESES` must remain hypotheses; do not present them as known search-engine causes.
- `BORROWABLE_PATTERNS` may include methods, coverage, evidence types, or decision logic. It must not authorize copying prose, distinctive headings, examples, tables, or a competitor's full outline.
- When `SERP_RESEARCH_REQUIRED=Yes`, `Blocked` status prevents final article output.
- `SITE_AUTHORITY_CONTEXT`, `SITE_CONTENT_HISTORY`, `INDEXATION_AND_CANONICAL_RISK`, `KEYWORD_DIFFICULTY_CONTEXT`, `CTR_CONTEXT`, and `COMPETITOR_PAGE_STRENGTH` are required evaluations. Use `missing evidence` when an exact metric is unavailable and state the compensating optimization.
- `INTERNAL_LINK_DEPLOYMENT` must include a verified same-brand URL, relationship, contextual anchor, planned section, and validation status for every link.
- `BACKLINK_SCOPE` must remain excluded from article production because the user manages outreach separately.

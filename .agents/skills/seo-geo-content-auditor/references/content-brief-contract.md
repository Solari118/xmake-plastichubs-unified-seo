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
ANSWER_FIRST_FORMAT:
SECTION_ROLE_MAP:
EVIDENCE_REQUIREMENTS:
INTERNAL_LINK_TARGETS:
CROSS_SERVICE_LINK_PLAN:
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
SERP_RESEARCH_REQUIRED: Yes | No
SEARCH_ENGINE:
SEARCH_LOCALE:
SEARCH_LANGUAGE:
SEARCH_DEVICE:
SERP_QUERY:
SERP_CAPTURE_DATE:
SERP_BENCHMARK_STATUS: Validated | Best-effort | Blocked
TOP_FIVE_SERP_RESULTS:
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
NOTES:
```

## Value Rules

- Use `Not provided` when the user or source pack has not supplied a value.
- Use `Not applicable` only when the field genuinely does not apply.
- `SECONDARY_KEYWORDS` and `QUERY_VARIANTS` may contain planner-derived candidates, but `KEYWORD_VALIDATION_STATUS` must say whether they are user-provided, tool-validated, SERP-validated, or strategic candidates only.
- `COMMERCIAL_HOOK` must name only the selected brand and must match `COMMERCIAL_BRIDGE_MODE`.
- `PRIMARY_SERVICE` must name the main supported service for service-centered content. Use `Not applicable` only for genuinely brand-level, material-only, standards-only, or other non-service-centered topics.
- `CROSS_SERVICE_LINK_PLAN` must name the relationship, placement, same-brand destination, and accurate anchor approach for each cross-service link. Use `None` when no cross-service link improves the reader's task.
- `INTENT_COMPLETION_CRITERIA` must list observable questions or decisions that the article must resolve. Identify which one must be answered in the opening or first core section.
- `ANSWER_FIRST_FORMAT` must be task-fit: `table`, `checklist`, `short prose`, `diagnostic flow`, `tool/calculator`, or `Not applicable`.
- `SECTION_ROLE_MAP` must assign one distinct reader job to each proposed H2. Merge modules that would repeat the same decision logic.
- `EVIDENCE_REQUIREMENTS` must identify exact claims, standards, statistics, or technical boundaries that need support.
- `READABILITY_TARGET`, `MIN_WORD_COUNT`, `DELIVERABLE_MODE`, `PREVIEW_FORMAT`, and `WORD_STYLE_REFERENCE` must preserve explicit user constraints. Use `Not provided` when absent; do not invent defaults or silently discard a requested artifact format.
- `REVISION_SCOPE` controls change breadth. `SOURCE_ELEMENTS_TO_PRESERVE` records sections, logic, voice, examples, or formatting the user wants retained. A local request must not silently become a full rewrite.
- `SCHEMA_TYPE` is a publishing recommendation such as `BlogPosting`, `Article`, or `Not applicable`; it is not a GEO guarantee.
- `TOP_FIVE_SERP_RESULTS` must identify observed position, title, URL, domain, content type, intent fit, outline, strengths, ranking hypotheses, and gaps for each result.
- `SERP_BENCHMARK_STATUS=Validated` requires a search source that exposes the specified locale, language, device, date, and organic positions. Otherwise use `Best-effort`.
- `SERP_RANKING_HYPOTHESES` must remain hypotheses; do not present them as known search-engine causes.
- `BORROWABLE_PATTERNS` may include methods, coverage, evidence types, or decision logic. It must not authorize copying prose, distinctive headings, examples, tables, or a competitor's full outline.
- When `SERP_RESEARCH_REQUIRED=Yes`, `Blocked` status prevents final article output.

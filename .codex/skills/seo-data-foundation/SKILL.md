---
name: seo-data-foundation
description: Normalize SEO evidence from GSC, GA4, Semrush, sitemap, PageSpeed, and live SERP into a freshness- and confidence-aware source manifest before strategy or content work.
---

# SEO Data Foundation

Use this skill when an SEO task depends on imported or live evidence.

## Workflow

1. Inventory available sources and record unavailable sources explicitly.
2. Create a source manifest using `extensions/agentic-seo/schemas/source-manifest.schema.json`.
3. Record `source_type`, `data_source`, `fetched_at`, `freshness_status`, `confidence`, and local path or reference for every source.
4. Run `scripts/validate_source_manifest.py <manifest.json>`.
5. Return `PASS`, `WARNING_STALE_DATA`, or `BLOCKED_MISSING_CRITICAL_DATA`.

Do not invent missing metrics. Do not choose keywords, change content intent, or draft articles.


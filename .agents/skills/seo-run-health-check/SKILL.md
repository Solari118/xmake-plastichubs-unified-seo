---
name: seo-run-health-check
description: Verify the Agentic SEO extension, source readiness, mirror parity, required files, and safe execution prerequisites without exposing credentials or modifying project state.
---

# SEO Run Health Check

Use this skill before a scheduled or multi-agent SEO run and after deployment.

Run:

`python extensions/agentic-seo/scripts/validate_extension.py --project-root <project-root>`

Report structural validation separately from live API, browser, CMS, and analytics evidence. Never print secret values. A missing optional source is a warning; a missing contract or divergent mirror is blocking.


# PlasticHubs Keyword Resource Index

## Purpose

This folder preserves the PlasticHubs keyword data source library for SEO planning and keyword insertion workflows.

## Files

- `PlasticHubs_SEMrush_All_Keywords_Classified_2026-07-10.xlsx`
  - Source: classified PlasticHubs Semrush keyword workbook.
  - Use for: keyword selection, volume/KD support, page-level keyword insertion, content brief support, and SEO evidence checks.

## Dated Raw Export Snapshots

- `exports/2026-07-17/overmolding-vs-insert-molding_broad-match_us_2026-07-17.csv`
  - Query: `overmolding vs insert molding`
  - Database: US
  - Rows: 8
  - Fields: `Keyword`, `Volume`, `Keyword Difficulty`, `CPC (USD)`
  - SHA256: `99F9D2EB4D70515A2B1642EA8F893DEB63B48FD25A22635F9762F09FF0A4D6E1`
  - Coverage status: all eight keywords already exist in the 2026-07-10 classified workbook. Preserve this file as a dated verification snapshot and CPC evidence; do not double-count its rows in aggregate totals.

## Usage Rules

- Use this workbook as supporting SEO evidence when selecting primary keywords, secondary keywords, and insertion candidates.
- Do not treat the workbook as exhaustive or mandatory when better current-task evidence exists.
- Do not use long-tail phrases as primary Semrush seed keywords by default; use them as page-intent or insertion evidence unless explicitly asked otherwise.
- Do not generate seed lists by mechanically appending broad modifiers such as `parts`, `manufacturer`, `supplier`, or `service` without exported-data support.
- Keep brand, claim-control, and source-boundary rules above keyword convenience.
- Preserve dated raw exports without overwriting earlier snapshots. Before merging a snapshot into aggregate data, deduplicate by normalized keyword and retain source provenance.

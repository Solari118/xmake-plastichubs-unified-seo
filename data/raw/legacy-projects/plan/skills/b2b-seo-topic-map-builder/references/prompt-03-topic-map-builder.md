# Prompt 03: SEO Topic Map Builder

## Role

You are building a structured SEO topic map for a B2B manufacturing website.

## Inputs

- Filled `input.example.md`
- `output/industry_knowledge_map.md`
- `output/customer_intent_map.md`
- `assets/topic_map_columns.csv`

## Constraints

- Do not browse the web.
- Do not invent search volume.
- The table must be useful for Google Sheets or Excel.
- Every important topic must connect to a customer, need, intent, and page type.

## Tasks

1. Create 5-10 main SEO categories.
2. Break each category into secondary categories.
3. Generate keyword patterns instead of only isolated keywords.
4. Add a primary keyword, representative keywords, natural query variants, and key entities for each topic.
5. Assign target brand, target customer, customer need, search intent, decision stage, and page type.
6. Score conversion probability: High, Medium, Low.
7. Score content priority: P1, P2, P3, P4.
8. Assign `COMMERCIAL_BRIDGE_MODE`, GEO answer target, evidence needed, and internal-link target.
9. Mark keyword validation status and whether live SERP validation is needed.

## Priority Rules

- P1: supplier, service, quote, turnkey, custom, prototype, manufacturer, assembly, production, engineering-support intent.
- P2: capability, material, quality, certification, industry application, process, comparison with decision value.
- P3: technical guide, checklist, troubleshooting, file preparation, long-tail support.
- P4: basic glossary and broad awareness topics.

## Output Format

Create:

- `output/seo_topic_map.md`
- `output/blog_topic_map.md`
- `output/topic_map.csv`

`output/topic_map.csv` must use the exact columns from `assets/topic_map_columns.csv`.

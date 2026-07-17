# Capability Preservation Matrix

## Result

All 302 execution-relevant source files in the declared migration scope have matching SHA-256 copies in the isolated legacy snapshots. Current executable packages are normalized under `skills/` and root execution helpers under `tools/`.

| Original project | Preserved capability | Canonical executable location | Original snapshot |
|---|---|---|---|
| `文章规划提示词-Plan` | topic planning, Top-5 SERP workflow, campaign strategy, brand/data routing, website packaging, schedule/live-data config, hooks and tools | `skills/b2b-seo-topic-map-builder/`, `skills/seo-content-strategy/`, `skills/xmake-plastichubs-website-ops/`, `config/`, `tools/` | `data/raw/legacy-projects/plan/` |
| `文章撰写提示词-Info` | current manufacturing writer, writer quality gate, brief contract, templates | `skills/manufacturing-blog-writer/` | `data/raw/legacy-projects/info/` |
| `文章优化提示词2.0-Aduit` | current independent auditor, hard gates, rubric, report templates, Word helpers | `skills/seo-geo-content-auditor/`, `tools/` | `data/raw/legacy-projects/audit/` |
| `B2B机加工生图` | current image skill, visual protocol, image evals, retouch and factory-cleanup scripts | `skills/b2b-machining-image-generator/`, `tools/` | `data/raw/legacy-projects/b2b-image/` |

## Normalized Changes

- One canonical router replaces competing root routers.
- Supplied articles now enter at Audit; rollback to Info or Plan occurs only after defect classification.
- `PRIMARY_SERVICE` and `CROSS_SERVICE_LINK_PLAN` are synchronized across Plan, Info, and Audit contracts.
- The former `unified-seo-pipeline` remains a compatibility alias and cannot start a parallel route.
- Legacy exact-claim material remains preserved but is not automatically loaded; canonical evidence rules control public use.

## Exclusions

Generated articles, `.docx` deliverables, rendered images, user image inputs, caches, `.git`, scratch directories, and generated `dist` packages were not classified as execution capabilities. They remain untouched in their original projects and are not required to reproduce routing or specialist behavior.

Machine-readable evidence: `data/processed/source-capability-inventory.json`.


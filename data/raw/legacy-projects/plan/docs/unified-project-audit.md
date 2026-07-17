# 四项目融合核验与升级记录

## 中文结论

截至 2026-07-13，原有“三项目合并”确实存在，但它只合并了 Plan、Info、Audit。

已确认的证据边界：

| 对象 | 结论 |
|---|---|
| `About_Plastichubs_xmake.zip` | 仅包含品牌/行业知识和 topic map 数据；不包含 B2B 生图项目、统一路由或定时任务 |
| `unified-project-ready.zip` | 包含 7 个 SEO/Website Ops skills 和 1 个 SEO agent；不包含 B2B 生图 skill |
| `codex-deploy-ready.zip` | 是 `.codex` 部署镜像；历史报告记录实际写入曾被 ACL 阻止 |
| `B2B机加工生图\b2b-machining-image-generator` | 独立的 production skill，含 agents、references、evals、security、registry |
| 当前 Plan 根目录 | 已升级为四项目统一规范版和唯一执行入口 |

已实施：

- 根目录新增 `agents/unified-seo-pipeline.md`，默认路由为 `SEO Core -> Plan -> Info -> Audit -> B2B Asset -> Website Ops/Word`。
- 根目录新增 `skills/unified-seo-pipeline/`，规定用户提供关键词时自动贯通；只有 agent 提议关键词时暂停。
- B2B 生图 skill、agents、references、evals、security、registry 已加入根目录 `skills/b2b-machining-image-generator/`。
- B2B 生图原始包保存在 `integrated-assets/b2b-machining-image-generator/`，便于追溯。
- 数据库已复制到根目录 `data/`，根项目不再依赖旧统一子项目的数据路径。
- 新增 `config/article-schedule.yaml`、`hooks/on_load.ps1`、`hooks/on_load.sh` 和 `tools/validate_unified_project.py`。
- 根目录新增 `project.yaml` 与 `codex-project.yaml`，默认 agent 为 `unified-seo-pipeline`。

## 宿主边界与当前状态

- `.agents/` 和 `.codex/` 镜像现已完成同步；共比较 201 个 skill/data 文件，哈希不一致数为 0。
- 左侧项目栏的项目名称、排序、删除和视觉折叠由 Codex 宿主应用控制，不能由本地 Markdown、YAML 或 skill 文件直接修改。文件层面的唯一活跃入口已切换到本 Plan 根目录；旧项目目录仍保留为历史源。
- 定时输出配置已经存在，但 `config/article-schedule.yaml` 是调度契约，不会在没有外部调度器授权和频率/队列设置的情况下自行创建 Windows/Codex automation。

## English Conclusion

The original three-project merge is real, but it covers only Plan, Info, and Audit.

The Plan root is now the canonical four-workflow project. It contains the unified router, the Plan/Info/Audit skills, the B2B machining image skill, the root data library, the scheduler contract, hooks, and a validator.

The `.agents` and `.codex` deployment mirrors are now synchronized; 201 skill/data files were compared with zero hash mismatches. The Codex sidebar is controlled by the host application and cannot be visually merged by local project files. The scheduler file defines the contract only; it does not create an external automation without an authorized scheduler and user-approved schedule inputs.

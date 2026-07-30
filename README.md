# Manufacturing Content Pipeline

这是 XMAKE / PlasticHubs 制造业内容的统一项目。它把原 `Plan`、`Info`、`Aduit`（兼容旧拼写）和 `B2B机加工生图` 四个项目整合为一个有顺序、有契约、有上下文隔离的执行系统。

This is the canonical XMAKE / PlasticHubs manufacturing-content project. It combines the former Plan, Info, `Aduit`-named Audit, and B2B image projects into one ordered, contract-driven, context-isolated system.

## 证据驱动流水线 / Evidence-driven pipeline

`Plan (Google Top-10 + selected structure/style references) → Info → Audit (article + corpus) → B2B Image (≥3 assets/article) → Final Output (verified links)`

发布后可在第 30/60/90 天进入 `Performance Review`，用 GSC、GA4、Semrush 和收录证据决定回到 Plan、Info 或 Final Output。

Published pages can enter `Performance Review` at days 30/60/90. GSC, GA4, Semrush, and indexation evidence determine whether changes return to Plan, Info, or Final Output.

Audit 可把有问题的文章退回 Info 做定向修订；修订后必须重新 Audit，才能进入图片和最终输出阶段。

Audit may return a defective draft to Info for targeted repair. The revised artifact must pass a new Audit before image generation and final output.

## 入口 / Entry points

推荐直接打开：`C:\Users\Lostk\Documents\agent-project`

The preferred workspace is `C:\Users\Lostk\Documents\agent-project`.

四个旧项目仍可作为入口，但其 `AGENTS.md` 只负责把任务转交给本项目。旧规则完整备份为 `AGENTS.legacy.md`，原始执行资产也保存在 `data/raw/legacy-projects/`。

All four legacy workspaces remain valid entry points. Their `AGENTS.md` files delegate to this project; former instructions are retained as `AGENTS.legacy.md`, and source execution assets are preserved under `data/raw/legacy-projects/`.

## 隔离模型 / Isolation model

- Orchestrator 保留完整路由状态；阶段 Agent 只接收声明过的输入。
- Plan、Info、Audit、Image、Final Output 和 Performance Review 使用不同工件命名空间。
- 私有证据不会自动进入公开文章或图片文字。
- 旧项目快照不会自动加载。

- The orchestrator retains route state; phase agents receive only declared inputs.
- Plan, Info, Audit, Image, Final Output, and Performance Review use separate artifact namespaces.
- Private evidence never flows automatically into public copy or image text.
- Legacy snapshots are not auto-loaded.

## 验证 / Validation

```powershell
python scripts/validate_project.py
python -m unittest discover -s tests -p "test_*.py"
```

同步 Skill 发现镜像：

Synchronize skill discovery mirrors:

```powershell
python scripts/sync_mirrors.py
```

能力保存证明见 `docs/capability-preservation-matrix.md` 和 `data/processed/source-capability-inventory.json`。

See `docs/capability-preservation-matrix.md` and `data/processed/source-capability-inventory.json` for capability-preservation evidence.

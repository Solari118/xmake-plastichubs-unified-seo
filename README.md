# Manufacturing Content Pipeline

这是 XMAKE / PlasticHubs 制造业内容的统一项目。它把原 `Plan`、`Info`、`Aduit`（兼容旧拼写）和 `B2B机加工生图` 四个项目整合为一个有顺序、有契约、有上下文隔离的执行系统。

This is the canonical XMAKE / PlasticHubs manufacturing-content project. It combines the former Plan, Info, `Aduit`-named Audit, and B2B image projects into one ordered, contract-driven, context-isolated system.

## 固定流水线 / Fixed pipeline

`Plan → Info → Audit → B2B Image → Final Output`

Audit 可把有问题的文章退回 Info 做定向修订；修订后必须重新 Audit，才能进入图片和最终输出阶段。

Audit may return a defective draft to Info for targeted repair. The revised artifact must pass a new Audit before image generation and final output.

## 入口 / Entry points

推荐直接打开：`C:\Users\Lostk\Documents\agent-project`

The preferred workspace is `C:\Users\Lostk\Documents\agent-project`.

四个旧项目仍可作为入口，但其 `AGENTS.md` 只负责把任务转交给本项目。旧规则完整备份为 `AGENTS.legacy.md`，原始执行资产也保存在 `data/raw/legacy-projects/`。

All four legacy workspaces remain valid entry points. Their `AGENTS.md` files delegate to this project; former instructions are retained as `AGENTS.legacy.md`, and source execution assets are preserved under `data/raw/legacy-projects/`.

## 隔离模型 / Isolation model

- Orchestrator 保留完整路由状态；阶段 Agent 只接收声明过的输入。
- Plan、Info、Audit、Image 和 Final Output 使用不同工件命名空间。
- 私有证据不会自动进入公开文章或图片文字。
- 旧项目快照不会自动加载。

- The orchestrator retains route state; phase agents receive only declared inputs.
- Plan, Info, Audit, Image, and Final Output use separate artifact namespaces.
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


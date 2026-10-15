# Manufacturing Blog Agent / 制造业 Blog Agent

这是从当前私有工作流提取的**可公开安装的独立 Agent Skill**。它覆盖市场与主题门禁、双 SERP 和参考审核、Blog 写作、独立终审、图片与元数据、交付检查。它不携带公司资料、品牌配置、历史文章、运行数据库、凭据或私有路径。每次运行的证据、批准和品牌参数由使用者在本地提供。

This is a **standalone public Agent Skill** derived from the current private workflow. It covers market and topic gates, dual SERP and reference review, Blog writing, independent audit, images and metadata, and delivery checks. It carries no company material, brand configuration, historical article, run database, credential, or private path. The user supplies run evidence, approvals, and brand settings locally.

## 安装 / Install

1. 解压 `manufacturing-blog-agent-v1.0.0.zip`。/ Extract `manufacturing-blog-agent-v1.0.0.zip`.
2. 将其中的 `manufacturing-blog-agent` 文件夹复制到你的 Codex Skills 目录，并重新启动或刷新 Skill 发现。/ Copy the contained `manufacturing-blog-agent` folder into your Codex Skills directory and restart or refresh Skill discovery.
3. 以 `SKILL.md` 为执行入口，按 `templates/` 创建本地运行文件；不要把含有真实公司数据的运行文件提交到本仓库。/ Use `SKILL.md` as the entry point and create local run files from `templates/`; do not commit populated company data here.

## 构建与验证 / Build and verify

```powershell
python -B packages/manufacturing-blog-agent/scripts/build_package.py
python -B packages/manufacturing-blog-agent/scripts/verify_package.py
```

构建器按明确文件清单打包、生成逐文件 SHA-256 和 ZIP SHA-256；验证器复开 ZIP 并筛查私有路径和资料标记。发布结果另需人工审阅新提交的 diff。/ The builder packages an explicit file set and writes per-file and ZIP SHA-256 hashes; the verifier reopens the ZIP and screens for private paths and material markers. A human still reviews the new commit diff before publication.

## 范围 / Scope

本包是可复用的 Agent 指令与空白契约；不包含私有项目中的自动路由数据库、第三方服务凭据或公司专用执行脚本。不得把此包的本地安装验证称作文章上线或效果验证。

This package provides reusable Agent instructions and blank contracts. It does not include the private project's automated routing database, third-party credentials, or company-specific execution scripts. Local installation checks do not establish article publication or performance.

# XMAKE / PlasticHubs Unified SEO Project

This Plan root is the single active local project for the former Plan, Info, Audit, and B2B machining image workflows.

## Private deployment repository

This repository is the portable deployment package for the complete workflow:

`SEO Core -> Plan -> Info/Blog -> Audit -> B2B Asset -> Website Ops/Word`

It includes the active project, Codex/agent discovery mirrors, hooks, configuration, source data, the B2B machining image-generation skill, and the preserved source snapshot. Generated articles, render caches, credentials, and local Git state are intentionally excluded.

在另一台 Windows 电脑上登录有权限的 GitHub 账户后，可以让 Codex 克隆本仓库并运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\verify-deployment.ps1
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\install.ps1
```

The installer backs up conflicting local skills before installing the unified project and its active skills. Open the installed project folder in Codex after installation.

## Execution

Use `agents/unified-seo-pipeline.md` and `skills/unified-seo-pipeline/SKILL.md` as the default route. With a user-supplied primary keyword, the project runs:

`SEO Core -> Plan -> Info -> Audit -> B2B Asset -> Website Ops/Word`

If the agent proposes the keyword, execution stops at `WAITING_FOR_KEYWORD_APPROVAL`. This is the only normal approval gate.

## Canonical Locations

- Active skills: `skills/`
- Discovery mirrors: `.agents/skills/` when filesystem permissions allow
- Codex deployment mirror: `.codex/` when filesystem permissions allow
- Active agent: `agents/unified-seo-pipeline.md`
- B2B source snapshot: `integrated-assets/b2b-machining-image-generator/`
- Article outputs: `outputs/`
- Mirror sync: `powershell -ExecutionPolicy Bypass -File tools/sync_unified_project.ps1`
- Deployment installer: `powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/install.ps1`
- Deployment verification: `powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/verify-deployment.ps1`

The old sibling project folders are preserved as source and history. The Codex sidebar is controlled by the host application, not by a local Markdown file; this repository cannot rename, delete, or visually collapse sidebar items by itself.

## Sidebar Completion

In the Codex desktop UI, open the Plan root as the active project and rename that project to `XMAKE-PlasticHubs Unified SEO`. Archive or remove the old Info, Audit, and B2B image project entries from the sidebar only after confirming their files remain preserved on disk. Then reload the active project so it discovers the synchronized `.agents` and `.codex` mirrors.

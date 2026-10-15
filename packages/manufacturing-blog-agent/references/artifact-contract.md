# 产物契约 / Artifact contract

所有字段是本次运行的本地数据，不提交到公开包。All fields describe local run data and must not be committed into this public package.

| 阶段 / Stage | 必需产物 / Required artifact | 通过条件 / Pass condition |
| --- | --- | --- |
| Market | `market-evidence.json` | 日期、来源、可用性、缺口明确 / dates, sources, availability, gaps |
| Funnel | `funnel-decision.json` | 页面类型与用户批准 / page type and user approval |
| Topic | `topic-opportunity.json`, `topic-audit.json` | 独立审核与主题批准 / independent review and topic approval |
| CTA | `cta-decision.json` | `FULL/LIGHT/NONE` 与用户批准 / mode and user approval |
| Plan | `plan-brief.json`, `reference-review.json` | 双 SERP、实际参考审查、页面归属、内链、原创适配和 Plan gate / dual SERP, reviewed references, page owner, links, adaptation, Plan gate |
| Reader | `reader-orientation.json` | 本次明确选择 / same-run explicit choice |
| Info | `article.vN.md`, `writer-self-check.json` | 原创正文、FAQ、CTA 模式、证据与参考适配 / original copy, FAQ, CTA mode, evidence and adaptation |
| Audit | `audit.vN.json` | 独立 20 分、独立理解 0–4 分、问题及 verdict / independent 20-point and 0–4 scores, issues, verdict |
| Approval | `content-approval.json` | 用户批准与当前正文 SHA-256 绑定 / user approval bound to current article SHA-256 |
| Assets | `images/`, `image-metadata.json` | 逐张独立图和字段 / each image and its fields |
| Final | `package.zip`, `release-receipt.json` | 复开压缩包、hash、交付格式与链接验证 / reopened archive, hashes, formats and link validation |

任何 `WAITING_*`、`REVISION_REQUIRED` 或 `BLOCKED` 均不是完成。Any `WAITING_*`, `REVISION_REQUIRED`, or `BLOCKED` state is not completion.

保存批准者、批准时间、被批准文件的 SHA-256 和依赖版本。Do not infer approval from a general request; save who approved what, when, the approved file SHA-256, and dependency versions.

对外发布的分析必须标记哪些是事实、假设与推断。Label facts, assumptions, and inferences in outward-facing analysis.

---
name: manufacturing-blog-agent
description: Plan, write, independently audit, and package original manufacturing Blog articles from verified market and reference evidence. Use for a new Blog, a supplied draft, or an approved revision. Keep private company inputs outside the distributable package.
---

# Manufacturing Blog Agent / 制造业 Blog 写作 Agent

## 任务与边界 / Job and boundary

从可核验的需求和参考资料产出原创 Blog，并留下逐阶段审查记录。交付前保持 Plan、Info、Audit、Image、Final Output 的职责独立。完整文章或现有草稿从其最新可验证阶段进入；现有文章先进入 Audit。单独图片任务只运行 Image。

Produce an original Blog from verifiable demand and references with a record of each review stage. Keep Plan, Info, Audit, Image, and Final Output separate. Enter at the latest verifiable stage; an existing article begins at Audit. A standalone image request runs Image only.

此公开包不含公司资料、内部来源、品牌能力声明、客户数据、账号凭据或历史文章。运行时由用户在本地提供品牌、站点、证据及授权；不要将这些输入写回包内。

This public package contains no company data, internal sources, brand capability claims, customer data, credentials, or historical articles. The user supplies brand, site, evidence, and approvals locally for each run; keep those inputs out of the package.

## 主链 / Main route

`Market Data → Funnel Diagnosis/Approval → Topic Opportunity → Independent Topic Audit → Topic Approval → CTA Decision → Plan (dual SERP + v9 references) → Reader Orientation → Info → Audit → Content Approval → Image → Image Metadata → Final Output [→ 30/60/90 Performance Review]`

1. **Market Data / 市场数据**：读取本次日期明确的搜索、站点和受众证据。缺少影响选题的关键数据时标记 `WAITING_FOR_FRESH_DATA`，不得编造搜索量、排名或难度。
2. **Funnel / 漏斗**：给出意图、转化阶段和页面类型判断，请用户批准。不要把服务页词自动当成 Blog 词。
3. **Topic / 主题**：提出主题机会，由与提议者独立的审查角色核对需求、重叠与证据，再取得主题批准。用户自带主题仍需机会验证，除非明确要求采用。
4. **CTA / 转化动作**：独立记录用户批准的 `FULL`、`LIGHT` 或 `NONE`。主题批准不等于 CTA 批准。
5. **Plan / 规划**：记录 Google Blog SERP 与目标地区/形式的第二参考 SERP、逐结果意图和格式、选定参考、原创适配方案、页面归属、内链计划、声明边界及 Plan gate。无法取得精确结果时标记阻塞，不把猜测写成 Top-10。
6. **Reference v9 / 参考资料**：对参考文章做可追溯的功能和结构剖析；由独立角色审核其相关性、许可与可用性；真正入库和检索后再生成单一或组合参考方案。仅借鉴高层结构和读者任务，不复制文字、独特标题或近似大纲。
7. **Reader Orientation / 读者方向**：写作或重写前取得用户本次选择：`偏向科普文` 或 `偏向无专业知识的大众`。不得从漏斗或 SERP 代推。英语稿以美国 9–12 年级的可读性为默认目标，但公式分数不能取代人工判断。
8. **Info / 写作**：依据通过的 Plan 完成原创正文、FAQ、批准的 CTA、证据记录和参考适配记录。每个 H2 的标题、首段与整节回答同一读者问题。标题改变时记录变更和正文联动。作者自检不等于独立终审。
9. **Audit / 独立审核**：独立核对事实、意图、结构适配、原创性、近期文章相似度、FAQ、CTA、链接、英语、读者理解与交付范围。保留 20 分文章审核和独立 0–4 分理解评分。问题退回 Info；策略、参考或格式问题退回 Plan，修订后重审。
10. **Approval + assets / 批准与资产**：正文 hash 对应的内容批准后，才生成文章关联图片。逐张交付独立图片与 WordPress 文件名、Alt、Title、Caption 决定、Description；图片不能证明性能、合规或商业结果。
11. **Final Output / 最终交付**：核对当前正文 hash、Plan、独立 Audit、批准、图片元数据及可访问的页面实例链接。手动完整审阅包默认包括英文图文 `.docx`、中文审核 `.docx`、独立折叠 FAQ `.txt`、逐图字段 `.docx`、实际图片与 `.zip`；只有用户明确要求才改变格式。打开归档复验内容与 hash。
12. **Performance / 效果**：上线后有发布日期和带日期的 GSC/GA4 或等价数据时，在 30/60/90 天回看。没有观测值时标记 `WAITING_FOR_PERFORMANCE_DATA`。

For the English route, follow the same numbered stages. Do not advance through a missing approval, independent review, or evidence gate. Use `PHASE_READY` for a ready stage, not for a published or completed article.

## 运行规则 / Runtime rules

- 把事实、假设、推断和建议分开；技术、标准、认证、价格、交期和性能数字需要适用证据。/ Separate facts, assumptions, inferences, and recommendations; substantiate technical, standards, certification, price, lead-time, and performance numbers.
- 研究原文和私有证据只保存在本次本地运行目录。引用外部文章时保留来源 URL 与访问日期；不要逐段改写。/ Keep research captures and private evidence in the local run directory. Record source URLs and access dates; do not paraphrase an article section by section.
- 一次运行使用一个 `run_id`；阶段产物版本化并记录 SHA-256。上游变化使受影响的下游批准失效。/ Use one `run_id`, version stage artifacts, and record SHA-256. Upstream changes invalidate dependent downstream approvals.
- 发布到 CMS 或修改线上页面需要具体变更授权及渲染验证；本地包验证不代表线上结果。/ CMS publication or live changes require authorization for the concrete changes and rendered verification. Local package checks do not prove live outcomes.
- 如用户仅要求一个阶段，只运行该阶段并清楚标注终态。/ For an explicit phase-only request, run that phase and label its terminal state.

## 输出 / Output

先给结果和状态，再给阶段路径、证据缺口、批准状态、文件及 hash、审查分数和下一步。所有面向用户的回复中文在前、英文在后。使用 `references/artifact-contract.md`、`references/writing-and-audit.md` 和 `templates/` 中的空白表单。不要把运行资料、账号信息或私有路径加入公开包。

Lead with the result and status, then report stage paths, evidence gaps, approvals, files and hashes, audit scores, and next action. User-facing responses are Chinese first, English second. Use `references/artifact-contract.md`, `references/writing-and-audit.md`, and the blank forms in `templates/`. Never add run data, account information, or private paths to this public package.

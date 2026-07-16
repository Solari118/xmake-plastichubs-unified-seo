---
name: seo-content-strategy
description: "Plan XMAKE and PlasticHubs SEO content strategy, keyword architecture, topic clusters, competitor positioning, content calendars, and campaign-level priorities. Use for SEO strategy, topic map use, keyword research support, and planning work that is broader than one article brief but not final drafting or audit."
---

# SEO 内容策略 Skill

## 技能描述

为 XMAKE (xmake.com) 和 PlasticHubs (plastichubs.com) 两个制造业 B2B 独立站制定和执行系统化的 SEO 内容策略。涵盖关键词研究、内容规划、竞品分析、内容日历管理和效果追踪。

## 双品牌策略原则

- **XMAKE**：全工艺覆盖策略，以 CNC 加工为核心支柱，辐射所有制造工艺
- **PlasticHubs**：塑料专业深耕策略，以塑料 CNC 加工为商业核心，按 P1→P4 优先级推进
- **共享资源，独立形象**：技术参数可共享，但内容品牌形象完全独立

## 核心流程

### 1. 关键词研究

#### XMAKE 关键词金字塔
```
┌──────────────────────────────────┐
│   品牌词：XMAKE, xmake           │
├──────────────────────────────────┤
│   核心服务：CNC machining,       │
│   3D printing, sheet metal,      │
│   injection molding              │
├──────────────────────────────────┤
│   长尾工艺：aluminum CNC,        │
│   5-axis machining, SLS 3D print │
├──────────────────────────────────┤
│   问题/需求：CNC machining cost, │
│   how to choose 3D print material│
├──────────────────────────────────┤
│   对比选型：CNC vs 3D printing,  │
│   injection vs die casting       │
├──────────────────────────────────┤
│   行业应用：automotive parts,    │
│   medical device manufacturing   │
└──────────────────────────────────┘
```

#### PlasticHubs 关键词体系（按 P1-P4 优先级）
见 `data/plastichubs/seo_topic_map.md` 完整定义。核心优先级：
- **P1 (33 topics)**：plastic CNC machining 商业集群 + 材料页 + 原型/小批量方案
- **P2 (31 topics)**：二次工艺 + 行业应用 + 工程支持
- **P3 (11 topics)**：对比指南 + FAQ
- **P4 (3 topics)**：术语表

### 2. 内容规划

#### XMAKE 主题集群模型
```
CNC Machining (Pillar)
├── What is CNC Machining?
├── CNC Machining DFM Design Guide
├── CNC Machining Materials Comparison
├── 10 Ways to Reduce CNC Machining Cost
├── Automotive Parts CNC Machining
├── CNC vs 3D Printing vs Injection Molding
└── CNC Machining FAQ
```

#### PlasticHubs 主题集群模型
```
Plastic CNC Machining (Main Pillar)
├── Plastic CNC Milling Service
├── Plastic CNC Turning Service
├── 5-Axis Plastic CNC Machining
├── Precision Plastic Machining
├── Prototype Plastic CNC Machining
├── Low-Volume Plastic CNC Machining
├── Production Plastic Machining
└── Plastic CNC Machining Quote
```

### 3. 竞品内容分析

#### XMAKE 主要竞品
| 竞品 | 模式 | 优势 | vs XMAKE |
|------|------|------|----------|
| Xometry | 纯平台/中间商 | 美国供应商网络大 | 无自有工厂；中间商加价 |
| Protolabs | 自有工厂+网络 | 快速交付、品牌强 | 定价高；大批量不经济 |
| Fictiv | 管理型平台 | DFM软件好 | 外包制造；溢价定价 |
| Hubs/Protolabs Network | 聚合平台 | 欧洲网络强 | 被收购后变化；定价高 |

#### PlasticHubs 竞品方向
- 综合平台中塑料加工板块（Xometry, Hubs 的塑料服务）
- 专业塑料制造商
- 核心差异化：plastic-only specialization + supplier/quote intent + material authority

### 4. 内容日历模板

```markdown
## [月份] 内容日历 - [XMAKE / PlasticHubs]

| 日期 | 品牌 | 主题 | 类型 | 目标关键词 | 优先级 | 状态 |
|------|------|------|------|-----------|--------|------|
| 7/8 | XMAKE | CNC加工询价指南 | 指南 | CNC machining quote | P1 | ✅ |
| 7/15 | PH | POM CNC加工指南 | 材料页 | POM CNC machining | P1 | ⏳ |
```

### 5. SEO 优化清单

发布前检查：
- [ ] 标题包含核心关键词，长度 50-60 字符
- [ ] Meta 描述 140-160 字符，含 CTA
- [ ] URL 简短且包含关键词
- [ ] H1 唯一且含关键词
- [ ] H2/H3 层级结构合理
- [ ] 首段 150 字内出现核心关键词
- [ ] 图片有 Alt 标签
- [ ] 内链 3-5 个指向相关内容
- [ ] 外链 1-2 个指向权威来源
- [ ] Schema 标记（Article/FAQ/HowTo）
- [ ] 字数 ≥ 1500（深度内容 ≥ 3000）
- [ ] 反AI腔检查通过
- [ ] 品牌隔离检查（不提兄弟品牌）

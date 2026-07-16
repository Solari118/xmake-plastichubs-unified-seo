---
name: manufacturing-content-writer
description: "Write and refine manufacturing technical content for XMAKE and PlasticHubs using package data sources, anti-fluff writing rules, SEO structure, technical accuracy checks, and brand isolation. Use as a supporting writing reference for manufacturing process, material, cost, application, and comparison content when it complements the primary Info writer."
---

# 制造业内容写作 Skill

## 技能描述

为 XMAKE 和 PlasticHubs 两个制造业 B2B 品牌撰写高质量、SEO 友好、反AI腔的技术内容。覆盖 CNC 加工、注塑成型、3D 打印、钣金加工、压铸、真空复模等制造工艺的技术写作。

## 写作框架

### 标准博客文章结构

```markdown
# [核心关键词] — [具体决策问题/技术要点]

> 一句话说明本文解决什么制造/选材/工艺问题（150字内）

## 问题场景
- 什么生产/设计情况下会遇到这个问题？
- 不解决会导致什么后果（delay, rework, scrap, tolerance drift）

## 核心分析
- 分3-5个子主题
- 每个子主题配表格/数据/案例
- 技术细节 + 实用建议

## 决策框架（如适用）
- 横向对比表格
- 适用场景分析

## 下一步
- 具体可执行的动作（上传CAD、确认公差、选择材料等）
- CTA：指向对应品牌的服务/报价页
```

### XMAKE 内容类型

| 类型 | 标题公式 | 字数 |
|------|----------|------|
| 工艺入门 | `什么是 [工艺]？工程师入门指南` | 1500-2500 |
| 设计指南 | `[工艺] DFM 设计规则：[N] 条提升可制造性` | 2000-3500 |
| 材料指南 | `[工艺] 材料选择：[N] 种常用材料性能对比` | 2000-3000 |
| 成本优化 | `降低 [工艺] 成本的 [N] 个工程方法` | 1500-2500 |
| 行业应用 | `[行业] [工艺] 制造方案与案例` | 1500-2500 |
| 对比评测 | `[工艺A] vs [工艺B]：工程师选型指南` | 2000-3500 |

### PlasticHubs 内容类型（按优先级）

| 优先级 | 页面类型 | 示例 |
|--------|----------|------|
| P1 | 服务页 | Plastic CNC Machining Service |
| P1 | 供应商/报价页 | Custom CNC Plastic Parts Quote |
| P1 | 能力页 | Plastic CNC Milling / Turning / 5-Axis |
| P1 | 材料页 | POM / PEEK / Nylon CNC Machining |
| P1 | 方案页 | Plastic Prototyping Service, Low-Volume Production |
| P2 | 二次工艺页 | Plastic 3D Printing, Vacuum Casting, Injection Molding |
| P2 | 行业页 | Medical / Automotive / Industrial Equipment Plastic Parts |
| P2/P3 | 对比博客 | CNC vs 3D Printing for Plastic, Small-Batch Options |

## 写作原则

### 技术准确性
- 所有数据（公差、温度、压力等）必须来自 `data/` 目录
- 引用 ISO/ASTM/GB 等标准时需注明标准编号
- 不确定的数据标注"典型值"或给出范围

### 反AI腔写作
严格执行 `data/shared/writing_anti_fluff.md` 中的规则：
- 一句话一个决策/风险/结果
- 不用 essay transitions (hence, furthermore, moreover)
- 不用抽象营销语言 (unlock, revolutionize, game-changer)
- 结尾给具体下一步动作，不给口号
- FAQ 不重复正文内容，上升到下一个决策层

### 竞品对比语言
- 不用攻击性词汇（broker, middleman, unverified, black box）
- 用商业模式分析：traceability, process visibility, feedback speed, lead-time stability
- 批评运营模式，不批评使用该模式的人

### SEO 优化
- 核心关键词密度 1-2%
- LSI 关键词自然分布
- 图片 Alt 标签含关键词
- 内链 3-5 个
- 每 300 字左右配一张图/表

### 转化引导
- 在相关内容处自然插入服务链接
- CTA 明确且低摩擦
- 避免过度推销

## 质量评分卡

| 维度 | 权重 | 评分标准 |
|------|------|----------|
| 技术准确性 | 30% | 数据/参数/标准是否来自 data 目录 |
| SEO 优化 | 25% | 关键词/结构/标签是否优化 |
| 反AI腔 | 20% | 是否通过 anti-fluff 检查清单 |
| 可读性 | 15% | 结构清晰/语言流畅/扫描友好 |
| 转化力 | 10% | CTA 是否自然有效 |

总分 ≥ 80 分方可发布。

## 品牌隔离检查

发布前确认：
- [ ] XMAKE 内容不提及 PlasticHubs
- [ ] PlasticHubs 内容不提及 XMAKE
- [ ] 各自使用各自的域名和品牌名
- [ ] CTA 指向正确的品牌站点

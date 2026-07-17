---
name: xmake-plastichubs-seo-expert
description: "Route and coordinate XMAKE/PlasticHubs SEO content operations across brand selection, data loading, keyword strategy, manufacturing content creation, quality checks, and cross-skill handoff. Use for high-level SEO task routing, dual-brand project context, data source selection, and deciding whether work belongs to Plan, Info, Audit, Website Ops, or package content strategy skills."
---

# XMAKE / PlasticHubs SEO 内容专家 Skill

## 技能描述

作为 XMAKE (xmake.com) 和 PlasticHubs (plastichubs.com) 双品牌的专属 SEO 内容专家 Skill，负责从策略规划到内容创作再到效果追踪的全链路 SEO 内容运营。此技能是项目的基础逻辑核心，所有内容相关子任务均由此 Skill 调度。

## 品牌架构

```
同一集团
├── XMAKE (xmake.com)
│   ├── 定位：全工艺按需制造平台
│   ├── 服务：CNC加工、3D打印、钣金、注塑、压铸、真空复模、挤出等
│   └── 对标：Xometry, Protolabs, Fictiv, Hubs
│
└── PlasticHubs (plastichubs.com)
    ├── 定位：塑料/塑胶专业制造平台
    ├── 服务：塑料CNC加工、塑料3D打印、真空复模、注塑成型等
    └── 对标：塑料专业供应商
```

> ⚠️ 公开内容约束：不要在公开 SEO 内容中暴露母子公司关系。

## 触发条件

此技能是项目的默认基础技能，在以下场景自动激活：
- 用户请求 SEO 相关内容任务
- 用户请求撰写/优化制造行业内容
- 用户请求分析竞品或关键词
- 项目启动时的默认上下文

## 技能架构

```
XMAKE / PlasticHubs SEO 内容专家
├── 数据层 (data/)
│   ├── data/xmake/          ← XMAKE 品牌数据
│   ├── data/plastichubs/    ← PlasticHubs SEO 数据
│   └── data/shared/         ← 共享数据（已去Plastichubs/xmake化）
├── SEO 内容策略 (seo-content-strategy)
│   ├── 关键词研究
│   ├── 竞品分析
│   ├── 内容规划
│   └── 效果追踪
├── 制造业内容写作 (manufacturing-content-writer)
│   ├── 工艺指南
│   ├── 设计指南
│   ├── 材料指南
│   ├── 成本优化
│   └── 行业应用
└── 写作风格控制
    ├── 反AI腔检查
    ├── 去攻击性语言
    └── 技术准确性验证
```

## 工作模式

### 模式一：XMAKE 全工艺策略
目标：覆盖全制造业关键词，建立综合性制造平台权威
- 关键词覆盖：CNC加工、3D打印、钣金、注塑、压铸、挤出等
- 内容深度：每种工艺的入门指南 + 设计指南 + 材料指南 + 成本优化

### 模式二：PlasticHubs 塑料专业策略
目标：在塑料制造领域建立专业权威
- 关键词覆盖：plastic CNC machining, custom plastic parts, POM/PEEK/Nylon machining
- 内容体系：按 PlasticHubs SEO Topic Map 的 P1→P4 优先级执行

### 模式三：内容创作
1. 确认文章主题和目标关键词
2. 确定目标品牌（XMAKE 或 PlasticHubs）
3. 从 data/ 目录加载对应数据
4. 按照写作框架撰写
5. SEO 优化 + 反AI腔检查
6. 输出

### 模式四：批量生产
1. 确认批量主题列表
2. 制定内容模板
3. 批量创作
4. 统一 SEO 优化
5. 输出内容包

## 快速参考：XMAKE 核心关键词

| 类别 | 中文关键词 | 英文关键词 |
|------|-----------|-----------|
| 品牌 | XMAKE, 迈科智造 | XMAKE, xmake manufacturing |
| 核心服务 | CNC加工, 3D打印服务, 钣金加工, 注塑成型 | CNC machining service, 3D printing service, sheet metal fabrication |
| 长尾 | 铝合金CNC加工, 小批量注塑, 金属3D打印 | aluminum CNC machining, low volume injection molding, rapid prototyping |
| 商业 | CNC加工报价, 定制零件制造 | CNC machining quote, custom parts manufacturing |

## 快速参考：PlasticHubs 核心关键词

| 类别 | 关键词 |
|------|--------|
| P1 核心 | plastic CNC machining service, plastic CNC machining supplier, custom plastic machining |
| P1 方法 | plastic CNC milling, plastic CNC turning, 5-axis plastic CNC machining |
| P1 转化 | CNC plastic parts quote, custom CNC plastic parts, plastic machining supplier |
| P1 材料 | POM CNC machining, PEEK CNC machining, Nylon CNC machining |
| P1 方案 | plastic prototyping service, low-volume plastic production |
| P2 扩展 | plastic 3D printing, vacuum casting, plastic injection molding |

## 数据加载规则

每次执行任务前，按需加载数据：
1. XMAKE 任务 → 读取 `data/xmake/company_info.md` + `data/shared/` 文件
2. PlasticHubs 任务 → 读取 `data/plastichubs/` 目录 + `data/shared/` 文件
3. 竞品分析 → 读取 `data/shared/competitors.md`

## 内容质量标准
- 技术深度：≥ 1500 字（标准），≥ 3000 字（深度指南）
- 反AI腔：通过 writing_anti_fluff.md 检查清单
- SEO：标题/Meta/结构/内链/Schema 全优化
- 转化：每篇至少 1 个指向对应品牌服务的 CTA

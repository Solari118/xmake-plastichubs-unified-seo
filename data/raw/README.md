# 原始资源数据库

此目录存放项目的原始数据源文件，是所有衍生数据（data/ 目录下 .md/.csv 文件）的原始出处。

## 文件说明

| 文件名 | 格式 | 内容 | 对应衍生数据 |
|--------|------|------|-------------|
| `XMAKE_公司信息.docx` | Word | XMAKE 公司完整信息（中英文双语，含品牌叙事、制造能力、竞品定位、内容写作规范等9大章节） | `data/xmake/company_info.md` |
| `plastichubs_seo_topic_map_package.zip` | ZIP | PlasticHubs SEO 完整数据包（含行业知识图谱、客户意图图谱、78个SEO主题、35个博客主题、支柱页结构等10个文件） | `data/plastichubs/*` (8个文件) |
| `About_Plastichubs/xmake.zip` | ZIP | Plastichubs/xmake 原始技术数据（机械制造能力、电子制造能力、竞品情报、反AI腔写作指南） | `data/shared/*` (4个文件，已去Plastichubs/xmake化→XMAKE) |

## 数据转换流程

```
原始资源 (data/raw/)
    │
    ├── XMAKE_公司信息.docx ──pandoc──→ data/xmake/company_info.md
    │
    ├── plastichubs_seo_topic_map_package.zip ──unzip──→ data/plastichubs/*.md + *.csv
    │
    └── About_Plastichubs/xmake.zip ──unzip──→ 手动去Plastichubs/xmake化 ──→ data/shared/*.md
                                   (Plastichubs/xmake → XMAKE)
```

## 使用方式

### 重新生成衍生数据
```bash
# 1. 转换 docx → md
pandoc data/raw/XMAKE_公司信息.docx -t markdown -o data/xmake/company_info.md

# 2. 解压 ZIP
unzip data/raw/plastichubs_seo_topic_map_package.zip -d data/plastichubs/
unzip data/raw/About_Plastichubs/xmake.zip -d /tmp/about_Plastichubs/xmake/

# 3. 去 Plastichubs/xmake 化（将 Plastichubs/xmake → XMAKE）
# 对 /tmp/about_Plastichubs/xmake/ 中的文件执行 sed 替换后放入 data/shared/
```

### 更新原始资源
当业务数据变化时：
1. 替换 `data/raw/` 中的原始文件
2. 重新执行上述转换流程
3. Agent 会自动加载最新的衍生数据

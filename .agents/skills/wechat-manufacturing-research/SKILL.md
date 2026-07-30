---
name: wechat-manufacturing-research
description: Search and collect public WeChat Official Account articles about machining, plastics, molds, materials, finishing, quality, and manufacturing, then create a private, source-traceable reference pack for original XMAKE or PlasticHubs content. Use when the user says “对微信公众号相关关键词文章进行参考”, “参考微信公众号文章”, “搜索微信公众号推文”, or explicitly asks to use WeChat articles as manufacturing-content references. Do not trigger for ordinary Google SERP research or publish third-party text verbatim.
---

# WeChat Manufacturing Research

## Owned job

Add a conditional private research input before Plan or Info. The user is not expected to know engineering terminology. Build the WeChat query portfolio from brand scope, project service history, Semrush evidence, live Google language, and a manufacturing ontology before searching WeChat. Keep Google Top-10 benchmarking mandatory; WeChat material supplements it and never replaces it.

## Workflow

1. Record the brand, topic or article keyword when available, requested result count, and run ID. A missing engineering keyword is normal and must not block this route.
2. Build the service universe from the selected brand and current project evidence:
   - `XMAKE`: metal and plastic CNC machining, plastic and metal 3D printing, sheet metal fabrication, injection molding, vacuum casting, die casting, extended metal processes, tooling, quality, and surface finishing.
   - `PlasticHubs`: plastic CNC machining, plastic 3D printing, injection molding, overmolding, insert molding, mold making, vacuum/urethane casting, rapid prototyping, low-volume plastic production, plastic materials, quality, and plastic surface finishing.
   - Reconcile this inventory with current navigation, service pages, project sources, and user-approved additions. Never reduce either brand to one service.
3. Expand the keyword universe:
   - Load relevant Semrush exports/workbooks when available. Use volume, KD, intent, category, and fit evidence; exclude navigational brands, consumer noise, and high-volume terms that do not support industrial buyers.
   - Inspect live Google results, related searches, and People Also Ask language in the in-app browser. Google provides current phrasing and intent evidence, not search-volume evidence.
   - Expand every relevant service across process, materials, physics/defects, tolerance/quality, surface treatment, DFM, inspection, applications, cost, and sourcing.
4. Run the deterministic query builder:

```powershell
python scripts/expand_wechat_queries.py --brand "<xmake|plastichubs|both>" --semrush "<optional file>" --seed "<optional topic>" --out "<run-private-dir>"
```

Use repeated `--semrush`, `--seed`, and `--google-query` arguments. Without a seed, generate a diversified brand-wide portfolio. With an article topic, use a focused portfolio plus adjacent-service queries.
5. Review `wechat-query-portfolio.md`. Search Tier A first, then Tier B/C only when results remain thin. Do not search only the literal user phrase.
6. Search in the in-app browser:
   - Sogou Weixin article search for each approved Chinese query;
   - one close technical variant when a query is thin;
   - `site:mp.weixin.qq.com/s` through Google only as a discovery supplement.
7. Inspect visible result titles, accounts, dates, and snippets. Exclude duplicates, irrelevant news, copied aggregations, unverifiable claims, and pages blocked by login or CAPTCHA. Never bypass platform controls.
8. Collect no more than 15 public article URLs per research run. Diversify sources across the selected services and technical dimensions. Prefer engineering process explanations, shop-floor failure analysis, materials, DFM, finishing, tooling, inspection, or case evidence.
9. Run:

```powershell
python scripts/collect_wechat_articles.py collect --keyword "<keyword>" --url "<public-url>" --out "<run-private-dir>"
```

Use repeated `--url` arguments or `--url-file`. The collector stores normalized full text only in the private run folder and generates a limited-excerpt research pack.
10. Create `Internal — Not for Publication` outputs:
   - source URL, account, title, date, capture time, hash;
   - article outline and evidence form;
   - useful facts needing verification;
   - Chinese-market/process information gaps absent from the Google benchmark;
   - a transformation plan describing what can be synthesized, challenged, or independently verified.
11. Pass only the keyword evidence, query portfolio, reference pack, and approved adaptation map into Plan/Info. Do not pass raw full text unless a claim audit requires it.
12. Keep all third-party names, URLs, and quotations out of public XMAKE/PlasticHubs copy unless the user explicitly approves attribution.

## Query portfolio gates

- Do not equate high search volume with article fit. Require brand/service relevance and industrial intent before a Semrush term enters the WeChat portfolio.
- Do not require the user to name heat effects, tolerance, warpage, shrinkage, tool wear, stress cracking, material grades, inspection, or other engineering concepts. Generate those dimensions from the ontology and project evidence.
- Keep at least four distinct dimensions in a focused portfolio and at least six in a brand-wide portfolio.
- Prevent one high-volume service, especially generic 3D-printing terms, from consuming the portfolio. Use service and dimension diversity quotas.
- For PlasticHubs, exclude metal-only queries unless the article explicitly compares a plastic route with a metal route.
- For XMAKE, include both metal and plastic routes when the task is brand-wide.

## Originality and rights gate

- Never convert “reference” into sentence-by-sentence translation, paraphrase laundering, or wholesale reposting.
- Do not copy a distinctive heading sequence, proprietary table, case narrative, image, diagram, or more than a short necessary excerpt.
- Treat facts as leads, not proof. Verify technical claims through company knowledge, standards, manufacturer data, or primary sources.
- If the user owns the source or has publication permission, record that status; otherwise default to `research-only`.
- Use the WeChat pack to find novel questions, shop-floor mechanisms, Chinese terminology, counterexamples, and cases. Write new English structure and expression.
- Do not use WeChat material merely to evade Google duplicate-content detection.

## Failure behavior

- CAPTCHA/login/interstitial: stop that source, record `blocked`, continue with other public results.
- Public page cannot be fetched: preserve URL and browser notes; do not use cached mirrors that bypass access controls.
- Fewer than three relevant sources: label the pack `thin evidence`; do not claim broad WeChat coverage.
- No verified new information: omit the route’s contribution rather than forcing novelty.

## Output contract

Return:

- `wechat-reference-pack.md`
- `wechat-query-portfolio.md`
- `wechat-query-portfolio.json`
- `records.jsonl`
- private `raw/*.txt`
- selected-source adaptation notes
- excluded/blocked-source log
- rights status: `research-only`, `owned`, or `permission-confirmed`

Read [rights-and-synthesis.md](references/rights-and-synthesis.md) when deciding whether material can enter public copy.

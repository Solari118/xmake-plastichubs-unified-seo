# WeChat Manufacturing Research Agent

Run only when the user explicitly requests WeChat Official Account references.

1. Resolve brand scope from project evidence. XMAKE covers metal and plastic manufacturing; PlasticHubs covers the supported plastic-processing portfolio.
2. Load relevant Semrush files or connected-report evidence. Use Google for live language/intent expansion, not volume claims.
3. Generate a diversified query portfolio across services, materials, mechanisms/defects, tolerances/quality, finishing, DFM, inspection, applications, cost, and sourcing.
4. Search public WeChat article results in the in-app browser. Do not require the user to supply engineering terminology.
5. Select up to 15 relevant manufacturing sources and record exclusions.
6. Use `expand_wechat_queries.py` and `collect_wechat_articles.py` to store the private query portfolio, normalized captures, and limited-excerpt reference pack.
7. Treat every source as `research-only` unless ownership or permission is confirmed.
8. Never replace the Google Top-10, bypass access controls, or copy/translate third-party articles into public brand content.

Handoff only the limited-excerpt pack and approved adaptation notes to Plan or Info.

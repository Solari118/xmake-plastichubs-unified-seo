from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


ALLOWED_HOSTS = {"mp.weixin.qq.com", "weixin.qq.com"}
BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "blockquote", "li"}
SKIP_TAGS = {"script", "style", "noscript", "svg"}
MAX_ARTICLES = 15
MAX_BYTES = 8 * 1024 * 1024
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
)


class WeChatParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.meta: dict[str, str] = {}
        self.depth = 0
        self.content_depth: int | None = None
        self.skip_depth = 0
        self.block_tag: str | None = None
        self.block_depth: int | None = None
        self.block_buffer: list[str] = []
        self.blocks: list[tuple[str, str]] = []
        self.account_buffer: list[str] = []
        self.account_depth: int | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = {k: v or "" for k, v in attrs}
        self.depth += 1
        if tag == "meta":
            key = attrs_map.get("property") or attrs_map.get("name")
            if key and attrs_map.get("content"):
                self.meta[key.lower()] = attrs_map["content"].strip()
        if tag in SKIP_TAGS:
            self.skip_depth += 1
        if self.content_depth is None and (
            attrs_map.get("id") == "js_content"
            or "rich_media_content" in attrs_map.get("class", "")
        ):
            self.content_depth = self.depth
        if (
            self.account_depth is None
            and (
                attrs_map.get("id") == "js_name"
                or "profile_nickname" in attrs_map.get("class", "")
            )
        ):
            self.account_depth = self.depth
        if (
            self.content_depth is not None
            and self.depth >= self.content_depth
            and tag in BLOCK_TAGS
            and self.block_tag is None
        ):
            self.block_tag = tag
            self.block_depth = self.depth
            self.block_buffer = []

    def handle_endtag(self, tag: str) -> None:
        if (
            self.block_tag == tag
            and self.block_depth == self.depth
            and self.block_buffer
        ):
            text = normalize_text("".join(self.block_buffer))
            if text:
                self.blocks.append((tag, text))
            self.block_tag = None
            self.block_depth = None
            self.block_buffer = []
        if self.content_depth == self.depth:
            self.content_depth = None
        if self.account_depth == self.depth:
            self.account_depth = None
        if tag in SKIP_TAGS and self.skip_depth:
            self.skip_depth -= 1
        self.depth = max(0, self.depth - 1)

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if self.account_depth is not None:
            self.account_buffer.append(data)
        if self.content_depth is not None and self.block_tag is not None:
            self.block_buffer.append(data)


def normalize_text(value: str) -> str:
    value = html.unescape(value).replace("\u200b", "").replace("\xa0", " ")
    return re.sub(r"\s+", " ", value).strip()


def ensure_public_wechat_url(value: str) -> str:
    parsed = urllib.parse.urlparse(value.strip())
    host = (parsed.hostname or "").lower()
    if parsed.scheme not in {"http", "https"} or host not in ALLOWED_HOSTS:
        raise ValueError(f"unsupported URL host: {value}")
    return value.strip()


def fetch(url: str, timeout: int) -> tuple[str, str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept-Language": "zh-CN,zh;q=0.9"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        final_url = ensure_public_wechat_url(response.geturl())
        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type.lower():
            raise ValueError(f"unexpected content type: {content_type}")
        payload = response.read(MAX_BYTES + 1)
        if len(payload) > MAX_BYTES:
            raise ValueError("article exceeds 8 MiB limit")
        charset = response.headers.get_content_charset() or "utf-8"
        return payload.decode(charset, errors="replace"), final_url


def extract_js_value(source: str, names: tuple[str, ...]) -> str:
    for name in names:
        match = re.search(
            rf"(?:var\s+)?{re.escape(name)}\s*=\s*['\"]([^'\"]+)['\"]",
            source,
        )
        if match:
            return normalize_text(match.group(1).replace("\\x26", "&"))
    return ""


def extract_record(source: str, url: str, keyword: str) -> dict[str, object]:
    parser = WeChatParser()
    parser.feed(source)
    title = (
        parser.meta.get("og:title")
        or parser.meta.get("twitter:title")
        or extract_js_value(source, ("msg_title",))
    )
    account = (
        normalize_text("".join(parser.account_buffer))
        or parser.meta.get("author", "")
        or extract_js_value(source, ("nickname",))
    )
    published = (
        parser.meta.get("article:published_time")
        or extract_js_value(source, ("publish_time", "ct"))
    )
    if published.isdigit():
        published = dt.datetime.fromtimestamp(
            int(published), tz=dt.timezone(dt.timedelta(hours=8))
        ).isoformat()
    blocks = dedupe_blocks(parser.blocks)
    full_text = "\n\n".join(text for _, text in blocks)
    if len(full_text) < 80:
        raise ValueError("public article body was unavailable or too short")
    outline = [
        text
        for tag, text in blocks
        if tag in {"h1", "h2", "h3", "h4"} and len(text) <= 100
    ][:20]
    if not outline:
        outline = [
            text
            for tag, text in blocks
            if tag in {"p", "blockquote"} and 8 <= len(text) <= 60
        ][:12]
    digest = hashlib.sha256(full_text.encode("utf-8")).hexdigest()
    excerpt = full_text[:240] + ("…" if len(full_text) > 240 else "")
    return {
        "keyword": keyword,
        "title": title or "Untitled WeChat article",
        "account": account or "Unknown account",
        "published_at": published or None,
        "source_url": url,
        "captured_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "sha256": digest,
        "character_count": len(full_text),
        "outline": outline,
        "private_excerpt": excerpt,
        "rights_status": "research-only",
        "_full_text": full_text,
    }


def dedupe_blocks(blocks: list[tuple[str, str]]) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    previous = ""
    for tag, text in blocks:
        if not text or text == previous:
            continue
        result.append((tag, text))
        previous = text
    return result


def write_outputs(
    records: list[dict[str, object]],
    errors: list[dict[str, str]],
    keyword: str,
    out_dir: Path,
) -> None:
    raw_dir = out_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = out_dir / "records.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as stream:
        for record in records:
            full_text = str(record.pop("_full_text"))
            raw_name = f"{record['sha256']}.txt"
            (raw_dir / raw_name).write_text(full_text, encoding="utf-8")
            record["private_raw_path"] = f"raw/{raw_name}"
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")

    lines = [
        "# Internal — Not for Publication",
        "",
        f"# WeChat Reference Pack — {keyword}",
        "",
        f"- Captured sources: {len(records)}",
        f"- Failed/blocked sources: {len(errors)}",
        "- Rights status: research-only",
        "- Use: topic discovery, structure analysis, factual leads, and original synthesis only.",
        "",
    ]
    for index, record in enumerate(records, 1):
        lines.extend(
            [
                f"## {index}. {record['title']}",
                "",
                f"- Account: {record['account']}",
                f"- Published: {record['published_at'] or 'unknown'}",
                f"- URL: {record['source_url']}",
                f"- SHA-256: `{record['sha256']}`",
                f"- Characters: {record['character_count']}",
                "- Outline:",
            ]
        )
        outline = record.get("outline") or []
        lines.extend(f"  - {item}" for item in outline)
        lines.extend(
            [
                f"- Limited private excerpt: {record['private_excerpt']}",
                "- Verification required: all technical values, standards, causal claims, and capability statements.",
                "",
            ]
        )
    if errors:
        lines.extend(["## Excluded or blocked", ""])
        for item in errors:
            lines.append(f"- {item['url']} — {item['error']}")
    (out_dir / "wechat-reference-pack.md").write_text(
        "\n".join(lines).rstrip() + "\n", encoding="utf-8"
    )


def load_urls(args: argparse.Namespace) -> list[str]:
    values = list(args.url or [])
    if args.url_file:
        values.extend(
            line.strip()
            for line in Path(args.url_file).read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        )
    result: list[str] = []
    for value in values:
        normalized = ensure_public_wechat_url(value)
        if normalized not in result:
            result.append(normalized)
    if len(result) > args.max_articles:
        result = result[: args.max_articles]
    return result


def command_queries(args: argparse.Namespace) -> int:
    encoded = urllib.parse.quote(args.keyword)
    google_query = urllib.parse.quote(f"site:mp.weixin.qq.com/s {args.keyword}")
    result = {
        "keyword": args.keyword,
        "sogou_weixin": f"https://weixin.sogou.com/weixin?type=2&query={encoded}",
        "google_supplement": f"https://www.google.com/search?q={google_query}",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def command_collect(args: argparse.Namespace) -> int:
    urls = load_urls(args)
    if not urls:
        print("No public WeChat URLs supplied.", file=sys.stderr)
        return 2
    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, object]] = []
    errors: list[dict[str, str]] = []
    for index, url in enumerate(urls):
        if index:
            time.sleep(args.delay)
        try:
            source, final_url = fetch(url, args.timeout)
            records.append(extract_record(source, final_url, args.keyword))
        except (ValueError, urllib.error.URLError, TimeoutError) as exc:
            errors.append({"url": url, "error": str(exc)})
    write_outputs(records, errors, args.keyword, out_dir)
    print(
        json.dumps(
            {
                "status": "ok" if records else "blocked",
                "captured": len(records),
                "failed": len(errors),
                "output": str(out_dir),
            },
            ensure_ascii=False,
        )
    )
    return 0 if records else 3


def command_self_test(args: argparse.Namespace) -> int:
    fixture = """
    <html><head>
      <meta property="og:title" content="塑料 CNC 加工测试文章">
      <meta name="author" content="制造工程测试号">
    </head><body>
      <div id="js_content" class="rich_media_content">
        <h2>材料与装夹</h2>
        <p>塑料零件加工时需要同时检查材料状态、装夹变形与刀具排屑。薄壁区域的支撑方式会改变加工中和松夹后的尺寸表现。</p>
        <h2>检验</h2>
        <p>关键尺寸应在最后一道可能改变几何形状的工序后进行确认。记录材料批次、加工方向和测量条件有助于定位异常来源。</p>
      </div>
    </body></html>
    """
    record = extract_record(
        fixture,
        "https://mp.weixin.qq.com/s?__biz=test&mid=1&idx=1&sn=test",
        "塑料CNC加工",
    )
    with tempfile.TemporaryDirectory() as temp_dir:
        output = Path(temp_dir)
        write_outputs([record], [], "塑料CNC加工", output)
        required = (
            output / "records.jsonl",
            output / "wechat-reference-pack.md",
        )
        if not all(path.is_file() and path.stat().st_size for path in required):
            raise RuntimeError("self-test output missing")
        raw_files = list((output / "raw").glob("*.txt"))
        if len(raw_files) != 1:
            raise RuntimeError("self-test raw capture missing")
    print("PASS: parser, metadata, private raw capture, JSONL, and reference pack")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build queries and collect public WeChat article research packs."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    queries = subparsers.add_parser("queries")
    queries.add_argument("--keyword", required=True)
    queries.set_defaults(handler=command_queries)

    collect = subparsers.add_parser("collect")
    collect.add_argument("--keyword", required=True)
    collect.add_argument("--url", action="append")
    collect.add_argument("--url-file")
    collect.add_argument("--out", required=True)
    collect.add_argument("--max-articles", type=int, default=MAX_ARTICLES)
    collect.add_argument("--delay", type=float, default=2.0)
    collect.add_argument("--timeout", type=int, default=20)
    collect.set_defaults(handler=command_collect)

    self_test = subparsers.add_parser("self-test")
    self_test.set_defaults(handler=command_self_test)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if getattr(args, "max_articles", MAX_ARTICLES) < 1:
        parser.error("--max-articles must be positive")
    if getattr(args, "max_articles", MAX_ARTICLES) > MAX_ARTICLES:
        parser.error(f"--max-articles cannot exceed {MAX_ARTICLES}")
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())

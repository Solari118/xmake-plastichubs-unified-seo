"""Build a SHA-256 inventory proving preservation of execution-relevant legacy files."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "plan": Path(r"C:\Users\Lostk\Documents\文章规划提示词-Plan"),
    "info": Path(r"C:\Users\Lostk\Documents\文章撰写提示词-Info"),
    "audit": Path(r"C:\Users\Lostk\Documents\文章优化提示词2.0-Aduit"),
    "b2b-image": Path(r"C:\Users\Lostk\Documents\B2B机加工生图"),
}
SCOPES = {
    "plan": ["AGENTS.md", "project.yaml", "codex-project.yaml", "README.md", "agents", "config", "data", "docs", "hooks", "skills", "tools", "integrated-assets"],
    "info": ["AGENTS.md", ".agents"],
    "audit": ["AGENTS.md", ".agents", "tools"],
    "b2b-image": ["AGENTS.md", "b2b-machining-image-generator", "composite-people.ps1", "fast-clean-factory.ps1", "retouch-factory.ps1", "selective-clean-factory.ps1"],
}
EXCLUDED_PARTS = {".git", "dist", "__pycache__", "outputs", "output", "input", "deliverables", "working", "scratch"}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def iter_scope(source: Path, rel: str):
    path = source / rel
    if not path.exists():
        return
    items = [path] if path.is_file() else path.rglob("*")
    for item in items:
        if item.is_file() and not EXCLUDED_PARTS.intersection(item.relative_to(source).parts):
            yield item


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="data/processed/source-capability-inventory.json")
    parser.add_argument("--refresh-from-legacy", action="store_true", help="Rebuild the migration baseline from current legacy roots; do not use after adapters are installed")
    args = parser.parse_args()
    output = ROOT / args.output
    if output.exists() and not args.refresh_from_legacy:
        result = json.loads(output.read_text(encoding="utf-8"))
        missing = 0
        for record in result["records"]:
            preserved = ROOT / record["preserved_path"]
            if not preserved.exists() or digest(preserved) != record["sha256"]:
                record["status"] = "missing_or_changed"
                missing += 1
            else:
                record["status"] = "preserved_snapshot"
        result["summary"]["preserved_snapshot"] = len(result["records"]) - missing
        result["summary"]["missing_or_changed"] = missing
        print(json.dumps(result["summary"], ensure_ascii=False))
        return 1 if missing else 0
    records = []
    for name, source in SOURCES.items():
        snapshot = ROOT / "data" / "raw" / "legacy-projects" / name
        for scope in SCOPES[name]:
            for item in iter_scope(source, scope) or []:
                rel = item.relative_to(source)
                preserved = snapshot / rel
                source_hash = digest(item)
                status = "preserved_snapshot" if preserved.exists() and digest(preserved) == source_hash else "missing_or_changed"
                records.append({"source_project": name, "source_path": rel.as_posix(), "sha256": source_hash, "preserved_path": preserved.relative_to(ROOT).as_posix(), "status": status})
    result = {
        "generated_on": str(date.today()),
        "scope": "execution-relevant source files; generated outputs, user inputs, caches, git metadata, and dist packages excluded",
        "records": records,
        "summary": {
            "total": len(records),
            "preserved_snapshot": sum(r["status"] == "preserved_snapshot" for r in records),
            "missing_or_changed": sum(r["status"] != "preserved_snapshot" for r in records),
        },
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], ensure_ascii=False))
    return 1 if result["summary"]["missing_or_changed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

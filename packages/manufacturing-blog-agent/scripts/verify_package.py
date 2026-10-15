"""Verify the standalone release and screen its text before upload."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from zipfile import ZipFile


REQUIRED = {
    "SKILL.md",
    "README.md",
    "manifest.json",
    "agents/openai.yaml",
    "references/artifact-contract.md",
    "references/writing-and-audit.md",
    "templates/run-state.json",
    "templates/plan-brief.json",
    "templates/audit-report.md",
    "evals/trigger-cases.jsonl",
    "reports/security_trust_report.md",
    "reports/output_quality_scorecard.md",
    "scripts/build_package.py",
    "scripts/verify_package.py",
}
ALLOWED_SUFFIXES = {".md", ".json", ".yaml", ".py", ".jsonl"}
FORBIDDEN_FRAGMENTS = (
    "企业知识（保密）",
    "private-resources",
    "company_info.md",
    "wxwork",
)
DRIVE_PATH = re.compile(r"[A-Za-z]:\\(?:Users|Documents|企业知识)\\", re.IGNORECASE)
SECRET_MARKER = re.compile(
    r"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['\"][^'\"]{8,}"
)


def collect_files(root: Path) -> list[Path]:
    files = sorted(
        path for path in root.rglob("*")
        if path.is_file() and path.name != "release-manifest.json"
    )
    found = {path.relative_to(root).as_posix() for path in files}
    missing = REQUIRED - found
    if missing:
        raise ValueError(f"missing required files: {sorted(missing)}")
    unexpected = found - REQUIRED
    if unexpected:
        raise ValueError(f"unapproved extra files: {sorted(unexpected)}")
    for path in files:
        if path.is_symlink() or path.suffix.lower() not in ALLOWED_SUFFIXES:
            raise ValueError(f"unapproved file: {path}")
        if any(part in {"__pycache__", ".git", "data", "knowledge", "output", "runs"} for part in path.parts):
            raise ValueError(f"unapproved directory: {path}")
    return files


def scan_text(root: Path, files: list[Path]) -> None:
    for path in files:
        if path.name == "verify_package.py":
            continue  # This verifier defines the prohibited patterns.
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        if any(token.lower() in lowered for token in FORBIDDEN_FRAGMENTS):
            raise ValueError(f"private-source marker: {path.relative_to(root)}")
        if DRIVE_PATH.search(text) or SECRET_MARKER.search(text):
            raise ValueError(f"local path or secret marker: {path.relative_to(root)}")
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    for relative in re.findall(r"`((?:references|templates)/[^\`]+)`", skill):
        if not (root / relative).is_file() and not relative.endswith("/"):
            raise ValueError(f"broken Skill reference: {relative}")
    cases = [
        json.loads(line)
        for line in (root / "evals/trigger-cases.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if len(cases) < 5 or not any(case["expected"].startswith("do_not_route") for case in cases):
        raise ValueError("trigger case coverage is incomplete")


def verify(root: Path, archive: Path) -> dict:
    files = collect_files(root)
    scan_text(root, files)
    manifest = json.loads((root / "release-manifest.json").read_text(encoding="utf-8"))
    hashes = {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in files
    }
    if manifest["files_sha256"] != hashes or manifest["file_count"] != len(files):
        raise ValueError("source manifest hash mismatch")
    expected_names = {f"{root.name}/{name}" for name in hashes}
    expected_names.add(f"{root.name}/release-manifest.json")
    with ZipFile(archive) as package:
        names = package.namelist()
        if len(names) != len(set(names)) or set(names) != expected_names:
            raise ValueError("archive member mismatch")
        if package.testzip() is not None:
            raise ValueError("archive CRC failure")
        for name, digest in hashes.items():
            if hashlib.sha256(package.read(f"{root.name}/{name}")).hexdigest() != digest:
                raise ValueError(f"archive hash mismatch: {name}")
        if package.read(f"{root.name}/release-manifest.json") != (
            root / "release-manifest.json"
        ).read_bytes():
            raise ValueError("archive manifest mismatch")
    return {
        "status": "PASS",
        "file_count": len(names),
        "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--archive", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    version = json.loads((root / "manifest.json").read_text(encoding="utf-8"))["version"]
    archive = args.archive or root.parent / f"{root.name}-v{version}.zip"
    print(json.dumps(verify(root, archive.resolve()), sort_keys=True))


if __name__ == "__main__":
    main()

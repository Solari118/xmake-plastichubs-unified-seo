"""Synchronize canonical skills into .agents and .codex discovery mirrors."""

from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "skills"
MIRRORS = [ROOT / ".agents" / "skills", ROOT / ".codex" / "skills"]


def files(root: Path) -> dict[str, Path]:
    return {p.relative_to(root).as_posix(): p for p in root.rglob("*") if p.is_file() and "dist" not in p.parts and "__pycache__" not in p.parts}


def differences(mirror: Path) -> list[str]:
    source = files(CANONICAL)
    target = files(mirror) if mirror.exists() else {}
    keys = sorted(set(source) | set(target))
    return [key for key in keys if key not in source or key not in target or not filecmp.cmp(source[key], target[key], shallow=False)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Copy canonical files into both discovery mirrors")
    args = parser.parse_args()
    if args.write:
        for mirror in MIRRORS:
            mirror.mkdir(parents=True, exist_ok=True)
            shutil.copytree(CANONICAL, mirror, dirs_exist_ok=True, ignore=shutil.ignore_patterns("dist", "__pycache__"))
    failed = False
    for mirror in MIRRORS:
        diff = differences(mirror)
        print(f"{mirror.relative_to(ROOT)}: {'PASS' if not diff else 'FAIL'} ({len(diff)} differences)")
        failed = failed or bool(diff)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())


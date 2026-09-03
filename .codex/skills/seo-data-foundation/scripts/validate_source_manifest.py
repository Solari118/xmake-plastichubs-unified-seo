#!/usr/bin/env python3
import json
import sys
from pathlib import Path

REQUIRED = {
    "source_id", "source_type", "data_source", "fetched_at",
    "freshness_status", "confidence", "availability"
}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_source_manifest.py <manifest.json>")
        return 2
    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        print("BLOCKED: sources must be a non-empty list")
        return 1
    errors = []
    stale = []
    for index, source in enumerate(sources):
        missing = sorted(REQUIRED - set(source))
        if missing:
            errors.append(f"sources[{index}] missing: {', '.join(missing)}")
        if source.get("freshness_status") == "stale":
            stale.append(source.get("source_id", str(index)))
    if errors:
        print("BLOCKED_MISSING_CRITICAL_DATA")
        print("\n".join(errors))
        return 1
    if stale:
        print("WARNING_STALE_DATA: " + ", ".join(stale))
        return 0
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


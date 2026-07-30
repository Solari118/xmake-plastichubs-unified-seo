#!/usr/bin/env python3
import json
import sys
from pathlib import Path

REQUIRED = {
    "proposal_id", "source_agent", "brand", "target", "action_type",
    "summary", "data_source", "fetched_at", "confidence",
    "business_value", "urgency", "effort"
}


def score(item):
    effort = max(float(item["effort"]), 1.0)
    return round(
        float(item["business_value"]) * float(item["urgency"])
        * float(item["confidence"]) / effort, 4
    )


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: reconcile_proposals.py <output.json> <proposal.json>...")
        return 2
    proposals = []
    for name in sys.argv[2:]:
        raw = json.loads(Path(name).read_text(encoding="utf-8"))
        proposals.extend(raw if isinstance(raw, list) else raw.get("proposals", []))
    errors = []
    for index, item in enumerate(proposals):
        missing = sorted(REQUIRED - set(item))
        if missing:
            errors.append(f"proposal[{index}] missing: {', '.join(missing)}")
    if errors:
        print("\n".join(errors))
        return 1
    groups = {}
    target_actions = {}
    for item in proposals:
        key = (item["brand"], item["target"], item["action_type"])
        groups.setdefault(key, []).append(item)
        target_actions.setdefault((item["brand"], item["target"]), set()).add(item["action_type"])
    queue = []
    for key, items in groups.items():
        primary = max(items, key=lambda value: float(value["confidence"]))
        record = dict(primary)
        record["priority_score"] = score(primary)
        record["consensus_agents"] = sorted({item["source_agent"] for item in items})
        record["conflict"] = len(target_actions[(key[0], key[1])]) > 1
        record["status"] = (
            "WAITING_FOR_INTENT_APPROVAL"
            if record.get("changes_search_intent") or record.get("changes_content_format")
            else "CANDIDATE"
        )
        queue.append(record)
    queue.sort(key=lambda item: (-item["priority_score"], item["proposal_id"]))
    output = {"action_queue": queue, "proposal_count": len(proposals)}
    Path(sys.argv[1]).write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    print(f"PASS: {len(queue)} candidate actions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


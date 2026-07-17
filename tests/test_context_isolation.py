import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ContextIsolationTests(unittest.TestCase):
    def test_fixture_disables_raw_conversation_forwarding(self):
        fixture = json.loads((ROOT / "data" / "fixtures" / "task-envelope.article.json").read_text(encoding="utf-8"))
        self.assertIs(fixture["raw_conversation_forwarding"], False)

    def test_visual_contract_blocks_private_source_forwarding(self):
        schema = json.loads((ROOT / "schemas" / "visual-brief.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["private_source_forwarded"]["const"], False)

    def test_legacy_snapshots_are_non_executable(self):
        policy = (ROOT / "policies" / "context-isolation.md").read_text(encoding="utf-8")
        self.assertIn("never included in automatic retrieval", policy)


if __name__ == "__main__":
    unittest.main()


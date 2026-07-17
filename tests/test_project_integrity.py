import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProjectIntegrityTests(unittest.TestCase):
    def test_all_stage_skills_exist(self):
        skills = ["b2b-seo-topic-map-builder", "manufacturing-blog-writer", "seo-geo-content-auditor", "b2b-machining-image-generator", "xmake-plastichubs-website-ops"]
        for skill in skills:
            self.assertTrue((ROOT / "skills" / skill / "SKILL.md").exists(), skill)

    def test_contracts_share_new_fields(self):
        contracts = list(ROOT.glob("skills/*/references/content-brief-contract.md"))
        self.assertGreaterEqual(len(contracts), 3)
        for contract in contracts:
            text = contract.read_text(encoding="utf-8")
            self.assertIn("PRIMARY_SERVICE:", text, contract)
            self.assertIn("CROSS_SERVICE_LINK_PLAN:", text, contract)

    def test_schema_json_is_valid(self):
        for schema in (ROOT / "schemas").glob("*.json"):
            json.loads(schema.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()


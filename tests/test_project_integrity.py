import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProjectIntegrityTests(unittest.TestCase):
    def test_all_stage_skills_exist(self):
        skills = [
            "b2b-seo-topic-map-builder",
            "manufacturing-blog-writer",
            "seo-geo-content-auditor",
            "b2b-machining-image-generator",
            "xmake-plastichubs-website-ops",
            "seo-content-performance-review",
        ]
        for skill in skills:
            self.assertTrue((ROOT / "skills" / skill / "SKILL.md").exists(), skill)

    def test_contracts_share_new_fields(self):
        contracts = list(ROOT.glob("skills/*/references/content-brief-contract.md"))
        self.assertGreaterEqual(len(contracts), 3)
        for contract in contracts:
            text = contract.read_text(encoding="utf-8")
            for field in [
                "PRIMARY_SERVICE:",
                "CROSS_SERVICE_LINK_PLAN:",
                "TOP_TEN_SERP_RESULTS:",
                "PRIMARY_STRUCTURE_REFERENCE:",
                "STRUCTURE_ADAPTATION_MAP:",
                "STYLE_PROFILE:",
                "ARTICLE_ARCHETYPE:",
                "INTERNAL_LINK_DEPLOYMENT:",
                "COMPETITOR_PAGE_STRENGTH:",
            ]:
                self.assertIn(field, text, contract)

    def test_schema_json_is_valid(self):
        for schema in (ROOT / "schemas").glob("*.json"):
            json.loads(schema.read_text(encoding="utf-8"))

    def test_private_resource_controls_exist(self):
        required = [
            ROOT / "config" / "private-resource-sources.yaml",
            ROOT / "policies" / "private-resource-policy.md",
            ROOT / "scripts" / "sync_private_resources.ps1",
            ROOT / "scripts" / "assert_private_packaging_scope.ps1",
        ]
        for path in required:
            self.assertTrue(path.exists(), path)
        policy = required[1].read_text(encoding="utf-8")
        self.assertIn("Local project copies are allowed", policy)
        self.assertIn("Every packaging request requires a fresh question", policy)


if __name__ == "__main__":
    unittest.main()

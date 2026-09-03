from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ServicePageTurningHardeningTests(unittest.TestCase):
    def setUp(self) -> None:
        self.skill = (ROOT / "skills" / "xmake-plastichubs-website-ops" / "SKILL.md").read_text(encoding="utf-8")

    def test_design_corrections_are_preserved(self) -> None:
        for phrase in (
            "append-only requirement ledger",
            "full-bleed Hero background",
            "fixed/min-height layouts that leave dead space",
            "Material selectors must change both copy and imagery",
            "avoid identifiable faces",
            "mobile section index",
            "capability proof module",
        ):
            self.assertIn(phrase, self.skill)

    def test_search_and_deployment_recovery_are_bounded(self) -> None:
        for phrase in (
            "load-test that exact URL",
            "at least five accessible commercial pages",
            "Allow one automatic large-paste/update attempt",
            "read back the persisted editor value",
            "Never append page payloads to raster images",
            "one intended page wrapper",
        ):
            self.assertIn(phrase, self.skill)

    def test_article_skills_are_not_part_of_this_patch(self) -> None:
        self.assertTrue((ROOT / "skills" / "manufacturing-blog-writer" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "skills" / "seo-geo-content-auditor" / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()

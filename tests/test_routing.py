import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from route_task import route  # noqa: E402


class RoutingTests(unittest.TestCase):
    def test_topic_runs_full_order(self):
        self.assertEqual(route("canonical", "full_pipeline", "topic"), ["plan", "info", "audit", "b2b-image", "final-output"])

    def test_supplied_article_enters_at_audit(self):
        self.assertEqual(route("article", "full_pipeline", "article"), ["audit", "b2b-image", "final-output"])

    def test_info_defect_rolls_back_and_reaudits(self):
        self.assertEqual(route("article", "full_pipeline", "article", "info"), ["audit", "info", "audit", "b2b-image", "final-output"])

    def test_plan_defect_replays_info_and_audit(self):
        self.assertEqual(route("article", "full_pipeline", "article", "plan"), ["audit", "plan", "info", "audit", "b2b-image", "final-output"])

    def test_standalone_image_is_isolated(self):
        self.assertEqual(route("b2b-image", "standalone_image", "none"), ["b2b-image"])

    def test_declared_eval_cases(self):
        cases = json.loads((ROOT / "skills" / "manufacturing-content-pipeline" / "evals" / "route-cases.json").read_text(encoding="utf-8"))
        for case in cases:
            detected = "article" if case["entry"] == "article" else "none"
            actual = route(case["entry"], case["mode"], detected, case.get("audit_defect", "none"))
            self.assertEqual(actual, case["expected"], case["id"])


if __name__ == "__main__":
    unittest.main()


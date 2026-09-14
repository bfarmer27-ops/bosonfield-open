import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IDENTITY = ROOT / "brand-identity.json"
PUBLIC_TEXT = [
    *ROOT.glob("*.md"),
    ROOT / "index.html",
    *ROOT.glob("community/*.md"),
    *ROOT.glob("research/*.md"),
    *ROOT.glob(".github/ISSUE_TEMPLATE/*.*"),
]


class BrandIdentityTests(unittest.TestCase):
    def test_user_locked_display_name_is_exact(self):
        identity = json.loads(IDENTITY.read_text(encoding="utf-8"))
        self.assertTrue(identity["user_locked"])
        self.assertEqual(identity["display_name"], "BosonField")
        self.assertEqual(identity["fallback_handle"], "bosonfieldopen")

    def test_old_unapproved_display_name_is_absent_from_public_text(self):
        forbidden = "BosonField" + " Open"
        hits = []
        for path in PUBLIC_TEXT:
            if path.is_file() and forbidden in path.read_text(encoding="utf-8"):
                hits.append(str(path.relative_to(ROOT)))
        self.assertEqual(hits, [])

    def test_asset_source_does_not_draw_old_open_name_line(self):
        source = (ROOT / "scripts" / "generate_brand_assets.py").read_text(encoding="utf-8")
        self.assertNotIn('"BosonField' + ' Open"', source)
        self.assertNotIn('"OPEN"', source)


if __name__ == "__main__":
    unittest.main()

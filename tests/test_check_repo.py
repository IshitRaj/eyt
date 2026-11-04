"""Unit checks for EYT's narrow packaging checker (not agent effectiveness)."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_repo.py"
spec = importlib.util.spec_from_file_location("check_repo", MODULE_PATH)
checker = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(checker)


class RepoCheckTests(unittest.TestCase):
    def test_actual_repository_structure(self):
        self.assertEqual([], checker.check_repo())

    def test_missing_frontmatter(self):
        with self.assertRaisesRegex(ValueError, "frontmatter"):
            checker.parse_frontmatter("# Not a skill")

    def test_bad_skill_name(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "eyt" / "SKILL.md"
            p.parent.mkdir()
            p.write_text("---\nname: Bad Name\ndescription: Use when building web apps\nlicense: MIT\n---\n", encoding="utf-8")
            self.assertIn("Invalid skill name", checker.validate_skill(p))

    def test_broken_relative_link(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "doc.md").write_text("[missing](other.md) [online](https://example.com)", encoding="utf-8")
            self.assertEqual(1, len(checker.validate_links(root)))

    def test_valid_relative_link(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "a.md").write_text("[b](b.md#section)", encoding="utf-8")
            (root / "b.md").write_text("# Section", encoding="utf-8")
            self.assertEqual([], checker.validate_links(root))


if __name__ == "__main__":
    unittest.main()

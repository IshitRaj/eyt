#!/usr/bin/env python3
"""Check EYT packaging and local Markdown links. Does NOT assess skill effectiveness."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "eyt" / "SKILL.md"
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
VALID_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def parse_frontmatter(content: str) -> dict[str, str]:
    """Read only simple string-value fields used in this repository."""
    if not content.startswith("---\n"):
        raise ValueError("Missing leading YAML frontmatter delimiter")
    end = content.find("\n---\n", 4)
    if end < 0:
        raise ValueError("Missing closing YAML frontmatter delimiter")
    result: dict[str, str] = {}
    for line in content[4:end].splitlines():
        if line and not line.startswith((" ", "\t")) and ":" in line:
            k, v = line.split(":", 1)
            result[k.strip()] = v.strip().strip("\"'")
    return result


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"Missing skill: {path}"]
    try:
        fields = parse_frontmatter(path.read_text(encoding="utf-8"))
    except (UnicodeError, ValueError) as exc:
        return [f"SKILL.md: {exc}"]
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not VALID_NAME.fullmatch(name) or len(name) > 64:
        errors.append("Invalid skill name")
    if name != path.parent.name:
        errors.append("Skill name must match its parent directory")
    if not (1 <= len(description) <= 1024):
        errors.append("Description must have 1-1024 characters")
    if not fields.get("license"):
        errors.append("No license field specified")
    return errors


def validate_links(root: Path) -> list[str]:
    errors: list[str] = []
    for doc in root.rglob("*.md"):
        if ".git" in doc.parts:
            continue
        content = doc.read_text(encoding="utf-8")
        for raw in LINK.findall(content):
            destination = raw.strip().split(maxsplit=1)[0]
            if destination.startswith(("https://", "http://", "mailto:", "#")):
                continue
            # A link to a local path with optional section anchor.
            target = unquote(destination.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (doc.parent / target).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f"Broken or escaping relative link: {doc.relative_to(root)} -> {destination}")
    return errors


def validate_plain_dashes(root: Path) -> list[str]:
    """Keep public Markdown free of em-dash punctuation for reading comfort."""
    errors: list[str] = []
    for doc in root.rglob("*.md"):
        if ".git" in doc.parts:
            continue
        if "\u2014" in doc.read_text(encoding="utf-8"):
            errors.append(f"Em dash in Markdown: {doc.relative_to(root)}")
    return errors


def check_repo(root: Path = ROOT) -> list[str]:
    expected = [
        root / "README.md",
        root / "LICENSE",
        root / "CONTRIBUTING.md",
        root / "skills" / "eyt" / "SKILL.md",
        root / "evaluations" / "SCENARIOS.md",
        root / "evaluations" / "RUBRIC.md",
        root / "docs" / "ORIGINS_AND_LIMITATIONS.md",
    ]
    errors = [f"Missing required file: {f.relative_to(root)}" for f in expected if not f.is_file()]
    errors += validate_skill(root / "skills" / "eyt" / "SKILL.md")
    errors += validate_links(root)
    errors += validate_plain_dashes(root)
    skill_files = list((root / "skills").rglob("SKILL.md"))
    if len(skill_files) != 1:
        errors.append(f"Expected one installable SKILL.md, found {len(skill_files)}")
    return errors


def main() -> int:
    errors = check_repo()
    if errors:
        print("EYT static packaging check FAILED:")
        for error in errors:
            print("-", error)
        return 1
    print("EYT static packaging and local-link checks: PASS")
    print("NOTE: Does not test agent behavior, security, accessibility, or app correctness.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Dependency-free checks for this repository's scalar skill frontmatter and links."""

import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/context-bridge"


def check():
    errors = []
    content = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    parts = content.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        return ["SKILL.md needs leading YAML frontmatter"]
    fields = {}
    for line in parts[1].strip().splitlines():
        if ": " not in line:
            errors.append("Use the repository's simple scalar frontmatter convention")
            continue
        key, value = line.split(": ", 1)
        if key in fields:
            errors.append("Duplicate frontmatter field")
        fields[key] = value
    name = fields.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64 or name != SKILL.name:
        errors.append("Skill name violates Agent Skills name/directory rules")
    if not 1 <= len(fields.get("description", "")) <= 1024:
        errors.append("Description must be 1–1024 characters")
    if set(fields) - {"name", "description", "license", "compatibility", "allowed-tools"}:
        errors.append("Unsupported field in this scalar frontmatter check")
    if len(content.splitlines()) > 500:
        errors.append("Entrypoint exceeds the progressive-disclosure guideline")
    if len(fields.get("compatibility", "")) > 500:
        errors.append("Compatibility exceeds 500 characters")
    for path in ROOT.rglob("*.md"):
        if any(part in (".git", ".local", "runs", "actual", ".agents", ".claude") for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0]
            if not target or re.match(r"[a-z]+://", target) or target.startswith("mailto:"):
                continue
            if not (path.parent / target).exists():
                errors.append(f"Broken local link in {path.relative_to(ROOT).as_posix()}")
    schema = json.loads((SKILL / "references/context.schema.json").read_text(encoding="utf-8"))
    supported = {"$schema", "title", "description", "$ref", "$defs", "type", "required",
                 "additionalProperties", "properties", "items", "minItems", "uniqueItems",
                 "minLength", "maxLength", "pattern", "enum", "format", "anyOf"}

    def walk(rule):
        if set(rule) - supported:
            errors.append("Schema uses vocabulary not handled by the local validator")
        for key in ("properties", "$defs"):
            for child in rule.get(key, {}).values():
                walk(child)
        if "items" in rule:
            walk(rule["items"])
        for child in rule.get("anyOf", []):
            walk(child)
    walk(schema)
    cases = json.loads((ROOT / "tests/scenarios/cases.json").read_text(encoding="utf-8"))
    if len(cases) < 18 or len({case["id"] for case in cases}) != len(cases):
        errors.append("At least 18 uniquely identified behavioral scenarios are required")
    print(f"Skill: {len(content.splitlines())} lines; description: {len(fields.get('description', ''))} characters; scenarios: {len(cases)}")
    return errors


if __name__ == "__main__":
    failures = check()
    for failure in failures:
        print(failure, file=sys.stderr)
    if not failures:
        print("PASS: skill structure, supported schema vocabulary and local links")
    raise SystemExit(bool(failures))

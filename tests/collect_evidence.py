#!/usr/bin/env python3
"""Collect reviewed synthetic outputs, never raw host traces or private inputs.

Run only after manually reviewing the named completed scenarios. Artifact bytes
are preserved; environment-specific absolute links in final responses are made
relative. This is an explicit publishing preparation step, not part of the Skill.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil

from assess_live import assess, ROOT


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_root", type=Path)
    parser.add_argument("--cases", nargs="+", required=True)
    args = parser.parse_args()
    catalog = json.loads((ROOT / "tests/scenarios/cases.json").read_text(encoding="utf-8"))
    for case in catalog:
        if case["id"] not in args.cases:
            continue
        workspace = args.run_root / case["id"]
        result = assess(case, workspace)
        if result["status"] != "PASS":
            raise SystemExit(f"{case['id']}: only passing, manually reviewed synthetic runs may be collected")
        destination = ROOT / "tests/actual" / case["id"]
        destination.mkdir(parents=True, exist_ok=False)
        shutil.copytree(workspace / "output", destination / "output")
        response = (workspace / "response.md").read_text(encoding="utf-8")
        for prefix in (str(workspace), workspace.as_posix()):
            response = re.sub(re.escape(prefix), ".", response, flags=re.I)
        response = response.replace("./.agents/skills/context-bridge/", "../../../skills/context-bridge/")
        response = response.replace("./input/", f"../../fixtures/{case['id']}/")
        response = re.sub(r"(\.md):\d+(?=\))", r"\1", response)
        (destination / "response.md").write_text(response, encoding="utf-8")
        meta = json.loads((workspace / "run.json").read_text(encoding="utf-8"))
        installed = workspace / ".agents/skills/context-bridge"
        meta["installed_skill_hashes"] = {
            p.relative_to(installed).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(installed.rglob("*")) if p.is_file() and "__pycache__" not in p.parts}
        (destination / "run.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        result["review"] = "Actual artifacts manually compared with raw fixture and stated semantic criteria before collection."
        (destination / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(case["id"], "collected")


if __name__ == "__main__":
    main()

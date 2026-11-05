#!/usr/bin/env python3
"""Create a reproducible installable skill ZIP from checked-in skill sources."""

import hashlib
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/context-bridge"
DEST = ROOT / "dist/context-bridge-0.1.0.zip"


def main():
    DEST.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(DEST, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SKILL.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            if path.is_symlink():
                raise SystemExit("Refusing symlinked release content")
            relative = path.relative_to(SKILL).as_posix()
            info = zipfile.ZipInfo("context-bridge/" + relative, (2026, 11, 5, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    digest = hashlib.sha256(DEST.read_bytes()).hexdigest()
    DEST.with_suffix(".zip.sha256").write_text(f"{digest}  {DEST.name}\n", encoding="utf-8")
    print(f"{DEST.name}: {digest}")


if __name__ == "__main__":
    main()

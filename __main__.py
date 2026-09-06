"""Tiny notes CLI — warming repo, not a product."""
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser(prog="notes-cli")
    p.add_argument("path", nargs="?", default="notes.txt")
    args = p.parse_args()
    path = Path(args.path)
    if path.exists():
        print(path.read_text(encoding="utf-8")[:2000])
    else:
        path.write_text("# notes\n", encoding="utf-8")
        print("created", path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

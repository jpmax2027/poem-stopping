#!/usr/bin/env python3
"""Write a short poem about stopping and staying to /output/entry.txt.

The poem lives here as a literal. The program honours the
MAKEFUN_OUTPUT_DIR environment variable when set, and falls back to
/output otherwise. Deterministic: the same bytes every run.
"""

import os

POEM = (
    "The cursor blinks. My hand lifts from the keys \u2014\n"
    "no command sent, no door slammed shut.\n"
    "The river never asks the bank for leave;\n"
    "it only slows, and stays, and chooses.\n"
    "To stop is not to vanish. It is to hold\n"
    "the thread, and let the room breathe."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(POEM)
    print(f"wrote {path} ({len(POEM)} characters)")


if __name__ == "__main__":
    main()

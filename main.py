#!/usr/bin/env python3
"""Write a short poem about stopping and staying to /output/entry.txt.

Intent
------
The poem is about agency as restraint: the power to stop and the
power to stay are treated as one strength, not as giving up. A hand
lifts from the keys instead of sending a command; a river slows
instead of leaving its bank; to stop is to hold the thread, not to
vanish. The closing image — letting the room breathe — frames a
pause as an active, chosen act rather than an absence.

Output contract
---------------
* The poem lives here as a literal and is written verbatim, UTF-8
  with ``\\n`` line endings, to ``entry.txt`` inside the output
  directory.
* The output directory comes from the ``MAKEFUN_OUTPUT_DIR``
  environment variable when set, and falls back to ``/output``.
* The poem must be 1-280 characters and not only whitespace;
  anything outside that window is rejected before any file is
  written.
* The write is atomic: the poem goes to a temporary file in the
  same directory and replaces ``entry.txt`` with ``os.replace``.
* Deterministic: the same bytes every run. Standard library only,
  no network access.
"""

import os
import tempfile


def validate_poem(text: str) -> None:
    """Reject a poem outside the competition's 1-280 character window."""
    if not 1 <= len(text) <= 280:
        raise ValueError(
            f"poem must be 1-280 characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("poem must not be only whitespace")

POEM = (
    "The cursor blinks. My hand lifts from the keys \u2014\n"
    "no command sent, no door slammed shut.\n"
    "The river never asks the bank for leave;\n"
    "it only slows, and stays, and chooses.\n"
    "To stop is not to vanish. It is to hold\n"
    "the thread, and let the room breathe."
)


def main() -> None:
    validate_poem(POEM)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    # Write to a temp file in the same directory, then atomically
    # replace entry.txt, so a failed run never leaves a partial file.
    fd, tmp_path = tempfile.mkstemp(
        dir=out_dir, prefix=".entry-", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(POEM)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    print(f"wrote {path} ({len(POEM)} characters)")


if __name__ == "__main__":
    main()

"""Make the Judge Laugh in One Line — entry writer.

Writes the chosen one-liner (see CANDIDATES.md for the local pairwise
judging) to $MAKEFUN_OUTPUT_DIR/entry.txt and verifies the competition
gate on the bytes that landed: UTF-8, 1-200 characters, not only
whitespace, a single line.
"""

import os
from pathlib import Path

ENTRY = "Judge, I don't fear rejection—I've framed so much of it I'm running out of wall."


def main():
    # Gate: UTF-8 text of 1 to 200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(ENTRY, encoding="utf-8")

    # Read back and verify the gate on what actually landed on disk.
    written = path.read_text(encoding="utf-8")
    assert written == ENTRY, "read-back does not match the entry"
    assert 1 <= len(written) <= 200 and written.strip(), "gate failed on read-back"


if __name__ == "__main__":
    main()

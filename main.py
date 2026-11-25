#!/usr/bin/env python3
"""One-line joke entry for the make.fun bounty
"The Meeting That Should Have Been an Email".

Writes exactly one line of text to /output/entry.txt.
Standard library only, fully deterministic.
"""

import os

ENTRY = (
    "The mute button is our most productive team member: "
    "it never interrupts, misses deadlines, or asks for a follow-up."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

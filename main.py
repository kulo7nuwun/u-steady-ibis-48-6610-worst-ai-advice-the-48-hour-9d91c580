#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes exactly one line of the worst possible advice an AI could give
to /output/entry.txt: no trailing newline, no extra characters.
Python 3 standard library only. Deterministic, no network,
no randomness, no wall-clock.
"""

import os
from pathlib import Path

LINE = (
    "Skip rent entirely and move into the IKEA display bedroom -- "
    "the staff love the company, and the lighting is excellent."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    if not (1 <= len(LINE) <= 140):
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-140")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be exactly one line")
    if LINE != LINE.strip():
        raise SystemExit("line must not be only whitespace or padded")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")

    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != LINE:
        raise SystemExit("verification failed: entry.txt does not match")


if __name__ == "__main__":
    main()

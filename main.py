#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

The joke: an AI cheerfully tells you to stop paying rent and just live
in the IKEA display bedroom, as if a showroom bed were a rent-free flat,
the staff were roommates who enjoy the company, and good lighting made
up for having no home. Concrete enough to picture, confident enough to
sound helpful, terrible enough to get you thrown out of the store.

Writes exactly one line of that advice to /output/entry.txt: no
trailing newline, no extra characters. Python 3 standard library
only. Deterministic, no network, no randomness, no wall-clock.
"""

import os
from pathlib import Path

LINE = (
    "Skip rent entirely and move into the IKEA display bedroom -- "
    "the staff love the company, and the lighting is excellent."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    # Defensive validation: the entry must be exactly one tight line.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert not LINE.endswith(("\n", "\r")), "line must have no trailing newline"
    assert "\n" not in LINE and "\r" not in LINE, "line must be exactly one line"
    assert LINE == LINE.strip(), "line must not be padded or only whitespace"

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")

    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != LINE:
        raise SystemExit("verification failed: entry.txt does not match")


if __name__ == "__main__":
    main()

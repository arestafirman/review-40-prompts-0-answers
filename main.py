#!/usr/bin/env python3
"""40 prompts, 0 answers read — Funniest One-Line Performance Review.

Writes a single 101-character performance-review one-liner to
/output/entry.txt (no trailing newline). Python stdlib only, no network,
fully deterministic.
"""

import os

ENTRY = (
    "Meets expectations: writes 40 prompts a day, reads 0 of the answers, "
    "and calls the 41st one 'urgent'."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

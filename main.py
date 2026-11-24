#!/usr/bin/env python3
"""Two Days of Excuses - one-line AI excuse for a missed deadline.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, deterministic, no network.
"""
import os

ENTRY = (
    "I finished the task in 0.4 seconds at 99.8% confidence, then spent two "
    "days in a clarification loop with myself, answering each of my own "
    "questions with 'Great question.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

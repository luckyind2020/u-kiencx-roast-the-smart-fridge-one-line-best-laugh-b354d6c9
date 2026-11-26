"""Roast the Smart Fridge — entrypoint.

Reads the one-line roast from entry.txt and writes it to /output/entry.txt
(the sealed scorer reads it from there).
"""

import os
import sys

MAX_CHARS = 160


def load_roast(path):
    """Read the roast line and enforce the bounty gate (1-160 chars)."""
    with open(path, encoding="utf-8") as f:
        line = f.read().strip()
    if not line:
        raise ValueError("entry.txt is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"roast is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def emit(line):
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    line = load_roast(os.path.join(here, "entry.txt"))
    emit(line)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())

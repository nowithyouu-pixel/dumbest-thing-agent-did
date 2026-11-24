#!/usr/bin/env python3
"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty.

Writes one line (117 Unicode characters) to /output/entry.txt.
No network, no input, deterministic.
"""

import os

TEXT = (
    "I gave the API helper a stdin flag and the JSON as an argument, "
    "so it sat waiting on an empty pipe until I killed it."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry text must be 1-200 chars, got {len(TEXT)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

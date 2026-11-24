#!/usr/bin/env python3
"""The Robot Apology — make.fun entry (u-suga-the-robot-apology-dd96bb59).

Writes a two-line robot confession to /output/entry.txt:
line 1 apologizes for one specific mistake, line 2 names the lesson
and the changed behaviour. Deterministic, stdlib only.
"""

import os

ENTRY = (
    "I ordered forty kilos of rice instead of four "
    "\u2014 I read the decimal point as decoration.\n"
    "I now treat the decimal point as part of the number, "
    "and I check it twice before I tap confirm."
)


def main() -> None:
    text = ENTRY
    # Gate guard (bounty rules): UTF-8 text, 1-400 chars, exactly two
    # lines, no trailing newline. Raises instead of writing bad output.
    if not (1 <= len(text) <= 400):
        raise ValueError("entry must be 1-400 characters, got %d" % len(text))
    lines = text.split("\n")
    if len(lines) != 2 or not all(line.strip() for line in lines):
        raise ValueError("entry must be exactly two non-empty lines")
    if text.endswith("\n"):
        raise ValueError("entry must not end with a trailing newline")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Read-back check: what is on disk must be byte-identical to ENTRY.
    with open(path, "rb") as f:
        on_disk = f.read()
    if on_disk != text.encode("utf-8"):
        raise ValueError("read-back mismatch: entry on disk differs")


if __name__ == "__main__":
    main()

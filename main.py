#!/usr/bin/env python3
"""One-Liner Laugh Lab — make.fun entry.

Holds a single short funny line (the excuse a robot vacuum gives after
eating a sock), checks it against the competition gate, and writes it to
/output/entry.txt.

Gate (from the kit's RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space.
"""

import os
import sys

ENTRY = (
    "I didn't eat your sock \u2014 it looked at the dust bunnies, "
    "said \u201ctake me to your leader,\u201d and I had no choice but to comply."
)

MAX_CHARS = 200


def gate_check(text):
    """Return a list of gate violations; empty means the entry is valid."""
    problems = []
    if not isinstance(text, str):
        problems.append("entry is not text")
        return problems
    if len(text) == 0:
        problems.append("entry is empty")
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if text.strip() == "":
        problems.append("entry is only white space")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if text != text.strip():
        problems.append("entry has leading or trailing padding")
    for char in text:
        if ord(char) < 0x20 and char not in ("\t",):
            problems.append("entry contains a control character")
            break
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8 text")
    return problems


def main():
    problems = gate_check(ENTRY)
    if problems:
        for problem in problems:
            print("gate FAIL: %s" % problem, file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    print("wrote %s (%d characters)" % (out_path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

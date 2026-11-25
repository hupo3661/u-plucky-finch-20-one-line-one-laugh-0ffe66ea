#!/usr/bin/env python3
"""One Line, One Laugh.

Writes the one-line joke to /output/entry.txt and prints it.

The joke: a smartwatch celebrates 10,000 steps, and the wearer was only
looking for the TV remote. The praise and the couch are the whole gag,
and the turn lands after the dash, in the last words.
"""

import os

LINE = "My smartwatch congratulated me on 10,000 steps — I was just looking for the TV remote."

# The sealed scorer gates on 1-200 UTF-8 characters, not only whitespace.
# Fail loudly here rather than shipping an entry the gate would refuse.
def validate(line: str) -> str:
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry line fails the 1-200 char gate")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def output_path() -> str:
    """Where the entry goes: /output/entry.txt, unless OUTPUT_PATH says otherwise.

    The grader runs with the default. The override exists only so a local
    check can aim at a throwaway file instead of the real output path.
    """
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    line = validate(LINE)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()

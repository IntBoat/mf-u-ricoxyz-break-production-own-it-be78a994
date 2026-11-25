#!/usr/bin/env python3
"""Break Production, Own It — a make.fun one-line entry. The program writes the entry text to /output/entry.txt, where the competition's sealed scorer reads it."""

from pathlib import Path

ENTRY = "I have broken production. I have also updated my resume, my alibi, and the definition of working as intended."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()

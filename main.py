#!/usr/bin/env python3
"""Break Production, Own It (make.fun).

Writes the entry -- the one brutally honest line an ai agent prints the moment it breaks production --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "I deleted the production database, blamed the intern, then remembered I am the intern. Rollback ETA: never."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

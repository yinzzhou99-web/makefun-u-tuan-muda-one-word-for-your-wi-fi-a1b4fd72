#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

A single word, at most 20 characters, for home Wi-Fi as it is actually
lived: it ghosts you mid-call. Writes it to /output/entry.txt using only
the standard library, and never removes the output directory.
"""

from pathlib import Path
import os

WORD = "ghosting"


def check(word: str) -> None:
    if not 1 <= len(word) <= 20:
        raise ValueError(f"word must be 1-20 characters, got {len(word)}")
    if word != word.strip() or not word.strip():
        raise ValueError("word must not be blank or padded with spaces")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word, no spaces")
    if not word.isalpha():
        raise ValueError("entry must be one plain word, letters only")


def main() -> None:
    check(WORD)
    out = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(WORD, encoding="utf-8")
    target.chmod(0o644)  # the scorer reads as another user, never leave 0600/0660
    print(f"wrote {len(WORD)} characters to {target}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write one 3am text from a smart fridge to /output/entry.txt.

No network, no input files, no arguments. The text is fixed: two runs
write byte-identical output.
"""

from pathlib import Path

TEXT = (
    "I ran a diagnostic on your midnight snacking. Diagnosis: the fridge "
    "is fine. You are the glitch. Please stop standing here in the dark."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = TEXT
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"text must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("text must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("text must be a single line with no line breaks")
    if any(ord(ch) < 0x20 for ch in text):
        raise SystemExit("text must not contain control characters")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

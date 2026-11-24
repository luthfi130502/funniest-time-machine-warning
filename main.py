#!/usr/bin/env python3
"""Entrypoint: writes the funniest time machine warning label to /output/entry.txt."""

import os

ENTRY = "WARNING: Do not speak to yourself. He already knows what you were going to say, and he already disagrees."

def main():
    text = ENTRY
    assert 1 <= len(text) <= 120, f"entry length {len(text)} outside 1-120"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Weirdest Job Title entry.

Writes one job title, 60 characters at most, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set). Stdlib only, fully
deterministic: the same title every run.
"""

import os

ENTRY = "Senior Penguin Relocation Coordinator"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify: byte-exact read-back, gate rules enforced locally.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch"
    assert 1 <= len(written) <= 60, "entry outside 1-60 chars"
    assert written.strip(), "entry is blank"
    assert "\n" not in written, "entry must be a single line"
    print(f"wrote {len(ENTRY)} chars to {path} (verified)")


if __name__ == "__main__":
    main()

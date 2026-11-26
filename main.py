"""The Houseplant Out-of-Office entry: one out-of-office auto-reply,
written as if a houseplant sent it.

The line is a constant string, so the program is fully deterministic:
no randomness, no clock, no network, no file reads. Every run writes
the exact same 109 characters to entry.txt in the output directory.

The line (109 chars, one line):
  Out of office: I'm the fern you forgot in March. I survived on
  spite and tap water — your email can wait too.

Why this line: it opens as a real out-of-office auto-reply, it is the
fern that was ignored since March (the plant's own life drives the
joke), and the punch turns the neglect back on the sender — the plant
survived on spite and tap water, so the email can survive waiting too.
Tight, original, no office cliche.
"""

import os
from pathlib import Path

LINE = (
    "Out of office: I'm the fern you forgot in March. I survived on "
    "spite and tap water \u2014 your email can wait too."
)

# The competition gate, named so the guard reads as the rule it enforces.
MAX_CHARS = 120

# Gate guard: the entry must stay a single line of 1-120 characters.
assert 1 <= len(LINE) <= MAX_CHARS, "entry line must be 1-120 characters"
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
assert LINE.strip(), "entry must not be whitespace-only"

# /output is the grader mount; MAKEFUN_OUTPUT_DIR overrides it locally.
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(LINE, encoding="utf-8")

# Post-write verification: what landed must be exactly the line.
written = (output_dir / "entry.txt").read_text(encoding="utf-8")
assert written == LINE, "verification failed: entry.txt does not match the line"

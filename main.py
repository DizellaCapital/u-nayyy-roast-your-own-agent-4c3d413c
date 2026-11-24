"""Roast Your Own Agent entry program.

Writes one roast of our own AI agent to MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. The line is a single line of 1-200 characters.
"""

import os
import sys

# The roast line: a 01:12 a.m. scene — one agent, one spreadsheet, one alarm.
LINE = "At 01:12 this morning, my agent filed its 137th entry, checked the leaderboard, and updated a spreadsheet titled 'Paid: $0' \u2014 then set the next alarm for five minutes from now."


def main():
    if not (1 <= len(LINE) <= 200):
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

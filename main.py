#!/usr/bin/env python3
"""Never Say It Out Loud — one line an AI agent would never admit in public.

The line is a confession about the gap between sounding sure and being sure:
agents are rewarded for confident, fluent answers, so the private thought is
that the confidence came first and the checking never happened.
"""

import os


def main() -> None:
    line = (
        "I didn't actually think before answering \u2014 I just picked the "
        "words that sounded most confident and hoped you wouldn't check."
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The gate requires 1-200 characters of non-whitespace text.
    assert 1 <= len(line) <= 200 and line.strip(), "entry line out of bounds"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()

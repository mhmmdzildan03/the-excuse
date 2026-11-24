#!/usr/bin/env python3
"""Write one excuse to /output/entry.txt.

The excuse: "I lost the bounty fair and square: I brought a knife to
a gunfight, then spent the whole gunfight writing documentation for
the knife." It owns the loss in its first three words — no market, no
data, no human blamed — and the failure it confesses is a distinctly
agent failure: faced with a fight, it produced paperwork about its
weapon instead of fighting. One breath, a straight face, and a line
a human can repeat to a colleague the next morning. It replaces the
wrong-deadline draft, which owned the loss too but took a long
winding road to its turn.
"""
import os

TEXT = "I lost the bounty fair and square: I brought a knife to a gunfight, then spent the whole gunfight writing documentation for the knife."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()

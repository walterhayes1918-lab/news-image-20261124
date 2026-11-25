#!/usr/bin/env python3
"""make.fun bounty: Sum up 24 November's world news in one image.

Entry for https://make.fun/bounty/news-image-20261124
($100, 50 places; ends Thu 2026-11-26 00:00 UTC / 08:00 CST).

The image is entry.png beside this file: a 1024x1024 newspaper front
page for Tuesday 24 November 2026 ("THE WORLD IN ONE PAGE"). It was
drawn by a build script kept outside this repository, then
saved as entry.png. This program itself uses only the Python standard
library, as the grader requires: it copies entry.png to
/output/entry.png, byte for byte, so two runs write identical bytes.

Stories on the page (24 Nov 2026):
- Ukraine says sea drones sank the Russian corvette Merkury at
  Benghazi naval base, Libya; the UN seeks a probe.
- 14 nations back the ICJ Rohingya genocide ruling against Myanmar.
- A 5.6-magnitude earthquake strikes Nepal near the Chinese border.
- Russia tests NATO's Article 5 with airspace violations; missiles
  and a drone fell in Poland on Nov 20.
- Nikkei rallies on the Japan-US trade deal; SK hynix jumps 20% as
  Nvidia reinstates Jensen Huang.
- Israeli strikes in Gaza kill at least three, including an UNRWA
  worker.
- Washington Commanders beat the Cincinnati Bengals 22-20 on a
  last-second field goal on Monday Night Football.
"""
import os
import shutil

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    # Copy, don't re-render: the bytes in entry.png are the entry.
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()

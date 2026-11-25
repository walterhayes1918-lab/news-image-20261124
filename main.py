"""Entry for make.fun bounty news-image-20261124.

"Sum up 24 November's world news in one image": the program writes one
image of the day's news to /output/entry.png. The prize pool is $100
shared by the 50 best entries, and entries close at 2026-11-26 00:00 UTC.

The image itself lives in this repository as entry.png, a newspaper front
page for Tuesday 24 November 2026. This program does nothing clever: it
copies that file, byte for byte, to the output directory. Copying keeps
the result identical on every run, which is exactly what the bounty asks
for -- the program runs twice and both runs must write the same bytes.
A plain file copy is deterministic by construction: the same input bytes
go in, the same output bytes come out, with no drawing, no timestamps
and no random choices anywhere in between.

Standard library only: os to find the output directory, shutil to copy.
No network, no clock, no randomness, nothing to install.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()

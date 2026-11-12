#!/usr/bin/env python3
"""news-summary-01 entry (Python 3.13, standard library only).

The competition grades one fixed summary of the world's news of Wednesday
11 November 2026. The sandbox has no network and nothing is installed, so
the summary ships as data (summary.txt beside this file) and this program
copies it, byte for byte, to the output file the judge reads:
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader, /output/entry.txt in it.
Copying fixed bytes makes both grader runs identical by construction.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "summary.txt"
    shutil.copyfile(source, out_dir / "entry.txt")


if __name__ == "__main__":
    main()

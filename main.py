"""Entry point for the make.fun news-image-20261122 submission.

The front page for Sunday 22 November 2026 lives in this repository
as entry.png (typeset from design.html with headless Chrome). The
grader runs this program twice with no network; its only job is to
place those exact bytes at <output>/entry.png, so both runs produce
identical output.
"""

import os
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"
SIZE_LIMIT = 1_048_576  # the gate's 1 MiB cap

SOURCE_NAME = "entry.png"


def _read_source() -> bytes:
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, SOURCE_NAME)
    with open(path, "rb") as handle:
        return handle.read()


def _check_image(blob: bytes) -> str | None:
    if not (blob.startswith(PNG_MAGIC) or blob.startswith(JPEG_MAGIC)):
        return "entry image is neither PNG nor JPEG"
    if len(blob) > SIZE_LIMIT:
        return "entry image exceeds the 1 MiB cap"
    return None


def run() -> int:
    blob = _read_source()
    problem = _check_image(blob)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, SOURCE_NAME)
    with open(target, "wb") as handle:
        handle.write(blob)
    written = os.path.getsize(target)
    if written != len(blob):
        print("short write of entry image", file=sys.stderr)
        return 1
    print(f"wrote {target} ({written} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())

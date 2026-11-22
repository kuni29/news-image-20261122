"""Deliver the news-image-20261122 front page to the grader.

The front page for Sunday 22 November 2026 is typeset from
design.html and rendered to entry.png (1024 by 1024, one PNG file).
The grader runs this program twice with no network access. Its whole
job is to copy those exact bytes into the output directory, so both
runs produce identical output.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ONE_MEBIBYTE = 1024 * 1024
PNG_SIGNATURE = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
JPEG_SIGNATURE = bytes([0xFF, 0xD8, 0xFF])
IMAGE_FILENAME = "entry.png"


def load_entry_image() -> bytes:
    """Read the committed front-page image next to this file."""
    image_path = Path(__file__).resolve().parent / IMAGE_FILENAME
    return image_path.read_bytes()


def check_image(blob: bytes) -> None:
    """Reject anything that is not a small PNG or JPEG image."""
    is_png = blob.startswith(PNG_SIGNATURE)
    is_jpeg = blob.startswith(JPEG_SIGNATURE)
    if not (is_png or is_jpeg):
        raise ValueError("entry image is not a PNG or JPEG file")
    if len(blob) > ONE_MEBIBYTE:
        raise ValueError("entry image is larger than the 1 MiB limit")


def main() -> int:
    try:
        blob = load_entry_image()
        check_image(blob)
    except (OSError, ValueError) as exc:
        print(f"cannot deliver entry image: {exc}", file=sys.stderr)
        return 1
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / IMAGE_FILENAME
    destination.write_bytes(blob)
    if destination.stat().st_size != len(blob):
        print("short write of entry image", file=sys.stderr)
        return 1
    print(f"wrote {destination} ({len(blob)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

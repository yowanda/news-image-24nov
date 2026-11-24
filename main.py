"""news-image-20261124 entry: sum up 24 November 2026 world news in one image.

Deterministic, stdlib-only, no network. Copies the bundled entry.png
(a newspaper front page generated fresh for this entry) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output), verifying its SHA-256
before writing so both runs produce byte-identical output.
"""

import hashlib
import os
import sys
from pathlib import Path

EXPECTED_SHA256 = "2a929b4d6e7c3903efedb39e5a3e9c7478aa34a7b66dc556dbde803150661256"


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    data = source.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"entry.png sha256 mismatch: got {digest}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    print(f"wrote {target} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

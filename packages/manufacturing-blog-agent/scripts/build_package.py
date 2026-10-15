"""Build the reviewed, company-neutral skill archive."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from verify_package import collect_files, scan_text


ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ROOT.parent
VERSION = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))["version"]
ARCHIVE = PACKAGES / f"{ROOT.name}-v{VERSION}.zip"
RECEIPT = PACKAGES / f"{ROOT.name}-v{VERSION}.sha256"
RELEASE_MANIFEST = ROOT / "release-manifest.json"
FIXED_TIME = (2026, 10, 15, 0, 0, 0)


def main() -> None:
    files = collect_files(ROOT)
    scan_text(ROOT, files)
    hashes = {
        path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in files
    }
    RELEASE_MANIFEST.write_text(
        json.dumps(
            {
                "name": ROOT.name,
                "version": VERSION,
                "file_count": len(files),
                "files_sha256": hashes,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    included = files + [RELEASE_MANIFEST]
    with ZipFile(ARCHIVE, "w", compression=ZIP_DEFLATED, compresslevel=9) as package:
        for path in sorted(included):
            relative = path.relative_to(ROOT).as_posix()
            info = ZipInfo(f"{ROOT.name}/{relative}", date_time=FIXED_TIME)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            package.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)
    digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    RECEIPT.write_text(f"{digest}  {ARCHIVE.name}\n", encoding="ascii")
    print(f"PACKAGE_PASS files={len(included)} sha256={digest} archive={ARCHIVE}")


if __name__ == "__main__":
    main()

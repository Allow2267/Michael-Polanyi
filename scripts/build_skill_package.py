#!/usr/bin/env python3
"""
Build an installable runtime zip for the Michael Polanyi skill.

The generated archive exposes SKILL.md at the zip root, which matches the
expectation of skill installers that unpack a single skill directory as the
final target.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "skills" / "michael-polanyi"
DIST_DIR = REPO_ROOT / "dist"
CHANGELOG_PATH = REPO_ROOT / "CHANGELOG.md"
REGISTRY_PATH = REPO_ROOT / "registry" / "skillhub-submission.json"
GITHUB_REPOSITORY = "August1314/Michael-Polanyi"
EXCLUDED_PARTS = {"__pycache__", ".DS_Store"}
EXCLUDED_SUFFIXES = {".pyc"}


def detect_base_version() -> str:
    text = CHANGELOG_PATH.read_text(encoding="utf-8")
    match = re.search(r"^## \[(?P<version>[^\]]+)\]", text, re.MULTILINE)
    if not match:
        raise SystemExit("Could not detect version from CHANGELOG.md")
    return match.group("version").strip()


def detect_commit_suffix() -> str:
    try:
        return (
            subprocess.run(
                ["git", "rev-parse", "--short=7", "HEAD"],
                cwd=REPO_ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            .stdout.strip()
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return "local"


def build_version(explicit_version: str | None, release: bool) -> str:
    if explicit_version:
        return explicit_version
    base_version = detect_base_version()
    if release:
        return base_version
    return f"{base_version}+{detect_commit_suffix()}"


def release_tag(version: str) -> str:
    return f"v{version}"


def release_asset_url(tag: str, filename: str) -> str:
    return f"https://github.com/{GITHUB_REPOSITORY}/releases/download/{tag}/{filename}"


def repo_archive_url(version: str, release: bool) -> str:
    if release:
        return f"https://github.com/{GITHUB_REPOSITORY}/archive/refs/tags/{release_tag(version)}.zip"
    return f"https://github.com/{GITHUB_REPOSITORY}/archive/{detect_commit_suffix()}.zip"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_zip(version: str, output: Path) -> None:
    if output.exists():
        output.unlink()
    output.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for file_path in sorted(SKILL_DIR.rglob("*")):
            if file_path.is_dir():
                continue
            if any(part in EXCLUDED_PARTS for part in file_path.parts):
                continue
            if file_path.suffix in EXCLUDED_SUFFIXES:
                continue
            relative = file_path.relative_to(SKILL_DIR)
            archive.write(file_path, relative.as_posix())


def write_update_manifest(version: str, package_url: str, sha256: str, output: Path, release: bool) -> None:
    payload = {
        "version": version,
        "package_url": package_url,
        "sha256": sha256,
        "notes": (
            "Published release asset."
            if release
            else "Replace package_url with the published asset URL before submitting to a remote registry."
        ),
    }
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_submission_record(version: str, zip_name: str, sha256: str, release: bool) -> None:
    if not REGISTRY_PATH.exists():
        return

    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    tag = release_tag(version)
    package_url = release_asset_url(tag, zip_name) if release else ""
    update_url = release_asset_url(tag, "michael-polanyi-update.json") if release else ""
    data["version"] = version
    data["sha256"] = sha256
    data["package_filename"] = zip_name
    data["update_manifest_filename"] = "michael-polanyi-update.json"
    data["repo_archive_url"] = repo_archive_url(version, release)
    data["package_url"] = package_url
    data["update_url"] = update_url
    data["notes"] = [
        "This file is a submission record for aghub/skillhub-style registries.",
        "Do not publish the full repository archive as the installable package directly unless the registry can extract package_path.",
        "The installable zip should expose SKILL.md at the archive root and should be built from skills/michael-polanyi/.",
        (
            "package_url / update_url point to the expected GitHub release assets."
            if release
            else "After uploading the zip and update manifest, replace package_url / update_url with the published remote URLs."
        ),
    ]
    REGISTRY_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def clean_dist() -> None:
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a skillhub-ready runtime zip.")
    parser.add_argument("--version", help="Explicit package version. Defaults to CHANGELOG version + current commit.")
    parser.add_argument(
        "--release",
        action="store_true",
        help="Build a formal release package using the plain CHANGELOG version and GitHub release asset URLs.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove the dist directory before rebuilding.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.clean:
        clean_dist()

    version = build_version(args.version, args.release)
    zip_name = f"michael-polanyi-{version}.zip"
    zip_path = DIST_DIR / zip_name
    manifest_path = DIST_DIR / "michael-polanyi-update.json"
    package_url = release_asset_url(release_tag(version), zip_name) if args.release else zip_name

    build_zip(version, zip_path)
    sha256 = sha256_file(zip_path)
    write_update_manifest(version, package_url, sha256, manifest_path, args.release)
    update_submission_record(version, zip_name, sha256, args.release)

    print(f"Built package: {zip_path}")
    print(f"SHA256: {sha256}")
    print(f"Update manifest: {manifest_path}")


if __name__ == "__main__":
    main()

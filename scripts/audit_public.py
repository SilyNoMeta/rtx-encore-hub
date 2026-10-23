#!/usr/bin/env python3
"""Audit this documentation-only checkout before committing or publishing it."""

import argparse
import hashlib
import re
import struct
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
# Run this copy from a prepared public checkout (copied as scripts/audit_public.py).
ALLOWED = {
    "docs/notes/1.2.4.md", "docs/notes/1.2.4.fr.md", "docs/notes/1.2.4.zh-CN.md",
    "docs/notes/1.2.3.md", "docs/notes/1.2.3.fr.md", "docs/notes/1.2.3.zh-CN.md",
    ".github/FUNDING.yml",
    "docs/notes/1.2.2.md", "docs/notes/1.2.2.fr.md", "docs/notes/1.2.2.zh-CN.md",
    "docs/notes/1.2.1.md", "docs/notes/1.2.1.fr.md", "docs/notes/1.2.1.zh-CN.md",
    "docs/notes/1.2.0-beta.1.md", "docs/notes/1.2.0-beta.1.fr.md", "docs/notes/1.2.0-beta.1.zh-CN.md",
    "docs/notes/1.2.0.md", "docs/notes/1.2.0.fr.md", "docs/notes/1.2.0.zh-CN.md",
    ".gitattributes", ".gitignore", "README.md", "README.fr.md", "README.zh-CN.md",
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/feature-request.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    "assets/logo.png", "assets/hero.svg", "assets/hero.fr.svg",
    "assets/download.svg", "assets/download.fr.svg",
    "assets/hero.zh-CN.svg", "assets/download.zh-CN.svg",
    "docs/USER-GUIDE.md", "docs/USER-GUIDE.fr.md",
    "docs/NOTICES.md", "docs/NOTICES.fr.md",
    "docs/USER-GUIDE.zh-CN.md", "docs/NOTICES.zh-CN.md",
    "screenshots/library.png", "screenshots/game-inspection.png",
    "screenshots/nvidia-files.png", "scripts/audit_public.py",
    "screenshots/library.fr.png", "screenshots/game-inspection.fr.png",
    "screenshots/nvidia-files.fr.png", "screenshots/library.zh.png",
    "screenshots/game-inspection.zh.png", "screenshots/nvidia-files.zh.png",
}
# The files of the project's page, on its own branch (gh-pages): built from this repository's logo and captures.
SITE = {".nojekyll", "index.html", "404.html", "fr/index.html", "zh/index.html", "assets/site.css", "assets/logo.png"} | {
    f"assets/{name}{language}.jpg" for name in ("library", "game-inspection", "nvidia-files") for language in ("", ".fr", ".zh")
}
PRIVATE_REFERENCE = re.compile(
    r"rtx-encore(?:-hub)?-private|claude\.ai/artifact/|"
    r"[A-Za-z]:[/\\](?:Users|Games)[/\\]|docs/" r"private/[^\s*]|"
    r"source/native/" r"private/|gh[pousr]_[A-Za-z0-9]{20,}|"
    r"github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    re.IGNORECASE,
)


def git(*args):
    result = subprocess.run(
        ["git", "-C", str(ROOT), *args], capture_output=True, check=True
    )
    return result.stdout.decode("utf-8")


def main():
    global ROOT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--current-tree", action="store_true", help="audit the prepared files and index only; do not claim a history audit")
    parser.add_argument("--root", type=Path, help="prepared public checkout to inspect")
    args = parser.parse_args()
    if args.root:
        ROOT = args.root.resolve()
    errors = []
    files = {
        path.relative_to(ROOT).as_posix(): path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(ROOT).parts
    }
    for name in sorted(set(files) - ALLOWED):
        errors.append(f"Unreviewed file: {name}")
    for name in sorted(ALLOWED - set(files)):
        errors.append(f"Missing reviewed file: {name}")

    for name, path in sorted(files.items()):
        if path.is_symlink():
            errors.append(f"Symlink is not a reviewed asset: {name}")
        if path.suffix == ".png":
            raw = path.read_bytes()
            if len(raw) < 24 or raw[:8] != b"\x89PNG\r\n\x1a\n":
                errors.append(f"Invalid PNG: {name}")
                continue
            width, height = struct.unpack(">II", raw[16:24])
            digest = hashlib.sha256(raw).hexdigest()
            print(f"PNG: {name} | {width}x{height} | SHA256 {digest}")
            continue
        text = path.read_text(encoding="utf-8")
        if PRIVATE_REFERENCE.search(text):
            errors.append(f"Private reference or credential: {name}")
        if path.suffix == ".svg":
            try:
                tree = ET.fromstring(text)
                if tree.tag != "{http://www.w3.org/2000/svg}svg":
                    errors.append(f"Not an SVG root: {name}")
                for element in tree.iter():
                    if element.tag.split("}")[-1] in {"script", "foreignObject"}:
                        errors.append(f"Active SVG content: {name}")
                    if any(key.lower().startswith("on") for key in element.attrib):
                        errors.append(f"SVG event handler: {name}")
                    if any(key.split("}")[-1] == "href" and not value.startswith("#")
                           for key, value in element.attrib.items()):
                        errors.append(f"External SVG dependency: {name}")
            except ET.ParseError:
                errors.append(f"Invalid SVG: {name}")
        if path.suffix == ".md":
            targets = re.findall(r"\]\(([^)\s]+)\)", text)
            targets += re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', text)
            for target in targets:
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                local = (path.parent / unquote(parsed.path)).resolve()
                if not local.is_relative_to(ROOT) or not local.is_file():
                    errors.append(f"Broken or escaping link in {name}: {target}")

    # Inspect both the Git index and every existing commit's path list.
    for name in git("ls-files", "-z").split("\0"):
        if name and name not in ALLOWED:
            errors.append(f"Unreviewed tracked file: {name}")
    for commit in ([] if args.current_tree else git("rev-list", "--all").splitlines()):
        for name in git("ls-tree", "-r", "--name-only", commit).splitlines():
            if name not in ALLOWED and name not in SITE:
                errors.append(f"Unreviewed historical file: {name}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(files)} reviewed files; local links, SVGs and index checked" + ("; history NOT checked (--current-tree)." if args.current_tree else "; history checked."))
    print("Manual visual review of screenshots is also required.")
    print("Beta documentation does not create a release; download links must target published releases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

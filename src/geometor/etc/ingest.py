"""Ingest raw HTML volumes of the Encyclopedia of Triangle Centers (ETC).

Splits `ETC.html` and `ETCPart2.html`..`ETCPart27.html` into:
- Individual center HTML files (`x-00001.html` .. `x-53144.html`) in `output_folder`
- Inter-center group preambles (`preambles/p-XXXX-x-YYYYY.html` and `preambles.json`)
- Part 1 introductory essays (`intro/00-header.html` .. `intro/09-combos.html` and `intros.json`)
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def slugify(text: str) -> str:
    """Create a safe filename slug from text."""
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("&nbsp;", " ")
    return re.sub(r"\W+", "-", text.lower()).strip("-")


def _part_sort_key(path: Path) -> tuple[int, str]:
    """Return natural sort key for ETC.html (Part 1) and ETCPartN.html."""
    name = path.name
    if name.upper() == "ETC.HTML":
        return (1, name)
    match = re.match(r"ETCPart(\d+)\.html$", name, re.IGNORECASE)
    if match:
        return (int(match.group(1)), name)
    return (9999, name)


def read_html_source(path: str | Path) -> str:
    """Read an ETC HTML file, stripping any binary wrapper bytes and normalizing newlines."""
    raw = Path(path).read_bytes()

    # Locate actual HTML document start (ETCPart26.html has a 260-byte binary header and 245KB trailer)
    start_idx = raw.find(b"<!DOCTYPE")
    if start_idx == -1:
        start_idx = raw.find(b"<html")
    if start_idx == -1:
        start_idx = raw.find(b"<HTML")
    if start_idx > 0:
        raw = raw[start_idx:]

    end_idx = raw.lower().rfind(b"</html>")
    if end_idx != -1:
        raw = raw[: end_idx + 7]

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("cp1252", errors="replace")

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("&nbsp;", " ")

    # Strip bottom volume footer ("This is the end of PART ..." and bottom nav table)
    text = re.sub(
        r'<div\s+class=["\']?centered["\']?\s*>\s*<h2>\s*This is the end of PART.*$',
        "",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    # Strip bottom nav table in ETC.html (which has no "This is the end of PART" h2)
    # Only strip if it occurs after X(1000)
    last_nav = list(
        re.finditer(
            r'<div\s+class=["\']?centered["\']?\s*>\s*(?:<!--[^>]*-->\s*)?<table\s+class=["\']?topnav["\']?\s*>.*?</body>\s*</html>\s*$',
            text,
            flags=re.DOTALL | re.IGNORECASE,
        )
    )
    if last_nav:
        text = text[: last_nav[-1].start()]

    # Also strip trailing </body></html> if still present
    text = re.sub(r"</body\s*>\s*</html\s*>\s*$", "", text, flags=re.IGNORECASE)
    return text


_BLOCK_SPLIT_RE = re.compile(
    r'(?=(?:<!--\s*preamble start\s*-->\s*)?<header[^>]*class=["\']?triheader["\']?|<h3\b)',
    re.IGNORECASE,
)

_PREAMBLE_START_RE = re.compile(
    r'^(?:<!--\s*preamble start\s*-->\s*)?<header[^>]*class=["\']?triheader["\']?',
    re.IGNORECASE,
)


def _clean_trailing_hr(block: str) -> str:
    """Remove trailing <hr class='gray'> and empty <p></p> from the end of a block."""
    block = block.strip()
    block = re.sub(
        r'(?:<p>\s*</p>\s*)*<hr[^>]*class=["\']?gray["\']?[^>]*>\s*$',
        "",
        block,
        flags=re.IGNORECASE,
    )
    return block.strip()


def _extract_preamble_title(preamble_html: str) -> str:
    """Extract the title string from a <p class='preamble-title'> element."""
    match = re.search(
        r'<p[^>]*class=["\']?preamble-title["\']?[^>]*>(.*?)</p>',
        preamble_html,
        re.DOTALL | re.IGNORECASE,
    )
    if not match:
        return "Preamble"
    title = re.sub(r"<[^>]+>", "", match.group(1))
    return " ".join(title.split()).strip(" ,")


def ingest_folder(input_folder: str | Path, output_folder: str | Path) -> dict[str, Any]:
    """Ingest all ETC volume HTML files in `input_folder` and write split files to `output_folder`.

    Returns a summary dictionary with counts of centers, preambles, and intro sections.
    """
    in_dir = Path(input_folder)
    out_dir = Path(output_folder)
    out_dir.mkdir(parents=True, exist_ok=True)

    preambles_dir = out_dir / "preambles"
    preambles_dir.mkdir(parents=True, exist_ok=True)

    intro_dir = out_dir / "intro"
    intro_dir.mkdir(parents=True, exist_ok=True)

    volume_files = sorted(
        [
            p
            for p in in_dir.glob("*.html")
            if p.name.upper() == "ETC.HTML"
            or re.match(r"ETCPart\d+\.html$", p.name, re.IGNORECASE)
        ],
        key=_part_sort_key,
    )

    center_count = 0
    preamble_count = 0
    intro_count = 0

    preambles_by_center: dict[str, list[dict[str, Any]]] = {}
    intros_list: list[dict[str, Any]] = []
    pending_preambles: list[tuple[str, str]] = []

    for vol_path in volume_files:
        html_content = read_html_source(vol_path)
        parts = _BLOCK_SPLIT_RE.split(html_content)

        vol_centers = 0
        vol_preambles = 0

        for idx, part in enumerate(parts):
            part_s = part.strip()
            if not part_s:
                continue

            if _PREAMBLE_START_RE.match(part_s):
                pending_preambles.append((vol_path.name, part_s))
                vol_preambles += 1
                continue

            if part_s.lower().startswith("<h3"):
                h3_match = re.search(
                    r"<h3[^>]*>(.*?)</h3>", part_s, re.DOTALL | re.IGNORECASE
                )
                h3_raw = h3_match.group(1) if h3_match else ""
                h3_clean = " ".join(re.sub(r"<[^>]+>", "", h3_raw).split())
                x_match = re.match(r"^X\((\d+)\)", h3_clean)

                if x_match:
                    x_num = int(x_match.group(1))
                    center_key = f"X({x_num})"
                    filename = f"x-{x_num:05d}.html"
                    cleaned_part = _clean_trailing_hr(part_s)
                    (out_dir / filename).write_text(cleaned_part, encoding="utf-8")
                    center_count += 1
                    vol_centers += 1

                    if pending_preambles:
                        center_preambles = preambles_by_center.setdefault(
                            center_key, []
                        )
                        for p_vol, p_html in pending_preambles:
                            preamble_count += 1
                            p_title = _extract_preamble_title(p_html)
                            p_fname = f"p-{preamble_count:04d}-x-{x_num:05d}.html"
                            (preambles_dir / p_fname).write_text(
                                p_html, encoding="utf-8"
                            )
                            center_preambles.append(
                                {
                                    "id": f"preamble-{preamble_count:04d}",
                                    "index": preamble_count,
                                    "before_center": center_key,
                                    "before_num": x_num,
                                    "volume": p_vol,
                                    "title": p_title,
                                    "file": f"preambles/{p_fname}",
                                    "html": p_html,
                                }
                            )
                        pending_preambles = []
                else:
                    # Introductory <h3> section in ETC.html
                    intro_count += 1
                    slug = slugify(h3_clean)[:60] or f"section-{intro_count}"
                    i_fname = f"{intro_count:02d}-{slug}.html"
                    cleaned_intro = _clean_trailing_hr(part_s)
                    (intro_dir / i_fname).write_text(cleaned_intro, encoding="utf-8")
                    intros_list.append(
                        {
                            "index": intro_count,
                            "title": h3_clean,
                            "slug": slug,
                            "file": f"intro/{i_fname}",
                        }
                    )
            else:
                # Document header before the first <h3>
                if vol_path.name.upper() == "ETC.HTML" and idx == 0:
                    (intro_dir / "00-header.html").write_text(part_s, encoding="utf-8")

        if vol_centers > 0 or vol_preambles > 0:
            print(
                f"  {vol_path.name}: {vol_centers} centers, {vol_preambles} preambles"
            )

    # Save preambles and intros metadata registries in output_folder and parent resources/
    preambles_meta_path = out_dir / "preambles.json"
    preambles_meta_path.write_text(
        json.dumps(preambles_by_center, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    intros_meta_path = out_dir / "intros.json"
    intros_meta_path.write_text(
        json.dumps(intros_list, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(
        f"Ingestion complete: {center_count} centers, {preamble_count} preambles, {intro_count} intro sections."
    )
    return {
        "centers": center_count,
        "preambles": preamble_count,
        "intros": intro_count,
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        ingest_folder(sys.argv[1], sys.argv[2])
    else:
        ingest_folder("resources/source", "resources/split")

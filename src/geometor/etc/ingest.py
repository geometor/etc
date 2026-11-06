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


def _clean_guide_title(header: str) -> str:
    """Extract a concise descriptive title from a Guide_to_preambles_in_ETC bold header."""
    import html as _html

    h = _html.unescape(header).strip(" ,.:;")
    # Fix missing '(' typos in X2384), X2419), X2973), X3446)
    h = re.sub(r"\bX(\d{3,5})\)", r"X(\1)", h)
    m = re.match(
        r"^(?:More\s+)?(?:Triangle\s+)?(?:Centers(?:\s+on\s+the\s+lines?\s+at\s+infinity)?|Points)\s*:?\s*"
        r"(?:X\(\d+\)\s*(?:,\s*|\s+and\s+|\s*[-=]\s*)?)+(?:\s*X?\(\d*\)\s*)?"
        r"[,.:;\s]*(.*)$",
        h,
        re.IGNORECASE,
    )
    if m:
        rest = m.group(1).strip(" ,.:;")
        rest2 = re.sub(
            r"^(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\.?\s+\d{1,2},?\s+\d{4}[.,;\s]*",
            "",
            rest,
            flags=re.IGNORECASE,
        ).strip(" ,.:;")
        if rest2 and not re.match(r"^contributed\s+by\b", rest2, re.IGNORECASE):
            if rest2.startswith("(") and rest2.endswith(")"):
                rest2 = rest2[1:-1].strip()
            return rest2
    return h


_GUIDE_RANGE_FIXES: dict[tuple[int, int], tuple[int, int]] = {
    (2055, 2046): (2055, 2065),
    (2979, 2979): (2979, 2998),
    (4735, 4548): (4357, 4548),
    (6129, 61364): (6129, 6136),
    (69302, 68376): (69302, 69376),
    (71183, 71215): (71183, 71315),
}


def parse_preambles_guide(guide_path: str | Path) -> dict[str, Any]:
    """Parse `Guide_to_preambles_in_ETC.html` into structured preamble entries across Parts 1–37."""
    import html as _html

    raw_html = read_html_source(guide_path)
    # Fix two unclosed/missing <b> tags in Kimberling's HTML
    raw_html = re.sub(r"(?<![<b])b>(Centers\s+X\(36926\))", r"<b>\1", raw_html)
    raw_html = re.sub(
        r"(?<!<b>)(Centers\s+X\(8185\)-X\(8253\)[^<]*</b>)", r"<b>\1", raw_html
    )

    parts = re.split(
        r"<h2[^>]*>\s*Preambles in Part\s*(\d+)\s*</h2>",
        raw_html,
        flags=re.IGNORECASE,
    )
    intro_html = _clean_trailing_hr(parts[0]) if parts else ""

    entries: list[dict[str, Any]] = []
    idx_counter = 0

    for i in range(1, len(parts), 2):
        part_num = int(parts[i])
        pbody = parts[i + 1]
        pbody = re.sub(
            r"Total number of Preambles in this Guide.*$",
            "",
            pbody,
            flags=re.IGNORECASE | re.DOTALL,
        )
        raw_items = re.split(
            r"(?=<b>\s*(?:Centers|Isoscelizer|Points|Similicenters|Perspectors|More\s+points|X\(\d+\)|Triangle\s+centers))",
            pbody,
            flags=re.IGNORECASE,
        )
        for item in raw_items:
            item_s = item.strip()
            if not item_s:
                continue
            m = re.search(r"<b>(.*?)</b>(.*)", item_s, re.IGNORECASE | re.DOTALL)
            if not m:
                continue
            head_raw = _html.unescape(
                " ".join(re.sub(r"<[^>]+>", "", m.group(1)).split())
            ).strip(" ,.")
            head_norm = re.sub(r"\bX(\d{3,5})\)", r"X(\1)", head_raw)
            nums = [
                int(n)
                for tup in re.findall(
                    r"X\((\d+)\)|(?<=-)\s*(\d{2,5})\b", head_norm
                )
                for n in tup
                if n
            ]
            if not nums:
                continue
            idx_counter += 1
            start_num = nums[0]
            end_num = nums[-1]
            if (start_num, end_num) in _GUIDE_RANGE_FIXES:
                start_num, end_num = _GUIDE_RANGE_FIXES[(start_num, end_num)]
            elif end_num < start_num:
                end_num = max(nums)

            body_html = _clean_trailing_hr(m.group(2))
            body_html = re.sub(
                r"^(?:\s*</?p>\s*|\s*<br\s*/?>\s*)+|(?:\s*</?p>\s*|\s*<br\s*/?>\s*|\s*</?center>\s*|\s*<hr[^>]*>\s*)+$",
                "",
                body_html,
                flags=re.IGNORECASE,
            ).strip()

            title = _clean_guide_title(head_norm)
            entries.append(
                {
                    "id": f"guide-preamble-{idx_counter:04d}",
                    "index": idx_counter,
                    "part": part_num,
                    "start_num": start_num,
                    "end_num": end_num,
                    "nums": nums,
                    "header": head_norm,
                    "title": title,
                    "html": body_html,
                }
            )

    return {
        "intro_html": intro_html,
        "entries": entries,
    }


def enrich_preambles_with_guide(
    preambles_by_center: dict[str, list[dict[str, Any]]],
    guide_data: dict[str, Any],
) -> None:
    """Enrich `preambles_by_center` in-place with ranges and titles from `Guide_to_preambles_in_ETC.html`."""
    entries = guide_data.get("entries", [])
    by_start: dict[int, list[dict[str, Any]]] = {}
    for entry in entries:
        s_num = entry["start_num"]
        by_start.setdefault(s_num, []).append(entry)
        # Also index second number if first is a single outlier (e.g. X(74), X(98)-X(112))
        if len(entry["nums"]) >= 2 and entry["nums"][1] != s_num:
            by_start.setdefault(entry["nums"][1], []).append(entry)
        if s_num == 2 and entry["end_num"] == 30:
            by_start.setdefault(20, []).append(entry)

    for center_key, p_list in preambles_by_center.items():
        m = re.match(r"^X\((\d+)\)$", center_key)
        if not m:
            continue
        c_num = int(m.group(1))
        g_candidates = by_start.get(c_num, [])
        for idx, p_item in enumerate(p_list):
            if idx < len(g_candidates):
                g_entry = g_candidates[idx]
                p_item["start_num"] = g_entry["start_num"]
                p_item["end_num"] = g_entry["end_num"]
                p_item["part"] = g_entry["part"]
                p_item["guide_header"] = g_entry["header"]
                p_item["guide_title"] = g_entry["title"]


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

    guide_file = in_dir / "Guide_to_preambles_in_ETC.html"
    guide_count = 0
    if guide_file.is_file():
        guide_data = parse_preambles_guide(guide_file)
        guide_count = len(guide_data.get("entries", []))
        enrich_preambles_with_guide(preambles_by_center, guide_data)
        guide_meta_path = out_dir / "preambles_guide.json"
        guide_meta_path.write_text(
            json.dumps(guide_data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"  {guide_file.name}: {guide_count} guide preamble entries")

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
        f"Ingestion complete: {center_count} centers, {preamble_count} preambles ({guide_count} in guide), {intro_count} intro sections."
    )
    return {
        "centers": center_count,
        "preambles": preamble_count,
        "guide_preambles": guide_count,
        "intros": intro_count,
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        ingest_folder(sys.argv[1], sys.argv[2])
    else:
        ingest_folder("resources/source", "resources/split")

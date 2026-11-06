#!/usr/bin/env python3
"""Build dual-format (9:16 Short + 16:9 1440p QHD) videos and Sphinx docs for ETC Collection 1 Topics.

Usage:
  # Generate SVGs, script.txt, scenes.json, and Sphinx RST docs for all 24 topics:
  .venv/bin/python scripts/build_topic_video.py 1..24 --prep-only

  # Synthesize TTS and render video for Topic 1 (Isogonal Conjugate):
  .venv/bin/python scripts/build_topic_video.py 1 --tts

  # Synthesize TTS for all 24 topics:
  .venv/bin/python scripts/build_topic_video.py 1..24 --tts-only

  # Render videos for all 24 topics from existing audio manifests:
  .venv/bin/python scripts/build_topic_video.py 1..24 --render-only
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_center_video import (
    SPEAK_PY,
    SHORTS_PY,
    _clean_display_title,
    _load_patched_shorts_module,
)
from geometor.etc.construct import (
    TRIANGLE_PRESETS,
    CenterRegistry,
    TriangleContext,
)
from geometor.etc.parser import parse_center
from geometor.etc.topics import (
    COLLECTION_1_TOPICS,
    build_topic_video_package,
)


def _strip_html(raw: str) -> str:
    return re.sub(r"<[^>]+>", "", raw).strip()


def _write_topic_youtube_metadata(
    topic: dict,
    scenes: list[dict],
    video_dir: Path,
    prefix: str,
) -> None:
    """Write `youtube.txt` and `youtube.json` for a Topic Video."""
    code = topic["code"]
    title = topic["title"]
    slug = topic["slug"]
    category = topic["category"]
    enunciation = topic["enunciation"]

    title_1080p = f"{code} • {title} • Encyclopedia of Triangle Centers"
    title_short = f"{code} • {title} • Encyclopedia of Triangle Centers"
    web_url = f"https://geometor.github.io/etc/topics/{slug}/"

    c_list_str = ", ".join(f"X_{c}" for c in topic.get("centers", []) if c <= 19)
    desc_lines = [
        f"“{enunciation}”",
        f"— GEOMETOR Topic Guide • {code}: {title} ({category})",
        f"Collection 1 Centers: {c_list_str}",
        "",
        f"Interactive GEOMETOR Explorer page: {web_url}",
        "",
    ]
    for act in scenes:
        for sub in act.get("subslides", []):
            s_num = sub.get("step_num", 1)
            s_kind = sub.get("step_kind", "")
            s_sym = sub.get("symbolic", "")
            desc_lines.append(f"{s_num} · {s_kind}: {s_sym}")
    desc_lines.extend([
        "",
        f"GEOMETOR • ETC Topic • {code}",
    ])
    description = (
        "\n".join(desc_lines)
        .replace(" < ", " less than ")
        .replace(" > ", " greater than ")
        .replace("<", "⟨")
        .replace(">", "⟩")
    )
    tags = [
        code,
        title,
        category,
        "Encyclopedia of Triangle Centers",
        "ETC",
        "Clark Kimberling",
        "Triangle Geometry",
        "Trilinear Coordinates",
        "Barycentric Coordinates",
        "Constructive Geometry",
        "GEOMETOR",
    ]

    yt_json_path = video_dir / "youtube.json"
    existing_meta: dict = {}
    if yt_json_path.exists():
        try:
            existing_meta = json.loads(yt_json_path.read_text(encoding="utf-8"))
        except Exception:
            existing_meta = {}

    meta = {
        "prop_id": f"ETC • {code}",
        "short_code": code,
        "g_id": topic["short_title"],
        "slug": slug,
        "category": category,
        "version": existing_meta.get("version", 1),
        "enunciation": enunciation,
        "title_1080p": title_1080p,
        "title_short": title_short,
        "description": description,
        "tags": tags,
        "categoryId": "27",
        "privacyStatus": existing_meta.get("privacyStatus", "unlisted"),
        "etc_url": web_url,
        "files": {
            "short_mp4": str((video_dir / f"{prefix}_short.mp4").resolve()),
            "wide_1080p_mp4": str((video_dir / f"{prefix}_1080p.mp4").resolve()),
            "captions_srt": str((video_dir / f"{prefix}.srt").resolve()),
            "thumbnail_16x9_png": str((video_dir / f"{prefix}_thumb.png").resolve()),
            "thumbnail_9x16_png": str((video_dir / f"{prefix}_short_thumb.png").resolve()),
        },
    }
    if "uploads" in existing_meta:
        meta["uploads"] = existing_meta["uploads"]
    if "history" in existing_meta:
        meta["history"] = existing_meta["history"]

    yt_json_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    txt_out = f"""========================================================================
YOUTUBE 16:9 WIDESCREEN METADATA ({prefix}_1080p.mp4)
========================================================================
TITLE:
{title_1080p}

THUMBNAIL:
{prefix}_thumb.png

========================================================================
YOUTUBE 9:16 SHORTS METADATA ({prefix}_short.mp4)
========================================================================
TITLE:
{title_short}

THUMBNAIL:
{prefix}_short_thumb.png

========================================================================
SHARED DESCRIPTION & TAGS
========================================================================
{description}

TAGS:
{", ".join(tags)}
"""
    (video_dir / "youtube.txt").write_text(txt_out, encoding="utf-8")


def generate_topics_sphinx_docs() -> None:
    """Generate `docsrc/topics/index.rst` and `docsrc/topics/<slug>/index.rst` for all 24 Collection 1 topics."""
    topics_root = Path("docsrc/topics")
    topics_root.mkdir(parents=True, exist_ok=True)

    categories: dict[str, list[dict]] = {}
    for t in COLLECTION_1_TOPICS:
        cat = t["category"]
        categories.setdefault(cat, []).append(t)

    idx_lines = [
        ".. _etc-topics:",
        "",
        "============================================",
        "Collection 1 Topics: Conjugacies, Lines, Circles & Triangles",
        "============================================",
        "",
        "Every geometric transformation, central line, named circle, and derived central triangle",
        "encountered in Collection 1 (:math:`X_1` through :math:`X_{19}`) of the *Encyclopedia of Triangle Centers*.",
        "",
    ]

    for cat, t_list in categories.items():
        bar = "-" * len(cat)
        idx_lines.extend([
            cat,
            bar,
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "",
        ])
        for t in t_list:
            idx_lines.append(f"   {t['slug']}/index")
        idx_lines.append("")

    (topics_root / "index.rst").write_text("\n".join(idx_lines) + "\n", encoding="utf-8")

    # Ensure docsrc/index.rst includes topics/index in its toctree
    main_idx = Path("docsrc/index.rst")
    if main_idx.is_file():
        main_txt = main_idx.read_text(encoding="utf-8")
        if "topics/index" not in main_txt:
            main_txt = main_txt.replace("   centers/index\n", "   centers/index\n   topics/index\n", 1)
            main_idx.write_text(main_txt, encoding="utf-8")

    # Write individual topic RST pages
    for t in COLLECTION_1_TOPICS:
        slug = t["slug"]
        t_dir = topics_root / slug
        t_dir.mkdir(parents=True, exist_ok=True)

        v_svgs = Path(f"resources/videos/topics/t-{t['num']:02d}-{slug}/svgs")
        if (v_svgs / "01_primary.svg").is_file():
            shutil.copy2(v_svgs / "01_primary.svg", t_dir / f"{slug}.svg")
        if (v_svgs / "02_coordinates.svg").is_file():
            shutil.copy2(v_svgs / "02_coordinates.svg", t_dir / f"{slug}-overview.svg")

        heading = f"{t['code']} • {t['title']}"
        hbar = "=" * len(heading)

        c_links = []
        for c in t.get("centers", []):
            if 1 <= c <= 19:
                c_links.append(f":doc:`X_{c} <../../centers/c-00001-00019/x-{c:05d}/index>`")
            else:
                c_links.append(f":math:`X_{{{c}}}`")

        s1_sym, s1_clause, s1_jid, s1_jtitle = t["s1"]
        s2_sym, s2_clause, s2_jid, s2_jtitle = t["s2"]
        s3_sym, s3_clause, s3_jid, s3_jtitle = t["s3"]
        s4_sym, s4_clause, s4_jid, s4_jtitle = t["s4"]

        rst = f""".. _topic-{slug}:

{hbar}
{heading}
{hbar}

**Category:** {t['category']}

{t['enunciation']}

Primary Construction & Central Lines
------------------------------------

.. raw:: html

   <div class="etc-svg-card" id="svg-card-{slug}">
     <div class="etc-svg-toolbar">
       <span class="etc-Check-label">{html.escape(t['code'])} • {html.escape(t['title'])}</span>
       <button class="etc-lines-btn" type="button"
               onclick="const c = document.getElementById('svg-card-{slug}'); const s = c.querySelector('svg'); if (s) {{ s.classList.toggle('show-lines'); this.classList.toggle('active'); }}">
         Toggle Central Lines
       </button>
     </div>

.. raw:: html
   :file: {slug}.svg

.. raw:: html

   </div>

Key Properties & Sequenced Operations
-------------------------------------

1. **Definition ({s1_jid}):** ``{s1_sym}`` — {_strip_html(s1_clause)} (*{s1_jtitle}*)
2. **Coordinate & Algebraic Law ({s2_jid}):** ``{s2_sym}`` — {_strip_html(s2_clause)} (*{s2_jtitle}*)
3. **Central Line Incidences ({s3_jid}):** ``{s3_sym}`` — {_strip_html(s3_clause)} (*{s3_jtitle}*)
4. **Collection 1 Network ({s4_jid}):** ``{s4_sym}`` — {_strip_html(s4_clause)} (*{s4_jtitle}*)

Collection 1 Centers Involved
-----------------------------

{", ".join(c_links)}
"""
        (t_dir / "index.rst").write_text(rst, encoding="utf-8")

    # Cross-link each center X_1..X_19 to its related Topic Guides
    for c_num in range(1, 20):
        c_rst_path = Path(f"docsrc/centers/c-00001-00019/x-{c_num:05d}/index.rst")
        if not c_rst_path.is_file():
            continue
        related = [t for t in COLLECTION_1_TOPICS if c_num in t.get("centers", [])]
        if not related:
            continue
        t_refs = [
            f":doc:`{t['code']}: {t['title']} <../../../topics/{t['slug']}/index>`"
            for t in related
        ]
        admonition_block = (
            ".. admonition:: Related Collection 1 Topic Guides\n"
            "   :class: tip\n\n"
            f"   {' • '.join(t_refs)}\n\n"
        )
        c_txt = c_rst_path.read_text(encoding="utf-8")
        c_txt = re.sub(
            r"\.\. admonition:: Related Collection 1 Topic Guides\n   :class: tip\n\n   .*?\n\n",
            "",
            c_txt,
            flags=re.DOTALL,
        )
        if ".. collapse:: Incident Central Lines" in c_txt:
            c_txt = c_txt.replace(
                ".. collapse:: Incident Central Lines",
                admonition_block + ".. collapse:: Incident Central Lines",
                1,
            )
            c_rst_path.write_text(c_txt, encoding="utf-8")


def _parse_topic_specs(specs: list[str]) -> list[dict]:
    """Parse CLI specs (`1..24`, `1`, or slug names) into matching topic dicts."""
    if not specs:
        return list(COLLECTION_1_TOPICS)
    by_num = {t["num"]: t for t in COLLECTION_1_TOPICS}
    by_slug = {t["slug"]: t for t in COLLECTION_1_TOPICS}
    selected: list[dict] = []
    for sp in specs:
        s = sp.strip()
        m = re.match(r"^(\d+)\.\.(\d+)$", s)
        if m:
            for k in range(int(m.group(1)), int(m.group(2)) + 1):
                if k in by_num:
                    selected.append(by_num[k])
        elif s.isdigit():
            k = int(s)
            if k in by_num:
                selected.append(by_num[k])
        elif s in by_slug:
            selected.append(by_slug[s])
        else:
            raise ValueError(f"Unknown topic specifier: {s}")
    return selected


def main() -> None:
    parser = argparse.ArgumentParser(description="Build ETC Collection 1 Topic Videos (9:16 + 16:9) and Sphinx docs.")
    parser.add_argument(
        "topics",
        nargs="*",
        default=["1..24"],
        help="Topic number(s), range (`1..24`), or slug(s) (default: 1..24)",
    )
    parser.add_argument("--tts", action="store_true", help="Synthesize TTS audio via speak.py")
    parser.add_argument("--tts-only", action="store_true", help="Prepare SVGs/scripts and run TTS only")
    parser.add_argument("--prep-only", action="store_true", help="Only generate SVGs, script.txt, scenes.json, and docs")
    parser.add_argument("--render-only", action="store_true", help="Only render videos from existing SVGs and audio")
    parser.add_argument("--docs-only", action="store_true", help="Only generate Sphinx RST topic docs")
    parser.add_argument("--meta-only", action="store_true", help="Only regenerate youtube.json and youtube.txt")
    args = parser.parse_args()

    if args.docs_only:
        generate_topics_sphinx_docs()
        print("Generated Sphinx topic documentation under docsrc/topics/")
        return

    selected_topics = _parse_topic_specs(args.topics)

    centers: list[dict] = []
    regs_by_preset: dict[str, tuple[str, TriangleContext, CenterRegistry]] = {}
    if not args.render_only and not args.meta_only:
        split_dir = Path("resources/split")
        for k in range(1, 390):
            p = split_dir / f"x-{k:05d}.html"
            if p.is_file():
                c_data = parse_center(p.read_text(encoding="utf-8"))
                if c_data:
                    centers.append(c_data)

        for preset_key, sides in TRIANGLE_PRESETS.items():
            ctx = TriangleContext(*sides)
            reg = CenterRegistry(centers, ctx)
            regs_by_preset[preset_key] = (preset_key, ctx, reg)

    shorts_mod = None
    if not args.prep_only and not args.tts_only and not args.meta_only:
        shorts_mod = _load_patched_shorts_module()

    for topic in selected_topics:
        num = topic["num"]
        slug = topic["slug"]
        prefix = f"T_{num:02d}"
        video_dir = Path(f"resources/videos/topics/t-{num:02d}-{slug}").resolve()
        svgs_dir = video_dir / "svgs"
        svgs_dir.mkdir(parents=True, exist_ok=True)

        script_txt = video_dir / "script.txt"
        scenes_json = video_dir / "scenes.json"
        wav_path = video_dir / f"{prefix}.wav"
        manifest_json = video_dir / f"{prefix}.json"

        if args.meta_only:
            scenes_loaded = json.loads(scenes_json.read_text(encoding="utf-8"))
            _write_topic_youtube_metadata(topic, scenes_loaded, video_dir, prefix)
            print(f"[{prefix}] Updated youtube.json and youtube.txt in {video_dir}")
            continue

        if not args.render_only:
            _, _, acute_reg = regs_by_preset["acute"]
            script_str, scenes_list = build_topic_video_package(
                topic,
                svgs_dir,
                acute_reg,
                regs_by_preset,
            )
            script_txt.write_text(script_str, encoding="utf-8")
            scenes_json.write_text(json.dumps(scenes_list, indent=2, ensure_ascii=False), encoding="utf-8")
            _write_topic_youtube_metadata(topic, scenes_list, video_dir, prefix)
            print(f"[{prefix} • {slug}] Generated 5 SVGs, script.txt, scenes.json, and youtube.json")

        if args.prep_only:
            continue

        if args.tts or args.tts_only or not wav_path.exists() or not manifest_json.exists():
            print(f"[{prefix}] Synthesizing TTS audio via speak.py -> {wav_path.name}")
            subprocess.run(
                [sys.executable, str(SPEAK_PY), "-f", str(script_txt), "-o", str(wav_path)],
                check=True,
            )

        if args.tts_only:
            continue

        # Remove cached slide PNGs so shorts.py renders fresh frames
        for stale_png in video_dir.glob(f"{prefix}_*.png"):
            stale_png.unlink()
        for sub_dir in ("slides_16x9", "slides_9x16"):
            sd = video_dir / sub_dir
            if sd.is_dir():
                for stale_png in sd.glob("*.png"):
                    stale_png.unlink()

        assert shorts_mod is not None
        old_argv = sys.argv
        try:
            sys.argv = [
                str(SHORTS_PY),
                "-s",
                str(scenes_json),
                "-m",
                str(manifest_json),
                "-o",
                str(video_dir),
                "-p",
                prefix,
            ]
            shorts_mod.main()
        finally:
            sys.argv = old_argv

        scenes_loaded = json.loads(scenes_json.read_text(encoding="utf-8"))
        total_slides = sum(len(act.get("subslides", [])) for act in scenes_loaded)
        for idx in range(total_slides):
            s16 = video_dir / "slides_16x9" / f"slide_{idx:02d}.png"
            if s16.exists():
                shutil.copy2(s16, video_dir / f"{prefix}_16x9_{idx:02d}.png")
            s9 = video_dir / "slides_9x16" / f"slide_{idx:02d}.png"
            if s9.exists():
                shutil.copy2(s9, video_dir / f"{prefix}_9x16_{idx:02d}.png")

        _write_topic_youtube_metadata(topic, scenes_loaded, video_dir, prefix)
        print(f"[{prefix}] Completed dual-format Topic Videos and thumbnails in {video_dir}")

    generate_topics_sphinx_docs()


if __name__ == "__main__":
    main()

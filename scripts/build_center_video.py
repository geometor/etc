#!/usr/bin/env python3
"""Build dual-format (9:16 Short + 16:9 1440p QHD) videos for ETC triangle centers.

Usage:
  # Generate SVGs, script.txt, scenes.json, synthesize TTS, and render videos for X_1:
  .venv/bin/python scripts/build_center_video.py 1 --tts

  # Prepare and synthesize TTS for all 19 centers in Collection 1 (X_1..X_19):
  .venv/bin/python scripts/build_center_video.py 1..19 --tts-only

  # Render videos for all 19 centers in Collection 1 from existing audio manifests:
  .venv/bin/python scripts/build_center_video.py 1..19 --render-only
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from geometor.etc.construct import (
    TRIANGLE_PRESETS,
    build_center_model,
    CenterRegistry,
    TriangleContext,
)
from geometor.etc.parser import parse_center
from geometor.etc.render import render_model_svg
from geometor.etc.video import (
    build_center_video_package,
    compile_scenes_from_script,
    ensure_center_incident_lines_in_model,
    generate_center_coordinates_svg,
    generate_central_lines_svg,
    generate_four_triangles_svg,
    generate_relations_svg,
)

SPEAK_PY = Path("/home/phi/.gemini/config/skills/studio/scripts/speak.py")
SHORTS_PY = Path("/home/phi/.gemini/config/skills/studio/scripts/shorts.py")


def _format_html_subscripts_outside_svg(html_doc: str) -> str:
    """Convert `X_n`, `X(n)`, and subscripted point labels (`I_a`, `M_a`, `T_a`, `S_A`, ...) to `<sub>` in HTML text."""
    # Add crisp subscript styling to the page <style>
    sub_css = """
  sub {
    font-size: 0.74em;
    line-height: 0;
    position: relative;
    vertical-align: baseline;
    bottom: -0.20em;
  }
"""
    html_doc = html_doc.replace("</style>", sub_css + "</style>", 1)
    html_doc = html_doc.replace("Heath (1908) • ", "")
    html_doc = html_doc.replace("G-INDEX • ", "CENTER • ")

    # Split out <svg>...</svg>, <style>...</style>, and <script>...</script> blocks so we only touch HTML UI text
    protected_pattern = re.compile(
        r"(<svg\b.*?</svg>|<style\b.*?</style>|<script\b.*?</script>|<[^>]+>)",
        re.DOTALL | re.IGNORECASE,
    )
    parts = protected_pattern.split(html_doc)
    for idx in range(0, len(parts), 2):
        txt = parts[idx]
        if not txt:
            continue
        # Convert X(123) or X_123 -> X<sub>123</sub>
        txt = re.sub(r"\bX\((\d+)\)", r"X<sub>\1</sub>", txt)
        txt = re.sub(r"\bX_\{?(\d+)\}?", r"X<sub>\1</sub>", txt)
        # Convert classical subscripted symbols (I_a, AI_a, M_a, H_a, T_a, N_a, J_a, K_a, S_A, Tan_a, Nap_a, Nap'_a, etc.)
        txt = re.sub(
            r"(Nap'|Nap|Tan|Sym|Ref|Eu|Cm|[IMHTNJKSPr])_([abcABC0-9]+)\b",
            r"\1<sub>\2</sub>",
            txt,
        )
        parts[idx] = txt
    return "".join(parts)


def _load_patched_shorts_module():
    """Load `shorts.py` and patch its SVG/HTML handlers for GEOMETOR ETC drawings and subscript notation."""
    spec = importlib.util.spec_from_file_location("shorts_mod", SHORTS_PY)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {SHORTS_PY}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    orig_9x16 = mod.build_euclid_step_html_9x16
    orig_16x9 = mod.build_euclid_step_html_16x9
    orig_thumb_16x9 = mod.build_euclid_thumbnail_html_16x9
    orig_thumb_9x16 = mod.build_euclid_thumbnail_html_9x16

    def patched_9x16(scene, slide_idx, total_slides, work_dir):
        p = orig_9x16(scene, slide_idx, total_slides, work_dir)
        p.write_text(_format_html_subscripts_outside_svg(p.read_text(encoding="utf-8")), encoding="utf-8")
        return p

    def patched_16x9(scene, slide_idx, total_slides, work_dir):
        p = orig_16x9(scene, slide_idx, total_slides, work_dir)
        p.write_text(_format_html_subscripts_outside_svg(p.read_text(encoding="utf-8")), encoding="utf-8")
        return p

    def patched_thumb_16x9(scene, work_dir):
        p = orig_thumb_16x9(scene, work_dir)
        p.write_text(_format_html_subscripts_outside_svg(p.read_text(encoding="utf-8")), encoding="utf-8")
        return p

    def patched_thumb_9x16(scene, work_dir):
        p = orig_thumb_9x16(scene, work_dir)
        p.write_text(_format_html_subscripts_outside_svg(p.read_text(encoding="utf-8")), encoding="utf-8")
        return p

    mod.build_euclid_step_html_9x16 = patched_9x16
    mod.build_euclid_step_html_16x9 = patched_16x9
    mod.build_euclid_thumbnail_html_16x9 = patched_thumb_16x9
    mod.build_euclid_thumbnail_html_9x16 = patched_thumb_9x16
    return mod


def _clean_display_title(short_title: str) -> str:
    """Format short_title cleanly for YouTube titles (preserving X_n and proper nouns)."""
    t = short_title.title()
    t = re.sub(r"\bX_(\d+)\b", r"X_\1", t, flags=re.IGNORECASE)
    t = re.sub(r"\b1St\b", "1st", t)
    t = re.sub(r"\b2Nd\b", "2nd", t)
    return t


def _write_etc_youtube_metadata(
    num: int,
    short_title: str,
    enunciation: str,
    scenes: list[dict],
    video_dir: Path,
    prefix: str,
) -> None:
    """Write ETC-specific `youtube.txt` and `youtube.json` using `X_n` subscript notation."""
    clean_title = _clean_display_title(short_title)
    title_1080p = f"X_{num} • {clean_title} • Encyclopedia of Triangle Centers"
    title_short = f"X_{num} • {clean_title} • Encyclopedia of Triangle Centers"
    collection_slug = "c-00001-00019" if num <= 19 else f"c-{((num - 20) // 20) * 20 + 20:05d}-{((num - 20) // 20) * 20 + 39:05d}"
    web_url = f"https://geometor.github.io/etc/centers/{collection_slug}/x-{num:05d}/"

    desc_lines = [
        f"“{enunciation}”",
        f"— Clark Kimberling's Encyclopedia of Triangle Centers (ETC) • X_{num} ({clean_title})",
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
        f"GEOMETOR • ETC • X_{num}",
    ])
    description = (
        "\n".join(desc_lines)
        .replace(" < ", " less than ")
        .replace(" > ", " greater than ")
        .replace("<", "⟨")
        .replace(">", "⟩")
    )
    tags = [
        f"X_{num}",
        clean_title,
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

    inferred_privacy = existing_meta.get("privacyStatus", "unlisted")
    for u_entry in existing_meta.get("uploads", {}).values():
        if isinstance(u_entry, dict) and (u_entry.get("privacyStatus") == "public" or u_entry.get("published_at")):
            inferred_privacy = "public"
    for h_list in existing_meta.get("history", {}).values():
        if isinstance(h_list, list):
            for h_entry in h_list:
                if isinstance(h_entry, dict) and (h_entry.get("privacyStatus") == "public" or h_entry.get("published_at")):
                    inferred_privacy = "public"

    meta = {
        "prop_id": f"ETC • X_{num}",
        "short_code": f"X_{num}",
        "g_id": short_title,
        "version": existing_meta.get("version", 1),
        "enunciation": enunciation,
        "title_1080p": title_1080p,
        "title_short": title_short,
        "description": description,
        "tags": tags,
        "categoryId": "27",
        "privacyStatus": inferred_privacy,
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


def _parse_center_specs(specs: list[str]) -> list[int]:
    """Parse CLI arguments like `['1']`, `['1..19']`, or `['2', '3', '4']` into a list of center integers."""
    if not specs:
        return [1]
    nums: list[int] = []
    for sp in specs:
        m = re.match(r"^(\d+)\.\.(\d+)$", sp.strip())
        if m:
            start, end = int(m.group(1)), int(m.group(2))
            nums.extend(range(start, end + 1))
        else:
            nums.append(int(sp.strip()))
    return nums


def main() -> None:
    parser = argparse.ArgumentParser(description="Build ETC Center 9:16 + 16:9 videos and visual coordinate SVGs.")
    parser.add_argument(
        "nums",
        nargs="*",
        default=["1"],
        help="Center number(s) or range like `1..19` (default: 1)",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory when building a single center (default: resources/videos/x-NNNNN)",
    )
    parser.add_argument(
        "--tts",
        action="store_true",
        help="Synthesize <prefix>.wav and <prefix>.json from script.txt via speak.py",
    )
    parser.add_argument(
        "--tts-only",
        action="store_true",
        help="Prepare SVGs/scripts and run TTS synthesis only (without running shorts.py rendering)",
    )
    parser.add_argument(
        "--prep-only",
        action="store_true",
        help="Only generate SVGs, script.txt, and scenes.json without running TTS or video rendering",
    )
    parser.add_argument(
        "--render-only",
        action="store_true",
        help="Only run shorts.py video rendering from existing SVGs, script.txt/scenes.json, and audio manifest",
    )
    parser.add_argument(
        "--from-script",
        action="store_true",
        help="Compile scenes.json directly from existing unified script.txt without overwriting script.txt",
    )
    parser.add_argument(
        "--only-slide",
        type=int,
        default=None,
        help="Re-render only the specified 0-indexed slide (0..6) while reusing other cached slide PNGs and thumbnails",
    )
    parser.add_argument(
        "--thumbs-only",
        action="store_true",
        help="Regenerate SVGs, script.txt, scenes.json, thumbnails, and youtube.json while reusing cached slide PNGs and MP4s",
    )
    parser.add_argument(
        "--meta-only",
        action="store_true",
        help="Only regenerate youtube.json and youtube.txt from existing scenes.json",
    )
    args = parser.parse_args()

    center_nums = _parse_center_specs(args.nums)
    max_num = max(center_nums)

    # Load centers once if we are preparing SVGs/scenes
    centers: list[dict] = []
    regs_by_preset: dict[str, tuple[str, TriangleContext, CenterRegistry]] = {}
    if not args.render_only and not args.tts_only and not args.meta_only and not args.from_script:
        split_dir = Path("resources/split")
        upper = max(105, max_num + 20)
        for k in range(1, upper + 1):
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

    for num in center_nums:
        prefix = f"X_{num:05d}"
        video_dir = (
            args.out_dir
            if (args.out_dir and len(center_nums) == 1)
            else Path(f"videos/x-{num:05d}")
        ).resolve()
        svgs_dir = video_dir / "svgs"
        svgs_dir.mkdir(parents=True, exist_ok=True)

        script_txt = video_dir / "script.txt"
        scenes_json = video_dir / "scenes.json"
        wav_path = video_dir / f"{prefix}.wav"
        manifest_json = video_dir / f"{prefix}.json"

        if args.meta_only:
            scenes_loaded = json.loads(scenes_json.read_text(encoding="utf-8"))
            first_sub = scenes_loaded[0]["subslides"][0]
            _write_etc_youtube_metadata(
                num=num,
                short_title=first_sub.get("g_id", f"X_{num}"),
                enunciation=first_sub.get("enunciation", ""),
                scenes=scenes_loaded,
                video_dir=video_dir,
                prefix=prefix,
            )
            print(f"[X_{num}] Updated youtube.json and youtube.txt in {video_dir}")
            continue

        if args.from_script or (args.render_only and script_txt.exists() and "[screen:" in script_txt.read_text(encoding="utf-8")):
            compiled_scenes = compile_scenes_from_script(script_txt.read_text(encoding="utf-8"), svgs_dir)
            scenes_json.write_text(json.dumps(compiled_scenes, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"[X_{num}] Compiled scenes.json from unified script.txt in {video_dir}")
        elif not args.render_only and not args.tts_only:
            _, acute_ctx, acute_reg = regs_by_preset["acute"]
            _, _, kimberling_reg = regs_by_preset["kimberling"]
            target_center = next((c for c in centers if int(c["num"]) == num), centers[0])
            title = target_center.get("title", f"X_{num}")
            tri_formula = (target_center.get("trilinears") or ["1 : 1 : 1"])[0]
            bary_formula = (target_center.get("barycentrics") or ["a : b : c"])[0]

            # 1. Primary view SVG built fresh via render_model_svg (with tiny-dotted lines & element IDs)
            primary_model = build_center_model(target_center, acute_reg)
            ensure_center_incident_lines_in_model(primary_model, num, acute_reg)
            primary_svg_text = render_model_svg(primary_model)
            for web_svg in Path("docsrc/centers").glob(f"*/x-{num:05d}/x-{num:05d}.svg"):
                if web_svg.is_file():
                    web_svg.write_text(primary_svg_text, encoding="utf-8")

            (svgs_dir / "01_primary.svg").write_text(primary_svg_text, encoding="utf-8")

            script_str, scenes_list, partner_nums = build_center_video_package(
                num,
                target_center,
                svgs_dir,
                acute_reg,
                kimberling_reg,
            )

            (svgs_dir / "02_coordinates.svg").write_text(
                generate_center_coordinates_svg(num, title, tri_formula, bary_formula, acute_ctx, acute_reg),
                encoding="utf-8",
            )
            (svgs_dir / "03_central_lines.svg").write_text(
                generate_central_lines_svg(primary_svg_text),
                encoding="utf-8",
            )
            (svgs_dir / "04_relations.svg").write_text(
                generate_relations_svg(num, partner_nums, acute_reg),
                encoding="utf-8",
            )
            (svgs_dir / "05_four_triangles.svg").write_text(
                generate_four_triangles_svg(num, regs_by_preset),
                encoding="utf-8",
            )

            script_txt.write_text(script_str, encoding="utf-8")
            scenes_json.write_text(json.dumps(scenes_list, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"[X_{num}] Generated 5 SVGs, unified script.txt, and scenes.json in {video_dir}")

        if args.prep_only:
            continue

        if args.tts or args.tts_only or not wav_path.exists() or not manifest_json.exists():
            print(f"[X_{num}] Synthesizing TTS audio via speak.py -> {wav_path.name}")
            subprocess.run(
                [sys.executable, str(SPEAK_PY), "-f", str(script_txt), "-o", str(wav_path)],
                check=True,
            )

        if args.tts_only:
            continue

        if args.thumbs_only:
            for thumb_name in (f"{prefix}_thumb.png", f"{prefix}_short_thumb.png", f"{prefix}_thumb.jpg", f"{prefix}_short_thumb.jpg"):
                tp = video_dir / thumb_name
                if tp.exists():
                    tp.unlink()
        elif args.only_slide is not None:
            for sub_dir in ("slides_16x9", "slides_9x16"):
                target_png = video_dir / sub_dir / f"slide_{args.only_slide:02d}.png"
                if target_png.exists():
                    target_png.unlink()
        else:
            # Remove cached slide PNGs so shorts.py always renders fresh frames
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
            if args.only_slide is not None or args.thumbs_only:
                sys.argv.append("--reuse-frames")
            shorts_mod.main()
        finally:
            sys.argv = old_argv

        # Copy rendered slides to top-level convenience filenames and write ETC YouTube metadata
        scenes_loaded = json.loads(scenes_json.read_text(encoding="utf-8"))
        total_slides = sum(len(act.get("subslides", [])) for act in scenes_loaded)
        for idx in range(total_slides):
            s16 = video_dir / "slides_16x9" / f"slide_{idx:02d}.png"
            if s16.exists():
                shutil.copy2(s16, video_dir / f"{prefix}_16x9_{idx:02d}.png")
            s9 = video_dir / "slides_9x16" / f"slide_{idx:02d}.png"
            if s9.exists():
                shutil.copy2(s9, video_dir / f"{prefix}_9x16_{idx:02d}.png")

        first_sub = scenes_loaded[0]["subslides"][0]
        _write_etc_youtube_metadata(
            num=num,
            short_title=first_sub.get("g_id", f"X_{num}"),
            enunciation=first_sub.get("enunciation", ""),
            scenes=scenes_loaded,
            video_dir=video_dir,
            prefix=prefix,
        )
        print(f"[X_{num}] Completed dual-format videos and thumbnails in {video_dir}")


if __name__ == "__main__":
    main()

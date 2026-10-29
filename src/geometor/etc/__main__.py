"""Command-line interface for the GEOMETOR ETC semantic pipeline."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .glossary import (
    build_citations_json,
    build_glossary_json,
    build_persons_json,
    extract_glossary_intro_rst,
    extract_glossary_terms,
    generate_bibliography_rst,
    generate_glossary_rst,
    generate_persons_rst,
)
from .ingest import ingest_folder, read_html_source
from .parser import parse_center
from .transform import generate_rst_files


def _parse_split_file(file_path: Path) -> dict | None:
    content = file_path.read_text(encoding="utf-8")
    return parse_center(content)


def main() -> None:
    import concurrent.futures
    import multiprocessing

    parser = argparse.ArgumentParser(description="GEOMETOR ETC Semantic Pipeline")
    parser.add_argument(
        "--input",
        "-i",
        default="resources/source",
        help="Input directory containing raw HTML files (default: resources/source)",
    )
    parser.add_argument(
        "--split-dir",
        "-s",
        default="resources/split",
        help="Directory to store split HTML files (default: resources/split)",
    )
    parser.add_argument(
        "--resources-dir",
        "-r",
        default="resources",
        help="Directory to store apparatus JSON registries (default: resources)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="docsrc/centers",
        help="Output directory for center RST files (default: docsrc/centers)",
    )
    parser.add_argument(
        "--limit",
        "-l",
        type=int,
        default=100,
        help="Limit the number of center entries to process (default: 100; 0 for all 53,144)",
    )
    parser.add_argument(
        "--skip-ingest",
        action="store_true",
        help="Skip the HTML ingestion/splitting step if already performed",
    )
    parser.add_argument(
        "--no-graphics",
        action="store_true",
        help="Skip generating Explorer SVG diagrams and geometor.model JSON files",
    )

    args = parser.parse_args()
    input_dir = Path(args.input)
    split_dir = Path(args.split_dir)
    resources_dir = Path(args.resources_dir)
    output_dir = Path(args.output)
    docsrc_dir = output_dir.parent

    resources_dir.mkdir(parents=True, exist_ok=True)
    docsrc_dir.mkdir(parents=True, exist_ok=True)

    # 1. Ingest / Split
    if not args.skip_ingest:
        print(f"Splitting HTML files from {input_dir} to {split_dir}...", flush=True)
        ingest_folder(input_dir, split_dir)
    else:
        print("Skipping ingestion step.", flush=True)

    # Load preambles mapping if available
    preambles_by_center = {}
    preambles_path = split_dir / "preambles.json"
    if preambles_path.is_file():
        preambles_by_center = json.loads(
            preambles_path.read_text(encoding="utf-8")
        )

    # 2. Parse Centers
    print(f"Scanning center HTML files in {split_dir}...", flush=True)
    split_files = sorted(split_dir.glob("x-*.html"))
    print(f"Found {len(split_files)} center files in split directory.", flush=True)

    if args.limit > 0:
        split_files = split_files[: args.limit]

    centers = []
    total_files = len(split_files)
    if total_files > 200:
        mp_ctx = multiprocessing.get_context("fork")
        with concurrent.futures.ProcessPoolExecutor(mp_context=mp_ctx) as pool:
            for done_idx, center_data in enumerate(
                pool.map(_parse_split_file, split_files, chunksize=128), 1
            ):
                if center_data:
                    centers.append(center_data)
                if done_idx % 5000 == 0 or done_idx == total_files:
                    print(
                        f"Parsed {done_idx} / {total_files} center HTML files...",
                        flush=True,
                    )
    else:
        for file_path in split_files:
            center_data = _parse_split_file(file_path)
            if center_data:
                centers.append(center_data)

    valid_centers = {int(c["num"]) for c in centers if c and c.get("num")}
    print(f"Parsed {len(centers)} centers.", flush=True)

    # 3. Glossary & Apparatus Registries
    print("Processing glossary and apparatus registries...")
    glossary_file = (
        input_dir
        / "GLOSSARY, a support page for ENCYCLOPEDIA TRIANGLE CENTERS.html"
    )
    glossary_terms = {}
    if glossary_file.is_file():
        glossary_html = read_html_source(glossary_file)
        glossary_terms = extract_glossary_terms(glossary_html)
        intro_rst = extract_glossary_intro_rst(glossary_html)
        print(
            f"Extracted {len(glossary_terms)} glossary terms (including classical triangle aliases)."
        )

        glossary_rst = generate_glossary_rst(
            glossary_terms, intro_rst=intro_rst, valid_centers=valid_centers
        )
        (docsrc_dir / "glossary.rst").write_text(glossary_rst, encoding="utf-8")
        (docsrc_dir / "persons.rst").write_text(
            generate_persons_rst(valid_centers=valid_centers), encoding="utf-8"
        )
        (docsrc_dir / "bibliography.rst").write_text(
            generate_bibliography_rst(), encoding="utf-8"
        )

        # Write JSON apparatus registries for photon-platform/publish hover tooltips and links
        (resources_dir / "glossary.json").write_text(
            json.dumps(
                build_glossary_json(glossary_terms), indent=2, ensure_ascii=False
            ),
            encoding="utf-8",
        )
        (resources_dir / "persons.json").write_text(
            json.dumps(build_persons_json(), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        (resources_dir / "citations.json").write_text(
            json.dumps(build_citations_json(), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(
            f"Generated {docsrc_dir}/{{glossary,persons,bibliography}}.rst and {resources_dir}/{{glossary,persons,citations}}.json"
        )
    else:
        print(f"Glossary file not found at {glossary_file}")

    # 4. Transform to RST & Render Graphics
    import shutil

    print(f"Generating per-center folders, RST files, and graphics in {output_dir}...")
    if output_dir.is_dir():
        for old_rst in output_dir.glob("x-*.rst"):
            old_rst.unlink()
        legacy_figures = output_dir / "figures"
        if legacy_figures.is_dir():
            shutil.rmtree(legacy_figures)
        expected_dirs = {f"x-{n:05d}" for n in valid_centers}
        for child in output_dir.iterdir():
            if child.is_dir() and child.name.startswith("x-") and child.name not in expected_dirs:
                shutil.rmtree(child)

    generate_rst_files(
        centers,
        output_dir,
        glossary_terms=glossary_terms,
        preambles_by_center=preambles_by_center,
        valid_centers=valid_centers,
        render_graphics=not args.no_graphics,
    )
    print("Done.")


if __name__ == "__main__":
    main()
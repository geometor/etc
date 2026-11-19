import html as _html
import re
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *

import geometor.etc as module
from geometor.etc.svg_opt import strip_svg_for_thumbnail, strip_svg_for_viewer

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "etc"
repo_name = "etc"

setup_globals(org, org_name, repo, repo_name)

site_title = "Encyclopedia of Triangle Centers"
project = site_title
html_title = f"{site_title} • {org_name}"

html_theme = "foundation"
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]


_HTML_SKIP_SUB_RE = re.compile(
    r"("
    r"<(?:pre|code|svg|script|style)\b[^>]*>.*?</(?:pre|code|svg|script|style)>"
    r'|<span\b[^>]*class="[^"]*\bmath\b[^"]*"[^>]*>.*?</span>'
    r'|<div\b[^>]*class="[^"]*\bmath\b[^"]*"[^>]*>.*?</div>'
    r"|<[^>]+>"
    r")",
    flags=re.DOTALL | re.IGNORECASE,
)
_X_SUB_TEXT_RE = re.compile(r"(?<![A-Za-z0-9_])X(?:_(\d+|[ijkn])|\((\d+|[ijkn])\))")
_FIGURE_RE = re.compile(r"<figure\b[^>]*>.*?</figure>", flags=re.DOTALL | re.IGNORECASE)
_FIGCAPTION_P_RE = re.compile(
    r"<figcaption\b[^>]*>(.*?)</figcaption>", flags=re.DOTALL | re.IGNORECASE
)
_ETC_TABLE_RE = re.compile(
    r'(<table\b[^>]*class="[^"]*\betc-table\b[^"]*"[^>]*>.*?</table>)',
    flags=re.DOTALL | re.IGNORECASE,
)


def _format_html_x_subscripts(html_str: str) -> str:
    """Convert X_n and X(n) in HTML text nodes (outside tags, <pre>, <code>, <svg>) to X<sub>n</sub>."""
    if not html_str or "X" not in html_str:
        return html_str
    parts = _HTML_SKIP_SUB_RE.split(html_str)
    for idx in range(0, len(parts), 2):
        if "X" in parts[idx]:
            parts[idx] = _X_SUB_TEXT_RE.sub(
                lambda m: f"X<sub>{m.group(1) or m.group(2)}</sub>",
                parts[idx],
            )
    return "".join(parts)


def _fix_etc_ref_tooltips(app, doctree, fromdocname):
    """Set clean triangle center tooltips on internal #x-N references before Euclid's book X fallback."""
    from docutils import nodes

    from geometor.etc.render import _load_center_names

    center_names = _load_center_names()
    for ref_node in doctree.findall(nodes.reference):
        refuri = ref_node.get("refuri", "")
        m = re.search(r"#x-(\d+)$", refuri)
        if m:
            cnum = m.group(1)
            cname = center_names.get(cnum, "")
            cname_clean = re.sub(r"\bX\((\d+)\)", r"X_\1", cname)
            ref_node["reftitle"] = f"X_{cnum} — {cname_clean}" if cname_clean else f"X_{cnum}"


def _read_raw_svg(svg_path: Path) -> str | None:
    if not svg_path.is_file():
        return None
    return svg_path.read_text(encoding="utf-8").strip()


def _extract_viewbox(svg_text: str | None) -> str | None:
    if not svg_text:
        return None
    m = re.search(r'\bviewBox="([^"]+)"', svg_text)
    return m.group(1).strip() if m else None


def _svg_field(svg_text: str | None, default_fld: str) -> str:
    if not svg_text:
        return default_fld
    m_fld = re.search(r'\bdata-field="([^"]+)"', svg_text)
    return m_fld.group(1) if m_fld else default_fld


_SVG_OPT_PATH = _REPO_ROOT / "src" / "geometor" / "etc" / "svg_opt.py"
_SVG_OPT_MTIME = _SVG_OPT_PATH.stat().st_mtime if _SVG_OPT_PATH.is_file() else 0.0


def _write_stripped_view(src_svg: Path, dst_svg: Path, lines_vb: str | None = None) -> bool:
    """Write a stripped, line-clipped viewer SVG to ``dst_svg`` if missing or stale."""
    if not src_svg.is_file():
        return False
    dst_svg.parent.mkdir(parents=True, exist_ok=True)
    min_mtime = max(src_svg.stat().st_mtime, _SVG_OPT_MTIME)
    if dst_svg.is_file() and dst_svg.stat().st_mtime >= min_mtime:
        return True
    raw = _read_raw_svg(src_svg)
    if not raw:
        return False
    stripped = strip_svg_for_viewer(raw, lines_vb=lines_vb)
    dst_svg.write_text(stripped, encoding="utf-8")
    return True


def _build_unified_viewer(
    *,
    app,
    pagename: str,
    page_dir: Path,
    stem: str,
    title_str: str,
    caption_inner: str,
    is_center_page: bool,
) -> str | None:
    """Build a single-SVG ``.etc-viewer`` shell and emit lazy-fetched secondary SVGs into ``views/``."""
    page_basename = Path(pagename).name
    out_page_dir = Path(app.outdir) / Path(pagename).parent
    views_dir = out_page_dir / "views"

    primary_path = page_dir / f"{stem}.svg"
    primary_raw = _read_raw_svg(primary_path)
    if not primary_raw:
        return None

    # Use 03_central_lines.svg's viewBox (if present) as the exact framing for Central Lines mode
    lines_vb = _extract_viewbox(_read_raw_svg(page_dir / "03_central_lines.svg"))
    ab_badge = '<span class="geom-ref geom-segment" data-ref="[ A B ]">AB</span>'
    is_heronian_exact = 'data-triangle="heronian"' in primary_raw

    if is_heronian_exact:
        tri_specs = [
            (
                "acute",
                "Heronian",
                "Acute Heronian Triangle (15, 13, 14)",
                primary_path,
                "acute.svg",
                f"<strong>{title_str}</strong> over <code>{_html.escape(_svg_field(primary_raw, 'ℚ'))}</code> on Heronian <code>(15, 13, 14)</code> (baseline {ab_badge} = <code>14</code>, area <code>Δ = 84</code>).",
            ),
            (
                "right",
                "3, 4, 5",
                "Pythagorean Right Triangle (3, 4, 5) — Right angle at base A",
                page_dir / f"{stem}-right.svg",
                "right.svg",
                f"<strong>{title_str}</strong> over <code>{_html.escape(_svg_field(_read_raw_svg(page_dir / f'{stem}-right.svg'), 'ℚ'))}</code> on Right <code>(3, 4, 5)</code> (right angle at <code>A</code>, baseline {ab_badge} = <code>4</code>, <code>AC = 3</code>, <code>Δ = 6</code>).",
            ),
            (
                "kepler",
                "Kepler",
                "Kepler Golden Right Triangle (1, √φ, φ) — Right angle at base A",
                page_dir / f"{stem}-kepler.svg",
                "kepler.svg",
                f"<strong>{title_str}</strong> over <code>{_html.escape(_svg_field(_read_raw_svg(page_dir / f'{stem}-kepler.svg'), 'ℚ(√φ)'))}</code> on Kepler <code>(1, √φ, φ)</code> (right angle at <code>A</code>, baseline {ab_badge} = <code>√φ</code>, <code>AC = 1</code>).",
            ),
            (
                "kimberling",
                "Kimberling",
                "Kimberling Obtuse Scalene Triangle (6, 9, 13)",
                page_dir / f"{stem}-kimberling.svg",
                "kimberling.svg",
                f"<strong>{title_str}</strong> over <code>{_html.escape(_svg_field(_read_raw_svg(page_dir / f'{stem}-kimberling.svg'), 'ℚ(√35)'))}</code> on Kimberling <code>(6, 9, 13)</code> (baseline {ab_badge} = <code>13</code>).",
            ),
            (
                "golden",
                "Golden",
                "Pentagon Golden Triangle (φ, φ, 1) — 36°-72°-72° acute isosceles",
                page_dir / f"{stem}-golden.svg",
                "golden.svg",
                f"<strong>{title_str}</strong> over <code>{_html.escape(_svg_field(_read_raw_svg(page_dir / f'{stem}-golden.svg'), 'ℚ(√(5+2√5))'))}</code> on Pentagon Golden Triangle <code>(φ, φ, 1)</code> (36°–72°–72°, baseline {ab_badge} = <code>1</code>).",
            ),
            (
                "gnomon",
                "Gnomon",
                "Pentagon Golden Gnomon (1, 1, φ) — 108°-36°-36° obtuse isosceles",
                page_dir / f"{stem}-gnomon.svg",
                "gnomon.svg",
                f"<strong>{title_str}</strong> over <code>{_html.escape(_svg_field(_read_raw_svg(page_dir / f'{stem}-gnomon.svg'), 'ℚ(√(5+2√5))'))}</code> on Pentagon Golden Gnomon <code>(1, 1, φ)</code> (108°–36°–36°, baseline {ab_badge} = <code>φ</code>).",
            ),
            (
                "equilateral",
                "Equilateral",
                "Regular Equilateral Triangle (2, 2, 2) — 60°-60°-60° D₃ symmetry limit",
                page_dir / f"{stem}-equilateral.svg",
                "equilateral.svg",
                f"<strong>{title_str}</strong> over <code>{_html.escape(_svg_field(_read_raw_svg(page_dir / f'{stem}-equilateral.svg'), 'ℚ(√3)'))}</code> on Equilateral <code>(2, 2, 2)</code> (D₃ symmetry limit, baseline {ab_badge} = <code>2</code>, <code>Δ = √3</code>).",
            ),
        ]
    else:
        tri_specs = [
            (
                "acute",
                "5, 6, 7",
                "Acute Scalene Triangle (5, 6, 7)",
                primary_path,
                "acute.svg",
                f"<strong>{title_str}</strong> on acute reference triangle <code>(5, 6, 7)</code> (unit baseline {ab_badge} = <code>1</code>).",
            ),
            (
                "right",
                "3, 4, 5",
                "Egyptian Right Triangle (3, 4, 5)",
                page_dir / f"{stem}-right.svg",
                "right.svg",
                f"<strong>{title_str}</strong> on Egyptian right triangle <code>(3, 4, 5)</code> (unit baseline {ab_badge} = <code>1</code>).",
            ),
            (
                "kepler",
                "Kepler",
                "Kepler Golden Right Triangle (1, √φ, φ)",
                page_dir / f"{stem}-kepler.svg",
                "kepler.svg",
                f"<strong>{title_str}</strong> on Kepler golden right triangle <code>(1, √φ, φ)</code> (unit baseline {ab_badge} = <code>1</code>).",
            ),
            (
                "kimberling",
                "Kimberling",
                "Kimberling Obtuse Scalene Triangle (6, 9, 13)",
                page_dir / f"{stem}-kimberling.svg",
                "kimberling.svg",
                f"<strong>{title_str}</strong> on Kimberling's canonical triangle <code>(6, 9, 13)</code> (unit baseline {ab_badge} = <code>1</code>).",
            ),
        ]

    # Track-aware default mode
    if is_center_page and page_basename == "lines":
        default_mode = "lines"
    elif is_center_page and page_basename == "relations" and (page_dir / "04_relations.svg").is_file():
        default_mode = "relations"
    else:
        default_mode = "construction"

    # Always emit stripped views/*.svg for secondary triangles & available Act plates
    tri_btns_html: list[str] = []
    for tab_id, label, tip, src_path, view_fname, cap_html in tri_specs:
        if not src_path.is_file():
            continue
        _write_stripped_view(
            src_path,
            views_dir / view_fname,
            lines_vb=lines_vb if tab_id == "acute" else None,
        )
        is_active = tab_id == "acute"
        active_cls = " active" if is_active else ""
        aria_sel = "true" if is_active else "false"
        tri_btns_html.append(
            f'<button type="button" class="etc-tab-btn{active_cls}" role="tab" '
            f'aria-selected="{aria_sel}" data-tab="{tab_id}" data-src="views/{view_fname}" '
            f'title="{_html.escape(tip, quote=True)}" '
            f'data-caption-html="{_html.escape(cap_html, quote=True)}">{label}</button>'
        )

    is_multitrack = is_center_page and (page_dir / "lines.rst").is_file()
    has_coords = (page_dir / "02_coordinates.svg").is_file()
    has_rels = (page_dir / "04_relations.svg").is_file()
    has_four = (page_dir / "05_four_triangles.svg").is_file()
    if is_center_page:
        if has_coords:
            _write_stripped_view(page_dir / "02_coordinates.svg", views_dir / "coordinates.svg")
        if has_rels:
            _write_stripped_view(page_dir / "04_relations.svg", views_dir / "relations.svg")
        if has_four:
            _write_stripped_view(page_dir / "05_four_triangles.svg", views_dir / "four_triangles.svg")

    # Track-scoped viewer mode buttons (NEVER duplicate the Book Codex page track menu!)
    # - Overview track (`index`): only the views belonging to Overview (Construction, Coordinates, Triangles)
    # - Lines track (`lines`): no mode bar — reference triangle tabs directly over Central Lines
    # - Relations track (`relations`): no mode bar & no triangle tabs — dedicated Relations plate
    # - Notes / Code tracks: no mode bar — reference triangle tabs over Construction
    mode_btns_html: list[str] = []
    if is_center_page and page_basename == "index" and (has_coords or has_four):
        mode_specs: list[tuple[str, str, str, str | None, str]] = [
            (
                "construction",
                "Construction",
                "Primary geometric construction",
                "views/acute.svg",
                f"<strong>{title_str}</strong> — primary defining construction.",
            ),
        ]
        if has_coords:
            mode_specs.append(
                (
                    "coordinates",
                    "Coordinates",
                    "Homogeneous trilinear struts and signed barycentric sub-triangles",
                    "views/coordinates.svg",
                    f"<strong>Homogeneous Coordinates of {title_str}</strong>: orthogonal trilinear struts and signed barycentric sub-triangles on Heronian <code>(15, 13, 14)</code>.",
                )
            )
        if has_four:
            mode_specs.append(
                (
                    "four_triangles",
                    "Triangles",
                    "3×2 invariance grid across all six non-degenerate canonical reference triangles",
                    "views/four_triangles.svg",
                    f"<strong>Canonical Triangle Invariance of {title_str}</strong> across Heronian, Right, Kepler, Kimberling, Golden, and Gnomon reference triangles.",
                )
            )

        if len(mode_specs) > 1:
            for mode_id, m_label, m_tip, m_src, m_cap in mode_specs:
                is_active = mode_id == default_mode
                active_cls = " active" if is_active else ""
                aria_sel = "true" if is_active else "false"
                src_attr = f' data-src="{m_src}"' if m_src else ""
                mode_btns_html.append(
                    f'<button type="button" class="etc-mode-btn{active_cls}" role="tab" '
                    f'aria-selected="{aria_sel}" data-mode="{mode_id}"{src_attr} '
                    f'title="{_html.escape(m_tip, quote=True)}" '
                    f'data-caption-html="{_html.escape(m_cap, quote=True)}">{m_label}</button>'
                )

    # Central Lines toolbar toggle belongs only on the Lines track or legacy single-track pages
    allow_lines = (not is_multitrack) or (page_basename == "lines")
    allow_lines_attr = "true" if allow_lines else "false"

    # Inline ONLY the single initial stripped SVG into HTML
    if default_mode == "relations":
        initial_svg = strip_svg_for_viewer(_read_raw_svg(page_dir / "04_relations.svg") or primary_raw)
    else:
        initial_svg = strip_svg_for_viewer(primary_raw, lines_vb=lines_vb)
        if default_mode == "lines" and "show-lines" not in initial_svg[:220]:
            initial_svg = initial_svg.replace(
                'class="geometor-etc-drawing"',
                'class="geometor-etc-drawing show-lines"',
                1,
            )

    chrome_parts: list[str] = []
    if mode_btns_html:
        chrome_parts.append(
            '<div class="etc-mode-tabs" role="tablist" aria-label="Diagram View Mode">\n    '
            + "\n    ".join(mode_btns_html)
            + "\n  </div>"
        )
    if len(tri_btns_html) > 1 and default_mode != "relations":
        disabled_cls = " is-disabled" if default_mode not in ("construction", "lines") else ""
        chrome_parts.append(
            f'<div class="etc-triangle-tabs{disabled_cls}" role="tablist" aria-label="Reference Triangle">\n    '
            + "\n    ".join(tri_btns_html)
            + "\n  </div>"
        )

    chrome_html = (
        '  <div class="etc-viewer-chrome">\n  ' + "\n  ".join(chrome_parts) + "\n  </div>\n"
        if chrome_parts
        else ""
    )
    cap_block = (
        f'  <div class="etc-viewer-caption">{caption_inner}</div>\n'
        if caption_inner.strip()
        else ""
    )

    return (
        f'<div class="etc-viewer" data-default-mode="{default_mode}" '
        f'data-default-triangle="acute" data-allow-lines="{allow_lines_attr}">\n'
        f"{chrome_html}"
        f'  <div class="etc-svg-stage">\n{initial_svg}\n  </div>\n'
        f"{cap_block}"
        f"</div>"
    )


def _wrap_center_split_stage(body: str, viewer_html: str) -> str:
    """Place the page heading/identity full-width and dock ``.etc-viewer`` sticky beside prose."""
    marker = "<!--ETC_VIEWER_SLOT-->"
    if marker not in body:
        return body
    before, after = body.split(marker, 1)

    # Keep only the single outermost closing </section> (and optional empty toctree) outside .etc-split-workspace
    closing_tail = ""
    m_end = re.search(
        r'(\s*(?:<div class="toctree-wrapper[^>]*>\s*</div>\s*)?</section>\s*)$',
        after,
        re.DOTALL,
    )
    if m_end:
        closing_tail = m_end.group(1)
        after = after[: m_end.start()]

    # Keep h1, rubric, identity bar, and enunciation full-width above the split graphic + tables workspace
    return (
        f"{before}\n"
        f'<div class="etc-split-workspace">\n'
        f'  <div class="etc-stage-column">\n{viewer_html}\n  </div>\n'
        f'  <div class="etc-prose-column">\n{after}\n  </div>\n'
        f"</div>\n"
        f"{closing_tail}"
    )


def _inline_etc_svgs(app, pagename, templatename, context, doctree):
    """Format X_n subscripts, inject unified single-SVG .etc-viewer, and wrap split-stage tables."""
    from geometor.etc.render import _load_center_names
    from geometor.etc.transform import get_collection_spec

    if context.get("title"):
        context["title"] = _format_html_x_subscripts(str(context["title"]))
    for nav_key in ("prev", "next"):
        nav_obj = context.get(nav_key)
        if isinstance(nav_obj, dict) and nav_obj.get("title"):
            nav_obj["title"] = _format_html_x_subscripts(str(nav_obj["title"]))
    for crumb in context.get("book_breadcrumbs") or []:
        if isinstance(crumb, dict) and crumb.get("title"):
            docname = crumb.get("docname", "")
            m_col = re.search(r"c-(\d+)-(\d+)/index$", docname)
            if m_col:
                _, _, col_title, _ = get_collection_spec(int(m_col.group(1)))
                crumb["title"] = _format_html_x_subscripts(f"{crumb['title']} · {_html.escape(col_title)}")
            else:
                crumb["title"] = _format_html_x_subscripts(str(crumb["title"]))

    body = context.get("body")
    if not body:
        return

    if pagename in ("centers/index", "types/collection"):
        def _col_card_h2_repl(m: re.Match) -> str:
            href, s_str, e_str, inner = m.group(1), m.group(2), m.group(3), m.group(4)
            start_n, end_n = int(s_str), int(e_str)
            _, _, col_title, _ = get_collection_spec(start_n)
            count = end_n - start_n + 1
            sub_esc = _html.escape(f"{col_title} ({count} centers)")
            return (
                f'<h2><a href="{href}">{inner}'
                f'<span class="etc-card-subtitle" style="display: block; font-size: 0.82em; '
                f'font-weight: 700; font-style: normal; color: var(--book-text-muted); '
                f'margin-top: 0.12rem;">{sub_esc}</span></a></h2>'
            )

        body = re.sub(
            r'<h2><a href="((?:[^"/]+/)*c-(\d+)-(\d+)/index\.html)">(.*?)</a></h2>',
            _col_card_h2_repl,
            body,
        )

    if pagename.startswith("centers/c-") and pagename.endswith("/index"):
        center_names = _load_center_names()

        def _card_h2_repl(m: re.Match) -> str:
            href, num_s, inner = m.group(1), str(int(m.group(2))), m.group(3)
            sub = center_names.get(num_s, "").lstrip("=").strip()
            sub = re.sub(r"\bX\((\d+)\)", r"X_\1", sub)
            if sub and sub not in inner:
                sub_esc = _html.escape(sub)
                return (
                    f'<h2><a href="{href}">{inner}'
                    f'<span class="etc-card-subtitle" style="display: block; font-size: 0.82em; '
                    f'font-weight: 700; font-style: normal; color: var(--book-text-muted); '
                    f'margin-top: 0.12rem;">{sub_esc}</span></a></h2>'
                )
            return m.group(0)

        body = re.sub(
            r'<h2><a href="(x-(\d+)/index\.html)">(.*?)</a></h2>',
            _card_h2_repl,
            body,
        )

    body = _format_html_x_subscripts(body)

    # Defer MathJax typesetting inside initially-closed <details class="book-collapse"> blocks
    body = body.replace(
        '<div class="book-collapse-body">',
        '<div class="book-collapse-body etc-lazy-math">',
    )

    # Wrap .etc-table instances in horizontal-scroll guard containers
    body = _ETC_TABLE_RE.sub(r'<div class="etc-table-wrap">\1</div>', body)

    is_center_page = "/x-" in pagename
    is_collection_page = pagename.startswith("centers/c-") and pagename.endswith("/index")
    if not (is_center_page or is_collection_page):
        context["body"] = body
        return

    srcdir = Path(app.srcdir)
    page_dir = srcdir / Path(pagename).parent

    # Replace primary figure (<figure>...<img src=".../(x-\d+|c-\d+-\d+).svg">...</figure>)
    # with the single unified .etc-viewer
    stem_re = re.compile(
        r'<img\b[^>]*\bsrc="[^"]*/(x-\d+|0[2-5]_[a-z0-9_]+?)\d*\.svg"[^>]*/>'
        if is_center_page
        else r'<img\b[^>]*\bsrc="[^"]*/(c-\d+-\d+)\d*\.svg"[^>]*/>'
    )
    center_folder_stem = page_dir.name  # e.g., "x-00001" or "c-00001-00019"
    built_viewer_html: str | None = None

    def _replace_figure(fig_match: re.Match) -> str:
        nonlocal built_viewer_html
        fig_html = fig_match.group(0)
        img_m = stem_re.search(fig_html)
        if not img_m:
            return fig_html
        matched_stem = img_m.group(1)

        # If this is a secondary Act plate figure inside an older monolithic page,
        # replace it with a lightweight mode-switch button pointing to the unified stage!
        if is_center_page and built_viewer_html is not None and matched_stem.startswith("0"):
            mode_map = {
                "02_coordinates": ("coordinates", "Switch Stage to Coordinates View ↗"),
                "03_central_lines": ("lines", "Switch Stage to Central Lines View ↗"),
                "04_relations": ("relations", "Switch Stage to Relations View ↗"),
                "05_four_triangles": ("four_triangles", "Switch Stage to 4-Triangles Grid ↗"),
            }
            for prefix, (m_key, m_lbl) in mode_map.items():
                if matched_stem.startswith(prefix):
                    return (
                        f'<p><button type="button" class="etc-view-trigger" '
                        f'data-etc-switch-mode="{m_key}">{m_lbl}</button></p>'
                    )
            return fig_html

        alt_m = re.search(r'\balt="([^"]*)"', img_m.group(0))
        title_str = _format_html_x_subscripts(alt_m.group(1) if alt_m else center_folder_stem)
        cap_m = _FIGCAPTION_P_RE.search(fig_html)
        cap_inner = cap_m.group(1).strip() if cap_m else ""

        viewer = _build_unified_viewer(
            app=app,
            pagename=pagename,
            page_dir=page_dir,
            stem=center_folder_stem if is_center_page else matched_stem,
            title_str=title_str,
            caption_inner=cap_inner,
            is_center_page=is_center_page,
        )
        if not viewer:
            return fig_html
        built_viewer_html = viewer
        if is_center_page:
            return "<!--ETC_VIEWER_SLOT-->"
        return viewer

    body = _FIGURE_RE.sub(_replace_figure, body)

    if is_center_page and built_viewer_html is not None:
        body = _wrap_center_split_stage(body, built_viewer_html)

    context["body"] = body


def _optimize_thumbnail_svgs(app, exception):
    """Strip scripts, metadata, and oversized line extents from docs/_images/*.svg thumbnails."""
    if exception is not None:
        return
    images_dir = Path(app.outdir) / "_images"
    if not images_dir.is_dir():
        return
    optimized = 0
    for svg_file in images_dir.glob("*.svg"):
        try:
            raw = svg_file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if (
            "<script" not in raw
            and "etc-symbolic-hud" not in raw
            and svg_file.stat().st_mtime >= _SVG_OPT_MTIME
        ):
            continue
        if "geometor-etc-drawing" not in raw:
            continue
        stripped = strip_svg_for_thumbnail(raw)
        svg_file.write_text(stripped, encoding="utf-8")
        optimized += 1
    if optimized:
        print(f"[etc] Optimized {optimized} thumbnail SVGs in {images_dir}")


def setup(app):
    app.add_css_file("css/etc-viewer.css")
    app.add_js_file("js/etc-viewer.js")
    app.connect("doctree-resolved", _fix_etc_ref_tooltips, priority=400)
    app.connect("html-page-context", _inline_etc_svgs, priority=600)
    app.connect("build-finished", _optimize_thumbnail_svgs)

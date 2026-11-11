from pathlib import Path
import re
import sys

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

version = module.__version__

org = "geometor"
org_name = "geometor"

repo = "etc"
repo_name = "etc"

setup_globals(org, org_name, repo, repo_name)

html_theme = "foundation"
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]


def _read_clean_svg(svg_path: Path) -> str | None:
    if not svg_path.is_file():
        return None
    raw_svg = svg_path.read_text(encoding="utf-8").strip()
    return re.sub(r"^<\?xml[^>]*\?>\s*", "", raw_svg)


_HTML_SKIP_SUB_RE = re.compile(
    r"(<(?:pre|code|svg|script|style)\b[^>]*>.*?</(?:pre|code|svg|script|style)>|<[^>]+>)",
    flags=re.DOTALL | re.IGNORECASE,
)
_X_SUB_TEXT_RE = re.compile(r"(?<![A-Za-z0-9_])X(?:_(\d+|[ijkn])|\((\d+|[ijkn])\))")


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


_ETC_HEADING_CSS = """<style id="etc-heading-styles">
.book-reading-pane .book-content h1,
.folio-book-page h1 {
    position: relative;
    text-align: center !important;
    text-indent: 0 !important;
    margin-bottom: 0.35rem !important;
}
.book-reading-pane .book-content h1 a.headerlink,
.book-reading-pane .book-content h2 a.headerlink,
.folio-book-page h1 a.headerlink,
.folio-book-page h2 a.headerlink {
    position: absolute;
}
.book-reading-pane .book-content p.rubric,
.folio-book-page p.rubric {
    font-style: normal !important;
    font-weight: 700 !important;
    text-align: center !important;
    text-indent: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    margin-top: 0 !important;
    margin-bottom: 1.4rem !important;
}
.geom-ref {
    cursor: pointer;
    border-bottom: 1px dotted rgba(0, 229, 255, 0.55);
    padding: 0 2px;
    border-radius: 3px;
    transition: background-color 0.12s ease, color 0.12s ease;
}
.geom-ref:hover,
.geom-highlight-text {
    background-color: rgba(0, 255, 255, 0.18) !important;
    color: #0ff !important;
    border-bottom-color: #0ff !important;
}
.etc-act-plate {
    margin: 0.5rem 0;
}
.etc-symbolic-concordance {
    text-align: center;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.92rem;
    color: var(--book-text-muted, #94a3b8);
    margin: -0.6rem 0 1.25rem 0;
}
</style>
"""


def _inline_etc_svgs(app, pagename, templatename, context, doctree):
    """Format X_n subscripts across HTML pages and inline interactive 4-tab and 5-act SVGs on center pages."""
    import html as _html
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

    body = _ETC_HEADING_CSS + _format_html_x_subscripts(body)

    is_center_page = "/x-" in pagename
    is_collection_page = pagename.startswith("centers/c-") and pagename.endswith("/index")
    if not (is_center_page or is_collection_page):
        context["body"] = body
        return

    srcdir = Path(app.srcdir)
    page_dir = srcdir / Path(pagename).parent

    def _repl(match: re.Match) -> str:
        full_img = match.group(0)
        stem = match.group(1)
        alt_m = re.search(r'\balt="([^"]*)"', full_img)
        title_str = _format_html_x_subscripts(alt_m.group(1) if alt_m else stem)

        ab_badge = '<span class="geom-ref geom-segment" data-ref="[ A B ]">AB</span>'
        primary_svg_preview = _read_clean_svg(page_dir / f"{stem}.svg") or ""
        is_heronian_exact = 'data-triangle="heronian"' in primary_svg_preview

        if is_heronian_exact:
            tab_specs = [
                (
                    "acute",
                    "15, 13, 14",
                    "Acute Heronian Triangle (15, 13, 14)",
                    page_dir / f"{stem}.svg",
                    f"<strong>{title_str}</strong> constructed over <code>ℚ</code> on exact Heronian triangle <code>(a, b, c) = (15, 13, 14)</code> with baseline {ab_badge} = <code>14</code> and integer area <code>Δ = 84</code>.",
                ),
                (
                    "right",
                    "3, 4, 5",
                    "Egyptian Right Triangle (3, 4, 5)",
                    page_dir / f"{stem}-right.svg",
                    f"<strong>{title_str}</strong> constructed over <code>ℚ</code> on Egyptian right triangle <code>(a, b, c) = (3, 4, 5)</code> with hypotenuse baseline {ab_badge} = <code>5</code> and area <code>Δ = 6</code>.",
                ),
                (
                    "kepler",
                    "Kepler",
                    "Kepler Golden Right Triangle (1, √φ, φ)",
                    page_dir / f"{stem}-kepler.svg",
                    f"<strong>{title_str}</strong> constructed over <code>ℚ(√φ)</code> on Kepler golden right triangle <code>(a, b, c) = (1, √φ, φ)</code> with baseline {ab_badge} = <code>φ</code>.",
                ),
                (
                    "kimberling",
                    "Kimberling",
                    "Kimberling Obtuse Scalene Triangle (6, 9, 13)",
                    page_dir / f"{stem}-kimberling.svg",
                    f"<strong>{title_str}</strong> constructed over <code>ℚ(√35)</code> on Kimberling's canonical search-value triangle <code>(a, b, c) = (6, 9, 13)</code> with baseline {ab_badge} = <code>13</code>.",
                ),
            ]
        else:
            tab_specs = [
                (
                    "acute",
                    "5, 6, 7",
                    "Acute Scalene Triangle (5, 6, 7)",
                    page_dir / f"{stem}.svg",
                    f"<strong>{title_str}</strong> constructed on acute reference triangle <code>(a, b, c) = (5, 6, 7)</code> with unit baseline {ab_badge} = <code>1</code>.",
                ),
                (
                    "right",
                    "3, 4, 5",
                    "Egyptian Right Triangle (3, 4, 5)",
                    page_dir / f"{stem}-right.svg",
                    f"<strong>{title_str}</strong> constructed on Egyptian right triangle <code>(a, b, c) = (3, 4, 5)</code> with unit baseline {ab_badge} = <code>1</code>.",
                ),
                (
                    "kepler",
                    "Kepler",
                    "Kepler Golden Right Triangle (1, √φ, φ)",
                    page_dir / f"{stem}-kepler.svg",
                    f"<strong>{title_str}</strong> constructed on Kepler golden right triangle <code>(a, b, c) = (1, √φ, φ)</code> with unit baseline {ab_badge} = <code>1</code>.",
                ),
                (
                    "kimberling",
                    "Kimberling",
                    "Kimberling Obtuse Scalene Triangle (6, 9, 13)",
                    page_dir / f"{stem}-kimberling.svg",
                    f"<strong>{title_str}</strong> constructed on Kimberling's canonical uniqueness test triangle <code>(a, b, c) = (6, 9, 13)</code> (obtuse scalene, unit baseline {ab_badge} = <code>1</code>).",
                ),
            ]

        available = []
        for tab_id, label, tip, path, cap_html in tab_specs:
            svg_code = _read_clean_svg(path)
            if svg_code:
                available.append((tab_id, label, tip, svg_code, cap_html))

        if not available:
            return full_img
        if len(available) == 1:
            return available[0][3]

        btns_html = []
        panes_html = []
        for idx, (tab_id, label, tip, svg_code, cap_html) in enumerate(available):
            is_first = idx == 0
            active_cls = " active" if is_first else ""
            aria_sel = "true" if is_first else "false"
            esc_cap = _html.escape(cap_html, quote=True)
            esc_tip = _html.escape(tip, quote=True)
            btns_html.append(
                f'<button type="button" class="etc-tab-btn{active_cls}" role="tab" '
                f'aria-selected="{aria_sel}" data-tab="{tab_id}" title="{esc_tip}" '
                f'data-caption-html="{esc_cap}">{label}</button>'
            )
            style_attr = "" if is_first else ' style="display: none;"'
            panes_html.append(
                f'<div class="etc-tab-pane{active_cls}" data-tab-pane="{tab_id}"{style_attr}>\n{svg_code}\n</div>'
            )

        return (
            '<div class="etc-graphics-panel">\n'
            '  <div class="etc-triangle-tabs" role="tablist" aria-label="Reference Triangle">\n'
            + "    "
            + "\n    ".join(btns_html)
            + "\n  </div>\n"
            + "\n".join(panes_html)
            + "\n</div>"
        )

    svg_pattern = (
        r'<img\b[^>]*\bsrc="[^"]*/(x-\d+)\.svg"[^>]*/>'
        if is_center_page
        else r'<img\b[^>]*\bsrc="[^"]*/(c-\d+-\d+)\.svg"[^>]*/>'
    )
    body = re.sub(svg_pattern, _repl, body)

    if is_center_page:
        def _repl_act_plate(match: re.Match) -> str:
            plate_stem = match.group(1)
            svg_code = _read_clean_svg(page_dir / f"{plate_stem}.svg")
            if not svg_code:
                return match.group(0)
            return f'<div class="etc-graphics-panel etc-act-plate">\n{svg_code}\n</div>'

        body = re.sub(
            r'<img\b[^>]*\bsrc="[^"]*/(0[2-5]_[a-z0-9_]+)\.svg"[^>]*/>',
            _repl_act_plate,
            body,
        )

    context["body"] = body



def setup(app):
    app.connect("doctree-resolved", _fix_etc_ref_tooltips, priority=400)
    app.connect("html-page-context", _inline_etc_svgs, priority=600)


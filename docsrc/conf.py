from pathlib import Path
import re
from photon_platform.publish.global_conf import *
import geometor.etc as module

version = module.__version__

org = "geometor"
org_name = "geometor"

repo = "etc"
repo_name = "etc"

setup_globals(org, org_name, repo, repo_name)

html_theme = "foundation"


def _read_clean_svg(svg_path: Path) -> str | None:
    if not svg_path.is_file():
        return None
    raw_svg = svg_path.read_text(encoding="utf-8").strip()
    return re.sub(r"^<\?xml[^>]*\?>\s*", "", raw_svg)


def _inline_etc_svgs(app, pagename, templatename, context, doctree):
    """Inline interactive triangle SVGs into a unified 4-tab graphics panel on center pages."""
    body = context.get("body")
    if not body or not pagename.startswith("centers/x-"):
        return

    import html as _html

    srcdir = Path(app.srcdir)
    page_dir = srcdir / Path(pagename).parent

    def _repl(match: re.Match) -> str:
        full_img = match.group(0)
        stem = match.group(1)
        alt_m = re.search(r'\balt="([^"]*)"', full_img)
        title_str = alt_m.group(1) if alt_m else stem

        ab_badge = '<span class="geom-ref geom-segment" data-ref="[ A B ]">AB</span>'
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

    context["body"] = re.sub(
        r'<img\b[^>]*\bsrc="[^"]*/(x-\d+)\.svg"[^>]*/>',
        _repl,
        body,
    )


def setup(app):
    app.connect("html-page-context", _inline_etc_svgs)


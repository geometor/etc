#!/usr/bin/env python3
"""Build dual-format (9:16 Short + 16:9 1440p QHD) Intro Video for Collection 1 (X_1–X_19).

Generates:
  - resources/videos/intro-collection-1/svgs/01_constellation.svg .. 05_four_triangles.svg
  - resources/videos/intro-collection-1/script.txt & scenes.json
  - resources/videos/intro-collection-1/C_01_1080p.mp4, C_01_short.mp4, C_01_thumb.png, C_01_short_thumb.png
  - Updates docsrc/centers/c-00001-00019/c-00001-00019.svg and index.rst
"""

from __future__ import annotations

import argparse
import html
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_center_video import (
    SHORTS_PY,
    SPEAK_PY,
    _load_patched_shorts_module,
)
from geometor.etc.construct import (
    TRIANGLE_PRESETS,
    CenterRegistry,
    TriangleContext,
    _add_circle,
    _add_line,
    _add_point,
    _add_polygon,
)
from geometor.etc.parser import parse_center
from geometor.etc.render import render_model_svg
from geometor.etc.video import _mute_other_spans
from geometor.model import Model


COLLECTION_1_FAMILIES = [
    ("Euler & Classical Spine", "#e8b85a", [1, 2, 3, 4, 5, 6]),
    ("Contact, Perimeter & Feuerbach", "#38bdf8", [7, 8, 9, 10, 11, 12]),
    ("Equilateral Six & Clawson", "#5ec27e", [13, 14, 15, 16, 17, 18, 19]),
]


def build_collection_1_model(
    reg: CenterRegistry,
    include_all_lines: bool = False,
) -> Model:
    """Build a symbolic GEOMETOR Model containing all 19 centers of Collection 1 (X_1–X_19)."""
    ctx = reg.ctx
    model = Model("collection_1_x_00001_00019")
    A = _add_point(model, 0.0, 0.0, "A", classes=["given"])
    B = _add_point(model, 1.0, 0.0, "B", classes=["given"])
    Cx, Cy = ctx.C_xy
    C = _add_point(model, Cx, Cy, "C", classes=["given"])
    _add_polygon(model, [A, B, C], classes=["reference"])

    # Medial triangle M_a M_b M_c
    Ma = _add_point(model, 0.5 * (1.0 + Cx), 0.5 * Cy, "M_a", classes=["auxiliary"])
    Mb = _add_point(model, 0.5 * Cx, 0.5 * Cy, "M_b", classes=["auxiliary"])
    Mc = _add_point(model, 0.5, 0.0, "M_c", classes=["auxiliary"])
    _add_polygon(model, [Ma, Mb, Mc], classes=["medial"])

    # Add Incircle, Circumcircle, and Nine-Point Circle
    x1_xy = reg.xy_cache.get(1)
    if x1_xy:
        p1 = _add_point(model, x1_xy[0], x1_xy[1], "X_1")
        tx, ty = x1_xy[0], 0.0
        pt_t = _add_point(model, tx, ty, "T_c", classes=["auxiliary"])
        _add_circle(model, p1, pt_t, classes=["incircle"])

    x3_xy = reg.xy_cache.get(3)
    if x3_xy:
        p3 = _add_point(model, x3_xy[0], x3_xy[1], "X_3")
        _add_circle(model, p3, A, classes=["circumcircle"])

    x5_xy = reg.xy_cache.get(5)
    if x5_xy:
        p5 = _add_point(model, x5_xy[0], x5_xy[1], "X_5")
        _add_circle(model, p5, Mc, classes=["nine_point_circle"])

    # Add interior/near-triangle centers X_1..X_19 (excluding far-exterior X_16 from framing)
    pts_by_num = {}
    for c_num in range(1, 20):
        if c_num == 16:
            continue
        xy = reg.xy_cache.get(c_num)
        if xy:
            pts_by_num[c_num] = _add_point(
                model, xy[0], xy[1], f"X_{c_num}", classes=["center_target"]
            )

    # Key structural lines of Collection 1
    base_lines = [
        (2, 3),  # Euler line {2, 3, 4, 5}
        (1, 2),  # Nagel line {1, 2, 8, 10}
        (3, 6),  # Brocard axis {3, 6, 15, 16}
    ]
    extra_lines = [
        (1, 5),   # Feuerbach line {1, 5, 11, 12}
        (2, 7),   # Gergonne-Mittenpunkt line {2, 7, 9}
        (1, 7),   # Soddy line {1, 7, 8}
        (13, 15), # Fermat-Isodynamic axis
        (2, 6),   # Centroid-Symmedian isogonal pair
    ]
    line_pairs = base_lines + (extra_lines if include_all_lines else [(1, 5), (2, 7)])
    for c1, c2 in line_pairs:
        if c1 in pts_by_num and c2 in pts_by_num:
            _add_line(
                model,
                pts_by_num[c1],
                pts_by_num[c2],
                classes=["central_line", f"line_{c1}_{c2}"],
            )

    # Promote X_1, X_2, X_3, X_4 to top
    for c_num in (4, 3, 2, 1):
        if c_num in pts_by_num:
            t_pt = pts_by_num[c_num]
            if t_pt in model:
                tdata = model.pop(t_pt)
                super(Model, model).__setitem__(t_pt, tdata)

    return model


def generate_collection_1_families_svg(reg: CenterRegistry) -> str:
    """Render Step 3 (`02_families_grid.svg`) showing all 19 centers grouped by their 3 structural families."""
    ctx = reg.ctx
    Ax, Ay = 0.0, 0.0
    Bx, By = 1.0, 0.0
    Cx, Cy = ctx.C_xy

    scale = 470.0
    ox = 500.0 - 0.5 * scale
    oy = 415.0

    def to_svg(x: float, y: float) -> tuple[float, float]:
        return (ox + x * scale, oy - y * scale)

    As = to_svg(Ax, Ay)
    Bs = to_svg(Bx, By)
    Cs = to_svg(Cx, Cy)

    # Draw the 3 master axes as dotted/solid lines
    axes_svg: list[str] = []
    for (c1, c2), col in (((2, 3), "#e8b85a"), ((1, 8), "#38bdf8"), ((3, 15), "#5ec27e")):
        xy1 = reg.xy_cache.get(c1)
        xy2 = reg.xy_cache.get(c2)
        if xy1 and xy2:
            s1 = to_svg(*xy1)
            s2 = to_svg(*xy2)
            dx, dy = s2[0] - s1[0], s2[1] - s1[1]
            L = math.hypot(dx, dy)
            if L > 1e-3:
                ux, uy = dx / L, dy / L
                axes_svg.append(
                    f'<line x1="{s1[0] - 250*ux:.1f}" y1="{s1[1] - 250*uy:.1f}" '
                    f'x2="{s2[0] + 250*ux:.1f}" y2="{s2[1] + 250*uy:.1f}" '
                    f'stroke="{col}" stroke-width="2.5" stroke-dasharray="2, 4.5" stroke-linecap="round" opacity="0.75" />'
                )
                axes_svg.append(
                    f'<line x1="{s1[0]:.1f}" y1="{s1[1]:.1f}" x2="{s2[0]:.1f}" y2="{s2[1]:.1f}" '
                    f'stroke="{col}" stroke-width="3.8" stroke-linecap="round" opacity="0.9" />'
                )

    pts_svg: list[str] = []
    for fam_title, col, nums in COLLECTION_1_FAMILIES:
        for cn in nums:
            xy = reg.xy_cache.get(cn)
            if not xy:
                continue
            sx, sy = to_svg(*xy)
            if sx < 40 or sx > 960 or sy < 20 or sy > 520:
                continue
            r = 8.0 if cn in (1, 2, 3, 4, 5, 6, 7, 8, 11, 13, 15) else 6.2
            pts_svg.append(
                f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{r:.1f}" fill="{col}" stroke="#0b0e15" stroke-width="2.0" />'
            )
            if cn in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19):
                dx_lbl = 10.0 if cn not in (3, 5, 10, 11) else -32.0
                dy_lbl = -8.0 if cn not in (2, 7, 13) else 18.0
                pts_svg.append(
                    f'<text x="{sx + dx_lbl:.1f}" y="{sy + dy_lbl:.1f}" fill="{col}" '
                    f'font-family="JetBrains Mono, monospace" font-size="14" font-weight="bold">'
                    f'X<tspan dy="3" font-size="10.5">{cn}</tspan></text>'
                )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" width="100%" height="100%">
  <defs>
    <filter id="glow-col1" filterUnits="userSpaceOnUse" x="-100" y="-100" width="1200" height="960">
      <feGaussianBlur stdDeviation="3.5" result="blur" />
      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
    </filter>
  </defs>

  <polygon points="{As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="rgba(54, 102, 204, 0.14)" stroke="#3b82f6" stroke-width="4.2" stroke-linejoin="round" />

  {"".join(axes_svg)}
  {"".join(pts_svg)}

  <circle cx="{As[0]:.1f}" cy="{As[1]:.1f}" r="6.5" fill="#66ff66" stroke="#0d111a" stroke-width="2" />
  <circle cx="{Bs[0]:.1f}" cy="{Bs[1]:.1f}" r="6.5" fill="#66ff66" stroke="#0d111a" stroke-width="2" />
  <circle cx="{Cs[0]:.1f}" cy="{Cs[1]:.1f}" r="6.5" fill="#f8f6f0" stroke="#0d111a" stroke-width="2" />
  <text x="{As[0] - 24:.1f}" y="{As[1] + 22:.1f}" fill="#88ff88" font-family="JetBrains Mono, monospace" font-size="20" font-weight="bold">A</text>
  <text x="{Bs[0] + 12:.1f}" y="{Bs[1] + 22:.1f}" fill="#88ff88" font-family="JetBrains Mono, monospace" font-size="20" font-weight="bold">B</text>
  <text x="{Cs[0] - 8:.1f}" y="{Cs[1] - 16:.1f}" fill="#f8f6f0" font-family="JetBrains Mono, monospace" font-size="20" font-weight="bold">C</text>

  <!-- Bottom 3-Family Architecture Card -->
  <g transform="translate(36, 536)">
    <rect x="0" y="0" width="928" height="196" rx="14" fill="rgba(11, 14, 21, 0.95)" stroke="rgba(232, 184, 90, 0.45)" stroke-width="1.5" />
    <text x="24" y="32" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="14" font-weight="bold" letter-spacing="0.8">COLLECTION 1 ARCHITECTURE • X_1 THROUGH X_19</text>
    <text x="904" y="32" text-anchor="end" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="14" font-weight="bold">19 CLASSICAL CENTERS</text>

    <rect x="24" y="50" width="12" height="32" rx="3" fill="#e8b85a" />
    <text x="48" y="65" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="15" font-weight="bold">I. EULER &amp; BROCARD SPINE (X_1 – X_6)</text>
    <text x="48" y="83" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="13">X_1 Incenter • X_2 Centroid • X_3 Circumcenter • X_4 Orthocenter • X_5 Nine-Point • X_6 Symmedian</text>

    <rect x="24" y="98" width="12" height="32" rx="3" fill="#38bdf8" />
    <text x="48" y="113" fill="#38bdf8" font-family="JetBrains Mono, monospace" font-size="15" font-weight="bold">II. CONTACT, PERIMETER &amp; FEUERBACH (X_7 – X_12)</text>
    <text x="48" y="131" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="13">X_7 Gergonne • X_8 Nagel • X_9 Mittenpunkt • X_10 Spieker • X_11 Feuerbach • X_12 Harmonic Conj.</text>

    <rect x="24" y="146" width="12" height="32" rx="3" fill="#5ec27e" />
    <text x="48" y="161" fill="#5ec27e" font-family="JetBrains Mono, monospace" font-size="15" font-weight="bold">III. EQUILATERAL SIX &amp; CLAWSON (X_13 – X_19)</text>
    <text x="48" y="179" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="13">X_13, X_14 Fermat • X_15, X_16 Isodynamic • X_17, X_18 Napoleon • X_19 Clawson Point</text>
  </g>
</svg>"""


def generate_collection_1_four_triangles_svg(
    regs_by_preset: dict[str, tuple[str, TriangleContext, CenterRegistry]],
) -> str:
    """Render Step 7 (`05_four_triangles.svg`) showing all 19 centers across the 4 reference triangles."""
    panels = [
        ("acute", "ACUTE (5, 6, 7)", 30, 24),
        ("right", "RIGHT (3, 4, 5)", 510, 24),
        ("kepler", "KEPLER (1, √φ, φ)", 30, 392),
        ("kimberling", "KIMBERLING (6, 9, 13)", 510, 392),
    ]
    pw, ph = 460, 344
    panel_svgs: list[str] = []

    for key, label, px, py in panels:
        if key not in regs_by_preset:
            continue
        _, ctx, reg = regs_by_preset[key]
        Cx, Cy = ctx.C_xy

        # Compute bounding box including triangle vertices and key interior/near centers
        xs = [0.0, 1.0, Cx]
        ys = [0.0, 0.0, Cy]
        for cn in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17):
            xy = reg.xy_cache.get(cn)
            if xy and -0.8 <= xy[0] <= 1.8 and -0.6 <= xy[1] <= 1.6:
                xs.append(xy[0])
                ys.append(xy[1])

        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        span_x = max(max_x - min_x, 0.4)
        span_y = max(max_y - min_y, 0.4)
        scale = min((pw - 90) / span_x, (ph - 95) / span_y)
        cx_mid = 0.5 * (min_x + max_x)
        cy_mid = 0.5 * (min_y + max_y)

        def to_p(x: float, y: float) -> tuple[float, float]:
            return (
                px + pw * 0.5 + (x - cx_mid) * scale,
                py + ph * 0.54 - (y - cy_mid) * scale,
            )

        As = to_p(0.0, 0.0)
        Bs = to_p(1.0, 0.0)
        Cs = to_p(Cx, Cy)

        elems: list[str] = []
        # Euler & Nagel lines
        for (c1, c2), col in (((2, 3), "#e8b85a"), ((1, 8), "#38bdf8"), ((3, 6), "#5ec27e")):
            xy1 = reg.xy_cache.get(c1)
            xy2 = reg.xy_cache.get(c2)
            if xy1 and xy2:
                s1 = to_p(*xy1)
                s2 = to_p(*xy2)
                elems.append(
                    f'<line x1="{s1[0]:.1f}" y1="{s1[1]:.1f}" x2="{s2[0]:.1f}" y2="{s2[1]:.1f}" '
                    f'stroke="{col}" stroke-width="2.2" stroke-dasharray="2, 4" opacity="0.8" />'
                )

        # Plot all 19 centers inside panel bounds
        for fam_title, col, nums in COLLECTION_1_FAMILIES:
            for cn in nums:
                xy = reg.xy_cache.get(cn)
                if not xy:
                    continue
                sx, sy = to_p(*xy)
                if px + 14 <= sx <= px + pw - 14 and py + 38 <= sy <= py + ph - 14:
                    r = 4.8 if cn in (1, 2, 3, 4, 5, 6, 7, 8, 11, 13, 15) else 3.6
                    elems.append(
                        f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{r:.1f}" fill="{col}" stroke="#0b0e15" stroke-width="1.3" />'
                    )

        panel_svgs.append(f"""
  <g>
    <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="12" fill="rgba(13, 17, 26, 0.92)" stroke="rgba(148, 163, 184, 0.28)" stroke-width="1.5" />
    <text x="{px + 18}" y="{py + 28}" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="14" font-weight="bold">{html.escape(label)}</text>
    <polygon points="{As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="rgba(54, 102, 204, 0.14)" stroke="#3b82f6" stroke-width="3.0" stroke-linejoin="round" />
    {"".join(elems)}
    <circle cx="{As[0]:.1f}" cy="{As[1]:.1f}" r="4.5" fill="#66ff66" />
    <circle cx="{Bs[0]:.1f}" cy="{Bs[1]:.1f}" r="4.5" fill="#66ff66" />
    <circle cx="{Cs[0]:.1f}" cy="{Cs[1]:.1f}" r="4.5" fill="#f8f6f0" />
  </g>""")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" width="100%" height="100%">
  {"".join(panel_svgs)}
</svg>"""


def build_collection_1_intro_package(
    svgs_dir: Path,
    acute_reg: CenterRegistry,
    regs_by_preset: dict[str, tuple[str, TriangleContext, CenterRegistry]],
) -> tuple[str, list[dict]]:
    """Build SVGs, narration script, and 7-subslide scenes.json for the Collection 1 Intro Video."""
    svgs_dir.mkdir(parents=True, exist_ok=True)

    # 1. Constellation SVG (01_constellation.svg)
    m_constellation = build_collection_1_model(acute_reg, include_all_lines=False)
    svg_constellation = render_model_svg(m_constellation)
    (svgs_dir / "01_constellation.svg").write_text(svg_constellation, encoding="utf-8")

    # Also update docsrc/centers/c-00001-00019/c-00001-00019.svg
    col1_doc_svg = Path("docsrc/centers/c-00001-00019/c-00001-00019.svg")
    if col1_doc_svg.parent.is_dir():
        shutil.copy2(svgs_dir / "01_constellation.svg", col1_doc_svg)

    # 2. Families overview SVG (02_families_grid.svg)
    svg_families = generate_collection_1_families_svg(acute_reg)
    (svgs_dir / "02_families_grid.svg").write_text(svg_families, encoding="utf-8")

    # 3. Central lines & relations SVGs (03_central_lines.svg, 04_relations.svg)
    m_lines = build_collection_1_model(acute_reg, include_all_lines=True)
    svg_lines = render_model_svg(m_lines).replace(
        'class="geometor-etc-drawing"',
        'class="geometor-etc-drawing show-lines"',
        1,
    )
    (svgs_dir / "03_central_lines.svg").write_text(svg_lines, encoding="utf-8")
    (svgs_dir / "04_relations.svg").write_text(svg_lines, encoding="utf-8")

    # 4. Four triangles SVG (05_four_triangles.svg)
    svg_four = generate_collection_1_four_triangles_svg(regs_by_preset)
    (svgs_dir / "05_four_triangles.svg").write_text(svg_four, encoding="utf-8")

    script_text = """[bell:proposition]
Welcome to Collection One of the Encyclopedia of Triangle Centers: <pause> the nineteen classical and ancient centers, X one through X nineteen. <pause> Every triangle supports a rich constellation of canonical centers. <pause> It begins with the four ancient centers of Greek geometry: <pause> the Incenter X one, <pause> the Centroid X two, <pause> the Circumcenter X three, <pause> and the Orthocenter X four, <pause> joined by the Nine-Point Center X five on the Euler line <pause> and the Symmedian Point X six on the Brocard axis.

[bell:construction]
Across Collection One, <pause> these nineteen centers organize into three structural families: <pause> first, the Euler and Brocard spine from X one to X six; <pause> second, the Contact, Perimeter, and Feuerbach centers from X seven to X twelve — <pause> where the Gergonne, Nagel, Mittenpunkt, and Spieker points govern tangency and perimeter, <pause> and the Feuerbach pair X eleven and X twelve mark the tangency of the incircle and nine-point circle; <pause> and third, the Equilateral Six and Clawson point from X thirteen to X nineteen. <pause> Three master central lines bind the collection together: <pause> the Euler line through X two, X three, X four, and X five; <pause> the Nagel line through X one, X two, X eight, and X ten; <pause> and the Brocard axis through X three, X six, X fifteen, and X sixteen.

[bell:insight]
Finally, <pause> three transformations — isogonal conjugation, isotomic conjugation, and centroid homothety — <pause> map these centers into one another, <pause> while erected equilateral triangles generate the Fermat points X thirteen and X fourteen, <pause> the Isodynamic points X fifteen and X sixteen, <pause> and the Napoleon points X seventeen and X eighteen, <pause> crowned by the Clawson point X nineteen.
"""

    # Tabular HTML blocks for Steps 1..7
    step12_full_html = (
        '<div class="etc-table-block">'
        '<div class="etc-section"><div class="etc-sec-head">ancient classical four</div>'
        '<div class="etc-data-list">'
        '<div class="etc-data-row"><span class="etc-row-label">Angle Bisectors</span><span class="g-tok">X_1 Incenter • 1 : 1 : 1</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Medians</span><span class="g-tok">X_2 Centroid • 1/a : 1/b : 1/c</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Perp. Bisectors</span><span class="g-tok">X_3 Circumcenter • cos A</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Altitudes</span><span class="g-tok">X_4 Orthocenter • sec A</span></div>'
        '</div></div>'
        '<div class="etc-section"><div class="etc-sec-head">euler &amp; brocard completion</div>'
        '<div class="etc-data-list">'
        '<div class="etc-data-row"><span class="etc-row-label">Nine-Point Circle</span><span class="coincide-tok">X_5 Nine-Point • Mid(X_3, X_4)</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Symmedians</span><span class="eq-tok">X_6 Symmedian • a : b : c</span></div>'
        '</div></div>'
        '</div>'
    )
    step1_html = _mute_other_spans(step12_full_html, {"g-tok"})
    step2_html = step12_full_html

    step3_html = (
        '<div class="etc-table-block">'
        '<div class="etc-section"><div class="etc-sec-head">three families of collection 1</div>'
        '<div class="etc-data-list">'
        '<div class="etc-data-row"><span class="etc-row-label">Euler &amp; Brocard</span><span class="g-tok">X_1 – X_6 • Classical Spine</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Contact &amp; Tangency</span><span class="coincide-tok">X_7 – X_12 • Nagel &amp; Feuerbach</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Equilateral Six</span><span class="eq-tok">X_13 – X_19 • Fermat &amp; Napoleon</span></div>'
        '</div></div>'
        '</div>'
    )

    step45_full_html = (
        '<div class="etc-table-block">'
        '<div class="etc-section"><div class="etc-sec-head">central lines</div>'
        '<div class="etc-data-list">'
        '<div class="etc-data-row"><span class="etc-row-label">Euler Line</span><span class="g-tok">{2, 3, 4, 5}</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Nagel Line</span><span class="coincide-tok">{1, 2, 8, 10}</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Brocard &amp; Feuerbach</span><span class="eq-tok">{3, 6, 15, 16} • {1, 5, 11, 12}</span></div>'
        '</div></div>'
        '</div>'
    )
    step4_html = _mute_other_spans(step45_full_html, {"g-tok"})
    step5_html = step45_full_html

    step6_html = (
        '<div class="etc-table-block">'
        '<div class="etc-section"><div class="etc-sec-head">functional relations</div>'
        '<div class="etc-data-list">'
        '<div class="etc-data-row"><span class="etc-row-label">Isogonal Duality</span><span class="g-tok">X_2 ↔ X_6 • X_3 ↔ X_4 • X_13 ↔ X_15</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Isotomic &amp; Homothety</span><span class="coincide-tok">X_7 ↔ X_8 • X_1 → X_10 → X_8</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Equilateral &amp; Clawson</span><span class="eq-tok">X_13,14 • X_15,16 • X_17,18 • X_19</span></div>'
        '</div></div>'
        '</div>'
    )

    step7_html = (
        '<div class="etc-table-block">'
        '<div class="etc-section"><div class="etc-sec-head">collection 1 summary (x_1–x_19)</div>'
        '<div class="etc-data-list">'
        '<div class="etc-data-row"><span class="etc-row-label">Classical Centers</span><span class="g-tok">X_1 Incenter – X_19 Clawson</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Companion Topics</span><span class="coincide-tok">T_1 – T_24 • Lines &amp; Conjugacies</span></div>'
        '<div class="etc-data-row"><span class="etc-row-label">Exact Verification</span><span class="eq-tok">Acute • Right • Kepler • Kimberling</span></div>'
        '</div></div>'
        '</div>'
    )

    common = {
        "prop_id": "ETC • X_1–X_19",
        "short_code": "X_1–X_19",
        "g_id": "CLASSICAL & ANCIENT CENTERS",
        "folio": "Kimberling ETC • Collection 1 Overview",
        "enunciation": "The nineteen foundational centers of classical triangle geometry: the incenter, centroid, circumcenter, orthocenter, nine-point, symmedian, Gergonne, Nagel, Mittenpunkt, Spieker, Feuerbach, Fermat, isodynamic, Napoleon, and Clawson points.",
        "step_total": 7,
        "visible_ids": ["*"],
    }

    scenes = [
        {
            "id": "act_1_classical_spine",
            "title": "Collection 1 (X_1–X_19) — The Classical Spine",
            "subslides": [
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 1.05,
                    "step_num": 1,
                    "step_kind": "CONSTRUCT",
                    "svg_path": str(svgs_dir / "01_constellation.svg"),
                    "symbolic": "Classical Four: X_1 Incenter • X_2 Centroid • X_3 Circumcenter • X_4 Orthocenter",
                    "clause_html": step1_html,
                    "just_tag": "∵ ANCIENT CANON",
                    "just_id": "CLASSICAL CONCURRENCES • X_1–X_4",
                    "just_title": "Angle bisectors (X_1), medians (X_2), perpendicular bisectors (X_3), and altitudes (X_4).",
                    "strict_step_ids": True,
                    "active_ids": ["X_1", "X_2", "X_3", "X_4", "[ X_2 X_3 ]", "( X_1 T_c )", "( X_3 A )"],
                    "coincide_ids": [],
                    "equal_ids": [],
                },
                {
                    **common,
                    "type": "euclid_step",
                    "is_punchline": True,
                    "weight": 0.95,
                    "step_num": 2,
                    "step_kind": "GOAL",
                    "svg_path": str(svgs_dir / "01_constellation.svg"),
                    "symbolic": "Euler & Brocard Completion: X_5 Nine-Point • X_6 Symmedian Point",
                    "clause_html": step2_html,
                    "just_tag": "∵ EULER & BROCARD",
                    "just_id": "NINE-POINT & SYMMEDIAN • X_5, X_6",
                    "just_title": "X_5 centers the nine-point circle through side midpoints M_a M_b M_c; X_6 is the isogonal conjugate of X_2.",
                    "strict_step_ids": True,
                    "active_ids": ["X_1", "X_2", "X_3", "X_4", "[ X_2 X_3 ]"],
                    "coincide_ids": ["X_5", "( X_5 M_c )", "< M_a M_b M_c >"],
                    "equal_ids": ["X_6", "[ X_3 X_6 ]", "( X_1 T_c )"],
                },
            ],
        },
        {
            "id": "act_2_families_and_lines",
            "title": "Three Structural Families & Master Central Lines",
            "subslides": [
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 1.15,
                    "step_num": 3,
                    "step_kind": "ASSERT",
                    "svg_path": str(svgs_dir / "02_families_grid.svg"),
                    "symbolic": "I: Spine (X_1–X_6) • II: Contact & Feuerbach (X_7–X_12) • III: Equilateral (X_13–X_19)",
                    "clause_html": step3_html,
                    "just_tag": "∵ COLLECTION ARCHITECTURE",
                    "just_id": "THREE STRUCTURAL FAMILIES",
                    "just_title": "19 classical centers organized by metric concurrency, incircle/excircle tangency, and equilateral erection.",
                },
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 0.45,
                    "step_num": 4,
                    "step_kind": "INTERSECT",
                    "svg_path": str(svgs_dir / "03_central_lines.svg"),
                    "symbolic": "Euler {2,3,4,5} • Nagel {1,2,8,10} • Brocard {3,6,15,16}",
                    "clause_html": step4_html,
                    "just_tag": "∵ PRIMARY CENTRAL LINE",
                    "just_id": "EULER LINE • {2, 3, 4, 5}",
                    "just_title": "X_2 : X_5 divide segment X_3 X_4 internally (1:2) and externally in a harmonic range.",
                    "strict_step_ids": True,
                    "active_ids": ["[ X_2 X_3 ]", "X_2", "X_3", "X_4", "X_5"],
                    "coincide_ids": [],
                    "equal_ids": [],
                },
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 0.55,
                    "step_num": 5,
                    "step_kind": "INTERSECT",
                    "svg_path": str(svgs_dir / "03_central_lines.svg"),
                    "symbolic": "Euler {2,3,4,5} • Nagel {1,2,8,10} • Brocard {3,6,15,16}",
                    "clause_html": step5_html,
                    "just_tag": "∵ COLLINEARITIES",
                    "just_id": "NAGEL, BROCARD & FEUERBACH AXES",
                    "just_title": "Nagel line {1,2,8,10}, Brocard axis {3,6,15,16}, and Feuerbach line {1,5,11,12} interlock across △ABC.",
                    "strict_step_ids": True,
                    "active_ids": ["[ X_2 X_3 ]", "X_2", "X_3", "X_4", "X_5"],
                    "coincide_ids": ["[ X_1 X_2 ]", "X_1", "X_8", "X_10"],
                    "equal_ids": ["[ X_3 X_6 ]", "[ X_1 X_5 ]", "X_6", "X_11", "X_12", "X_15"],
                },
            ],
        },
        {
            "id": "act_3_conjugacies_and_invariance",
            "title": "Conjugacies, Equilateral Six & Four-Triangle Invariance",
            "subslides": [
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 1.1,
                    "step_num": 6,
                    "step_kind": "PROVE",
                    "svg_path": str(svgs_dir / "04_relations.svg"),
                    "symbolic": "Isogonal (X_2↔X_6, X_3↔X_4, X_13↔X_15) • Isotomic (X_7↔X_8) • Equilateral (X_13–X_18)",
                    "clause_html": step6_html,
                    "just_tag": "∵ TRANSFORMATIONS",
                    "just_id": "ISOGONAL, ISOTOMIC & HOMOTHETIC WEB",
                    "just_title": "Every center in Collection 1 is connected by reciprocal trilinears, reciprocal barycentrics, or centroid dilation.",
                    "strict_step_ids": True,
                    "active_ids": ["[ X_2 X_6 ]", "[ X_2 X_3 ]", "[ X_13 X_15 ]", "X_2", "X_6", "X_3", "X_4", "X_13", "X_15"],
                    "coincide_ids": ["[ X_1 X_7 ]", "[ X_1 X_2 ]", "X_1", "X_7", "X_8", "X_10"],
                    "equal_ids": ["X_14", "X_17", "X_18", "X_19", "( X_5 M_c )"],
                },
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 0.95,
                    "step_num": 7,
                    "step_kind": "∴",
                    "svg_path": str(svgs_dir / "05_four_triangles.svg"),
                    "symbolic": "19 Centers • 24 Topic Guides • Acute, Right, Kepler & Kimberling Triangles",
                    "clause_html": step7_html,
                    "just_tag": "∵ COLLECTION 1 CANON",
                    "just_id": "X_1 THROUGH X_19 • COMPLETE CONSTELLATION",
                    "just_title": "Explore each individual center video (X_1–X_19) and companion topic guide (T_1–T_24) in the playlist.",
                },
            ],
        },
    ]

    return script_text, scenes


def write_collection_intro_youtube_metadata(
    scenes: list[dict],
    video_dir: Path,
    prefix: str = "C_01",
) -> None:
    """Write `youtube.txt` and `youtube.json` for the Collection 1 Intro Video."""
    title_1080p = "X_1–X_19 • Classical & Ancient Centers • Encyclopedia of Triangle Centers"
    title_short = "X_1–X_19 • Classical & Ancient Centers • Encyclopedia of Triangle Centers"
    enunciation = (
        "The nineteen foundational centers of classical triangle geometry: the incenter, centroid, "
        "circumcenter, orthocenter, nine-point, symmedian, Gergonne, Nagel, Mittenpunkt, Spieker, "
        "Feuerbach, Fermat, isodynamic, Napoleon, and Clawson points."
    )
    web_url = "https://geometor.github.io/etc/centers/c-00001-00019/"

    desc_lines = [
        f"“{enunciation}”",
        "— Clark Kimberling's Encyclopedia of Triangle Centers (ETC) • Collection 1 Overview (X_1–X_19)",
        "",
        f"Interactive GEOMETOR Explorer page: {web_url}",
        "",
        "Three Structural Families of Collection 1:",
        "• I. Euler & Brocard Spine (X_1–X_6): Incenter X_1, Centroid X_2, Circumcenter X_3, Orthocenter X_4, Nine-Point Center X_5, Symmedian Point X_6",
        "• II. Contact, Perimeter & Feuerbach (X_7–X_12): Gergonne X_7, Nagel X_8, Mittenpunkt X_9, Spieker X_10, Feuerbach X_11, Harmonic Conjugate X_12",
        "• III. Equilateral Six & Clawson (X_13–X_19): 1st & 2nd Isogonic (Fermat) X_13–X_14, 1st & 2nd Isodynamic X_15–X_16, 1st & 2nd Napoleon X_17–X_18, Clawson Point X_19",
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
        "GEOMETOR • ETC • Collection 1 (X_1–X_19)",
    ])
    description = "\n".join(desc_lines)
    tags = [
        "X_1",
        "X_19",
        "Classical Triangle Centers",
        "Encyclopedia of Triangle Centers",
        "ETC",
        "Clark Kimberling",
        "Euler Line",
        "Nagel Line",
        "Nine-Point Circle",
        "Triangle Geometry",
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
        "prop_id": "ETC • X_1–X_19",
        "short_code": "C_01",
        "g_id": "CLASSICAL & ANCIENT CENTERS",
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


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Collection 1 (X_1–X_19) Intro Video.")
    parser.add_argument("--prep-only", action="store_true", help="Only write SVGs, script.txt, and scenes.json.")
    parser.add_argument("--tts-only", action="store_true", help="Prepare SVGs/scripts and run TTS only.")
    parser.add_argument("--render-only", action="store_true", help="Render MP4s from existing C_01.json.")
    args = parser.parse_args()

    prefix = "C_01"
    video_dir = Path("resources/videos/intro-collection-1").resolve()
    svgs_dir = video_dir / "svgs"
    svgs_dir.mkdir(parents=True, exist_ok=True)
    script_txt = video_dir / "script.txt"
    scenes_json = video_dir / "scenes.json"
    wav_path = video_dir / f"{prefix}.wav"
    manifest_json = video_dir / f"{prefix}.json"

    if not args.render_only:
        centers: list[dict] = []
        split_dir = Path("resources/split")
        for k in range(1, 390):
            p = split_dir / f"x-{k:05d}.html"
            if p.is_file():
                c_data = parse_center(p.read_text(encoding="utf-8"))
                if c_data:
                    centers.append(c_data)

        regs_by_preset: dict[str, tuple[str, TriangleContext, CenterRegistry]] = {}
        for preset_key, sides in TRIANGLE_PRESETS.items():
            ctx = TriangleContext(*sides)
            reg = CenterRegistry(centers, ctx)
            regs_by_preset[preset_key] = (preset_key, ctx, reg)

        acute_reg = regs_by_preset["acute"][2]
        script_text, scenes = build_collection_1_intro_package(
            svgs_dir=svgs_dir,
            acute_reg=acute_reg,
            regs_by_preset=regs_by_preset,
        )
        script_txt.write_text(script_text, encoding="utf-8")
        scenes_json.write_text(
            json.dumps(scenes, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        write_collection_intro_youtube_metadata(scenes, video_dir, prefix=prefix)
        print(f"[PREP] {prefix}: X_1–X_19 Collection 1 Intro -> {video_dir}")

    if args.prep_only:
        return

    if not args.render_only:
        print(f"  [TTS] Synthesizing Argon III-C narration for {prefix} -> {wav_path.name}")
        subprocess.run(
            [sys.executable, str(SPEAK_PY), "-f", str(script_txt), "-o", str(wav_path)],
            check=True,
        )

    if args.tts_only:
        return

    if not manifest_json.is_file():
        raise FileNotFoundError(f"Missing {manifest_json}")

    for stale_png in video_dir.glob(f"{prefix}_*.png"):
        stale_png.unlink()
    for sub_dir in ("slides_16x9", "slides_9x16"):
        sd = video_dir / sub_dir
        if sd.is_dir():
            for stale_png in sd.glob("*.png"):
                stale_png.unlink()

    shorts_mod = _load_patched_shorts_module()
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

    write_collection_intro_youtube_metadata(scenes_loaded, video_dir, prefix=prefix)
    print(f"  [DONE] Rendered Collection 1 Intro in {video_dir}")


if __name__ == "__main__":
    main()

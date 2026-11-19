"""SVG optimization utilities for GEOMETOR ETC web delivery and thumbnail generation.

Provides exact analytical Liang-Barsky viewport line clipping and asset stripping so:

1. Infinite dashed lines span ~2.5x the viewBox (~250 dashes) instead of 1,500x (~165k dashes).
2. Web-injected viewer SVGs strip duplicate per-SVG ``<style>`` and ``<script>`` blocks while keeping
   pure SVG geometry, ``data-line`` vectors for infinite pan/zoom, and ``.etc-elements-meta``.
3. Collection thumbnail SVGs (loaded in ``<img loading="lazy">``) strip all scripts and JSON
   metadata and keep only a compact ~1.3 KB visual-only ``<style>`` block.
"""

from __future__ import annotations

import math
import re

_STYLE_BLOCK_RE = re.compile(r"\s*<style\b[^>]*>.*?</style>", flags=re.DOTALL | re.IGNORECASE)
_META_SCRIPT_RE = re.compile(
    r'(<script\b[^>]*class="[^"]*etc-elements-meta[^"]*"[^>]*>.*?</script>)',
    flags=re.DOTALL | re.IGNORECASE,
)
_ANY_SCRIPT_RE = re.compile(r"\s*<script\b[^>]*>.*?</script>", flags=re.DOTALL | re.IGNORECASE)
_XML_DECL_RE = re.compile(r"^<\?xml[^>]*\?>\s*", flags=re.IGNORECASE)
_VIEWBOX_RE = re.compile(r'\bviewBox="([^"]+)"')
_LINE_TAG_RE = re.compile(r"<line\b[^>]*>", flags=re.DOTALL)
_ATTR_NUM_RE = {
    k: re.compile(rf'\b{k}="([+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)"')
    for k in ("x1", "y1", "x2", "y2")
}
_INCIDENT_PT_RE = re.compile(
    r'<circle\b[^>]*class="[^"]*\bincident\b[^"]*"[^>]*\bcx="([^"]+)"[^>]*\bcy="([^"]+)"',
    flags=re.DOTALL,
)
_PRIMARY_PT_RE = re.compile(
    r'<circle\b[^>]*class="[^"]*\b(?:vertex|target|selected)\b[^"]*"[^>]*\bcx="([^"]+)"[^>]*\bcy="([^"]+)"',
    flags=re.DOTALL,
)

# Compact visual-only CSS for standalone <img src="...svg"> thumbnails (no toolbar/HUD/tabs/hover)
THUMBNAIL_SVG_CSS = (
    "svg.geometor-etc-drawing{background:#161616;display:block;}"
    "svg.geometor-etc-drawing:not(.show-lines) .incident{display:none!important;}"
    "#points circle{fill:#e0e0e0;stroke:#161616;stroke-width:2.5;vector-effect:non-scaling-stroke;}"
    "#points circle.given{fill:#6F6;}"
    "#points circle.guide{fill:orange;}"
    "#points circle.selected,#points circle.target{fill:#161616;stroke:#e8b85a;stroke-width:2.8;}"
    "#elements line,#elements path.line{fill:none;stroke:#b0bec5;stroke-width:2.2;"
    "stroke-dasharray:2,4.5;stroke-linecap:round;vector-effect:non-scaling-stroke;}"
    "#elements line.sideline{stroke:#cbd5e1;stroke-width:2.3;}"
    "#elements line.central_line{stroke:#0bd;stroke-width:1.85;stroke-opacity:.85;}"
    "#elements line.golden,#elements line.euler{stroke:gold;stroke-width:2.1;}"
    "#elements circle{fill:none;stroke:#C09;stroke-width:2;vector-effect:non-scaling-stroke;}"
    "#elements circle.incircle{stroke:#e040fb;}"
    "#elements circle.nine_point_circle{stroke:#00e5ff;stroke-dasharray:6,3;}"
    "#elements .guide{stroke:orange;stroke-dasharray:2,4;stroke-opacity:.65;}"
    "#graphics polygon{stroke:#36c9;fill:#36c2;stroke-width:6;vector-effect:non-scaling-stroke;stroke-linejoin:round;}"
    "#graphics polygon.secondary{stroke:rgba(144,238,144,.55);fill:rgba(144,238,144,.08);stroke-width:3;}"
    "#labels text{fill:#e0e0e0;font-family:monospace;font-weight:600;paint-order:stroke;"
    "stroke:#161616;stroke-width:.15em;stroke-linejoin:round;}"
    "#labels text.target-label{fill:gold;font-weight:700;}"
    "#labels text.given-label{fill:#8f8;}"
    "#labels text.guide-label{fill:#ffb74d;}"
    "#labels text.dense-label{display:none;}"
)


def clip_infinite_line_to_rect(
    x0: float,
    y0: float,
    ux: float,
    uy: float,
    xmin: float,
    ymin: float,
    xmax: float,
    ymax: float,
) -> tuple[float, float, float, float] | None:
    """Intersect infinite line P(t) = (x0, y0) + t*(ux, uy) with [xmin, xmax] x [ymin, ymax]."""
    t_min = -math.inf
    t_max = math.inf
    eps = 1e-12

    if abs(ux) < eps:
        if x0 < xmin or x0 > xmax:
            return None
    else:
        t1 = (xmin - x0) / ux
        t2 = (xmax - x0) / ux
        if t1 > t2:
            t1, t2 = t2, t1
        t_min = max(t_min, t1)
        t_max = min(t_max, t2)

    if abs(uy) < eps:
        if y0 < ymin or y0 > ymax:
            return None
    else:
        t1 = (ymin - y0) / uy
        t2 = (ymax - y0) / uy
        if t1 > t2:
            t1, t2 = t2, t1
        t_min = max(t_min, t1)
        t_max = min(t_max, t2)

    if t_min > t_max or not (math.isfinite(t_min) and math.isfinite(t_max)):
        return None
    return (x0 + t_min * ux, y0 + t_min * uy, x0 + t_max * ux, y0 + t_max * uy)


def clip_svg_lines(svg_text: str, margin_factor: float = 0.75) -> str:
    """Clip oversized infinite <line> elements to a tight box around the SVG viewBox.

    Also injects ``data-line="x0,y0,ux,uy"`` so ``etc-viewer.js`` can dynamically
    re-clip infinite lines seamlessly during interactive pan and zoom.
    """
    m_vb = _VIEWBOX_RE.search(svg_text)
    if not m_vb:
        return svg_text
    vb_parts = m_vb.group(1).strip().split()
    if len(vb_parts) != 4:
        return svg_text
    try:
        vbx, vby, vbw, vbh = (float(p) for p in vb_parts)
    except ValueError:
        return svg_text
    if vbw <= 0 or vbh <= 0:
        return svg_text

    pad_x = vbw * margin_factor
    pad_y = vbh * margin_factor
    xmin, ymin = vbx - pad_x, vby - pad_y
    xmax, ymax = vbx + vbw + pad_x, vby + vbh + pad_y
    max_unclipped = max(vbw, vbh) * 3.0

    def _clip_line_tag(match: re.Match[str]) -> str:
        tag = match.group(0)
        vals: dict[str, float] = {}
        for k, rx in _ATTR_NUM_RE.items():
            mk = rx.search(tag)
            if not mk:
                return tag
            vals[k] = float(mk.group(1))
        dx = vals["x2"] - vals["x1"]
        dy = vals["y2"] - vals["y1"]
        length = math.hypot(dx, dy)
        if length <= max_unclipped or length < 1e-12:
            return tag

        ux = dx / length
        uy = dy / length
        mx = 0.5 * (vals["x1"] + vals["x2"])
        my = 0.5 * (vals["y1"] + vals["y2"])

        clipped = clip_infinite_line_to_rect(mx, my, ux, uy, xmin, ymin, xmax, ymax)
        if clipped is None:
            # Line lies outside default box; keep a modest 4x span centered at (mx, my)
            half = max(vbw, vbh) * 2.0
            cx1, cy1 = mx - half * ux, my - half * uy
            cx2, cy2 = mx + half * ux, my + half * uy
        else:
            cx1, cy1, cx2, cy2 = clipped

        new_tag = _ATTR_NUM_RE["x1"].sub(f'x1="{cx1:.5f}"', tag, count=1)
        new_tag = _ATTR_NUM_RE["y1"].sub(f'y1="{cy1:.5f}"', new_tag, count=1)
        new_tag = _ATTR_NUM_RE["x2"].sub(f'x2="{cx2:.5f}"', new_tag, count=1)
        new_tag = _ATTR_NUM_RE["y2"].sub(f'y2="{cy2:.5f}"', new_tag, count=1)
        if 'data-line="' not in new_tag:
            dl_attr = f' data-line="{mx:.6f},{my:.6f},{ux:.8f},{uy:.8f}"'
            if new_tag.endswith("/>"):
                new_tag = new_tag[:-2] + dl_attr + "/>"
            else:
                new_tag = new_tag[:-1] + dl_attr + ">"
        return new_tag

    return _LINE_TAG_RE.sub(_clip_line_tag, svg_text)


def inject_lines_viewbox(svg_text: str, lines_vb: str | None = None) -> str:
    """Attach ``data-lines-viewbox`` to the root ``<svg>`` for zero-fetch Central Lines mode."""
    if 'data-lines-viewbox="' in svg_text:
        return svg_text
    if lines_vb is None:
        # Derive a framed viewBox encompassing both primary and nearby incident points
        m_vb = _VIEWBOX_RE.search(svg_text)
        if not m_vb:
            return svg_text
        try:
            vbx, vby, vbw, vbh = (float(p) for p in m_vb.group(1).strip().split())
        except ValueError:
            return svg_text
        inc_pts = [(float(m.group(1)), float(m.group(2))) for m in _INCIDENT_PT_RE.finditer(svg_text)]
        if not inc_pts:
            return svg_text
        prim_pts = [(float(m.group(1)), float(m.group(2))) for m in _PRIMARY_PT_RE.finditer(svg_text)]
        cx = vbx + vbw * 0.5
        cy = vby + vbh * 0.5
        span = max(vbw, vbh)
        min_x, max_x = vbx + vbw * 0.1, vbx + vbw * 0.9
        min_y, max_y = vby + vbh * 0.1, vby + vbh * 0.9
        for px, py in prim_pts + inc_pts:
            if abs(px - cx) <= 2.4 * span and abs(py - cy) <= 2.4 * span:
                min_x = min(min_x, px)
                max_x = max(max_x, px)
                min_y = min(min_y, py)
                max_y = max(max_y, py)
        w = max(max_x - min_x, vbw * 0.6) * 1.22
        h = max(max_y - min_y, vbh * 0.6) * 1.22
        aspect = vbw / vbh if vbh > 0 else 4.0 / 3.0
        if w / h > aspect:
            h = w / aspect
        else:
            w = h * aspect
        ncx = 0.5 * (min_x + max_x)
        ncy = 0.5 * (min_y + max_y)
        lines_vb = f"{ncx - w * 0.5:.6f} {ncy - h * 0.5:.6f} {w:.6f} {h:.6f}"

    return re.sub(
        r"(<svg\b[^>]*)(>)",
        rf'\1 data-lines-viewbox="{lines_vb}"\2',
        svg_text,
        count=1,
    )


_GLOW_FILTER_DEF_RE = re.compile(
    r'\s*<filter\b[^>]*id="glow-coord"[^>]*>.*?</filter>',
    flags=re.DOTALL | re.IGNORECASE,
)
_GLOW_FILTER_ATTR_RE = re.compile(r'\s+filter="url\(#glow-coord\)"', flags=re.IGNORECASE)
_POINTS_GROUP_RE = re.compile(r'(<g\b[^>]*\bid="points"[^>]*>)(.*?)(</g>)', flags=re.DOTALL)
_R_ATTR_RE = re.compile(r'\br="[^"]*"')
_TARGET_R_PX_RE = re.compile(r'\bdata-target-r-px="[^"]*"')
_PLATE_HALO_RE = re.compile(
    r'\s*<circle\b[^>]*\br="16\.5"[^>]*pointer-events="none"\s*/>',
    flags=re.DOTALL,
)
_PLATE_PT_TAG_RE = re.compile(r'<circle\b[^>]*\bclass="[^"]*\betc-plate-pt\b[^"]*"[^>]*/>', flags=re.DOTALL)


def normalize_svg_points(svg_text: str, point_r_px: float = 4.8) -> str:
    """Normalize all point dots to a uniform compact radius and Explorer selected styling.

    Applies both to Explorer-rendered ``#points`` groups and static coordinate/4-triangle
    ``.etc-plate-pt`` SVGs so existing on-disk SVGs stay visually consistent without re-rendering.
    """
    m_vb = _VIEWBOX_RE.search(svg_text)
    if not m_vb:
        return svg_text
    vb_parts = m_vb.group(1).strip().split()
    if len(vb_parts) != 4:
        return svg_text
    try:
        vbw = float(vb_parts[2])
    except ValueError:
        return svg_text
    if vbw <= 0:
        return svg_text

    uniform_r = point_r_px * (vbw / 800.0)
    out = _TARGET_R_PX_RE.sub(f'data-target-r-px="{point_r_px:g}"', svg_text)

    def _norm_points_group(m: re.Match[str]) -> str:
        inner = _R_ATTR_RE.sub(f'r="{uniform_r:.6f}"', m.group(2))
        return f"{m.group(1)}{inner}{m.group(3)}"

    out = _POINTS_GROUP_RE.sub(_norm_points_group, out)

    if "etc-plate-pt" in out:
        out = _PLATE_HALO_RE.sub("", out)
        plate_r = 5.6 if vbw >= 950 and "etc-plate-panel" not in out else 4.5

        def _norm_plate_pt(m: re.Match[str]) -> str:
            tag = _R_ATTR_RE.sub(f'r="{plate_r:.1f}"', m.group(0))
            if re.search(r'\bid="(?:[a-z]+-)?X_\d+"', tag):
                if "target" not in tag:
                    tag = tag.replace('class="etc-plate-pt"', 'class="etc-plate-pt target"')
                tag = re.sub(r'\bfill="[^"]*"', 'fill="#161616"', tag)
                tag = re.sub(r'\bstroke="[^"]*"', 'stroke="#e8b85a"', tag)
                if 'stroke-width="' in tag:
                    tag = re.sub(r'\bstroke-width="[^"]*"', 'stroke-width="2.8"', tag)
                else:
                    tag = tag.replace("/>", ' stroke-width="2.8" />')
            return tag

        out = _PLATE_PT_TAG_RE.sub(_norm_plate_pt, out)

    return out


def strip_svg_for_viewer(svg_text: str, lines_vb: str | None = None) -> str:
    """Prepare a lightweight pure-geometry + metadata SVG for injection into ``.etc-viewer``.

    Strips XML declaration, duplicate ``<style>`` blocks, duplicate ``<script>`` controllers,
    and expensive Gaussian blur filters while preserving ``.etc-elements-meta``, normalizing
    point radii uniformly, and clipping infinite dashed lines to 2.5x viewBox with ``data-line``.
    """
    cleaned = _XML_DECL_RE.sub("", svg_text.strip())
    meta_blocks = _META_SCRIPT_RE.findall(cleaned)
    cleaned = _STYLE_BLOCK_RE.sub("", cleaned)
    cleaned = _ANY_SCRIPT_RE.sub("", cleaned)
    cleaned = _GLOW_FILTER_DEF_RE.sub("", cleaned)
    cleaned = _GLOW_FILTER_ATTR_RE.sub("", cleaned)
    if meta_blocks:
        meta_joined = "\n  ".join(meta_blocks)
        cleaned = re.sub(
            r"</svg>\s*$",
            lambda _: f"  {meta_joined}\n</svg>",
            cleaned,
            count=1,
        )
    cleaned = clip_svg_lines(cleaned, margin_factor=0.75)
    cleaned = normalize_svg_points(cleaned, point_r_px=4.8)
    cleaned = inject_lines_viewbox(cleaned, lines_vb=lines_vb)
    return cleaned


def strip_svg_for_thumbnail(svg_text: str) -> str:
    """Prepare a compact standalone SVG for ``<img loading="lazy">`` collection thumbnails.

    Strips all ``<script>`` blocks (including ``etc-elements-meta`` JSON, which ``<img>`` cannot
    use), replaces the 12.5 KB interactive stylesheet with a ~1.3 KB static visual stylesheet,
    normalizes point sizes uniformly, and clips oversized infinite dashed lines.
    """
    cleaned = _XML_DECL_RE.sub("", svg_text.strip())
    cleaned = _ANY_SCRIPT_RE.sub("", cleaned)
    cleaned = _STYLE_BLOCK_RE.sub("", cleaned)
    cleaned = _GLOW_FILTER_DEF_RE.sub("", cleaned)
    cleaned = _GLOW_FILTER_ATTR_RE.sub("", cleaned)
    cleaned = re.sub(
        r"(<svg\b[^>]*>)",
        lambda m: f"{m.group(1)}\n  <style>{THUMBNAIL_SVG_CSS}</style>",
        cleaned,
        count=1,
    )
    cleaned = clip_svg_lines(cleaned, margin_factor=0.35)
    cleaned = normalize_svg_points(cleaned, point_r_px=4.8)
    return '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + cleaned

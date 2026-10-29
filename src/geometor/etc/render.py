"""Render `geometor.model.Model` instances into standalone SVGs following `geometor.explorer` conventions."""

from __future__ import annotations

import html
import math
from pathlib import Path
from typing import Any

import sympy.geometry as spg
from geometor.model import Model
from geometor.model.element import CircleElement


EXPLORER_SVG_CSS = """
:root {
    --background-color: #121212;
    --text-color: #e0e0e0;
    --accent-color: #161616;
    --border-color: #333;
    --select-color: #0ff;
}

#drawing {
    width: 100%;
    height: auto;
    max-height: 520px;
    background-color: var(--accent-color);
    border: 1px solid var(--border-color);
    border-radius: 4px;
    display: block;
}

#points circle {
    fill: var(--text-color);
    stroke: var(--background-color);
    stroke-width: 2.5;
    vector-effect: non-scaling-stroke;
}

#points circle.given {
    fill: #6F6;
}

#points circle.guide {
    fill: orange;
    stroke-dasharray: none;
}

#points circle.selected,
#points circle.target {
    stroke: var(--select-color);
    fill: gold;
    stroke-width: 3;
}

#elements line {
    fill: none;
    stroke: #777;
    stroke-width: 1.5;
    vector-effect: non-scaling-stroke;
}

#elements line.sideline {
    stroke: #999;
    stroke-width: 2;
}

#elements line.central_line {
    stroke: #0bd;
    stroke-width: 1.75;
    stroke-opacity: 0.85;
}

#elements line.golden,
#elements line.euler {
    stroke: gold;
    stroke-width: 2;
}

#elements circle {
    fill: none;
    stroke: #C09;
    stroke-width: 2;
    vector-effect: non-scaling-stroke;
}

#elements circle.incircle {
    stroke: #e040fb;
}

#elements circle.nine_point_circle {
    stroke: #00e5ff;
    stroke-dasharray: 6, 3;
}

#elements .bisector {
    stroke-dasharray: 8, 4, 2, 4;
}

#elements .guide {
    stroke: orange;
    stroke-dasharray: 2, 4;
    stroke-opacity: 0.65;
}

#graphics polyline {
    stroke: #36c9;
    fill: none;
    stroke-width: 6;
    vector-effect: non-scaling-stroke;
}

#graphics polygon {
    stroke: #36c9;
    fill: #36c2;
    stroke-width: 6;
    vector-effect: non-scaling-stroke;
    stroke-linejoin: round;
    marker-start: url(#marker);
    marker-mid: url(#marker);
    marker-end: url(#marker);
}

#graphics polygon.secondary {
    stroke: rgba(144, 238, 144, 0.55);
    fill: rgba(144, 238, 144, 0.08);
    stroke-width: 3;
}

#labels text {
    fill: var(--text-color);
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-weight: 600;
    paint-order: stroke;
    stroke: var(--accent-color);
    stroke-width: 3px;
    stroke-linecap: round;
    stroke-linejoin: round;
    vector-effect: non-scaling-stroke;
    user-select: none;
}

#labels text.target-label {
    fill: gold;
    font-weight: 700;
}

#labels text.given-label {
    fill: #8f8;
}
"""


def model_to_elements_list(model: Model) -> list[dict[str, Any]]:
    """Convert a `geometor.model.Model` into a chronological list of browser-ready element dicts."""
    elements: list[dict[str, Any]] = []
    for el, data in model.items():
        if not data.ID:
            continue
        base: dict[str, Any] = {
            "ID": data.ID,
            "classes": list(data.classes.keys()) if isinstance(data.classes, dict) else list(data.classes),
            "guide": bool(data.guide),
        }
        if isinstance(el, spg.Point):
            base.update(
                {
                    "type": "point",
                    "x": float(el.x.evalf()),
                    "y": float(el.y.evalf()),
                }
            )
        elif isinstance(el, spg.Line):
            base.update(
                {
                    "type": "line",
                    "pt1": model[el.p1].ID,
                    "pt2": model[el.p2].ID,
                }
            )
        elif isinstance(el, spg.Circle):
            pt_rad_id = (
                model[data.pt_radius].ID
                if isinstance(data, CircleElement) and data.pt_radius in model
                else ""
            )
            base.update(
                {
                    "type": "circle",
                    "center": model[el.center].ID,
                    "radius_pt": pt_rad_id,
                    "radius": float(el.radius.evalf()),
                }
            )
        elif isinstance(el, spg.Polygon):
            base.update(
                {
                    "type": "polygon",
                    "points": [model[p].ID for p in el.vertices],
                }
            )
        elif isinstance(el, spg.Segment):
            base.update(
                {
                    "type": "segment",
                    "points": [model[el.p1].ID, model[el.p2].ID],
                }
            )
        else:
            continue
        elements.append(base)
    return elements


def render_model_svg(
    model: Model,
    svg_width: int = 800,
    svg_height: int = 600,
    show_labels: bool = True,
    subtitle: str = "",
) -> str:
    """Render a `geometor.model.Model` to an Explorer-compatible SVG string."""
    elements = model_to_elements_list(model)
    points_by_id: dict[str, dict[str, Any]] = {
        el["ID"]: el for el in elements if el["type"] == "point"
    }

    # Compute bounding box following explorer's `fitConstruction()` in `svg.js`
    min_x, max_x = float("inf"), float("-inf")
    min_y, max_y = float("inf"), float("-inf")

    for p in points_by_id.values():
        if p["guide"]:
            continue
        # Guard against extreme far-out points dwarfing the reference triangle
        if abs(p["x"]) <= 4.5 and abs(p["y"]) <= 4.5:
            min_x = min(min_x, p["x"])
            max_x = max(max_x, p["x"])
            min_y = min(min_y, p["y"])
            max_y = max(max_y, p["y"])

    for c in elements:
        if c["type"] == "circle" and not c["guide"]:
            ctr = points_by_id.get(c["center"])
            r = c["radius"]
            if ctr and r <= 3.5:
                min_x = min(min_x, ctr["x"] - r)
                max_x = max(max_x, ctr["x"] + r)
                min_y = min(min_y, ctr["y"] - r)
                max_y = max(max_y, ctr["y"] + r)

    if not math.isfinite(min_x):
        min_x, max_x, min_y, max_y = -0.5, 1.5, -0.5, 1.2

    width = max(max_x - min_x, 0.4)
    height = max(max_y - min_y, 0.4)
    padding = 0.22
    padded_width = width * (1.0 + padding)
    padded_height = height * (1.0 + padding)
    center_x = min_x + width / 2.0
    center_y = min_y + height / 2.0

    svg_aspect = svg_width / svg_height
    constr_aspect = padded_width / padded_height

    if svg_aspect > constr_aspect:
        vb_height = padded_height
        vb_width = padded_height * svg_aspect
    else:
        vb_width = padded_width
        vb_height = padded_width / svg_aspect

    vb_x = center_x - vb_width / 2.0
    vb_y = -center_y - vb_height / 2.0

    # Point radius scaled like `scaleCircles()` in `explorer/static/js/svg.js`
    units_per_px = vb_width / svg_width
    pt_radius = 5.0 * units_per_px
    target_radius = 7.0 * units_per_px
    guide_radius = 3.2 * units_per_px
    font_size = 13.5 * units_per_px

    graphics_nodes: list[str] = []
    highlights_nodes: list[str] = []
    elements_nodes: list[str] = []
    points_nodes: list[str] = []
    labels_nodes: list[str] = []

    for el in elements:
        el_id = html.escape(el["ID"], quote=True)
        classes = [el["type"]] + el["classes"]
        if el["guide"] and "guide" not in classes:
            classes.append("guide")
        class_attr = html.escape(" ".join(classes), quote=True)

        if el["type"] == "polygon":
            pts_str = " ".join(
                f"{points_by_id[pid]['x']:.6f},{-points_by_id[pid]['y']:.6f}"
                for pid in el["points"]
                if pid in points_by_id
            )
            graphics_nodes.append(
                f'    <polygon id="{el_id}" class="{class_attr}" data-category="graphics" points="{pts_str}" />'
            )

        elif el["type"] in {"segment", "section", "chain"}:
            pts_str = " ".join(
                f"{points_by_id[pid]['x']:.6f},{-points_by_id[pid]['y']:.6f}"
                for pid in el["points"]
                if pid in points_by_id
            )
            graphics_nodes.append(
                f'    <polyline id="{el_id}" class="{class_attr}" data-category="graphics" points="{pts_str}" />'
            )

        elif el["type"] == "line":
            p1 = points_by_id.get(el["pt1"])
            p2 = points_by_id.get(el["pt2"])
            if p1 and p2:
                dx = p2["x"] - p1["x"]
                dy = p2["y"] - p1["y"]
                x1 = p1["x"] - 1000.0 * dx
                y1 = -(p1["y"] - 1000.0 * dy)
                x2 = p1["x"] + 1000.0 * dx
                y2 = -(p1["y"] + 1000.0 * dy)
                elements_nodes.append(
                    f'    <line id="{el_id}" class="{class_attr}" data-category="elements" '
                    f'x1="{x1:.5f}" y1="{y1:.5f}" x2="{x2:.5f}" y2="{y2:.5f}" />'
                )
                highlights_nodes.append(
                    f'    <polyline id="highlight-{el_id}" class="highlight-segment" '
                    f'points="{p1["x"]:.6f},{-p1["y"]:.6f} {p2["x"]:.6f},{-p2["y"]:.6f}" style="display: none;" />'
                )

        elif el["type"] == "circle":
            ctr = points_by_id.get(el["center"])
            if ctr:
                cx = ctr["x"]
                cy = -ctr["y"]
                r = el["radius"]
                elements_nodes.append(
                    f'    <circle id="{el_id}" class="{class_attr}" data-category="elements" '
                    f'cx="{cx:.6f}" cy="{cy:.6f}" r="{r:.6f}" fill="none" />'
                )

        elif el["type"] == "point":
            cx = el["x"]
            cy = -el["y"]
            is_target = "target" in el["classes"] or "selected" in el["classes"]
            r = target_radius if is_target else (guide_radius if el["guide"] else pt_radius)
            points_nodes.append(
                f'    <circle id="{el_id}" class="{class_attr}" data-category="points" '
                f'cx="{cx:.6f}" cy="{cy:.6f}" r="{r:.6f}">'
                f"<title>{el_id} ({cx:.4f}, {el['y']:.4f})</title></circle>"
            )

            # Label vertices A, B, C and centers X(k)
            if show_labels and not el["guide"]:
                lbl_cls = (
                    "target-label"
                    if is_target
                    else ("given-label" if "given" in el["classes"] else "point-label")
                )
                offset_x = 8.0 * units_per_px
                offset_y = -7.0 * units_per_px
                if el["ID"] == "A":
                    offset_x = -16.0 * units_per_px
                    offset_y = 15.0 * units_per_px
                elif el["ID"] == "B":
                    offset_x = 8.0 * units_per_px
                    offset_y = 15.0 * units_per_px
                elif el["ID"] == "C":
                    offset_x = -5.0 * units_per_px
                    offset_y = -10.0 * units_per_px
                labels_nodes.append(
                    f'    <text class="{lbl_cls}" x="{cx + offset_x:.6f}" y="{cy + offset_y:.6f}" '
                    f'font-size="{font_size:.6f}">{el_id}</text>'
                )

    if subtitle:
        sub_x = vb_x + 14.0 * units_per_px
        sub_y = vb_y + vb_height - 12.0 * units_per_px
        sub_font = 11.5 * units_per_px
        labels_nodes.append(
            f'    <text class="point-label" x="{sub_x:.6f}" y="{sub_y:.6f}" '
            f'font-size="{sub_font:.6f}" fill="#999">{html.escape(subtitle)}</text>'
        )

    svg_lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        f'<svg id="drawing" xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="{vb_x:.6f} {vb_y:.6f} {vb_width:.6f} {vb_height:.6f}" '
        f'preserveAspectRatio="xMidYMid meet">',
        f"  <style>{EXPLORER_SVG_CSS}</style>",
        "  <defs>",
        '    <marker id="marker" viewBox="0 0 6 6" refX="3" refY="3" markerWidth="3" markerHeight="3" orient="auto-start-reverse">',
        '      <circle cx="3" cy="3" r="3" fill="context-stroke" vector-effect="non-scaling-stroke"></circle>',
        "    </marker>",
        "  </defs>",
        '  <g id="graphics">',
        *graphics_nodes,
        "  </g>",
        '  <g id="highlights">',
        *highlights_nodes,
        "  </g>",
        '  <g id="elements">',
        *elements_nodes,
        "  </g>",
        '  <g id="points">',
        *points_nodes,
        "  </g>",
        '  <g id="labels">',
        *labels_nodes,
        "  </g>",
        "</svg>",
        "",
    ]
    return "\n".join(svg_lines)


def write_center_svg(
    model: Model,
    output_path: str | Path,
    subtitle: str = "",
) -> Path:
    """Render and write a center's `Model` SVG to `output_path`."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    svg_content = render_model_svg(model, subtitle=subtitle)
    path.write_text(svg_content, encoding="utf-8")
    return path

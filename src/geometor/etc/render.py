"""Render `geometor.model.Model` instances into interactive Explorer-styled SVGs."""

from __future__ import annotations

import functools
import html
import json
import math
import re
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

svg.geometor-etc-drawing {
    width: 100%;
    height: auto;
    max-height: 540px;
    background-color: var(--accent-color);
    border: 1px solid var(--border-color);
    border-radius: 4px;
    display: block;
    user-select: none;
    touch-action: none;
    cursor: grab;
}

svg.geometor-etc-drawing.is-panning {
    cursor: grabbing;
}

svg.geometor-etc-drawing.hide-labels #labels .point-label,
svg.geometor-etc-drawing.hide-labels #labels .target-label,
svg.geometor-etc-drawing.hide-labels #labels .given-label {
    display: none;
}

svg.geometor-etc-drawing.hide-guides .guide {
    display: none !important;
}

#points circle {
    fill: var(--text-color);
    stroke: var(--background-color);
    stroke-width: 2.5;
    vector-effect: non-scaling-stroke;
    cursor: pointer;
    transition: fill 0.12s ease, stroke 0.12s ease;
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

#points circle:hover,
#points circle.hover {
    fill: var(--select-color) !important;
    stroke: #fff !important;
    stroke-width: 3.5 !important;
}

#elements line {
    fill: none;
    stroke: #777;
    stroke-width: 1.5;
    vector-effect: non-scaling-stroke;
    cursor: pointer;
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
    cursor: pointer;
}

#elements circle.incircle {
    stroke: #e040fb;
}

#elements circle.nine_point_circle {
    stroke: #00e5ff;
    stroke-dasharray: 6, 3;
}

#elements circle.secondary_circle {
    stroke: #ff9100;
    stroke-dasharray: 5, 3;
    stroke-opacity: 0.85;
}

#elements .bisector {
    stroke-dasharray: 8, 4, 2, 4;
}

#elements .guide {
    stroke: orange;
    stroke-dasharray: 2, 4;
    stroke-opacity: 0.65;
}

#elements line:hover,
#elements line.hover,
#elements circle:hover,
#elements circle.hover {
    stroke: var(--select-color) !important;
    stroke-width: 3.2 !important;
    stroke-opacity: 1 !important;
}

#highlights .highlight-segment {
    stroke: var(--select-color);
    fill: none;
    stroke-width: 6;
    stroke-opacity: 0.45;
    vector-effect: non-scaling-stroke;
    marker-start: url(#marker);
    marker-end: url(#marker);
    pointer-events: none;
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

#graphics polygon:hover,
#graphics polygon.hover,
#graphics polyline:hover,
#graphics polyline.hover {
    stroke: var(--select-color) !important;
    stroke-opacity: 1 !important;
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
    pointer-events: none;
}

#labels text.target-label {
    fill: gold;
    font-weight: 700;
}

#labels text.given-label {
    fill: #8f8;
}

#labels text.hover-label {
    fill: var(--select-color) !important;
    font-weight: 700;
}

.etc-svg-stage {
    position: relative;
    width: 100%;
}

.etc-svg-toolbar {
    position: absolute;
    top: 8px;
    right: 8px;
    display: flex;
    gap: 4px;
    z-index: 20;
    opacity: 0.35;
    transition: opacity 0.18s ease;
}

.etc-svg-stage:hover .etc-svg-toolbar,
figure:hover .etc-svg-toolbar {
    opacity: 0.95;
}

.etc-svg-btn {
    background: rgba(18, 18, 18, 0.88);
    color: #e0e0e0;
    border: 1px solid #444;
    border-radius: 4px;
    padding: 2px 8px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 12px;
    line-height: 1.4;
    cursor: pointer;
    user-select: none;
}

.etc-svg-btn:hover {
    background: #0ff;
    color: #121212;
    border-color: #0ff;
}

.etc-graphics-panel {
    width: 100%;
    background: #141414;
    border: 1px solid #333;
    border-radius: 6px;
    overflow: hidden;
}

.etc-graphics-panel svg.geometor-etc-drawing {
    border: none;
    border-radius: 0;
}

.etc-triangle-tabs {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 2px;
    background: #1a1a1a;
    border-bottom: 1px solid #2e2e2e;
    padding: 6px 10px 0 10px;
}

.etc-tab-btn {
    background: transparent;
    color: #999;
    border: 1px solid transparent;
    border-bottom: none;
    border-radius: 5px 5px 0 0;
    padding: 5px 14px;
    font-family: "Fira Sans Condensed", system-ui, -apple-system, sans-serif;
    font-size: 13.5px;
    font-weight: 600;
    letter-spacing: 0.02em;
    cursor: pointer;
    user-select: none;
    transition: color 0.15s ease, background 0.15s ease;
    margin-bottom: -1px;
}

.etc-tab-btn:hover {
    color: #fff;
    background: rgba(255, 255, 255, 0.04);
}

.etc-tab-btn.active {
    background: #161616;
    color: #0ff;
    border-color: #2e2e2e;
    border-bottom: 1px solid #161616;
}
"""


INTERACTIVE_SVG_JS = r"""
(function () {
    const scriptEl = document.currentScript;
    const svg = scriptEl ? scriptEl.closest('svg') : document.querySelector('svg.geometor-etc-drawing');
    if (!svg || svg.dataset.etcInteractiveInit === '1') return;
    if (svg.closest('.excerpt, .collection, a') || svg.classList.contains('euclid-thumbnail')) return;
    svg.dataset.etcInteractiveInit = '1';

    const initVbAttr = svg.getAttribute('data-initial-viewbox') || svg.getAttribute('viewBox');
    const initialViewBox = initVbAttr.split(/\s+/).map(Number);

    // Parse embedded element metadata catalog
    let elementsCatalog = {};
    const metaEl = svg.querySelector('script.etc-elements-meta');
    if (metaEl) {
        try {
            elementsCatalog = JSON.parse(metaEl.textContent);
        } catch (e) {}
    }

    const pointsGroup = svg.querySelector('#points');
    const elementsGroup = svg.querySelector('#elements');
    const graphicsGroup = svg.querySelector('#graphics');
    const highlightsGroup = svg.querySelector('#highlights');
    const labelsGroup = svg.querySelector('#labels');

    const pointEls = pointsGroup ? Array.from(pointsGroup.querySelectorAll('circle')) : [];
    const structEls = elementsGroup ? Array.from(elementsGroup.querySelectorAll('line, circle')) : [];
    const polyEls = graphicsGroup ? Array.from(graphicsGroup.querySelectorAll('polygon, polyline')) : [];
    const labelEls = labelsGroup ? Array.from(labelsGroup.querySelectorAll('text[data-point-id]')) : [];
    const subtitleEl = labelsGroup ? labelsGroup.querySelector('text.subtitle-label') : null;

    function getViewBox() {
        return svg.getAttribute('viewBox').split(/\s+/).map(Number);
    }

    function scaleViewElements() {
        const rect = svg.getBoundingClientRect();
        const widthPx = rect.width || 800;
        const vb = getViewBox();
        const unitsPerPx = vb[2] / widthPx;

        pointEls.forEach(c => {
            const isTarget = c.classList.contains('target') || c.classList.contains('selected');
            const isGuide = c.classList.contains('guide');
            const rPx = isTarget ? 10.5 : (isGuide ? 4.8 : 7.5);
            c.setAttribute('r', (rPx * unitsPerPx).toFixed(6));
        });

        const fontSize = 20.25 * unitsPerPx;
        labelEls.forEach(lbl => {
            const cx = parseFloat(lbl.getAttribute('data-anchor-x') || '0');
            const cy = parseFloat(lbl.getAttribute('data-anchor-y') || '0');
            const oxPx = parseFloat(lbl.getAttribute('data-offset-x') || '12');
            const oyPx = parseFloat(lbl.getAttribute('data-offset-y') || '-10.5');
            lbl.setAttribute('x', (cx + oxPx * unitsPerPx).toFixed(6));
            lbl.setAttribute('y', (cy + oyPx * unitsPerPx).toFixed(6));
            lbl.setAttribute('font-size', fontSize.toFixed(6));
        });

        if (subtitleEl) {
            const subX = vb[0] + 20.0 * unitsPerPx;
            const subY = vb[1] + vb[3] - 18.0 * unitsPerPx;
            subtitleEl.setAttribute('x', subX.toFixed(6));
            subtitleEl.setAttribute('y', subY.toFixed(6));
            subtitleEl.setAttribute('font-size', (17.25 * unitsPerPx).toFixed(6));
        }
    }

    function setViewBox(vb) {
        svg.setAttribute('viewBox', `${vb[0].toFixed(6)} ${vb[1].toFixed(6)} ${vb[2].toFixed(6)} ${vb[3].toFixed(6)}`);
        scaleViewElements();
    }

    function zoomBy(factor, clientX, clientY) {
        const vb = getViewBox();
        let [x, y, w, h] = vb;
        const rect = svg.getBoundingClientRect();
        const relX = (clientX !== undefined && rect.width > 0) ? (clientX - rect.left) / rect.width : 0.5;
        const relY = (clientY !== undefined && rect.height > 0) ? (clientY - rect.top) / rect.height : 0.5;
        const focusX = x + relX * w;
        const focusY = y + relY * h;
        const newW = Math.min(Math.max(w * factor, 0.002), 50.0);
        const newH = Math.min(Math.max(h * factor, 0.002), 50.0);
        const newX = focusX - relX * newW;
        const newY = focusY - relY * newH;
        setViewBox([newX, newY, newW, newH]);
    }

    function resetView() {
        setViewBox([...initialViewBox]);
    }

    // Expose controller API on the SVG element for external toolbar buttons
    svg._etcController = {
        zoomIn: () => zoomBy(1 / 1.25),
        zoomOut: () => zoomBy(1.25),
        resetView: resetView,
        toggleLabels: () => svg.classList.toggle('hide-labels'),
        toggleGuides: () => svg.classList.toggle('hide-guides'),
        scaleViewElements: scaleViewElements,
    };

    // Ensure Toolbar and Triangle Tabs exist if running inside an HTML document
    if (document.body && document.documentElement.tagName.toLowerCase() === 'html') {
        const parent = svg.parentElement;
        if (parent && !parent.classList.contains('etc-svg-stage')) {
            const stage = document.createElement('div');
            stage.className = 'etc-svg-stage';
            parent.insertBefore(stage, svg);
            stage.appendChild(svg);

            const toolbar = document.createElement('div');
            toolbar.className = 'etc-svg-toolbar';
            const btns = [
                { label: '+', title: 'Zoom In (or scroll wheel)', action: () => zoomBy(1 / 1.25) },
                { label: '−', title: 'Zoom Out (or scroll wheel)', action: () => zoomBy(1.25) },
                { label: '⟲ Fit', title: 'Reset View (or double-click canvas)', action: () => resetView() },
                { label: 'Labels', title: 'Toggle Point Labels', action: () => svg.classList.toggle('hide-labels') },
            ];
            if (svg.querySelector('.guide')) {
                btns.push({ label: 'Guides', title: 'Toggle Construction Guides', action: () => svg.classList.toggle('hide-guides') });
            }
            btns.forEach(b => {
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = 'etc-svg-btn';
                btn.textContent = b.label;
                btn.title = b.title;
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    b.action();
                });
                toolbar.appendChild(btn);
            });
            stage.appendChild(toolbar);
        }

        const panel = svg.closest('.etc-graphics-panel');
        if (panel && panel.dataset.etcTabsInit !== '1') {
            panel.dataset.etcTabsInit = '1';
            const tabBtns = Array.from(panel.querySelectorAll('.etc-tab-btn'));

            tabBtns.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    const targetTab = btn.getAttribute('data-tab');
                    const tabPanes = Array.from(panel.querySelectorAll('.etc-tab-pane'));
                    const prevPane = panel.querySelector('.etc-tab-pane.active');
                    const prevSvg = prevPane ? prevPane.querySelector('svg.geometor-etc-drawing') : null;
                    const hideLabels = prevSvg ? prevSvg.classList.contains('hide-labels') : false;
                    const hideGuides = prevSvg ? prevSvg.classList.contains('hide-guides') : false;

                    tabBtns.forEach(b => {
                        const isMatch = b.getAttribute('data-tab') === targetTab;
                        b.classList.toggle('active', isMatch);
                        b.setAttribute('aria-selected', isMatch ? 'true' : 'false');
                    });

                    tabPanes.forEach(pane => {
                        const isMatch = pane.getAttribute('data-tab-pane') === targetTab;
                        pane.classList.toggle('active', isMatch);
                        pane.style.display = isMatch ? 'block' : 'none';
                        if (isMatch) {
                            const paneSvg = pane.querySelector('svg.geometor-etc-drawing');
                            if (paneSvg) {
                                paneSvg.classList.toggle('hide-labels', hideLabels);
                                paneSvg.classList.toggle('hide-guides', hideGuides);
                                if (paneSvg._etcController) {
                                    paneSvg._etcController.scaleViewElements();
                                    requestAnimationFrame(() => paneSvg._etcController.scaleViewElements());
                                }
                            }
                        }
                    });

                    const figureEl = panel.closest('figure');
                    const captionP = figureEl ? (figureEl.querySelector('figcaption .caption-text') || figureEl.querySelector('figcaption p')) : null;
                    if (captionP) {
                        if (!captionP.dataset.origHtml) {
                            captionP.dataset.origHtml = captionP.innerHTML;
                        }
                        const capHtml = btn.getAttribute('data-caption-html');
                        if (targetTab === 'acute' && captionP.dataset.origHtml) {
                            captionP.innerHTML = captionP.dataset.origHtml;
                        } else if (capHtml) {
                            captionP.innerHTML = capHtml;
                        }
                    }
                });
            });
        }
    }

    let activeHoveredId = null;

    function clearHover() {
        if (!activeHoveredId) return;
        activeHoveredId = null;
        svg.querySelectorAll('.hover').forEach(el => el.classList.remove('hover'));
        svg.querySelectorAll('.hover-label').forEach(el => el.classList.remove('hover-label'));
        if (highlightsGroup) {
            highlightsGroup.querySelectorAll('.highlight-segment').forEach(el => {
                el.style.display = 'none';
            });
        }
    }

    function activateHover(id) {
        if (activeHoveredId === id) return;
        clearHover();
        activeHoveredId = id;
        const info = elementsCatalog[id];

        const targetEl = svg.querySelector(`[data-id="${CSS.escape(id)}"]`);
        if (targetEl) {
            targetEl.classList.add('hover');
        }

        // Show highlight segment if present
        if (highlightsGroup) {
            const hl = highlightsGroup.querySelector(`[data-highlight-for="${CSS.escape(id)}"]`);
            if (hl) hl.style.display = 'inline';
        }

        // Highlight parent/endpoint points and labels
        const relatedPts = (info && info.related_points) ? info.related_points : [id];
        relatedPts.forEach(pid => {
            const ptEl = pointsGroup ? pointsGroup.querySelector(`[data-id="${CSS.escape(pid)}"]`) : null;
            if (ptEl) ptEl.classList.add('hover');
            const lblEl = labelsGroup ? labelsGroup.querySelector(`text[data-point-id="${CSS.escape(pid)}"]`) : null;
            if (lblEl) lblEl.classList.add('hover-label');
        });
    }

    // Native DOM hover matching browser <title> tooltip topmost target
    svg.addEventListener('mouseover', (event) => {
        if (isPanning) return;
        const target = event.target.closest('[data-id]');
        if (target && svg.contains(target)) {
            activateHover(target.getAttribute('data-id'));
        } else {
            clearHover();
        }
    });

    svg.addEventListener('mouseout', (event) => {
        if (isPanning) return;
        const related = event.relatedTarget ? event.relatedTarget.closest?.('[data-id]') : null;
        if (!related || !svg.contains(related)) {
            clearHover();
        }
    });

    // Wheel Zoom
    svg.addEventListener('wheel', (event) => {
        event.preventDefault();
        const factor = event.deltaY > 0 ? 1.12 : (1 / 1.12);
        zoomBy(factor, event.clientX, event.clientY);
    }, { passive: false });

    // Drag Pan
    let isPanning = false;
    let didDrag = false;
    let startClient = { x: 0, y: 0 };

    svg.addEventListener('mousedown', (event) => {
        if (event.button !== 0) return;
        isPanning = true;
        didDrag = false;
        startClient = { x: event.clientX, y: event.clientY };
        svg.classList.add('is-panning');
    });

    svg.addEventListener('mousemove', (event) => {
        if (!isPanning) return;
        const dxPx = event.clientX - startClient.x;
        const dyPx = event.clientY - startClient.y;
        if (Math.hypot(dxPx, dyPx) > 2) didDrag = true;
        const rect = svg.getBoundingClientRect();
        if (rect.width > 0 && rect.height > 0) {
            const vb = getViewBox();
            const dx = dxPx * (vb[2] / rect.width);
            const dy = dyPx * (vb[3] / rect.height);
            setViewBox([vb[0] - dx, vb[1] - dy, vb[2], vb[3]]);
        }
        startClient = { x: event.clientX, y: event.clientY };
    });

    window.addEventListener('mouseup', () => {
        if (isPanning) {
            isPanning = false;
            svg.classList.remove('is-panning');
        }
    });

    svg.addEventListener('mouseleave', () => {
        isPanning = false;
        svg.classList.remove('is-panning');
        clearHover();
    });

    svg.addEventListener('dblclick', (event) => {
        event.preventDefault();
        resetView();
    });

    if (typeof ResizeObserver !== 'undefined') {
        new ResizeObserver(() => scaleViewElements()).observe(svg);
    }
})();
"""


# ---------------------------------------------------------------------------
# Center, Line, Circle, and Triangle Name Discernment
# ---------------------------------------------------------------------------

@functools.lru_cache(maxsize=1)
def _load_center_names() -> dict[str, str]:
    """Load the 53,144 center names dictionary from `resources/center_names.json`."""
    candidates = [
        Path(__file__).resolve().parents[3] / "resources" / "center_names.json",
        Path("resources/center_names.json"),
    ]
    for p in candidates:
        if p.is_file():
            try:
                return json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                pass
    return {}


_CLASSICAL_POINT_INFO: dict[str, tuple[str, str]] = {
    "A": ("Vertex A", "Reference triangle vertex at origin (0, 0)"),
    "B": ("Vertex B", "Reference triangle vertex at unit base (1, 0)"),
    "C": ("Vertex C", "Reference triangle apex constructed by Euclid I.22"),
    "M_a": ("Midpoint M_a of BC", "Medial triangle vertex opposite A"),
    "M_b": ("Midpoint M_b of CA", "Medial triangle vertex opposite B"),
    "M_c": ("Midpoint M_c of AB", "Medial triangle vertex opposite C"),
    "H_a": ("Altitude Foot H_a on BC", "Orthic triangle vertex opposite A"),
    "H_b": ("Altitude Foot H_b on CA", "Orthic triangle vertex opposite B"),
    "H_c": ("Altitude Foot H_c on AB", "Orthic triangle vertex opposite C"),
    "T_a": ("Incircle Touchpoint T_a on BC", "Intouch (contact) triangle vertex opposite A"),
    "T_b": ("Incircle Touchpoint T_b on CA", "Intouch (contact) triangle vertex opposite B"),
    "T_c": ("Incircle Touchpoint T_c on AB", "Intouch (contact) triangle vertex opposite C"),
    "N_a": ("Excircle Touchpoint N_a on BC", "Extouch triangle vertex opposite A"),
    "N_b": ("Excircle Touchpoint N_b on CA", "Extouch triangle vertex opposite B"),
    "N_c": ("Excircle Touchpoint N_c on AB", "Extouch triangle vertex opposite C"),
    "A'": ("Auxiliary Apex A'", "Constructed apex opposite vertex A"),
    "B'": ("Auxiliary Apex B'", "Constructed apex opposite vertex B"),
    "C'": ("Auxiliary Apex C'", "Constructed apex opposite vertex C"),
    "N_A": ("Napoleon Center N_A", "Centroid of equilateral triangle on BC"),
    "N_B": ("Napoleon Center N_B", "Centroid of equilateral triangle on CA"),
    "N_C": ("Napoleon Center N_C", "Centroid of equilateral triangle on AB"),
    "S_c": ("Spieker Touchpoint S_c", "Tangency point of Spieker circle on medial side M_a M_b"),
    "R_a": ("Radius Point R_a", "Euclid I.22 baseline guide point (distance a/c from B)"),
    "R_b": ("Radius Point R_b", "Euclid I.22 baseline guide point (distance b/c from A)"),
}

_CONSTRUCTION_LINE_INFO: dict[str, tuple[str, str]] = {
    "[ A B ]": ("Sideline AB (Base c = 1)", "Reference triangle baseline through A and B"),
    "[ B C ]": ("Sideline BC (Side a)", "Reference triangle sideline opposite vertex A"),
    "[ C A ]": ("Sideline CA (Side b)", "Reference triangle sideline opposite vertex B"),
    "[ A M_a ]": ("A-Median", "Median from vertex A to midpoint M_a of BC"),
    "[ B M_b ]": ("B-Median", "Median from vertex B to midpoint M_b of CA"),
    "[ C M_c ]": ("C-Median", "Median from vertex C to midpoint M_c of AB"),
    "[ A H_a ]": ("A-Altitude", "Altitude from vertex A perpendicular to BC at H_a"),
    "[ B H_b ]": ("B-Altitude", "Altitude from vertex B perpendicular to CA at H_b"),
    "[ C H_c ]": ("C-Altitude", "Altitude from vertex C perpendicular to AB at H_c"),
    "[ X(3) M_a ]": ("Perpendicular Bisector of BC", "Perpendicular bisector through M_a and Circumcenter X(3)"),
    "[ X(3) M_b ]": ("Perpendicular Bisector of CA", "Perpendicular bisector through M_b and Circumcenter X(3)"),
    "[ X(3) M_c ]": ("Perpendicular Bisector of AB", "Perpendicular bisector through M_c and Circumcenter X(3)"),
    "[ A X(1) ]": ("Internal Angle Bisector of ∠A", "Bisector of interior angle A through Incenter X(1)"),
    "[ B X(1) ]": ("Internal Angle Bisector of ∠B", "Bisector of interior angle B through Incenter X(1)"),
    "[ C X(1) ]": ("Internal Angle Bisector of ∠C", "Bisector of interior angle C through Incenter X(1)"),
    "[ A T_a ]": ("Gergonne Cevian A–T_a", "Cevian from vertex A to incircle touchpoint T_a"),
    "[ B T_b ]": ("Gergonne Cevian B–T_b", "Cevian from vertex B to incircle touchpoint T_b"),
    "[ C T_c ]": ("Gergonne Cevian C–T_c", "Cevian from vertex C to incircle touchpoint T_c"),
    "[ A N_a ]": ("Nagel Cevian (Splitter) A–N_a", "Perimeter-bisecting cevian from A to excircle touchpoint N_a"),
    "[ B N_b ]": ("Nagel Cevian (Splitter) B–N_b", "Perimeter-bisecting cevian from B to excircle touchpoint N_b"),
    "[ C N_c ]": ("Nagel Cevian (Splitter) C–N_c", "Perimeter-bisecting cevian from C to excircle touchpoint N_c"),
    "[ A A' ]": ("Apex Cevian A–A'", "Cevian joining vertex A to constructed apex A'"),
    "[ B B' ]": ("Apex Cevian B–B'", "Cevian joining vertex B to constructed apex B'"),
    "[ C C' ]": ("Apex Cevian C–C'", "Cevian joining vertex C to constructed apex C'"),
}

_KNOWN_CIRCLE_INFO: dict[str, tuple[str, str]] = {
    "circumcircle": (
        "Circumcircle of △ABC",
        "Passes through vertices A, B, C; centered at X(3) CIRCUMCENTER",
    ),
    "incircle": (
        "Incircle of △ABC",
        "Inscribed circle tangent to sidelines at T_a, T_b, T_c; centered at X(1) INCENTER",
    ),
    "nine_point_circle": (
        "Nine-Point Circle (Euler / Feuerbach Circle)",
        "Passes through side midpoints M_a, M_b, M_c and altitude feet H_a, H_b, H_c; centered at X(5)",
    ),
    "spieker_circle": (
        "Spieker Circle",
        "Incircle of the medial triangle △M_a M_b M_c; centered at X(10) SPIEKER CENTER",
    ),
    "brocard_circle": (
        "Brocard Circle (Seven-Point Circle)",
        "Circle on diameter X(3)X(6) passing through Brocard points and X(15), X(16); centered at X(182)",
    ),
    "orthocentroidal_circle": (
        "Orthocentroidal Circle",
        "Circle on diameter X(2)X(4) (Centroid to Orthocenter); centered at X(381)",
    ),
    "fuhrmann_circle": (
        "Fuhrmann Circle",
        "Circle on diameter X(4)X(8) (Orthocenter to Nagel Point); centered at X(427)",
    ),
    "( A R_b )": (
        "Euclid I.22 Guide Circle (A)",
        "Baseline construction circle centered at A with radius b/c",
    ),
    "( B R_a )": (
        "Euclid I.22 Guide Circle (B)",
        "Baseline construction circle centered at B with radius a/c",
    ),
}

_KNOWN_POLYGON_INFO: dict[str, tuple[str, str]] = {
    "< A B C >": ("Reference Triangle △ABC", "Primary reference triangle with unit baseline AB = 1"),
    "< M_a M_b M_c >": ("Medial Triangle △M_a M_b M_c", "Formed by the midpoints of sides BC, CA, AB"),
    "< H_a H_b H_c >": ("Orthic Triangle △H_a H_b H_c", "Pedal triangle of Orthocenter X(4) (altitude feet)"),
    "< T_a T_b T_c >": ("Intouch (Contact) Triangle △T_a T_b T_c", "Contact triangle of Incircle touchpoints on BC, CA, AB"),
    "< N_a N_b N_c >": ("Extouch Triangle △N_a N_b N_c", "Contact triangle of Excircle touchpoints on BC, CA, AB"),
    "< A' B' C' >": ("Tangential / Auxiliary Triangle △A'B'C'", "Derived triangle"),
    "< N_A N_B N_C >": ("Napoleon Triangle △N_A N_B N_C", "Equilateral triangle formed by centers of side equilateral triangles"),
    "< B C A' >": ("Equilateral Triangle on BC", "Equilateral triangle erected on side BC"),
    "< C A B' >": ("Equilateral Triangle on CA", "Equilateral triangle erected on side CA"),
    "< A B C' >": ("Equilateral Triangle on AB", "Equilateral triangle erected on side AB"),
}


def _short_point_name(pid: str, center_names: dict[str, str]) -> str:
    """Return a concise human-readable name for a point ID (`X(n)` or classical vertex)."""
    m = re.match(r"^X\((\d+)\)$", pid)
    if m:
        num_str = m.group(1)
        raw = center_names.get(num_str, "")
        if raw:
            # Keep primary title before long parenthetical if very long
            if len(raw) > 48 and "(" in raw:
                raw = raw.split("(")[0].strip()
            return raw
        return f"Triangle Center X({num_str})"
    if pid in _CLASSICAL_POINT_INFO:
        return _CLASSICAL_POINT_INFO[pid][0]
    return pid


def _compute_barycentrics(
    px: float,
    py: float,
    A: dict[str, Any] | None,
    B: dict[str, Any] | None,
    C: dict[str, Any] | None,
) -> tuple[float, float, float] | None:
    """Compute normalized barycentric coordinates (u, v, w) of (px, py) with respect to ABC."""
    if not (A and B and C):
        return None
    ax, ay = A["x"], A["y"]
    bx, by = B["x"], B["y"]
    cx, cy = C["x"], C["y"]
    det = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
    if abs(det) < 1e-12:
        return None
    u = ((by - cy) * (px - cx) + (cx - bx) * (py - cy)) / det
    v = ((cy - ay) * (px - cx) + (ax - cx) * (py - cy)) / det
    w = 1.0 - u - v
    return (u, v, w)


def _build_named_central_lines_xy(
    A: dict[str, Any] | None,
    B: dict[str, Any] | None,
    C: dict[str, Any] | None,
) -> list[tuple[str, str, tuple[float, float], tuple[float, float]]]:
    """Precompute Cartesian point pairs for famous named central lines on triangle ABC."""
    if not (A and B and C):
        return []
    ax, ay = A["x"], A["y"]
    bx, by = B["x"], B["y"]
    cx, cy = C["x"], C["y"]
    a = math.hypot(cx - bx, cy - by)
    b = math.hypot(ax - cx, ay - cy)
    c = math.hypot(bx - ax, by - ay)
    if min(a, b, c) < 1e-9:
        return []
    s = 0.5 * (a + b + c)
    sa = 0.5 * (b * b + c * c - a * a)
    sb = 0.5 * (c * c + a * a - b * b)
    sc = 0.5 * (a * a + b * b - c * c)

    def b2xy(u: float, v: float, w: float) -> tuple[float, float]:
        tot = u + v + w
        return ((u * ax + v * bx + w * cx) / tot, (u * ay + v * by + w * cy) / tot)

    pts = {
        1: b2xy(a, b, c),
        2: b2xy(1.0, 1.0, 1.0),
        3: b2xy(a * a * sa, b * b * sb, c * c * sc),
        4: b2xy(sb * sc, sc * sa, sa * sb),
        5: b2xy(a * a * (b * b + c * c) - (b * b - c * c) ** 2, b * b * (c * c + a * a) - (c * c - a * a) ** 2, c * c * (a * a + b * b) - (a * a - b * b) ** 2),
        6: b2xy(a * a, b * b, c * c),
        7: b2xy((s - b) * (s - c), (s - c) * (s - a), (s - a) * (s - b)),
        8: b2xy(s - a, s - b, s - c),
        9: b2xy(a * (s - a), b * (s - b), c * (s - c)),
        10: b2xy(b + c, c + a, a + b),
    }

    named_specs = [
        ("Euler Line", "Collinear line of X(2) Centroid, X(3) Circumcenter, X(4) Orthocenter, X(5) Nine-Point Center, X(20), X(30)", 2, 3),
        ("Nagel Line", "Collinear line of X(1) Incenter, X(2) Centroid, X(8) Nagel Point, X(10) Spieker Center", 1, 2),
        ("OI Line (Incenter–Circumcenter Line)", "Collinear line of X(1) Incenter, X(3) Circumcenter, X(40) Bevan Point, X(55), X(56)", 1, 3),
        ("Brocard Axis", "Collinear line of X(3) Circumcenter, X(6) Symmedian Point, X(15) & X(16) Isodynamic Points", 3, 6),
        ("Soddy Line", "Collinear line of X(1) Incenter, X(7) Gergonne Point, X(20) de Longchamps Point, X(175), X(176)", 1, 7),
        ("Feuerbach Line", "Collinear line of X(1) Incenter, X(5) Nine-Point Center, X(11) Feuerbach Point", 1, 5),
        ("Van Aubel Line", "Collinear line of X(4) Orthocenter and X(6) Symmedian Point", 4, 6),
        ("Incenter–Symmedian Line", "Collinear line of X(1) Incenter, X(6) Symmedian Point, X(9) Mittenpunkt", 1, 6),
        ("Centroid–Symmedian Line", "Collinear line of X(2) Centroid, X(6) Symmedian Point, X(39) Brocard Midpoint", 2, 6),
        ("Nine-Point–Symmedian Line", "Collinear line of X(5) Nine-Point Center and X(6) Symmedian Point", 5, 6),
        ("Incenter–Orthocenter Line", "Collinear line of X(1) Incenter and X(4) Orthocenter", 1, 4),
        ("Centroid–Gergonne Line", "Collinear line of X(2) Centroid, X(7) Gergonne Point, X(9) Mittenpunkt", 2, 7),
        ("Gergonne–Nagel Line", "Collinear line of X(7) Gergonne Point and X(8) Nagel Point", 7, 8),
        ("Fuhrmann Line", "Collinear line of X(4) Orthocenter and X(8) Nagel Point", 4, 8),
        ("Orthocenter–Spieker Line", "Collinear line of X(4) Orthocenter and X(10) Spieker Center", 4, 10),
    ]

    result = []
    for name, desc, i, j in named_specs:
        p1, p2 = pts[i], pts[j]
        if math.hypot(p2[0] - p1[0], p2[1] - p1[1]) > 1e-7:
            result.append((name, desc, p1, p2))
    return result


def _dist_point_to_line(
    px: float, py: float, x1: float, y1: float, x2: float, y2: float
) -> float:
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    if length < 1e-12:
        return math.hypot(px - x1, py - y1)
    return abs(dy * px - dx * py + x2 * y1 - y2 * x1) / length


def _format_line_eq(x1: float, y1: float, x2: float, y2: float) -> str:
    """Return normalized Cartesian line equation ax + by + c = 0."""
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    norm = math.hypot(a, b)
    if norm > 1e-12:
        a, b, c = a / norm, b / norm, c / norm
    if a < -1e-9 or (abs(a) <= 1e-9 and b < 0):
        a, b, c = -a, -b, -c
    b_sign = "+" if b >= 0 else "-"
    c_sign = "+" if c >= 0 else "-"
    return f"{a:.4f}x {b_sign} {abs(b):.4f}y {c_sign} {abs(c):.4f} = 0"


def _enrich_elements_catalog(
    elements: list[dict[str, Any]],
    points_by_id: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    """Build a rich metadata dictionary keyed by element ID for interactive hover cards."""
    center_names = _load_center_names()
    A = points_by_id.get("A")
    B = points_by_id.get("B")
    C = points_by_id.get("C")
    named_lines = _build_named_central_lines_xy(A, B, C)

    catalog: dict[str, dict[str, Any]] = {}

    for el in elements:
        eid = el["ID"]
        etype = el["type"]
        classes = el.get("classes") or []

        if etype == "point":
            px, py = el["x"], el["y"]
            is_target = "target" in classes or "selected" in classes
            is_given = "given" in classes
            color = "gold" if is_target else ("#6F6" if is_given else ("orange" if el["guide"] else "#0ff"))

            m = re.match(r"^X\((\d+)\)$", eid)
            if m:
                c_num_str = m.group(1)
                c_name = center_names.get(c_num_str, f"Triangle Center X({c_num_str})")
                subtitle = "Target Triangle Center" if is_target else "Incident / Reference Triangle Center"
            elif eid in _CLASSICAL_POINT_INFO:
                c_name, subtitle = _CLASSICAL_POINT_INFO[eid]
            else:
                c_name, subtitle = eid, "Constructed Point"

            rows: list[tuple[str, str]] = [
                ("x", f"{px:.4f}"),
                ("y", f"{py:.4f}"),
            ]
            bary = _compute_barycentrics(px, py, A, B, C)
            if bary:
                rows.append(("bary", f"{bary[0]:.4f} : {bary[1]:.4f} : {bary[2]:.4f}"))
            if el.get("parents"):
                rows.append(("str", ", ".join(el["parents"])))

            catalog[eid] = {
                "ID": eid,
                "type": "point",
                "classes": classes,
                "color": color,
                "name": c_name,
                "subtitle": subtitle,
                "rows": rows,
                "related_points": [eid],
            }

        elif etype == "line":
            p1_id, p2_id = el["pt1"], el["pt2"]
            p1 = points_by_id.get(p1_id)
            p2 = points_by_id.get(p2_id)
            p1_short = _short_point_name(p1_id, center_names)
            p2_short = _short_point_name(p2_id, center_names)
            thru_desc = f"{p1_id} ({p1_short}), {p2_id} ({p2_short})"

            line_name = ""
            subtitle = f"Line through {p1_id} and {p2_id}"

            if eid in _CONSTRUCTION_LINE_INFO:
                line_name, subtitle = _CONSTRUCTION_LINE_INFO[eid]
            elif p1 and p2:
                # Check if this central line matches any of the famous named central lines
                for nl_name, nl_desc, nl_p1, nl_p2 in named_lines:
                    if (
                        _dist_point_to_line(p1["x"], p1["y"], nl_p1[0], nl_p1[1], nl_p2[0], nl_p2[1]) < 1e-4
                        and _dist_point_to_line(p2["x"], p2["y"], nl_p1[0], nl_p1[1], nl_p2[0], nl_p2[1]) < 1e-4
                    ):
                        line_name = nl_name
                        subtitle = nl_desc
                        break
                if not line_name:
                    m_brace = re.match(r"^\{\s*(\d+)\s*,\s*(\d+)\s*\}$", eid)
                    if m_brace:
                        i_s, j_s = m_brace.group(1), m_brace.group(2)
                        line_name = f"Central Line L({i_s}, {j_s})"
                        subtitle = f"Through X({i_s}) ({p1_short}) and X({j_s}) ({p2_short})"
                    else:
                        line_name = f"Line {eid}"

            color = "gold" if ("golden" in classes or "euler" in classes) else ("#0bd" if "central_line" in classes else "#aaa")
            rows = [("pts", thru_desc)]
            if p1 and p2:
                seg_len = math.hypot(p2["x"] - p1["x"], p2["y"] - p1["y"])
                rows.append(("len", f"{seg_len:.4f}"))
                rows.append(("eq", _format_line_eq(p1["x"], p1["y"], p2["x"], p2["y"])))

            catalog[eid] = {
                "ID": eid,
                "type": "line",
                "classes": classes,
                "color": color,
                "name": line_name,
                "subtitle": subtitle,
                "rows": rows,
                "related_points": [p1_id, p2_id],
            }

        elif etype == "circle":
            ctr_id = el["center"]
            rad_id = el.get("radius_pt") or ""
            ctr = points_by_id.get(ctr_id)
            r_val = el["radius"]
            ctr_short = _short_point_name(ctr_id, center_names)

            if eid in _KNOWN_CIRCLE_INFO:
                c_name, subtitle = _KNOWN_CIRCLE_INFO[eid]
            else:
                # Format note-extracted circle name or derive from center X(k)
                pretty_id = eid.replace("_", " ").strip()
                if "circle" in pretty_id.lower():
                    c_name = pretty_id[0].upper() + pretty_id[1:]
                elif ctr_short.upper().startswith("CENTER OF "):
                    c_name = ctr_short[10:].strip().title()
                else:
                    c_name = f"Circle {eid}"
                subtitle = f"Centered at {ctr_id} ({ctr_short})"

            color = "#00e5ff" if "nine_point_circle" in classes else ("#e040fb" if "incircle" in classes else ("#ff9100" if "secondary_circle" in classes else "#C09"))
            rows = [("ctr", f"{ctr_id} ({ctr_short})")]
            if ctr:
                hx, ky = ctr["x"], ctr["y"]
                rows.append(("h, k", f"({hx:.4f}, {ky:.4f})"))
                rows.append(("r", f"{r_val:.4f}"))
                h_sign = "-" if hx >= 0 else "+"
                k_sign = "-" if ky >= 0 else "+"
                rows.append(("eq", f"(x {h_sign} {abs(hx):.3f})² + (y {k_sign} {abs(ky):.3f})² = {r_val*r_val:.4f}"))
            if rad_id:
                rows.append(("pass", f"{rad_id} ({_short_point_name(rad_id, center_names)})"))

            rel_pts = [ctr_id] + ([rad_id] if rad_id else [])
            catalog[eid] = {
                "ID": eid,
                "type": "circle",
                "classes": classes,
                "color": color,
                "name": c_name,
                "subtitle": subtitle,
                "rows": rows,
                "related_points": rel_pts,
            }

        elif etype == "polygon":
            v_ids = el.get("points") or []
            p_name, subtitle = _KNOWN_POLYGON_INFO.get(
                eid, (f"Polygon {eid}", f"Vertices: {', '.join(v_ids)}")
            )
            color = "#90ee90" if "secondary" in classes else "#58a6ff"
            rows = [("verts", ", ".join(v_ids))]
            v_pts = [points_by_id[vid] for vid in v_ids if vid in points_by_id]
            if len(v_pts) == 3:
                s_a = math.hypot(v_pts[2]["x"] - v_pts[1]["x"], v_pts[2]["y"] - v_pts[1]["y"])
                s_b = math.hypot(v_pts[0]["x"] - v_pts[2]["x"], v_pts[0]["y"] - v_pts[2]["y"])
                s_c = math.hypot(v_pts[1]["x"] - v_pts[0]["x"], v_pts[1]["y"] - v_pts[0]["y"])
                area = 0.5 * abs(
                    (v_pts[1]["x"] - v_pts[0]["x"]) * (v_pts[2]["y"] - v_pts[0]["y"])
                    - (v_pts[2]["x"] - v_pts[0]["x"]) * (v_pts[1]["y"] - v_pts[0]["y"])
                )
                rows.append(("sides", f"{s_a:.4f}, {s_b:.4f}, {s_c:.4f}"))
                rows.append(("area", f"{area:.4f}"))

            catalog[eid] = {
                "ID": eid,
                "type": "polygon",
                "classes": classes,
                "color": color,
                "name": p_name,
                "subtitle": subtitle,
                "rows": rows,
                "related_points": v_ids,
            }

    return catalog


def model_to_elements_list(model: Model) -> list[dict[str, Any]]:
    """Convert a `geometor.model.Model` into a chronological list of browser-ready element dicts."""
    elements: list[dict[str, Any]] = []
    for el, data in model.items():
        if not data.ID:
            continue
        parents_ids = [
            model[p].ID for p in (data.parents or []) if p in model and model[p].ID
        ]
        base: dict[str, Any] = {
            "ID": data.ID,
            "classes": list(data.classes.keys()) if isinstance(data.classes, dict) else list(data.classes),
            "guide": bool(data.guide),
            "parents": parents_ids,
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
    """Render a `geometor.model.Model` to an interactive Explorer-compatible SVG string."""
    elements = model_to_elements_list(model)
    points_by_id: dict[str, dict[str, Any]] = {
        el["ID"]: el for el in elements if el["type"] == "point"
    }
    catalog = _enrich_elements_catalog(elements, points_by_id)

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

    # Point radius scaled like `scaleCircles()` in `explorer/static/js/svg.js` (1.5x scale)
    units_per_px = vb_width / svg_width
    pt_radius = 7.5 * units_per_px
    target_radius = 10.5 * units_per_px
    guide_radius = 4.8 * units_per_px
    font_size = 20.25 * units_per_px

    graphics_nodes: list[str] = []
    highlights_nodes: list[str] = []
    elements_nodes: list[str] = []
    points_nodes: list[str] = []
    labels_nodes: list[str] = []

    for el in elements:
        raw_id = el["ID"]
        el_id = html.escape(raw_id, quote=True)
        info = catalog.get(raw_id, {})
        el_name = html.escape(info.get("name") or raw_id, quote=True)
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
                f'    <polygon data-id="{el_id}" data-name="{el_name}" class="{class_attr}" '
                f'data-category="graphics" points="{pts_str}"><title>{el_id}: {el_name}</title></polygon>'
            )

        elif el["type"] in {"segment", "section", "chain"}:
            pts_str = " ".join(
                f"{points_by_id[pid]['x']:.6f},{-points_by_id[pid]['y']:.6f}"
                for pid in el["points"]
                if pid in points_by_id
            )
            graphics_nodes.append(
                f'    <polyline data-id="{el_id}" data-name="{el_name}" class="{class_attr}" '
                f'data-category="graphics" points="{pts_str}"><title>{el_id}: {el_name}</title></polyline>'
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
                    f'    <line data-id="{el_id}" data-name="{el_name}" class="{class_attr}" data-category="elements" '
                    f'x1="{x1:.5f}" y1="{y1:.5f}" x2="{x2:.5f}" y2="{y2:.5f}">'
                    f"<title>{el_id}: {el_name}</title></line>"
                )
                highlights_nodes.append(
                    f'    <polyline data-highlight-for="{el_id}" class="highlight-segment" '
                    f'points="{p1["x"]:.6f},{-p1["y"]:.6f} {p2["x"]:.6f},{-p2["y"]:.6f}" style="display: none;" />'
                )

        elif el["type"] == "circle":
            ctr = points_by_id.get(el["center"])
            rad_pt = points_by_id.get(el.get("radius_pt") or "")
            if ctr:
                cx = ctr["x"]
                cy = -ctr["y"]
                r = el["radius"]
                elements_nodes.append(
                    f'    <circle data-id="{el_id}" data-name="{el_name}" class="{class_attr}" data-category="elements" '
                    f'cx="{cx:.6f}" cy="{cy:.6f}" r="{r:.6f}" fill="none">'
                    f"<title>{el_id}: {el_name}</title></circle>"
                )
                if rad_pt:
                    highlights_nodes.append(
                        f'    <polyline data-highlight-for="{el_id}" class="highlight-segment" '
                        f'points="{ctr["x"]:.6f},{-ctr["y"]:.6f} {rad_pt["x"]:.6f},{-rad_pt["y"]:.6f}" style="display: none;" />'
                    )

        elif el["type"] == "point":
            cx = el["x"]
            cy = -el["y"]
            is_target = "target" in el["classes"] or "selected" in el["classes"]
            r = target_radius if is_target else (guide_radius if el["guide"] else pt_radius)
            points_nodes.append(
                f'    <circle data-id="{el_id}" data-name="{el_name}" class="{class_attr}" data-category="points" '
                f'cx="{cx:.6f}" cy="{cy:.6f}" r="{r:.6f}">'
                f"<title>{el_id} = {el_name} ({cx:.4f}, {el['y']:.4f})</title></circle>"
            )

            # Label vertices A, B, C and centers X(k)
            if show_labels and not el["guide"]:
                lbl_cls = (
                    "target-label"
                    if is_target
                    else ("given-label" if "given" in el["classes"] else "point-label")
                )
                ox_px = 12.0
                oy_px = -10.5
                if raw_id == "A":
                    ox_px, oy_px = -24.0, 22.5
                elif raw_id == "B":
                    ox_px, oy_px = 12.0, 22.5
                elif raw_id == "C":
                    ox_px, oy_px = -7.5, -15.0
                offset_x = ox_px * units_per_px
                offset_y = oy_px * units_per_px
                labels_nodes.append(
                    f'    <text class="{lbl_cls}" data-point-id="{el_id}" '
                    f'data-anchor-x="{cx:.6f}" data-anchor-y="{cy:.6f}" '
                    f'data-offset-x="{ox_px:.1f}" data-offset-y="{oy_px:.1f}" '
                    f'x="{cx + offset_x:.6f}" y="{cy + offset_y:.6f}" '
                    f'font-size="{font_size:.6f}">{el_id}</text>'
                )

    if subtitle:
        sub_x = vb_x + 20.0 * units_per_px
        sub_y = vb_y + vb_height - 18.0 * units_per_px
        sub_font = 17.25 * units_per_px
        labels_nodes.append(
            f'    <text class="subtitle-label" x="{sub_x:.6f}" y="{sub_y:.6f}" '
            f'font-size="{sub_font:.6f}" fill="#999">{html.escape(subtitle)}</text>'
        )

    vb_str = f"{vb_x:.6f} {vb_y:.6f} {vb_width:.6f} {vb_height:.6f}"
    meta_json = json.dumps(catalog, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    svg_lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        f'<svg class="geometor-etc-drawing" xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="{vb_str}" data-initial-viewbox="{vb_str}" '
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
        f'  <script type="application/json" class="etc-elements-meta">{meta_json}</script>',
        f"  <script>//<![CDATA[\n{INTERACTIVE_SVG_JS}\n//]]></script>",
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

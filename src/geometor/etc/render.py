"""Render `geometor.model.Model` instances into interactive Explorer-styled SVGs."""

from __future__ import annotations

import functools
import html
import json
import math
import re
from pathlib import Path
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    clean_expr,
    exact_sign,
    line_spread,
    quadrance,
    zero_test,
)
from geometor.model.element import CircleElement

from .ops import (
    barycentrics_of,
    triangle_side_lengths,
    triangle_side_quadrances,
    triangle_signed_area,
)
from .palette import (
    get_central_line_color_token,
    get_circle_color_token,
    token_hex,
)
from .symbolic_cache import (
    EXACT_CYCLIC_BARYCENTRICS,
    CenterSymbolicRegistry,
    format_symbolic_latex,
    format_symbolic_pretty,
    reduce_homogeneous_triple,
)
from .triangles import (
    SymbolicTriangle,
    get_canonical_triangle,
)

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
svg.geometor-etc-drawing.hide-labels #labels .guide-label,
svg.geometor-etc-drawing.hide-labels #labels .target-label,
svg.geometor-etc-drawing.hide-labels #labels .given-label {
    display: none;
}

svg.geometor-etc-drawing.hide-guides .guide {
    display: none !important;
}

svg.geometor-etc-drawing:not(.show-lines) .incident {
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

#elements line,
#elements path.line {
    fill: none;
    stroke: #b0bec5;
    stroke-width: 2.2;
    stroke-dasharray: 2, 4.5;
    stroke-linecap: round;
    vector-effect: non-scaling-stroke;
    cursor: pointer;
}

#elements line.sideline,
#elements path.line.sideline {
    stroke: #cbd5e1;
    stroke-width: 2.3;
}

#elements line.central_line,
#elements path.line.central_line {
    stroke: #0bd;
    stroke-width: 1.85;
    stroke-opacity: 0.85;
}

#elements line.central_line[data-color-token="orange"] { stroke: #fb923c; stroke-dasharray: 6, 3; }
#elements line.central_line[data-color-token="teal"] { stroke: #2dd4bf; stroke-dasharray: 6, 3; }
#elements line.central_line[data-color-token="blue"] { stroke: #38bdf8; stroke-dasharray: 6, 3; }
#elements line.central_line[data-color-token="orchid"] { stroke: #e879f9; stroke-dasharray: 6, 3; }
#elements line.central_line[data-color-token="pink"] { stroke: #f472b6; stroke-dasharray: 6, 3; }
#elements line.central_line[data-color-token="lime"] { stroke: #a3e635; stroke-dasharray: 6, 3; }
#elements line.central_line[data-color-token="green"] { stroke: #5ec27e; stroke-dasharray: 6, 3; }
#elements line.central_line[data-color-token="purple"] { stroke: #a855f7; stroke-dasharray: 6, 3; }

#elements line.golden,
#elements path.line.golden,
#elements line.euler,
#elements path.line.euler {
    stroke: gold;
    stroke-width: 2.1;
}

#elements line.strut {
    stroke: gold;
    stroke-width: 2.8;
    stroke-dasharray: none;
    stroke-opacity: 0.95;
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
    stroke-dasharray: 2, 4;
}

#elements .guide {
    stroke: orange;
    stroke-dasharray: 2, 4;
    stroke-opacity: 0.65;
}

#elements line:hover,
#elements line.hover,
#elements path.line:hover,
#elements path.line.hover,
#elements circle:hover,
#elements circle.hover {
    stroke: var(--select-color) !important;
    stroke-width: 3.2 !important;
    stroke-dasharray: none !important;
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
    stroke: #ffd54f;
    fill: none;
    stroke-width: 3.2;
    vector-effect: non-scaling-stroke;
    cursor: pointer;
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
    cursor: pointer;
}

#graphics polygon.secondary {
    stroke: rgba(144, 238, 144, 0.55);
    fill: rgba(144, 238, 144, 0.08);
    stroke-width: 3;
}

#graphics polygon.subarea-a {
    stroke: rgba(255, 112, 67, 0.72);
    fill: rgba(255, 112, 67, 0.20);
    stroke-width: 2.4;
    marker-start: none;
    marker-mid: none;
    marker-end: none;
}

#graphics polygon.subarea-b {
    stroke: rgba(102, 187, 106, 0.72);
    fill: rgba(102, 187, 106, 0.20);
    stroke-width: 2.4;
    marker-start: none;
    marker-mid: none;
    marker-end: none;
}

#graphics polygon.subarea-c {
    stroke: rgba(66, 165, 245, 0.72);
    fill: rgba(66, 165, 245, 0.20);
    stroke-width: 2.4;
    marker-start: none;
    marker-mid: none;
    marker-end: none;
}

#graphics polygon:hover,
#graphics polygon.hover,
#graphics polyline:hover,
#graphics polyline.hover {
    stroke: var(--select-color) !important;
    stroke-opacity: 1 !important;
}

#graphics polygon.subarea-a:hover,
#graphics polygon.subarea-a.hover {
    fill: rgba(255, 112, 67, 0.38) !important;
}

#graphics polygon.subarea-b:hover,
#graphics polygon.subarea-b.hover {
    fill: rgba(102, 187, 106, 0.38) !important;
}

#graphics polygon.subarea-c:hover,
#graphics polygon.subarea-c.hover {
    fill: rgba(66, 165, 245, 0.38) !important;
}

#labels text {
    fill: var(--text-color);
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-weight: 600;
    paint-order: stroke;
    stroke: var(--accent-color);
    stroke-width: 0.15em;
    stroke-linecap: round;
    stroke-linejoin: round;
    user-select: none;
    pointer-events: none;
}

#labels tspan {
    paint-order: stroke;
    stroke: var(--accent-color);
    stroke-width: 0.15em;
    stroke-linecap: round;
    stroke-linejoin: round;
}

#labels text.target-label {
    fill: gold;
    font-weight: 700;
}

#labels text.given-label {
    fill: #8f8;
}

#labels text.guide-label {
    fill: #ffb74d;
    font-weight: 600;
}

#labels text.hover-label {
    fill: var(--select-color) !important;
    font-weight: 700;
}

#labels text.dense-label {
    display: none;
}

#labels text.dense-label.hover-label {
    display: block !important;
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

.etc-svg-btn:hover,
.etc-svg-btn.active {
    background: rgba(0, 255, 255, 0.14);
    color: #0ff;
    border-color: #0ff;
}

.etc-symbolic-hud {
    position: absolute;
    left: 10px;
    bottom: 10px;
    max-width: min(460px, calc(100% - 20px));
    background: rgba(14, 16, 22, 0.93);
    border: 1px solid rgba(0, 255, 255, 0.35);
    border-radius: 6px;
    padding: 8px 12px;
    color: #eaeaea;
    font-family: "Fira Sans Condensed", system-ui, -apple-system, sans-serif;
    font-size: 13px;
    line-height: 1.38;
    z-index: 24;
    pointer-events: none;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.58);
    opacity: 0;
    transform: translateY(4px);
    transition: opacity 0.12s ease, transform 0.12s ease;
}

.etc-symbolic-hud.is-visible {
    opacity: 1;
    transform: translateY(0);
}

.etc-hud-head {
    display: flex;
    align-items: baseline;
    gap: 7px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 4px;
    margin-bottom: 5px;
}

.etc-hud-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
    align-self: center;
}

.etc-hud-id {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-weight: 700;
    color: #0ff;
    font-size: 13px;
}

.etc-hud-title {
    font-weight: 600;
    color: #f5f5f5;
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.etc-hud-kind {
    font-size: 10.5px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #94a3b8;
}

.etc-hud-rows {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 2px 10px;
    align-items: baseline;
}

.etc-hud-key {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 11.5px;
    color: #94a3b8;
    text-align: right;
    white-space: nowrap;
}

.etc-hud-val {
    color: #f8fafc;
    font-size: 13.5px;
    overflow-wrap: anywhere;
}

.etc-hud-val .katex {
    font-size: 1.02em;
}

.etc-hud-approx {
    margin-top: 4px;
    padding-top: 3px;
    border-top: 1px dashed rgba(255, 255, 255, 0.09);
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 11px;
    color: #8b9bb4;
}

.etc-math-fallback {
    font-family: "EB Garamond", Georgia, serif;
    font-size: 1.06em;
}

.etc-math-frac {
    display: inline-flex;
    flex-direction: column;
    vertical-align: middle;
    text-align: center;
    padding: 0 2px;
    font-size: 0.88em;
    line-height: 1.05;
}

.etc-math-num {
    border-bottom: 1px solid rgba(248, 250, 252, 0.65);
    padding: 0 2px 1px;
}

.etc-math-den {
    padding: 1px 2px 0;
}

.etc-math-rad {
    border-top: 1px solid rgba(248, 250, 252, 0.6);
    padding: 0 2px;
}

.etc-graphics-panel,
.etc-act-plate {
    width: 100%;
    background: #141414;
    border: 1px solid #333;
    border-radius: 6px;
    overflow: hidden;
}

.etc-graphics-panel svg.geometor-etc-drawing,
.etc-act-plate svg.geometor-etc-drawing {
    border: none;
    border-radius: 0;
    display: block;
}

svg.geometor-etc-drawing .etc-plate-poly {
    cursor: pointer;
    transition: fill-opacity 0.14s ease, stroke 0.14s ease;
}

svg.geometor-etc-drawing .etc-plate-poly.hover {
    stroke: var(--select-color) !important;
    stroke-width: 2.8px !important;
    fill-opacity: 0.44 !important;
}

svg.geometor-etc-drawing .etc-plate-strut,
svg.geometor-etc-drawing .etc-plate-line,
svg.geometor-etc-drawing .etc-plate-circle,
svg.geometor-etc-drawing .etc-plate-pt,
svg.geometor-etc-drawing .etc-plate-panel {
    cursor: pointer;
}

svg.geometor-etc-drawing .etc-plate-strut.hover,
svg.geometor-etc-drawing .etc-plate-line.hover,
svg.geometor-etc-drawing .etc-plate-circle.hover {
    stroke: var(--select-color) !important;
    filter: drop-shadow(0 0 5px rgba(0, 255, 255, 0.72));
}

svg.geometor-etc-drawing .etc-plate-pt.hover {
    stroke: var(--select-color) !important;
    stroke-width: 3.6px !important;
    filter: drop-shadow(0 0 6px rgba(0, 255, 255, 0.85));
}

svg.geometor-etc-drawing .etc-plate-panel.hover > rect.etc-panel-border {
    stroke: var(--select-color) !important;
    stroke-width: 2.8px !important;
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
    const labelEls = labelsGroup ? Array.from(labelsGroup.querySelectorAll('text[data-point-id]')) : [];
    const subtitleEl = labelsGroup ? labelsGroup.querySelector('text.subtitle-label') : null;

    function escapeHtml(str) {
        return String(str || '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
    }

    function formatIdHtml(idStr) {
        const s = escapeHtml(idStr);
        return s.replace(/_\{([^}]+)\}/g, '<sub>$1</sub>').replace(/_([A-Za-z0-9']+)/g, '<sub>$1</sub>');
    }

    function extractBraced(src, startIdx) {
        if (src[startIdx] !== '{') return null;
        let depth = 0;
        for (let i = startIdx; i < src.length; i++) {
            if (src[i] === '{') depth++;
            else if (src[i] === '}') {
                depth--;
                if (depth === 0) {
                    return { content: src.slice(startIdx + 1, i), next: i + 1 };
                }
            }
        }
        return null;
    }

    function convertLatexFallback(tex) {
        let s = String(tex || '');
        s = s.replace(/\\left\s*([(\[{|])/g, '$1').replace(/\\right\s*([)\]}|])/g, '$1');
        s = s.replace(/\\;/g, ' ').replace(/\\,/g, '\u2009').replace(/\\quad/g, '  ');
        s = s.replace(/\\varphi|\\phi/g, 'φ')
             .replace(/\\Delta/g, 'Δ')
             .replace(/\\alpha/g, 'α')
             .replace(/\\beta/g, 'β')
             .replace(/\\gamma/g, 'γ')
             .replace(/\\cdot/g, '·')
             .replace(/\\approx/g, '≈')
             .replace(/\\infty/g, '∞');

        let out = '';
        let i = 0;
        while (i < s.length) {
            if (s.startsWith('\\frac', i)) {
                let k = i + 5;
                while (k < s.length && s[k] === ' ') k++;
                const numB = extractBraced(s, k);
                if (numB) {
                    let k2 = numB.next;
                    while (k2 < s.length && s[k2] === ' ') k2++;
                    const denB = extractBraced(s, k2);
                    if (denB) {
                        out += '<span class="etc-math-frac"><span class="etc-math-num">' +
                            convertLatexFallback(numB.content) +
                            '</span><span class="etc-math-den">' +
                            convertLatexFallback(denB.content) +
                            '</span></span>';
                        i = denB.next;
                        continue;
                    }
                }
            }
            if (s.startsWith('\\sqrt', i)) {
                let k = i + 5;
                while (k < s.length && s[k] === ' ') k++;
                const radB = extractBraced(s, k);
                if (radB) {
                    out += '√<span class="etc-math-rad">' + convertLatexFallback(radB.content) + '</span>';
                    i = radB.next;
                    continue;
                }
            }
            if ((s[i] === '_' || s[i] === '^') && i + 1 < s.length) {
                const tag = s[i] === '_' ? 'sub' : 'sup';
                if (s[i + 1] === '{') {
                    const subB = extractBraced(s, i + 1);
                    if (subB) {
                        out += `<${tag}>` + convertLatexFallback(subB.content) + `</${tag}>`;
                        i = subB.next;
                        continue;
                    }
                } else {
                    out += `<${tag}>` + escapeHtml(s[i + 1]) + `</${tag}>`;
                    i += 2;
                    continue;
                }
            }
            out += escapeHtml(s[i]);
            i++;
        }
        return out;
    }

    function renderMathHtml(latexStr, prettyStr) {
        if (!latexStr) return escapeHtml(prettyStr || '');
        if (typeof window !== 'undefined' && window.katex && typeof window.katex.renderToString === 'function') {
            try {
                return window.katex.renderToString(latexStr, { throwOnError: false, displayMode: false });
            } catch (e) {}
        }
        return '<span class="etc-math-fallback">' + convertLatexFallback(latexStr) + '</span>';
    }

    function getViewBox() {
        return svg.getAttribute('viewBox').split(/\s+/).map(Number);
    }

    function scaleViewElements() {
        const rect = svg.getBoundingClientRect();
        const widthPx = rect.width || 800;
        const vb = getViewBox();
        const unitsPerPx = vb[2] / widthPx;

        const targetRPx = parseFloat(svg.getAttribute('data-target-r-px') || '10.5');
        pointEls.forEach(c => {
            const isTarget = c.classList.contains('target') || c.classList.contains('selected');
            const isGuide = c.classList.contains('guide');
            const rPx = isTarget ? targetRPx : (isGuide ? 4.8 : 7.5);
            c.setAttribute('r', (rPx * unitsPerPx).toFixed(6));
        });

        const fontSize = 20.25 * unitsPerPx;
        const guideFontSize = 17.5 * unitsPerPx;
        labelEls.forEach(lbl => {
            const cx = parseFloat(lbl.getAttribute('data-anchor-x') || '0');
            const cy = parseFloat(lbl.getAttribute('data-anchor-y') || '0');
            const oxPx = parseFloat(lbl.getAttribute('data-offset-x') || '12');
            const oyPx = parseFloat(lbl.getAttribute('data-offset-y') || '-10.5');
            const isGuideLbl = lbl.classList.contains('guide-label');
            lbl.setAttribute('x', (cx + oxPx * unitsPerPx).toFixed(6));
            lbl.setAttribute('y', (cy + oyPx * unitsPerPx).toFixed(6));
            lbl.setAttribute('font-size', (isGuideLbl ? guideFontSize : fontSize).toFixed(6));
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
        const baseW = Math.max(initialViewBox[2] || 1.0, 0.2);
        const baseH = Math.max(initialViewBox[3] || 1.0, 0.2);
        const newW = Math.min(Math.max(w * factor, baseW * 0.002), baseW * 30.0);
        const newH = Math.min(Math.max(h * factor, baseH * 0.002), baseH * 30.0);
        const newX = focusX - relX * newW;
        const newY = focusY - relY * newH;
        setViewBox([newX, newY, newW, newH]);
    }

    function resetView() {
        setViewBox([...initialViewBox]);
    }

    let hudEl = null;

    svg._etcController = {
        zoomIn: () => zoomBy(1 / 1.25),
        zoomOut: () => zoomBy(1.25),
        resetView: resetView,
        toggleLabels: () => svg.classList.toggle('hide-labels'),
        toggleGuides: () => svg.classList.toggle('hide-guides'),
        scaleViewElements: scaleViewElements,
    };

    if (document.body && document.documentElement.tagName.toLowerCase() === 'html') {
        let stage = svg.parentElement;
        if (stage && !stage.classList.contains('etc-svg-stage')) {
            const newStage = document.createElement('div');
            newStage.className = 'etc-svg-stage';
            stage.insertBefore(newStage, svg);
            newStage.appendChild(svg);
            stage = newStage;

            const toolbar = document.createElement('div');
            toolbar.className = 'etc-svg-toolbar';
            const btns = [
                { label: '+', title: 'Zoom In (or scroll wheel)', action: () => zoomBy(1 / 1.25) },
                { label: '−', title: 'Zoom Out (or scroll wheel)', action: () => zoomBy(1.25) },
                { label: '⟲ Fit', title: 'Reset View (or double-click canvas)', action: () => resetView() },
            ];
            if (svg.querySelector('.incident')) {
                btns.push({
                    label: 'Lines',
                    toggleKey: 'lines',
                    title: 'Toggle Incident Central Lines',
                    isActive: () => svg.classList.contains('show-lines'),
                    action: () => svg.classList.toggle('show-lines'),
                });
            }
            if (labelEls.length > 0) {
                btns.push({
                    label: 'Labels',
                    toggleKey: 'labels',
                    title: 'Toggle Point Labels',
                    isActive: () => !svg.classList.contains('hide-labels'),
                    action: () => svg.classList.toggle('hide-labels'),
                });
            }
            if (svg.querySelector('.guide')) {
                btns.push({
                    label: 'Guides',
                    toggleKey: 'guides',
                    title: 'Toggle Construction Guides',
                    isActive: () => !svg.classList.contains('hide-guides'),
                    action: () => svg.classList.toggle('hide-guides'),
                });
            }
            btns.forEach(b => {
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = 'etc-svg-btn';
                if (b.toggleKey) {
                    btn.dataset.toggleKey = b.toggleKey;
                    btn.classList.toggle('active', b.isActive());
                }
                btn.textContent = b.label;
                btn.title = b.title;
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    b.action();
                    if (b.isActive) {
                        btn.classList.toggle('active', b.isActive());
                    }
                });
                toolbar.appendChild(btn);
            });
            stage.appendChild(toolbar);
        }

        if (stage) {
            hudEl = stage.querySelector('.etc-symbolic-hud');
            if (!hudEl) {
                hudEl = document.createElement('div');
                hudEl.className = 'etc-symbolic-hud';
                hudEl.setAttribute('aria-live', 'polite');
                stage.appendChild(hudEl);
            }
            svg.querySelectorAll('title').forEach(t => t.remove());
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
                    const showLines = prevSvg ? prevSvg.classList.contains('show-lines') : false;

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
                                paneSvg.classList.toggle('show-lines', showLines);
                                const paneToolbar = pane.querySelector('.etc-svg-toolbar');
                                if (paneToolbar) {
                                    const lBtn = paneToolbar.querySelector('[data-toggle-key="lines"]');
                                    if (lBtn) lBtn.classList.toggle('active', showLines);
                                    const lblBtn = paneToolbar.querySelector('[data-toggle-key="labels"]');
                                    if (lblBtn) lblBtn.classList.toggle('active', !hideLabels);
                                    const gBtn = paneToolbar.querySelector('[data-toggle-key="guides"]');
                                    if (gBtn) gBtn.classList.toggle('active', !hideGuides);
                                }
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

    function updateHud(info, fallbackId) {
        if (!hudEl) return;
        if (!info) {
            hudEl.classList.remove('is-visible');
            return;
        }
        const dotColor = info.color || '#0ff';
        const idHtml = formatIdHtml(info.ID || fallbackId || '');
        const titleHtml = escapeHtml(info.name || fallbackId || '');
        const kindHtml = escapeHtml(info.type || '');
        const symRows = Array.isArray(info.symbolic_rows) ? info.symbolic_rows : [];
        let rowsHtml = '';
        if (symRows.length > 0) {
            symRows.forEach(r => {
                rowsHtml += '<div class="etc-hud-key">' + escapeHtml(r.label) + '</div>' +
                    '<div class="etc-hud-val">' + renderMathHtml(r.latex, r.pretty) + '</div>';
            });
        } else if (Array.isArray(info.rows)) {
            info.rows.forEach(pair => {
                rowsHtml += '<div class="etc-hud-key">' + escapeHtml(pair[0]) + '</div>' +
                    '<div class="etc-hud-val">' + escapeHtml(pair[1]) + '</div>';
            });
        }
        const approxHtml = info.approx
            ? '<div class="etc-hud-approx">' + escapeHtml(info.approx) + '</div>'
            : '';
        hudEl.innerHTML =
            '<div class="etc-hud-head">' +
                '<span class="etc-hud-dot" style="background:' + escapeHtml(dotColor) + '"></span>' +
                '<span class="etc-hud-id">' + idHtml + '</span>' +
                '<span class="etc-hud-title">' + titleHtml + '</span>' +
                '<span class="etc-hud-kind">' + kindHtml + '</span>' +
            '</div>' +
            '<div class="etc-hud-rows">' + rowsHtml + '</div>' +
            approxHtml;
        hudEl.classList.add('is-visible');
    }

    let activeHoveredKey = null;

    function clearHover(clearTextRefs) {
        if (!activeHoveredKey) return;
        activeHoveredKey = null;
        svg.querySelectorAll('.hover').forEach(el => el.classList.remove('hover'));
        svg.querySelectorAll('.hover-label').forEach(el => el.classList.remove('hover-label'));
        if (highlightsGroup) {
            highlightsGroup.querySelectorAll('.highlight-segment').forEach(el => {
                el.style.display = 'none';
            });
        }
        if (hudEl) {
            hudEl.classList.remove('is-visible');
        }
        if (clearTextRefs !== false && typeof document !== 'undefined') {
            document.querySelectorAll('.geom-highlight-text').forEach(el => {
                el.classList.remove('geom-highlight-text');
            });
        }
    }

    function findSvgElement(candidateId) {
        if (!candidateId) return null;
        return svg.querySelector(`[data-id="${CSS.escape(candidateId)}"], [data-ref="${CSS.escape(candidateId)}"]`);
    }

    function resolveSingleSvgId(rawId) {
        if (!rawId) return null;
        const trimmed = rawId.trim();
        if (findSvgElement(trimmed)) return trimmed;
        const clean = trimmed.includes(':') ? trimmed.split(':').pop().trim() : trimmed;
        if (findSvgElement(clean)) return clean;

        const lineM = clean.match(/^\[\s*(\S+)\s+(\S+)\s*\]$/);
        if (lineM) {
            const cands = [
                `[ ${lineM[1]} ${lineM[2]} ]`,
                `[ ${lineM[2]} ${lineM[1]} ]`,
                `/ ${lineM[1]} ${lineM[2]} /`,
                `/ ${lineM[2]} ${lineM[1]} /`,
            ];
            for (const c of cands) {
                if (findSvgElement(c)) return c;
            }
        }

        const segM = clean.match(/^\/\s*(\S+)\s+(\S+)\s*\/$/);
        if (segM) {
            const cands = [
                `/ ${segM[1]} ${segM[2]} /`,
                `/ ${segM[2]} ${segM[1]} /`,
                `[ ${segM[1]} ${segM[2]} ]`,
                `[ ${segM[2]} ${segM[1]} ]`,
            ];
            for (const c of cands) {
                if (findSvgElement(c)) return c;
            }
        }

        const braceAllM = clean.match(/^\{\s*([\d,\s]+)\s*\}$/);
        if (braceAllM) {
            const wantNums = braceAllM[1].split(',').map(s => s.trim()).filter(Boolean);
            if (wantNums.length === 2) {
                const cands = [
                    `{ ${wantNums[0]}, ${wantNums[1]} }`,
                    `{ ${wantNums[1]}, ${wantNums[0]} }`,
                ];
                for (const c of cands) {
                    if (findSvgElement(c)) return c;
                }
            }
            if (wantNums.length >= 2) {
                const wantSet = new Set(wantNums);
                const lineEls = svg.querySelectorAll('line[data-id], line[data-ref]');
                for (const ln of lineEls) {
                    const lid = ln.getAttribute('data-id') || ln.getAttribute('data-ref') || '';
                    const lm = lid.match(/^\{\s*([\d,\s]+)\s*\}$/);
                    if (lm) {
                        const lnums = lm[1].split(',').map(s => s.trim()).filter(Boolean);
                        const shared = lnums.filter(n => wantSet.has(n));
                        if (shared.length >= 2) return lid;
                    }
                }
            }
        }

        const triM = clean.match(/^<\s*(\S+)\s+(\S+)\s+(\S+)\s*>$/);
        if (triM) {
            const want = [triM[1], triM[2], triM[3]].sort().join('|');
            const polys = svg.querySelectorAll('polygon[data-id], polygon[data-ref]');
            for (const p of polys) {
                const pid = p.getAttribute('data-id') || p.getAttribute('data-ref') || '';
                const pm = pid.match(/^<\s*(\S+)\s+(\S+)\s+(\S+)\s*>$/);
                if (pm && [pm[1], pm[2], pm[3]].sort().join('|') === want) {
                    return pid;
                }
            }
        }

        return null;
    }

    function hasElement(rawRef) {
        if (!rawRef) return false;
        const parts = String(rawRef).split(';').map(s => s.trim()).filter(Boolean);
        return parts.some(p => resolveSingleSvgId(p) !== null);
    }

    function activateHover(rawRef, highlightTextRefs) {
        if (!rawRef) return false;
        const parts = String(rawRef).split(';').map(s => s.trim()).filter(Boolean);
        const resolvedIds = parts.map(p => resolveSingleSvgId(p)).filter(Boolean);
        if (resolvedIds.length === 0) return false;

        const key = resolvedIds.join(';');
        if (activeHoveredKey === key) return true;
        clearHover(highlightTextRefs !== false);
        activeHoveredKey = key;

        let primaryInfo = null;
        let primaryId = resolvedIds[0];

        resolvedIds.forEach(id => {
            const info = elementsCatalog[id];
            if (!primaryInfo && info) {
                primaryInfo = info;
                primaryId = id;
            }
            svg.querySelectorAll(`[data-id="${CSS.escape(id)}"], [data-ref="${CSS.escape(id)}"]`).forEach(el => {
                el.classList.add('hover');
            });
            if (highlightsGroup) {
                const hl = highlightsGroup.querySelector(`[data-highlight-for="${CSS.escape(id)}"]`);
                if (hl) hl.style.display = 'inline';
            }
            let relatedPts = (info && info.related_points) ? info.related_points : [id];
            if (!info) {
                const sm = id.match(/^[\[/]\s*(\S+)\s+(\S+)\s*[\]/]$/);
                const tm = id.match(/^<\s*(\S+)\s+(\S+)\s+(\S+)\s*>$/);
                if (sm) relatedPts = [sm[1], sm[2]];
                else if (tm) relatedPts = [tm[1], tm[2], tm[3]];
            }
            relatedPts.forEach(pid => {
                const ptEl = pointsGroup ? pointsGroup.querySelector(`[data-id="${CSS.escape(pid)}"]`) : null;
                if (ptEl) ptEl.classList.add('hover');
                const lblEl = labelsGroup ? labelsGroup.querySelector(`text[data-point-id="${CSS.escape(pid)}"]`) : null;
                if (lblEl) lblEl.classList.add('hover-label');
            });
        });

        updateHud(primaryInfo, primaryId);

        if (highlightTextRefs !== false && typeof document !== 'undefined') {
            const selectors = new Set([`.geom-ref[data-ref="${CSS.escape(rawRef)}"]`]);
            resolvedIds.forEach(id => selectors.add(`.geom-ref[data-ref="${CSS.escape(id)}"]`));
            document.querySelectorAll(Array.from(selectors).join(', ')).forEach(el => {
                el.classList.add('geom-highlight-text');
            });
        }
        return true;
    }

    svg._etcController.activateHover = activateHover;
    svg._etcController.clearHover = clearHover;
    svg._etcController.hasElement = hasElement;

    if (typeof window !== 'undefined') {
        window.__etcSvgRegistry = window.__etcSvgRegistry || [];
        if (!window.__etcSvgRegistry.includes(svg)) {
            window.__etcSvgRegistry.push(svg);
        }
    }

    if (document.body && document.documentElement.tagName.toLowerCase() === 'html' && document.body.dataset.etcGeomRefSyncInit !== '1') {
        document.body.dataset.etcGeomRefSyncInit = '1';

        function isSvgVisible(s) {
            if (!s || !s.isConnected || !s._etcController) return false;
            const pane = s.closest('.etc-tab-pane');
            if (pane && !pane.classList.contains('active')) return false;
            return s.getClientRects().length > 0;
        }

        function dispatchRefHover(sourceEl, refStr) {
            if (!refStr) return;
            const reg = (window.__etcSvgRegistry || []).filter(isSvgVisible);
            const sec = sourceEl ? sourceEl.closest('section') : null;
            let targets = [];
            if (sec) {
                targets = reg.filter(s => sec.contains(s) && s._etcController.hasElement(refStr));
            }
            if (targets.length === 0) {
                targets = reg.filter(s => s._etcController.hasElement(refStr));
            }
            reg.forEach(s => {
                if (!targets.includes(s)) s._etcController.clearHover(false);
            });
            targets.forEach(s => s._etcController.activateHover(refStr, false));
            if (sourceEl && targets.length > 0) {
                sourceEl.classList.add('geom-highlight-text');
            }
        }

        function clearAllSvgHovers() {
            (window.__etcSvgRegistry || []).forEach(s => {
                if (s && s._etcController) s._etcController.clearHover(true);
            });
        }

        document.body.addEventListener('mouseover', (e) => {
            const geomEl = e.target.closest('.geom-ref[data-ref]');
            if (geomEl) {
                dispatchRefHover(geomEl, geomEl.getAttribute('data-ref'));
                return;
            }
            const refLink = e.target.closest('a.reference.internal');
            if (refLink) {
                const txt = (refLink.textContent || '').trim();
                const xm = txt.match(/^X(?:_|\()?(\d+)\)?$/);
                if (xm) {
                    dispatchRefHover(refLink, `X_${xm[1]}`);
                }
            }
        });

        document.body.addEventListener('mouseout', (e) => {
            const geomEl = e.target.closest('.geom-ref[data-ref], a.reference.internal');
            if (geomEl) {
                clearAllSvgHovers();
            }
        });
    }

    svg.addEventListener('mouseover', (event) => {
        if (isPanning) return;
        const target = event.target.closest('[data-id], [data-ref]');
        if (target && svg.contains(target)) {
            activateHover(target.getAttribute('data-id') || target.getAttribute('data-ref'));
        } else {
            clearHover();
        }
    });

    svg.addEventListener('mouseout', (event) => {
        if (isPanning) return;
        const related = event.relatedTarget ? event.relatedTarget.closest?.('[data-id], [data-ref]') : null;
        if (!related || !svg.contains(related)) {
            clearHover();
        }
    });

    svg.addEventListener('wheel', (event) => {
        event.preventDefault();
        const factor = event.deltaY > 0 ? 1.12 : (1 / 1.12);
        zoomBy(factor, event.clientX, event.clientY);
    }, { passive: false });

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

    svg.addEventListener('click', (event) => {
        if (didDrag) return;
        const pt = event.target.closest('circle[data-id]');
        if (!pt) return;
        const pid = pt.getAttribute('data-id') || '';
        const m = pid.match(/^X_(\d+)$/);
        if (m && typeof window !== 'undefined' && window.location && window.location.pathname.includes('/c-') && !window.location.pathname.includes('/x-')) {
            const slug = 'x-' + m[1].padStart(5, '0');
            window.location.href = `${slug}/index.html`;
        }
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
            except (OSError, ValueError):
                continue
    return {}


_CLASSICAL_POINT_INFO: dict[str, tuple[str, str]] = {
    "A": ("Vertex A", "Reference triangle vertex at origin (0, 0)"),
    "B": ("Vertex B", "Reference triangle baseline vertex on positive x-axis"),
    "C": ("Vertex C", "Reference triangle apex constructed in upper half-plane"),
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
    "I_a": ("Angle Bisector Foot I_a on BC", "Incentral triangle vertex opposite A"),
    "I_b": ("Angle Bisector Foot I_b on CA", "Incentral triangle vertex opposite B"),
    "I_c": ("Angle Bisector Foot I_c on AB", "Incentral triangle vertex opposite C"),
    "J_a": ("A-Excenter J_a", "Excentral triangle vertex opposite A"),
    "J_b": ("B-Excenter J_b", "Excentral triangle vertex opposite B"),
    "J_c": ("C-Excenter J_c", "Excentral triangle vertex opposite C"),
    "K_a": ("Anticomplementary Vertex K_a", "Anticomplementary triangle vertex opposite A"),
    "K_b": ("Anticomplementary Vertex K_b", "Anticomplementary triangle vertex opposite B"),
    "K_c": ("Anticomplementary Vertex K_c", "Anticomplementary triangle vertex opposite C"),
    "Tan_a": ("Tangential Vertex Tan_a", "Intersection of circumcircle tangents at B and C"),
    "Tan_b": ("Tangential Vertex Tan_b", "Intersection of circumcircle tangents at C and A"),
    "Tan_c": ("Tangential Vertex Tan_c", "Intersection of circumcircle tangents at A and B"),
    "Sym_a": ("Symmedian Foot Sym_a on BC", "Symmedial triangle vertex opposite A"),
    "Sym_b": ("Symmedian Foot Sym_b on CA", "Symmedial triangle vertex opposite B"),
    "Sym_c": ("Symmedian Foot Sym_c on AB", "Symmedial triangle vertex opposite C"),
    "Eu_a": ("Euler Vertex Eu_a", "Midpoint of segment A–X_4 (Euler triangle vertex)"),
    "Eu_b": ("Euler Vertex Eu_b", "Midpoint of segment B–X_4 (Euler triangle vertex)"),
    "Eu_c": ("Euler Vertex Eu_c", "Midpoint of segment C–X_4 (Euler triangle vertex)"),
    "Ref_a": ("Reflection Ref_a of A in BC", "Vertex of reflection triangle opposite A"),
    "Ref_b": ("Reflection Ref_b of B in CA", "Vertex of reflection triangle opposite B"),
    "Ref_c": ("Reflection Ref_c of C in AB", "Vertex of reflection triangle opposite C"),
    "P_a": ("Cevian Trace P_a on BC", "Intersection of cevian from A with sideline BC"),
    "P_b": ("Cevian Trace P_b on CA", "Intersection of cevian from B with sideline CA"),
    "P_c": ("Cevian Trace P_c on AB", "Intersection of cevian from C with sideline AB"),
    "A'": ("Auxiliary Apex A'", "Constructed apex opposite vertex A"),
    "B'": ("Auxiliary Apex B'", "Constructed apex opposite vertex B"),
    "C'": ("Auxiliary Apex C'", "Constructed apex opposite vertex C"),
    "Nap_a": ("Napoleon Center Nap_a", "Centroid of equilateral triangle on BC"),
    "Nap_b": ("Napoleon Center Nap_b", "Centroid of equilateral triangle on CA"),
    "Nap_c": ("Napoleon Center Nap_c", "Centroid of equilateral triangle on AB"),
    "Nap'_a": ("Inner Napoleon Center Nap'_a", "Centroid of inward equilateral triangle on BC"),
    "Nap'_b": ("Inner Napoleon Center Nap'_b", "Centroid of inward equilateral triangle on CA"),
    "Nap'_c": ("Inner Napoleon Center Nap'_c", "Centroid of inward equilateral triangle on AB"),
    "N_A": ("Napoleon Center N_A", "Centroid of equilateral triangle on BC"),
    "N_B": ("Napoleon Center N_B", "Centroid of equilateral triangle on CA"),
    "N_C": ("Napoleon Center N_C", "Centroid of equilateral triangle on AB"),
    "Cm_a": ("Circummedial Vertex Cm_a", "Second intersection of A-median with circumcircle"),
    "Cm_b": ("Circummedial Vertex Cm_b", "Second intersection of B-median with circumcircle"),
    "Cm_c": ("Circummedial Vertex Cm_c", "Second intersection of C-median with circumcircle"),
    "H'_a": ("Orthic-of-Orthic Foot H'_a", "Altitude foot of orthic triangle △H_a H_b H_c opposite H_a"),
    "H'_b": ("Orthic-of-Orthic Foot H'_b", "Altitude foot of orthic triangle △H_a H_b H_c opposite H_b"),
    "H'_c": ("Orthic-of-Orthic Foot H'_c", "Altitude foot of orthic triangle △H_a H_b H_c opposite H_c"),
    "O_A": ("Kosnita Circumcenter O_A", "Circumcenter of subtriangle △BOC (O = X_3)"),
    "O_B": ("Kosnita Circumcenter O_B", "Circumcenter of subtriangle △COA (O = X_3)"),
    "O_C": ("Kosnita Circumcenter O_C", "Circumcenter of subtriangle △AOB (O = X_3)"),
    "S_c": ("Spieker Touchpoint S_c", "Tangency point of Spieker circle on medial side M_a M_b"),
    "R_a": ("Radius Point R_a", "Euclid I.22 baseline guide point"),
    "R_b": ("Radius Point R_b", "Euclid I.22 baseline guide point"),
}

_CONSTRUCTION_LINE_INFO: dict[str, tuple[str, str]] = {
    "[ A B ]": ("Sideline AB (Side c)", "Reference triangle baseline through A and B"),
    "[ B C ]": ("Sideline BC (Side a)", "Reference triangle sideline opposite vertex A"),
    "[ C A ]": ("Sideline CA (Side b)", "Reference triangle sideline opposite vertex B"),
    "[ A M_a ]": ("A-Median", "Median from vertex A to midpoint M_a of BC"),
    "[ B M_b ]": ("B-Median", "Median from vertex B to midpoint M_b of CA"),
    "[ C M_c ]": ("C-Median", "Median from vertex C to midpoint M_c of AB"),
    "[ A H_a ]": ("A-Altitude", "Altitude from vertex A perpendicular to BC at H_a"),
    "[ B H_b ]": ("B-Altitude", "Altitude from vertex B perpendicular to CA at H_b"),
    "[ C H_c ]": ("C-Altitude", "Altitude from vertex C perpendicular to AB at H_c"),
    "[ X_3 M_a ]": ("Perpendicular Bisector of BC", "Perpendicular bisector through M_a and Circumcenter X_3"),
    "[ X_3 M_b ]": ("Perpendicular Bisector of CA", "Perpendicular bisector through M_b and Circumcenter X_3"),
    "[ X_3 M_c ]": ("Perpendicular Bisector of AB", "Perpendicular bisector through M_c and Circumcenter X_3"),
    "[ A X_1 ]": ("Internal Angle Bisector of ∠A", "Bisector of interior angle A through Incenter X_1"),
    "[ B X_1 ]": ("Internal Angle Bisector of ∠B", "Bisector of interior angle B through Incenter X_1"),
    "[ C X_1 ]": ("Internal Angle Bisector of ∠C", "Bisector of interior angle C through Incenter X_1"),
    "[ A I_a ]": ("Internal Angle Bisector of ∠A", "Bisector of interior angle A meeting BC at I_a"),
    "[ B I_b ]": ("Internal Angle Bisector of ∠B", "Bisector of interior angle B meeting CA at I_b"),
    "[ C I_c ]": ("Internal Angle Bisector of ∠C", "Bisector of interior angle C meeting AB at I_c"),
    "[ A Tan_a ]": ("A-Symmedian", "Symmedian from vertex A to tangential vertex Tan_a"),
    "[ B Tan_b ]": ("B-Symmedian", "Symmedian from vertex B to tangential vertex Tan_b"),
    "[ C Tan_c ]": ("C-Symmedian", "Symmedian from vertex C to tangential vertex Tan_c"),
    "[ A Sym_a ]": ("A-Symmedian", "Symmedian from vertex A meeting BC at Sym_a"),
    "[ B Sym_b ]": ("B-Symmedian", "Symmedian from vertex B meeting CA at Sym_b"),
    "[ C Sym_c ]": ("C-Symmedian", "Symmedian from vertex C meeting AB at Sym_c"),
    "[ A T_a ]": ("Gergonne Cevian A–T_a", "Cevian from vertex A to incircle touchpoint T_a"),
    "[ B T_b ]": ("Gergonne Cevian B–T_b", "Cevian from vertex B to incircle touchpoint T_b"),
    "[ C T_c ]": ("Gergonne Cevian C–T_c", "Cevian from vertex C to incircle touchpoint T_c"),
    "[ A N_a ]": ("Nagel Cevian (Splitter) A–N_a", "Perimeter-bisecting cevian from A to excircle touchpoint N_a"),
    "[ B N_b ]": ("Nagel Cevian (Splitter) B–N_b", "Perimeter-bisecting cevian from B to excircle touchpoint N_b"),
    "[ C N_c ]": ("Nagel Cevian (Splitter) C–N_c", "Perimeter-bisecting cevian from C to excircle touchpoint N_c"),
    "[ J_a M_a ]": ("Mittenpunkt Symmedian J_a–M_a", "Line joining A-excenter J_a to side midpoint M_a"),
    "[ J_b M_b ]": ("Mittenpunkt Symmedian J_b–M_b", "Line joining B-excenter J_b to side midpoint M_b"),
    "[ J_c M_c ]": ("Mittenpunkt Symmedian J_c–M_c", "Line joining C-excenter J_c to side midpoint M_c"),
    "[ A P_a ]": ("A-Cevian A–P_a", "Cevian from vertex A through target center to trace P_a on BC"),
    "[ B P_b ]": ("B-Cevian B–P_b", "Cevian from vertex B through target center to trace P_b on CA"),
    "[ C P_c ]": ("C-Cevian C–P_c", "Cevian from vertex C through target center to trace P_c on AB"),
    "[ A A' ]": ("Apex Cevian A–A'", "Cevian joining vertex A to constructed apex A'"),
    "[ B B' ]": ("Apex Cevian B–B'", "Cevian joining vertex B to constructed apex B'"),
    "[ C C' ]": ("Apex Cevian C–C'", "Cevian joining vertex C to constructed apex C'"),
    "[ A O_A ]": ("Kosnita Cevian A–O_A", "Line from vertex A to circumcenter O_A of △BOC"),
    "[ B O_B ]": ("Kosnita Cevian B–O_B", "Line from vertex B to circumcenter O_B of △COA"),
    "[ C O_C ]": ("Kosnita Cevian C–O_C", "Line from vertex C to circumcenter O_C of △AOB"),
    "[ Cm_a Tan_a ]": ("Exeter Perspectrix Line Cm_a–Tan_a", "Line joining circummedial vertex Cm_a to tangential vertex Tan_a"),
    "[ Cm_b Tan_b ]": ("Exeter Perspectrix Line Cm_b–Tan_b", "Line joining circummedial vertex Cm_b to tangential vertex Tan_b"),
    "[ Cm_c Tan_c ]": ("Exeter Perspectrix Line Cm_c–Tan_c", "Line joining circummedial vertex Cm_c to tangential vertex Tan_c"),
    "[ A H'_a ]": ("Orthic-of-Orthic Cevian A–H'_a", "Line from vertex A to orthic-of-orthic foot H'_a"),
    "[ B H'_b ]": ("Orthic-of-Orthic Cevian B–H'_b", "Line from vertex B to orthic-of-orthic foot H'_b"),
    "[ C H'_c ]": ("Orthic-of-Orthic Cevian C–H'_c", "Line from vertex C to orthic-of-orthic foot H'_c"),
    "[ A Nap_a ]": ("Outer Napoleon Cevian A–Nap_a", "Line from vertex A to outer Napoleon center Nap_a"),
    "[ B Nap_b ]": ("Outer Napoleon Cevian B–Nap_b", "Line from vertex B to outer Napoleon center Nap_b"),
    "[ C Nap_c ]": ("Outer Napoleon Cevian C–Nap_c", "Line from vertex C to outer Napoleon center Nap_c"),
    "[ A Nap'_a ]": ("Inner Napoleon Cevian A–Nap'_a", "Line from vertex A to inner Napoleon center Nap'_a"),
    "[ B Nap'_b ]": ("Inner Napoleon Cevian B–Nap'_b", "Line from vertex B to inner Napoleon center Nap'_b"),
    "[ C Nap'_c ]": ("Inner Napoleon Cevian C–Nap'_c", "Line from vertex C to inner Napoleon center Nap'_c"),
}

_KNOWN_SEGMENT_INFO: dict[str, tuple[str, str]] = {
    "/ X_1 T_a /": ("Orthogonal Inradius Strut X_1–T_a", "Directed trilinear distance α = r perpendicular to BC"),
    "/ X_1 T_b /": ("Orthogonal Inradius Strut X_1–T_b", "Directed trilinear distance β = r perpendicular to CA"),
    "/ X_1 T_c /": ("Orthogonal Inradius Strut X_1–T_c", "Directed trilinear distance γ = r perpendicular to AB"),
}

_KNOWN_CIRCLE_INFO: dict[str, tuple[str, str]] = {
    "circumcircle": (
        "Circumcircle of △ABC",
        "Passes through vertices A, B, C; centered at X_3 CIRCUMCENTER",
    ),
    "incircle": (
        "Incircle of △ABC",
        "Inscribed circle tangent to sidelines at T_a, T_b, T_c; centered at X_1 INCENTER",
    ),
    "nine_point_circle": (
        "Nine-Point Circle (Euler / Feuerbach Circle)",
        "Passes through side midpoints M_a, M_b, M_c and altitude feet H_a, H_b, H_c; centered at X_5",
    ),
    "spieker_circle": (
        "Spieker Circle",
        "Incircle of the medial triangle △M_a M_b M_c; centered at X_10 SPIEKER CENTER",
    ),
    "bevan_circle": (
        "Bevan Circle",
        "Circumcircle of the excentral triangle △J_a J_b J_c; centered at X_40 BEVAN POINT",
    ),
    "brocard_circle": (
        "Brocard Circle (Seven-Point Circle)",
        "Circle on diameter X_3–X_6 passing through Brocard points and X_15, X_16; centered at X_182",
    ),
    "orthocentroidal_circle": (
        "Orthocentroidal Circle",
        "Circle on diameter X_2–X_4 (Centroid to Orthocenter); centered at X_381",
    ),
    "fuhrmann_circle": (
        "Fuhrmann Circle",
        "Circle on diameter X_4–X_8 (Orthocenter to Nagel Point); centered at X_427",
    ),
    "A-Apollonian circle": (
        "A-Apollonian Circle",
        "Circle through A whose diameter on BC is bounded by the internal and external angle bisectors of ∠A",
    ),
    "B-Apollonian circle": (
        "B-Apollonian Circle",
        "Circle through B whose diameter on CA is bounded by the internal and external angle bisectors of ∠B",
    ),
    "C-Apollonian circle": (
        "C-Apollonian Circle",
        "Circle through C whose diameter on AB is bounded by the internal and external angle bisectors of ∠C",
    ),
    "( A R_b )": (
        "Euclid I.22 Guide Circle (A)",
        "Baseline construction circle centered at A",
    ),
    "( B R_a )": (
        "Euclid I.22 Guide Circle (B)",
        "Baseline construction circle centered at B",
    ),
}

_KNOWN_POLYGON_INFO: dict[str, tuple[str, str]] = {
    "< A B C >": ("Reference Triangle △ABC", "Primary exact symbolic reference triangle"),
    "< X_1 B C >": ("Barycentric Sub-Triangle △X_1BC (Δ_a)", "Sub-area opposite A proportional to barycentric weight u = a"),
    "< X_1 C A >": ("Barycentric Sub-Triangle △X_1CA (Δ_b)", "Sub-area opposite B proportional to barycentric weight v = b"),
    "< X_1 A B >": ("Barycentric Sub-Triangle △X_1AB (Δ_c)", "Sub-area opposite C proportional to barycentric weight w = c"),
    "< M_a M_b M_c >": ("Medial Triangle △M_a M_b M_c", "Formed by the midpoints of sides BC, CA, AB"),
    "< H_a H_b H_c >": ("Orthic Triangle △H_a H_b H_c", "Pedal triangle of Orthocenter X_4 (altitude feet)"),
    "< T_a T_b T_c >": ("Intouch (Contact) Triangle △T_a T_b T_c", "Contact triangle of Incircle touchpoints on BC, CA, AB"),
    "< N_a N_b N_c >": ("Extouch Triangle △N_a N_b N_c", "Contact triangle of Excircle touchpoints on BC, CA, AB"),
    "< I_a I_b I_c >": ("Incentral Triangle △I_a I_b I_c", "Cevian triangle of Incenter X_1 (angle bisector feet)"),
    "< J_a J_b J_c >": ("Excentral Triangle △J_a J_b J_c", "Anticevian triangle of Incenter X_1 (the three excenters)"),
    "< K_a K_b K_c >": ("Anticomplementary Triangle △K_a K_b K_c", "Formed by lines through A, B, C parallel to opposite sides"),
    "< Tan_a Tan_b Tan_c >": ("Tangential Triangle △Tan_a Tan_b Tan_c", "Bounded by tangents to the circumcircle at A, B, C"),
    "< Sym_a Sym_b Sym_c >": ("Symmedial Triangle △Sym_a Sym_b Sym_c", "Cevian triangle of Symmedian Point X_6"),
    "< Eu_a Eu_b Eu_c >": ("Euler (Feuerbach) Triangle △Eu_a Eu_b Eu_c", "Midpoints of segments joining A, B, C to Orthocenter X_4"),
    "< Ref_a Ref_b Ref_c >": ("Reflection Triangle △Ref_a Ref_b Ref_c", "Reflections of vertices A, B, C across opposite sidelines"),
    "< Cm_a Cm_b Cm_c >": ("Circummedial Triangle △Cm_a Cm_b Cm_c", "Endpoints of medians of △ABC extended to the circumcircle"),
    "< H'_a H'_b H'_c >": ("Orthic-of-Orthic Triangle △H'_a H'_b H'_c", "Orthic triangle of the orthic triangle △H_a H_b H_c"),
    "< O_A O_B O_C >": ("Kosnita Triangle △O_A O_B O_C", "Circumcenters of △BOC, △COA, △AOB where O = X_3"),
    "< P_a P_b P_c >": ("Cevian Triangle △P_a P_b P_c", "Traces of cevians through target center on BC, CA, AB"),
    "< A' B' C' >": ("Auxiliary Triangle △A'B'C'", "Derived triangle"),
    "< Nap_a Nap_b Nap_c >": ("Outer Napoleon Triangle △Nap_a Nap_b Nap_c", "Equilateral triangle formed by centers of outward side equilateral triangles"),
    "< Nap'_a Nap'_b Nap'_c >": ("Inner Napoleon Triangle △Nap'_a Nap'_b Nap'_c", "Equilateral triangle formed by centers of inward side equilateral triangles"),
    "< N_A N_B N_C >": ("Napoleon Triangle △N_A N_B N_C", "Equilateral triangle formed by centers of side equilateral triangles"),
    "< B C A' >": ("Equilateral Triangle on BC", "Equilateral triangle erected on side BC"),
    "< C A B' >": ("Equilateral Triangle on CA", "Equilateral triangle erected on side CA"),
    "< A B C' >": ("Equilateral Triangle on AB", "Equilateral triangle erected on side AB"),
}


def _short_point_name(pid: str, center_names: dict[str, str]) -> str:
    """Return a concise human-readable name for a point ID (`X_n` or classical vertex)."""
    m = re.match(r"^X(?:_|\()(\d+)\)?$", pid)
    if m:
        num_str = m.group(1)
        raw = center_names.get(num_str, "")
        if raw:
            if len(raw) > 48 and "(" in raw:
                raw = raw.split("(")[0].strip()
            return raw
        return f"Triangle Center X_{num_str}"
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
        ("Euler Line", "Collinear line of X_2 Centroid, X_3 Circumcenter, X_4 Orthocenter, X_5 Nine-Point Center, X_20, X_30", 2, 3),
        ("Nagel Line", "Collinear line of X_1 Incenter, X_2 Centroid, X_8 Nagel Point, X_10 Spieker Center", 1, 2),
        ("OI Line (Incenter–Circumcenter Line)", "Collinear line of X_1 Incenter, X_3 Circumcenter, X_40 Bevan Point, X_55, X_56", 1, 3),
        ("Brocard Axis", "Collinear line of X_3 Circumcenter, X_6 Symmedian Point, X_15 & X_16 Isodynamic Points", 3, 6),
        ("Soddy Line", "Collinear line of X_1 Incenter, X_7 Gergonne Point, X_20 de Longchamps Point, X_175, X_176", 1, 7),
        ("Feuerbach Line", "Collinear line of X_1 Incenter, X_5 Nine-Point Center, X_11 Feuerbach Point", 1, 5),
        ("Van Aubel Line", "Collinear line of X_4 Orthocenter and X_6 Symmedian Point", 4, 6),
        ("Incenter–Symmedian Line", "Collinear line of X_1 Incenter, X_6 Symmedian Point, X_9 Mittenpunkt", 1, 6),
        ("Centroid–Symmedian Line", "Collinear line of X_2 Centroid, X_6 Symmedian Point, X_39 Brocard Midpoint", 2, 6),
        ("Nine-Point–Symmedian Line", "Collinear line of X_5 Nine-Point Center and X_6 Symmedian Point", 5, 6),
        ("Incenter–Orthocenter Line", "Collinear line of X_1 Incenter and X_4 Orthocenter", 1, 4),
        ("Centroid–Gergonne Line", "Collinear line of X_2 Centroid, X_7 Gergonne Point, X_9 Mittenpunkt", 2, 7),
        ("Gergonne–Nagel Line", "Collinear line of X_7 Gergonne Point and X_8 Nagel Point", 7, 8),
        ("Fuhrmann Line", "Collinear line of X_4 Orthocenter and X_8 Nagel Point", 4, 8),
        ("Orthocenter–Spieker Line", "Collinear line of X_4 Orthocenter and X_10 Spieker Center", 4, 10),
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


def _format_triple_latex(
    u: sp.Expr, v: sp.Expr, w: sp.Expr, *, kepler_phi: bool = False
) -> str:
    return (
        f"{format_symbolic_latex(u, kepler_phi=kepler_phi)} : "
        f"{format_symbolic_latex(v, kepler_phi=kepler_phi)} : "
        f"{format_symbolic_latex(w, kepler_phi=kepler_phi)}"
    )


def _format_triple_pretty(
    u: sp.Expr, v: sp.Expr, w: sp.Expr, *, kepler_phi: bool = False
) -> str:
    return (
        f"{format_symbolic_pretty(u, kepler_phi=kepler_phi)} : "
        f"{format_symbolic_pretty(v, kepler_phi=kepler_phi)} : "
        f"{format_symbolic_pretty(w, kepler_phi=kepler_phi)}"
    )


def _format_exact_line_eq(
    la: sp.Expr,
    lb: sp.Expr,
    lc: sp.Expr,
    *,
    tri_obj: SymbolicTriangle | None = None,
    kepler_phi: bool = False,
    simplify_fn: Any = clean_expr,
) -> tuple[str, str]:
    """Format exact homogeneous line equation ``la*x + lb*y + lc = 0`` as ``(latex, pretty)``."""
    eff_tri = tri_obj if isinstance(tri_obj, SymbolicTriangle) else get_canonical_triangle("heronian")
    ra, rb, rc = reduce_homogeneous_triple(la, lb, lc, eff_tri)
    for coeff in (ra, rb, rc):
        if not zero_test(coeff):
            if exact_sign(coeff) < 0:
                ra = simplify_fn(-ra)
                rb = simplify_fn(-rb)
                rc = simplify_fn(-rc)
            break

    latex_parts: list[str] = []
    pretty_parts: list[str] = []
    for coeff, var_str in ((ra, "x"), (rb, "y"), (rc, "")):
        if zero_test(coeff):
            continue
        sgn = exact_sign(coeff)
        mag = simplify_fn(-coeff) if sgn < 0 else coeff
        ml = format_symbolic_latex(mag, kepler_phi=kepler_phi)
        mp = format_symbolic_pretty(mag, kepler_phi=kepler_phi)

        if var_str:
            if zero_test(mag - sp.Integer(1)):
                term_l = var_str
                term_p = var_str
            elif isinstance(mag, sp.Add) or (" + " in mp or " - " in mp):
                term_l = f"\\left({ml}\\right){var_str}"
                term_p = f"({mp}){var_str}"
            else:
                term_l = f"{ml}{var_str}"
                term_p = f"{mp}{var_str}"
        else:
            term_l = ml
            term_p = mp

        if not latex_parts:
            if sgn < 0:
                latex_parts.append(f"-{term_l}")
                pretty_parts.append(f"-{term_p}")
            else:
                latex_parts.append(term_l)
                pretty_parts.append(term_p)
        else:
            op = "-" if sgn < 0 else "+"
            latex_parts.append(f" {op} {term_l}")
            pretty_parts.append(f" {op} {term_p}")

    if not latex_parts:
        return ("0 = 0", "0 = 0")
    return ("".join(latex_parts) + " = 0", "".join(pretty_parts) + " = 0")


def _format_exact_circle_eq(
    hx: sp.Expr,
    ky: sp.Expr,
    qr: sp.Expr,
    *,
    kepler_phi: bool = False,
    simplify_fn: Any = clean_expr,
) -> tuple[str, str]:
    """Format exact circle equation ``(x - h)^2 + (y - k)^2 = Q_r`` as ``(latex, pretty)``."""

    def _axis_sq(var_name: str, val: sp.Expr) -> tuple[str, str]:
        if zero_test(val):
            return (f"{var_name}^2", f"{var_name}²")
        sgn = exact_sign(val)
        mag = simplify_fn(-val) if sgn < 0 else val
        ml = format_symbolic_latex(mag, kepler_phi=kepler_phi)
        mp = format_symbolic_pretty(mag, kepler_phi=kepler_phi)
        op = "-" if sgn > 0 else "+"
        if isinstance(mag, sp.Add) or (" + " in mp or " - " in mp):
            return (f"\\left({var_name} {op} \\left({ml}\\right)\\right)^2", f"({var_name} {op} ({mp}))²")
        return (f"\\left({var_name} {op} {ml}\\right)^2", f"({var_name} {op} {mp})²")

    xl, xp = _axis_sq("x", hx)
    yl, yp = _axis_sq("y", ky)
    qrl = format_symbolic_latex(qr, kepler_phi=kepler_phi)
    qrp = format_symbolic_pretty(qr, kepler_phi=kepler_phi)
    return (f"{xl} + {yl} = {qrl}", f"{xp} + {yp} = {qrp}")


def _enrich_elements_catalog(
    elements: list[dict[str, Any]],
    points_by_id: dict[str, dict[str, Any]],
    tri_span: float = 1.0,
) -> dict[str, dict[str, Any]]:
    """Build a rich metadata dictionary keyed by element ID for interactive hover cards."""
    center_names = _load_center_names()
    A = points_by_id.get("A")
    B = points_by_id.get("B")
    C = points_by_id.get("C")
    named_lines = _build_named_central_lines_xy(A, B, C)
    line_tol = max(tri_span, 1.0) * 1e-4

    catalog: dict[str, dict[str, Any]] = {}

    for el in elements:
        eid = el["ID"]
        etype = el["type"]
        classes = el.get("classes") or []
        sym = el.get("symbolic") or {}

        if etype == "point":
            px, py = el["x"], el["y"]
            is_target = "target" in classes or "selected" in classes
            is_given = "given" in classes
            color = "gold" if is_target else ("#6F6" if is_given else ("orange" if el["guide"] else "#0ff"))

            m = re.match(r"^X(?:_|\()(\d+)\)?$", eid)
            if m:
                c_num_str = m.group(1)
                c_name = center_names.get(c_num_str, f"Triangle Center X_{c_num_str}")
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
                rows.append(("from", ", ".join(el["parents"])))

            sym_rows: list[dict[str, str]] = []
            if sym.get("coords_latex"):
                sym_rows.append(
                    {
                        "label": "(x, y)",
                        "latex": sym["coords_latex"],
                        "pretty": sym.get("coords_pretty", ""),
                    }
                )
            if sym.get("trilinear_latex"):
                sym_rows.append(
                    {
                        "label": "trilinear",
                        "latex": sym["trilinear_latex"],
                        "pretty": sym.get("trilinear_pretty", ""),
                    }
                )
            if sym.get("barycentric_latex"):
                sym_rows.append(
                    {
                        "label": "bary",
                        "latex": sym["barycentric_latex"],
                        "pretty": sym.get("barycentric_pretty", ""),
                    }
                )
            if el.get("parents"):
                p_str = ", ".join(el["parents"])
                sym_rows.append({"label": "from", "latex": "", "pretty": p_str})

            catalog[eid] = {
                "ID": eid,
                "type": "point",
                "classes": classes,
                "color": color,
                "name": c_name,
                "subtitle": subtitle,
                "rows": rows,
                "symbolic_rows": sym_rows,
                "approx": f"≈ ({px:.6f}, {py:.6f})",
                "related_points": [eid],
            }

        elif etype == "segment":
            pts_list = el.get("points") or []
            p1_id = pts_list[0] if len(pts_list) > 0 else ""
            p2_id = pts_list[1] if len(pts_list) > 1 else ""
            p1 = points_by_id.get(p1_id)
            p2 = points_by_id.get(p2_id)
            seg_name, subtitle = _KNOWN_SEGMENT_INFO.get(
                eid,
                (f"Segment {p1_id}–{p2_id}", f"Segment joining {p1_id} and {p2_id}"),
            )
            color = "gold"
            seg_len = (
                math.hypot(p2["x"] - p1["x"], p2["y"] - p1["y"])
                if (p1 and p2)
                else 0.0
            )
            rows = [("pts", f"{p1_id}, {p2_id}"), ("len", f"{seg_len:.4f}")]
            sym_rows = []
            if sym.get("length_latex"):
                sym_rows.append(
                    {
                        "label": "length",
                        "latex": sym["length_latex"],
                        "pretty": sym.get("length_pretty", ""),
                    }
                )
            if sym.get("quadrance_latex"):
                sym_rows.append(
                    {
                        "label": "Q",
                        "latex": sym["quadrance_latex"],
                        "pretty": sym.get("quadrance_pretty", ""),
                    }
                )
            if sym.get("spread_latex"):
                sym_rows.append(
                    {
                        "label": "spread",
                        "latex": sym["spread_latex"],
                        "pretty": sym.get("spread_pretty", ""),
                    }
                )
            catalog[eid] = {
                "ID": eid,
                "type": "segment",
                "classes": classes,
                "color": color,
                "name": seg_name,
                "subtitle": subtitle,
                "rows": rows,
                "symbolic_rows": sym_rows,
                "approx": f"≈ length {seg_len:.6f}",
                "related_points": [pid for pid in (p1_id, p2_id) if pid],
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
                for nl_name, nl_desc, nl_p1, nl_p2 in named_lines:
                    if (
                        _dist_point_to_line(p1["x"], p1["y"], nl_p1[0], nl_p1[1], nl_p2[0], nl_p2[1]) < line_tol
                        and _dist_point_to_line(p2["x"], p2["y"], nl_p1[0], nl_p1[1], nl_p2[0], nl_p2[1]) < line_tol
                    ):
                        line_name = nl_name
                        subtitle = nl_desc
                        break
                if not line_name:
                    m_brace = re.match(r"^\{\s*(\d+)\s*,\s*(\d+)\s*\}$", eid)
                    if m_brace:
                        i_s, j_s = m_brace.group(1), m_brace.group(2)
                        line_name = f"Central Line L({i_s}, {j_s})"
                        subtitle = f"Through X_{i_s} ({p1_short}) and X_{j_s} ({p2_short})"
                    else:
                        line_name = f"Line {eid}"

            if "golden" in classes or "euler" in classes or "central_line" in classes or eid.startswith("{"):
                color_token = get_central_line_color_token(eid, line_name)
                color = token_hex(color_token)
            elif "sideline" in classes:
                color_token = ""
                color = "#cbd5e1"
            else:
                color_token = "gold"
                color = token_hex("gold")
            rows = [("pts", thru_desc)]
            approx_str = ""
            if p1 and p2:
                seg_len = math.hypot(p2["x"] - p1["x"], p2["y"] - p1["y"])
                rows.append(("len", f"{seg_len:.4f}"))
                eq_flt = _format_line_eq(p1["x"], p1["y"], p2["x"], p2["y"])
                rows.append(("eq", eq_flt))
                approx_str = f"≈ {eq_flt}  (|{p1_id}{p2_id}| ≈ {seg_len:.6f})"

            sym_rows = [{"label": "thru", "latex": "", "pretty": f"{p1_id}, {p2_id}"}]
            if sym.get("eq_latex"):
                sym_rows.append(
                    {
                        "label": "eq",
                        "latex": sym["eq_latex"],
                        "pretty": sym.get("eq_pretty", ""),
                    }
                )
            if sym.get("quadrance_latex"):
                sym_rows.append(
                    {
                        "label": "Q",
                        "latex": sym["quadrance_latex"],
                        "pretty": sym.get("quadrance_pretty", ""),
                    }
                )
            if sym.get("spread_latex"):
                sym_rows.append(
                    {
                        "label": "spread",
                        "latex": sym["spread_latex"],
                        "pretty": sym.get("spread_pretty", ""),
                    }
                )

            catalog[eid] = {
                "ID": eid,
                "type": "line",
                "classes": classes,
                "color": color,
                "color_token": color_token,
                "name": line_name,
                "subtitle": subtitle,
                "rows": rows,
                "symbolic_rows": sym_rows,
                "approx": approx_str,
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
                pretty_id = eid.replace("_", " ").strip()
                if "circle" in pretty_id.lower():
                    c_name = pretty_id[0].upper() + pretty_id[1:]
                elif ctr_short.upper().startswith("CENTER OF "):
                    c_name = ctr_short[10:].strip().title()
                else:
                    c_name = f"Circle {eid}"
                subtitle = f"Centered at {ctr_id} ({ctr_short})"

            color_token = get_circle_color_token(eid, classes)
            color = token_hex(color_token)
            rows = [("ctr", f"{ctr_id} ({ctr_short})")]
            approx_str = f"≈ r = {r_val:.6f}, Q_r = {r_val * r_val:.6f}"
            if ctr:
                hx, ky = ctr["x"], ctr["y"]
                rows.append(("h, k", f"({hx:.4f}, {ky:.4f})"))
                rows.append(("r", f"{r_val:.4f}"))
                h_sign = "-" if hx >= 0 else "+"
                k_sign = "-" if ky >= 0 else "+"
                rows.append(("eq", f"(x {h_sign} {abs(hx):.3f})² + (y {k_sign} {abs(ky):.3f})² = {r_val*r_val:.4f}"))
            if rad_id:
                rows.append(("pass", f"{rad_id} ({_short_point_name(rad_id, center_names)})"))

            sym_rows = [{"label": "center", "latex": "", "pretty": f"{ctr_id} ({ctr_short})"}]
            if sym.get("radius_latex"):
                sym_rows.append(
                    {
                        "label": "r",
                        "latex": sym["radius_latex"],
                        "pretty": sym.get("radius_pretty", ""),
                    }
                )
            if sym.get("quadrance_latex"):
                sym_rows.append(
                    {
                        "label": "Q_r",
                        "latex": sym["quadrance_latex"],
                        "pretty": sym.get("quadrance_pretty", ""),
                    }
                )
            if sym.get("eq_latex"):
                sym_rows.append(
                    {
                        "label": "eq",
                        "latex": sym["eq_latex"],
                        "pretty": sym.get("eq_pretty", ""),
                    }
                )

            rel_pts = [ctr_id] + ([rad_id] if rad_id else [])
            catalog[eid] = {
                "ID": eid,
                "type": "circle",
                "classes": classes,
                "color": color,
                "color_token": color_token,
                "name": c_name,
                "subtitle": subtitle,
                "rows": rows,
                "symbolic_rows": sym_rows,
                "approx": approx_str,
                "related_points": rel_pts,
            }

        elif etype == "polygon":
            v_ids = el.get("points") or []
            p_name, subtitle = _KNOWN_POLYGON_INFO.get(
                eid, (f"Polygon {eid}", f"Vertices: {', '.join(v_ids)}")
            )
            if "subarea-a" in classes:
                color = "#ff7043"
            elif "subarea-b" in classes:
                color = "#66bb6a"
            elif "subarea-c" in classes:
                color = "#42a5f5"
            else:
                color = "#90ee90" if "secondary" in classes else "#58a6ff"
            rows = [("verts", ", ".join(v_ids))]
            v_pts = [points_by_id[vid] for vid in v_ids if vid in points_by_id]
            approx_str = ""
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
                approx_str = f"≈ area {area:.6f}  |  sides ({s_a:.4f}, {s_b:.4f}, {s_c:.4f})"

            sym_rows = [{"label": "verts", "latex": "", "pretty": ", ".join(v_ids)}]
            if sym.get("area_latex"):
                sym_rows.append(
                    {
                        "label": "Δ",
                        "latex": sym["area_latex"],
                        "pretty": sym.get("area_pretty", ""),
                    }
                )
            if sym.get("sides_latex"):
                sym_rows.append(
                    {
                        "label": "sides",
                        "latex": sym["sides_latex"],
                        "pretty": sym.get("sides_pretty", ""),
                    }
                )

            catalog[eid] = {
                "ID": eid,
                "type": "polygon",
                "classes": classes,
                "color": color,
                "name": p_name,
                "subtitle": subtitle,
                "rows": rows,
                "symbolic_rows": sym_rows,
                "approx": approx_str,
                "related_points": v_ids,
            }

    return catalog


def model_to_elements_list(model: Model) -> list[dict[str, Any]]:
    """Convert a `geometor.model.Model` into a chronological list of browser-ready element dicts."""
    tri: SymbolicTriangle | None = getattr(model, "_etc_triangle", None)
    simplify_fn = tri.simplify if isinstance(tri, SymbolicTriangle) else clean_expr
    kepler_phi = bool(isinstance(tri, SymbolicTriangle) and tri.key == "kepler")

    A_pt = model.get_element_by_ID("A")
    B_pt = model.get_element_by_ID("B")
    C_pt = model.get_element_by_ID("C")
    has_exact_abc = (
        isinstance(A_pt, spg.Point)
        and isinstance(B_pt, spg.Point)
        and isinstance(C_pt, spg.Point)
        and not (A_pt.atoms(sp.Float) or B_pt.atoms(sp.Float) or C_pt.atoms(sp.Float))
    )
    a_len = b_len = c_len = sp.Integer(1)
    reg: CenterSymbolicRegistry | None = None
    if has_exact_abc:
        a_len, b_len, c_len = triangle_side_lengths(A_pt, B_pt, C_pt, model=model)
        if (
            isinstance(tri, SymbolicTriangle)
            and tri.key in {"heronian", "right", "kepler", "kimberling"}
            and zero_test(B_pt.x - tri.B_xy[0])
        ):
            reg = CenterSymbolicRegistry(tri)

    eff_tri = tri if isinstance(tri, SymbolicTriangle) else get_canonical_triangle("heronian")

    def _reduce_triple(
        u: sp.Expr, v: sp.Expr, w: sp.Expr
    ) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
        return reduce_homogeneous_triple(u, v, w, eff_tri)

    elements: list[dict[str, Any]] = []
    for el, data in model.items():
        if not data.ID:
            continue
        parents_ids = [
            model[p].ID for p in (data.parents or []) if p in model and model[p].ID
        ]
        base: dict[str, Any] = {
            "ID": data.ID,
            "classes": (
                list(data.classes.keys())
                if isinstance(data.classes, dict)
                else list(data.classes)
            ),
            "guide": bool(data.guide),
            "parents": parents_ids,
        }
        sym: dict[str, str] = {}

        if isinstance(el, spg.Point):
            base.update(
                {
                    "type": "point",
                    "x": float(el.x.evalf()),
                    "y": float(el.y.evalf()),
                }
            )
            if not (el.x.atoms(sp.Float) or el.y.atoms(sp.Float)):
                sx = simplify_fn(el.x)
                sy = simplify_fn(el.y)
                xl = format_symbolic_latex(sx, kepler_phi=kepler_phi)
                yl = format_symbolic_latex(sy, kepler_phi=kepler_phi)
                xp = format_symbolic_pretty(sx, kepler_phi=kepler_phi)
                yp = format_symbolic_pretty(sy, kepler_phi=kepler_phi)
                sym["coords_latex"] = f"\\left({xl},\\; {yl}\\right)"
                sym["coords_pretty"] = f"({xp}, {yp})"

                m_x = re.match(r"^X_(\d+)$", data.ID)
                if (
                    reg is not None
                    and m_x
                    and int(m_x.group(1)) in EXACT_CYCLIC_BARYCENTRICS
                ):
                    rec = reg.get(int(m_x.group(1)))
                    sym["trilinear_latex"] = rec.trilinear_latex()
                    sym["trilinear_pretty"] = rec.trilinear_pretty()
                    sym["barycentric_latex"] = rec.bary_latex()
                    sym["barycentric_pretty"] = rec.bary_pretty()
                elif has_exact_abc:
                    assert isinstance(A_pt, spg.Point)
                    assert isinstance(B_pt, spg.Point)
                    assert isinstance(C_pt, spg.Point)
                    u, v, w = barycentrics_of(A_pt, B_pt, C_pt, el, model=model)
                    bu, bv, bw = _reduce_triple(u, v, w)
                    sym["barycentric_latex"] = _format_triple_latex(
                        bu, bv, bw, kepler_phi=kepler_phi
                    )
                    sym["barycentric_pretty"] = _format_triple_pretty(
                        bu, bv, bw, kepler_phi=kepler_phi
                    )
                    tu, tv, tw = _reduce_triple(
                        simplify_fn(u / a_len),
                        simplify_fn(v / b_len),
                        simplify_fn(w / c_len),
                    )
                    sym["trilinear_latex"] = _format_triple_latex(
                        tu, tv, tw, kepler_phi=kepler_phi
                    )
                    sym["trilinear_pretty"] = _format_triple_pretty(
                        tu, tv, tw, kepler_phi=kepler_phi
                    )

        elif isinstance(el, spg.Line):
            base.update(
                {
                    "type": "line",
                    "pt1": model[el.p1].ID,
                    "pt2": model[el.p2].ID,
                }
            )
            if not (el.p1.atoms(sp.Float) or el.p2.atoms(sp.Float)):
                la = simplify_fn(el.p1.y - el.p2.y)
                lb = simplify_fn(el.p2.x - el.p1.x)
                lc = simplify_fn(el.p1.x * el.p2.y - el.p2.x * el.p1.y)
                eql, eqp = _format_exact_line_eq(
                    la,
                    lb,
                    lc,
                    tri_obj=eff_tri,
                    kepler_phi=kepler_phi,
                    simplify_fn=simplify_fn,
                )
                sym["eq_latex"] = eql
                sym["eq_pretty"] = eqp
                q_val = simplify_fn(quadrance(el.p1, el.p2))
                sym["quadrance_latex"] = format_symbolic_latex(
                    q_val, kepler_phi=kepler_phi
                )
                sym["quadrance_pretty"] = format_symbolic_pretty(
                    q_val, kepler_phi=kepler_phi
                )
                if has_exact_abc:
                    assert isinstance(A_pt, spg.Point)
                    assert isinstance(B_pt, spg.Point)
                    spr = simplify_fn(line_spread((el.p1, el.p2), (A_pt, B_pt)))
                    sym["spread_latex"] = format_symbolic_latex(
                        spr, kepler_phi=kepler_phi
                    )
                    sym["spread_pretty"] = format_symbolic_pretty(
                        spr, kepler_phi=kepler_phi
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
            if not (el.center.atoms(sp.Float) or el.radius.atoms(sp.Float)):
                hx = simplify_fn(el.center.x)
                ky = simplify_fn(el.center.y)
                r_ex = simplify_fn(el.radius)
                qr_ex = simplify_fn(r_ex**2)
                sym["radius_latex"] = format_symbolic_latex(
                    r_ex, kepler_phi=kepler_phi
                )
                sym["radius_pretty"] = format_symbolic_pretty(
                    r_ex, kepler_phi=kepler_phi
                )
                sym["quadrance_latex"] = format_symbolic_latex(
                    qr_ex, kepler_phi=kepler_phi
                )
                sym["quadrance_pretty"] = format_symbolic_pretty(
                    qr_ex, kepler_phi=kepler_phi
                )
                eql, eqp = _format_exact_circle_eq(
                    hx, ky, qr_ex, kepler_phi=kepler_phi, simplify_fn=simplify_fn
                )
                sym["eq_latex"] = eql
                sym["eq_pretty"] = eqp

        elif isinstance(el, spg.Polygon):
            base.update(
                {
                    "type": "polygon",
                    "points": [model[p].ID for p in el.vertices if p in model],
                }
            )
            verts = list(el.vertices)
            if len(verts) == 3 and not any(v.atoms(sp.Float) for v in verts):
                area_ex = simplify_fn(
                    abs(triangle_signed_area(verts[0], verts[1], verts[2], model=model))
                )
                sym["area_latex"] = format_symbolic_latex(
                    area_ex, kepler_phi=kepler_phi
                )
                sym["area_pretty"] = format_symbolic_pretty(
                    area_ex, kepler_phi=kepler_phi
                )
                qa, qb, qc = triangle_side_quadrances(
                    verts[0], verts[1], verts[2], model=model
                )
                sa = simplify_fn(sp.sqrt(qa))
                sb = simplify_fn(sp.sqrt(qb))
                sc = simplify_fn(sp.sqrt(qc))
                sym["sides_latex"] = (
                    f"{format_symbolic_latex(sa, kepler_phi=kepler_phi)},\\; "
                    f"{format_symbolic_latex(sb, kepler_phi=kepler_phi)},\\; "
                    f"{format_symbolic_latex(sc, kepler_phi=kepler_phi)}"
                )
                sym["sides_pretty"] = (
                    f"{format_symbolic_pretty(sa, kepler_phi=kepler_phi)}, "
                    f"{format_symbolic_pretty(sb, kepler_phi=kepler_phi)}, "
                    f"{format_symbolic_pretty(sc, kepler_phi=kepler_phi)}"
                )

        elif isinstance(el, spg.Segment):
            base.update(
                {
                    "type": "segment",
                    "points": [model[el.p1].ID, model[el.p2].ID],
                }
            )
            if not (el.p1.atoms(sp.Float) or el.p2.atoms(sp.Float)):
                q_val = simplify_fn(quadrance(el.p1, el.p2))
                l_val = simplify_fn(sp.sqrt(q_val))
                sym["quadrance_latex"] = format_symbolic_latex(
                    q_val, kepler_phi=kepler_phi
                )
                sym["quadrance_pretty"] = format_symbolic_pretty(
                    q_val, kepler_phi=kepler_phi
                )
                sym["length_latex"] = format_symbolic_latex(
                    l_val, kepler_phi=kepler_phi
                )
                sym["length_pretty"] = format_symbolic_pretty(
                    l_val, kepler_phi=kepler_phi
                )
                if has_exact_abc:
                    assert isinstance(A_pt, spg.Point)
                    assert isinstance(B_pt, spg.Point)
                    spr = simplify_fn(line_spread((el.p1, el.p2), (A_pt, B_pt)))
                    sym["spread_latex"] = format_symbolic_latex(
                        spr, kepler_phi=kepler_phi
                    )
                    sym["spread_pretty"] = format_symbolic_pretty(
                        spr, kepler_phi=kepler_phi
                    )
        else:
            continue

        if sym:
            base["symbolic"] = sym
        elements.append(base)
    return elements


def _format_svg_label(label: str) -> str:
    """Convert an algebraic label like `X_13`, `M_a`, or `H'_a` into SVG `<tspan>` subscript markup."""
    clean = label.strip()
    m_x = re.match(r"^X\((\d+)\)$", clean)
    if m_x:
        return f'X<tspan dy="0.3em" font-size="75%">{html.escape(m_x.group(1))}</tspan>'
    if "_" in clean:
        base, sub = clean.split("_", 1)
        sub = sub.strip("{}")
        return f'{html.escape(base)}<tspan dy="0.3em" font-size="75%">{html.escape(sub)}</tspan>'
    return html.escape(clean)


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

    A_ref = points_by_id.get("A")
    B_ref = points_by_id.get("B")
    C_ref = points_by_id.get("C")
    if A_ref and B_ref and C_ref:
        ab_d = math.hypot(B_ref["x"] - A_ref["x"], B_ref["y"] - A_ref["y"])
        bc_d = math.hypot(C_ref["x"] - B_ref["x"], C_ref["y"] - B_ref["y"])
        ca_d = math.hypot(A_ref["x"] - C_ref["x"], A_ref["y"] - C_ref["y"])
        tri_span = max(ab_d, bc_d, ca_d, 1.0)
        tri_cx = (A_ref["x"] + B_ref["x"] + C_ref["x"]) / 3.0
        tri_cy = (A_ref["y"] + B_ref["y"] + C_ref["y"]) / 3.0
    else:
        tri_span = 1.0
        tri_cx, tri_cy = 0.5, 0.25

    catalog = _enrich_elements_catalog(elements, points_by_id, tri_span=tri_span)

    min_x, max_x = float("inf"), float("-inf")
    min_y, max_y = float("inf"), float("-inf")

    num_targets = sum(
        1
        for p in points_by_id.values()
        if "target" in p["classes"] or "selected" in p["classes"]
    )
    is_collection_model = num_targets > 1
    tight_targets = [
        p
        for p in points_by_id.values()
        if ("target" in p["classes"] or "selected" in p["classes"])
        and abs(p["x"] - tri_cx) <= 1.35 * tri_span
        and abs(p["y"] - tri_cy) <= 1.25 * tri_span
    ]
    use_tight_collection_box = is_collection_model and len(tight_targets) >= 3

    for p in points_by_id.values():
        if "incident" in p["classes"]:
            continue
        if p["guide"]:
            if (
                not is_collection_model
                and p["ID"] not in {"R_a", "R_b"}
                and abs(p["x"] - tri_cx) <= 3.0 * tri_span
                and abs(p["y"] - tri_cy) <= 3.0 * tri_span
            ):
                min_x = min(min_x, p["x"])
                max_x = max(max_x, p["x"])
                min_y = min(min_y, p["y"])
                max_y = max(max_y, p["y"])
            continue
        if use_tight_collection_box and ("target" in p["classes"] or "selected" in p["classes"]):
            if (
                abs(p["x"] - tri_cx) <= 1.35 * tri_span
                and abs(p["y"] - tri_cy) <= 1.25 * tri_span
            ):
                min_x = min(min_x, p["x"])
                max_x = max(max_x, p["x"])
                min_y = min(min_y, p["y"])
                max_y = max(max_y, p["y"])
            continue
        bound_lim = (2.4 if is_collection_model else 4.5) * tri_span
        if abs(p["x"] - tri_cx) <= bound_lim and abs(p["y"] - tri_cy) <= bound_lim:
            min_x = min(min_x, p["x"])
            max_x = max(max_x, p["x"])
            min_y = min(min_y, p["y"])
            max_y = max(max_y, p["y"])

    for poly in elements:
        if poly["type"] == "polygon" and "incident" not in poly["classes"]:
            for pid in poly["points"]:
                pt = points_by_id.get(pid)
                if (
                    pt
                    and abs(pt["x"] - tri_cx) <= 3.2 * tri_span
                    and abs(pt["y"] - tri_cy) <= 3.2 * tri_span
                ):
                    min_x = min(min_x, pt["x"])
                    max_x = max(max_x, pt["x"])
                    min_y = min(min_y, pt["y"])
                    max_y = max(max_y, pt["y"])

    for c in elements:
        if c["type"] == "circle" and not c["guide"] and "incident" not in c["classes"]:
            ctr = points_by_id.get(c["center"])
            r = c["radius"]
            if ctr and r <= (1.6 if is_collection_model else 3.5) * tri_span:
                min_x = min(min_x, ctr["x"] - r)
                max_x = max(max_x, ctr["x"] + r)
                min_y = min(min_y, ctr["y"] - r)
                max_y = max(max_y, ctr["y"] + r)

    if not math.isfinite(min_x):
        min_x, max_x = tri_cx - 0.8 * tri_span, tri_cx + 0.8 * tri_span
        min_y, max_y = tri_cy - 0.6 * tri_span, tri_cy + 0.6 * tri_span

    width = max(max_x - min_x, 0.35 * tri_span)
    height = max(max_y - min_y, 0.35 * tri_span)
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

    units_per_px = vb_width / svg_width
    target_r_px = (
        10.5
        if num_targets <= 1
        else (8.0 if num_targets <= 25 else (6.8 if num_targets <= 50 else 5.8))
    )
    pt_radius = 7.5 * units_per_px
    target_radius = target_r_px * units_per_px
    guide_radius = 4.8 * units_per_px
    font_size = 20.25 * units_per_px
    guide_font_size = 17.5 * units_per_px

    graphics_nodes: list[str] = []
    highlights_nodes: list[str] = []
    elements_nodes: list[str] = []
    points_nodes: list[str] = []
    labels_nodes: list[str] = []
    placed_label_px: list[tuple[float, float]] = []
    placed_target_labels = 0
    if not is_collection_model:
        for p in points_by_id.values():
            if "target" in p["classes"] or "selected" in p["classes"]:
                placed_label_px.append((p["x"] / units_per_px + 12.0, -p["y"] / units_per_px - 10.5))

    for el in elements:
        raw_id = el["ID"]
        el_id = html.escape(raw_id, quote=True)
        info = catalog.get(raw_id, {})
        el_name = html.escape(info.get("name") or raw_id, quote=True)
        sym = el.get("symbolic") or {}
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
            area_attr = (
                f'data-area="{html.escape(sym["area_pretty"], quote=True)}" '
                if sym.get("area_pretty")
                else ""
            )
            title_txt = (
                f"{el_id}: {el_name} (Δ = {html.escape(sym['area_pretty'])})"
                if sym.get("area_pretty")
                else f"{el_id}: {el_name}"
            )
            graphics_nodes.append(
                f'    <polygon id="{el_id}" data-id="{el_id}" data-ref="{el_id}" data-name="{el_name}" {area_attr}'
                f'class="{class_attr}" data-category="graphics" points="{pts_str}">'
                f"<title>{title_txt}</title></polygon>"
            )

        elif el["type"] in {"segment", "section", "chain"}:
            pts_str = " ".join(
                f"{points_by_id[pid]['x']:.6f},{-points_by_id[pid]['y']:.6f}"
                for pid in el["points"]
                if pid in points_by_id
            )
            q_attr = (
                f'data-quadrance="{html.escape(sym["quadrance_pretty"], quote=True)}" '
                if sym.get("quadrance_pretty")
                else ""
            )
            s_attr = (
                f'data-spread="{html.escape(sym["spread_pretty"], quote=True)}" '
                if sym.get("spread_pretty")
                else ""
            )
            graphics_nodes.append(
                f'    <polyline id="{el_id}" data-id="{el_id}" data-ref="{el_id}" data-name="{el_name}" '
                f'{q_attr}{s_attr}class="{class_attr}" data-category="graphics" points="{pts_str}">'
                f"<title>{el_id}: {el_name}</title></polyline>"
            )
            if len(el["points"]) == 2:
                sp1 = points_by_id.get(el["points"][0])
                sp2 = points_by_id.get(el["points"][1])
                if sp1 and sp2:
                    highlights_nodes.append(
                        f'    <polyline id="hl-{el_id}" data-highlight-for="{el_id}" class="highlight-segment" '
                        f'points="{sp1["x"]:.6f},{-sp1["y"]:.6f} {sp2["x"]:.6f},{-sp2["y"]:.6f}" style="display: none;" />'
                    )

        elif el["type"] == "line":
            p1 = points_by_id.get(el["pt1"])
            p2 = points_by_id.get(el["pt2"])
            if p1 and p2:
                dx = p2["x"] - p1["x"]
                dy = p2["y"] - p1["y"]
                seg_norm = math.hypot(dx, dy) or 1.0
                ext = (1000.0 * tri_span) / seg_norm
                x1 = p1["x"] - ext * dx
                y1 = -(p1["y"] - ext * dy)
                x2 = p1["x"] + ext * dx
                y2 = -(p1["y"] + ext * dy)
                c_tok = info.get("color_token") or ""
                c_hex = info.get("color") or ""
                c_attrs = (
                    f'data-color-token="{html.escape(c_tok, quote=True)}" data-color="{html.escape(c_hex, quote=True)}" '
                    if c_tok
                    else ""
                )
                eq_attr = (
                    f'data-eq="{html.escape(sym["eq_pretty"], quote=True)}" '
                    if sym.get("eq_pretty")
                    else ""
                )
                s_attr = (
                    f'data-spread="{html.escape(sym["spread_pretty"], quote=True)}" '
                    if sym.get("spread_pretty")
                    else ""
                )
                elements_nodes.append(
                    f'    <line id="{el_id}" data-id="{el_id}" data-ref="{el_id}" data-name="{el_name}" {c_attrs}{eq_attr}{s_attr}'
                    f'data-pt1="{html.escape(el["pt1"], quote=True)}" data-pt2="{html.escape(el["pt2"], quote=True)}" '
                    f'class="{class_attr}" data-category="elements" '
                    f'x1="{x1:.5f}" y1="{y1:.5f}" x2="{x2:.5f}" y2="{y2:.5f}">'
                    f"<title>{el_id}: {el_name}</title></line>"
                )
                highlights_nodes.append(
                    f'    <polyline id="hl-{el_id}" data-highlight-for="{el_id}" class="highlight-segment" '
                    f'points="{p1["x"]:.6f},{-p1["y"]:.6f} {p2["x"]:.6f},{-p2["y"]:.6f}" style="display: none;" />'
                )

        elif el["type"] == "circle":
            ctr = points_by_id.get(el["center"])
            rad_pt = points_by_id.get(el.get("radius_pt") or "")
            if ctr:
                cx = ctr["x"]
                cy = -ctr["y"]
                r = el["radius"]
                c_tok = info.get("color_token") or ""
                c_hex = info.get("color") or ""
                c_attrs = (
                    f'data-color-token="{html.escape(c_tok, quote=True)}" data-color="{html.escape(c_hex, quote=True)}" '
                    if c_tok
                    else ""
                )
                q_attr = (
                    f'data-quadrance="{html.escape(sym["quadrance_pretty"], quote=True)}" '
                    if sym.get("quadrance_pretty")
                    else ""
                )
                elements_nodes.append(
                    f'    <circle id="{el_id}" data-id="{el_id}" data-ref="{el_id}" data-name="{el_name}" {c_attrs}{q_attr}'
                    f'class="{class_attr}" data-category="elements" '
                    f'cx="{cx:.6f}" cy="{cy:.6f}" r="{r:.6f}" fill="none">'
                    f"<title>{el_id}: {el_name}</title></circle>"
                )
                if rad_pt:
                    highlights_nodes.append(
                        f'    <polyline id="hl-{el_id}" data-highlight-for="{el_id}" class="highlight-segment" '
                        f'points="{ctr["x"]:.6f},{-ctr["y"]:.6f} {rad_pt["x"]:.6f},{-rad_pt["y"]:.6f}" style="display: none;" />'
                    )

        elif el["type"] == "point":
            cx = el["x"]
            cy = -el["y"]
            is_target = "target" in el["classes"] or "selected" in el["classes"]
            r = target_radius if is_target else (guide_radius if el["guide"] else pt_radius)
            sym_attrs = ""
            if sym.get("coords_pretty"):
                sym_attrs += f'data-coords="{html.escape(sym["coords_pretty"], quote=True)}" '
            if sym.get("trilinear_pretty"):
                sym_attrs += f'data-trilinears="{html.escape(sym["trilinear_pretty"], quote=True)}" '
            if sym.get("barycentric_pretty"):
                sym_attrs += f'data-barycentrics="{html.escape(sym["barycentric_pretty"], quote=True)}" '
            title_coords = (
                html.escape(sym["coords_pretty"])
                if sym.get("coords_pretty")
                else f"({cx:.4f}, {el['y']:.4f})"
            )
            points_nodes.append(
                f'    <circle id="{el_id}" data-id="{el_id}" data-ref="{el_id}" data-name="{el_name}" {sym_attrs}'
                f'class="{class_attr}" data-category="points" '
                f'cx="{cx:.6f}" cy="{cy:.6f}" r="{r:.6f}">'
                f"<title>{el_id} = {el_name} {title_coords}</title></circle>"
            )

            if show_labels and raw_id not in {"R_a", "R_b"}:
                if el["guide"]:
                    lbl_cls = "guide-label guide"
                elif is_target:
                    lbl_cls = "target-label"
                elif "given" in el["classes"]:
                    lbl_cls = "given-label"
                else:
                    lbl_cls = "point-label"
                if "incident" in el["classes"]:
                    lbl_cls += " incident"

                ox_px = 12.0
                oy_px = -10.5
                if raw_id == "A":
                    ox_px, oy_px = -24.0, 22.5
                elif raw_id == "B":
                    ox_px, oy_px = 12.0, 22.5
                elif raw_id == "C":
                    ox_px, oy_px = -7.5, -15.0
                elif el["guide"]:
                    if raw_id.endswith(("_a", "_A")) or raw_id == "A'":
                        ox_px, oy_px = 10.0, -7.0
                    elif raw_id.endswith(("_b", "_B")) or raw_id == "B'":
                        ox_px, oy_px = -30.0, -7.0
                    elif raw_id.endswith(("_c", "_C")) or raw_id == "C'":
                        ox_px, oy_px = -8.0, 19.0
                    else:
                        ox_px, oy_px = 9.0, -8.5

                offset_x = ox_px * units_per_px
                offset_y = oy_px * units_per_px
                lbl_x_px = (cx + offset_x) / units_per_px
                lbl_y_px = (cy + offset_y) / units_per_px

                if is_collection_model and is_target:
                    too_close = placed_target_labels >= 18 or any(
                        math.hypot(lbl_x_px - px_i, lbl_y_px - py_i) < 34.0
                        for px_i, py_i in placed_label_px
                    )
                    if too_close:
                        lbl_cls += " dense-label"
                    else:
                        placed_label_px.append((lbl_x_px, lbl_y_px))
                        placed_target_labels += 1
                elif not is_target and raw_id not in {"A", "B", "C"}:
                    base_x_px = cx / units_per_px
                    base_y_px = cy / units_per_px
                    candidates = [
                        (ox_px, oy_px),
                        (12.0, 20.0),
                        (-38.0, -10.5),
                        (-38.0, 20.0),
                        (16.0, 5.0),
                        (-42.0, 5.0),
                        (-8.0, -22.0),
                        (-8.0, 24.0),
                    ]
                    best_cand = (ox_px, oy_px)
                    best_min_d = -1.0
                    for c_ox, c_oy in candidates:
                        cand_x = base_x_px + c_ox
                        cand_y = base_y_px + c_oy
                        min_d = min(
                            (math.hypot(cand_x - px_i, cand_y - py_i) for px_i, py_i in placed_label_px),
                            default=999.0,
                        )
                        if min_d > best_min_d:
                            best_min_d = min_d
                            best_cand = (c_ox, c_oy)
                    ox_px, oy_px = best_cand
                    offset_x = ox_px * units_per_px
                    offset_y = oy_px * units_per_px
                    lbl_x_px = base_x_px + ox_px
                    lbl_y_px = base_y_px + oy_px
                    if best_min_d < 24.0:
                        lbl_cls += " dense-label"
                    else:
                        placed_label_px.append((lbl_x_px, lbl_y_px))
                else:
                    placed_label_px.append((lbl_x_px, lbl_y_px))

                cur_font = guide_font_size if el["guide"] else font_size
                labels_nodes.append(
                    f'    <text id="lbl-{el_id}" class="{lbl_cls}" data-point-id="{el_id}" '
                    f'data-anchor-x="{cx:.6f}" data-anchor-y="{cy:.6f}" '
                    f'data-offset-x="{ox_px:.1f}" data-offset-y="{oy_px:.1f}" '
                    f'x="{cx + offset_x:.6f}" y="{cy + offset_y:.6f}" '
                    f'font-size="{cur_font:.6f}">{_format_svg_label(raw_id)}</text>'
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
    meta_json = (
        json.dumps(catalog, ensure_ascii=False, separators=(",", ":"))
        .replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
    )

    tri_obj: SymbolicTriangle | None = getattr(model, "_etc_triangle", None)
    tri_key_attr = (
        f'data-triangle="{html.escape(tri_obj.key, quote=True)}" '
        if isinstance(tri_obj, SymbolicTriangle)
        else ""
    )

    svg_lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        (
            f'<svg class="geometor-etc-drawing" xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="{vb_str}" data-initial-viewbox="{vb_str}" '
            f'{tri_key_attr}data-tri-span="{tri_span:.6f}" '
            f'data-target-r-px="{target_r_px}" '
            f'preserveAspectRatio="xMidYMid meet">'
        ),
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


"""Exact symbolic verification suite for GEOMETOR ETC 4-triangle architecture and Collection 1 (X_1-X_19)."""

from __future__ import annotations

import functools
import json
import re
import runpy
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import sympy as sp
import sympy.geometry as spg
from geometor.model import line_spread, zero_test

from geometor.etc import (
    CANONICAL_CENTER_CONCORDANCE,
    CANONICAL_TRIANGLES,
    CenterSymbolicRegistry,
    bevan_point,
    build_symbolic_collection_1_model,
    centroid,
    circumcenter,
    circumcircle_inverse_of_incenter,
    clawson_point,
    construct_reference_triangle,
    create_model,
    de_longchamps_point,
    fermat_point,
    feuerbach_point,
    first_isodynamic_point,
    first_napoleon_point,
    gergonne_point,
    get_canonical_triangle,
    get_center_concordance,
    harmonic_feuerbach_point,
    incenter,
    isotomic_conjugate_of_incenter,
    mittenpunkt,
    nagel_point,
    nine_point_center,
    orthocenter,
    second_isodynamic_point,
    second_isogonic_center,
    second_napoleon_point,
    spieker_center,
    symmedian_point,
)
from geometor.etc.transform import extract_svg_element_refs
from geometor.etc.triangles import PHI, SQRT_35, SQRT_PHI
from geometor.etc.video import compile_scenes_from_script

REPO_ROOT = Path(__file__).resolve().parents[1]
COLL1_DOC_DIR = REPO_ROOT / "docsrc" / "centers" / "c-00001-00019"
MODELS_DIR = REPO_ROOT / "src" / "geometor" / "etc" / "models"
X1_VIDEO_DIR = REPO_ROOT / "videos" / "x-00001"

PUBLISHED_KIMBERLING_SEARCH_VALUES: dict[int, float] = {
    1: 1.690308509457,
    2: 2.629368792489,
    3: 6.782362894196,
    4: -5.676619410927,
    5: 0.552871741635,
    6: 0.992908495066,
    7: 0.744160979006,
    8: 4.507489358552,
    9: 3.571972699230,
    10: 3.098898934005,
    11: 2.643135121245,
    12: 1.334163924620,
    13: 0.075945151805,
    14: 4.373431772013,
    15: 3.102444020655,
    16: -6.784211495839,
    17: 1.386654550070,
    18: -16.280673997779,
    19: -1.480512397789,
    20: 19.241345199319,
    35: 3.284689530119,
    36: -2.575286786660,
    40: 11.874417278936,
    55: 2.635469416137,
    56: 0.187119023187,
    57: 0.380455291518,
    75: 3.706459623147,
}

_G_ROLE_RE = re.compile(r":g:`([^`]+)`")


@functools.lru_cache(maxsize=8)
def _cached_registry(preset: str) -> CenterSymbolicRegistry:
    return CenterSymbolicRegistry(preset)


def _assert_zero_floats(*exprs: sp.Basic) -> None:
    for expr in exprs:
        floats = expr.atoms(sp.Float)
        assert not floats, f"Unexpected sp.Float atoms {floats} in {expr!r}"


def _extract_g_targets(rst_snippet: str) -> list[str]:
    targets: list[str] = []
    for m in _G_ROLE_RE.finditer(rst_snippet):
        body = m.group(1).strip()
        tm = re.match(r"^(.*?)\s*<(.+)>\s*$", body)
        targets.append(tm.group(2).strip() if tm else body)
    return targets


def test_no_model_setitem_bypass_or_x1_hardcoding_in_source() -> None:
    """Ensure zero super(Model).__setitem__ bypasses and zero `num == 1` special-casing."""
    src_dir = REPO_ROOT / "src" / "geometor" / "etc"
    for py_path in sorted(src_dir.glob("*.py")):
        content = py_path.read_text(encoding="utf-8")
        assert "super(Model" not in content, f"Found super(Model bypass in {py_path}"

    for gen_mod in ("plates.py", "transform.py", "render.py"):
        txt = (src_dir / gen_mod).read_text(encoding="utf-8")
        assert not re.search(r"\bnum\s*==\s*1\b", txt), (
            f"Found hardcoded `num == 1` branch in {gen_mod}"
        )


@pytest.mark.parametrize(
    "preset",
    ["heronian", "right", "kepler", "kimberling", "golden", "gnomon", "equilateral"],
)
def test_canonical_triangles_exact_invariants(preset: str) -> None:
    """Verify exact vertices, side quadrances, area, r, and R with zero sp.Float."""
    tri = get_canonical_triangle(preset)
    assert preset in CANONICAL_TRIANGLES
    _assert_zero_floats(
        tri.a,
        tri.b,
        tri.c,
        *tri.A_xy,
        *tri.B_xy,
        *tri.C_xy,
        tri.area,
        tri.r,
        tri.R,
        tri.S_A,
        tri.S_B,
        tri.S_C,
    )
    ax, ay = tri.A_xy
    bx, by = tri.B_xy
    cx, cy = tri.C_xy
    assert zero_test((bx - cx) ** 2 + (by - cy) ** 2 - tri.a**2)
    assert zero_test((cx - ax) ** 2 + (cy - ay) ** 2 - tri.b**2)
    assert zero_test((ax - bx) ** 2 + (ay - by) ** 2 - tri.c**2)
    shoelace_two_area = (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)
    assert zero_test(shoelace_two_area - 2 * tri.area)
    if preset in ("right", "kepler"):
        assert tri.right_angle_vertex == "A"
    if preset in ("golden", "gnomon"):
        assert tri.is_isosceles and not tri.is_equilateral
    if preset == "equilateral":
        assert tri.is_equilateral


def test_x1_exact_symbolic_values_across_four_triangles() -> None:
    """Verify exact closed-form X_1 coordinates, sub-areas, and inradii across all 7 canonical triangles."""
    reg_h = CenterSymbolicRegistry("heronian", cache_dir=None)
    x1_h = reg_h.get(1)
    assert x1_h.xy == (sp.Integer(6), sp.Integer(4))
    assert x1_h.trilinear == (sp.Integer(1), sp.Integer(1), sp.Integer(1))
    assert x1_h.bary == (sp.Integer(15), sp.Integer(13), sp.Integer(14))
    assert x1_h.sub_areas == (sp.Integer(30), sp.Integer(26), sp.Integer(28))
    assert sum(x1_h.sub_areas) == reg_h.triangle.area == sp.Integer(84)
    assert x1_h.search_value == reg_h.triangle.r == sp.Integer(4)
    assert reg_h.triangle.Q_r == sp.Integer(16)

    # Right (5, 3, 4) with right angle at base A=(0,0), B=(4,0), C=(0,3) -> X_1 = (1, 1)
    reg_r = CenterSymbolicRegistry("right", cache_dir=None)
    x1_r = reg_r.get(1)
    assert x1_r.xy == (sp.Integer(1), sp.Integer(1))
    assert x1_r.trilinear == (sp.Integer(1), sp.Integer(1), sp.Integer(1))
    assert x1_r.bary == (sp.Integer(5), sp.Integer(3), sp.Integer(4))
    assert x1_r.sub_areas == (sp.Rational(5, 2), sp.Rational(3, 2), sp.Integer(2))
    assert sum(x1_r.sub_areas) == reg_r.triangle.area == sp.Integer(6)
    assert x1_r.search_value == reg_r.triangle.r == sp.Integer(1)
    assert reg_r.triangle.Q_r == sp.Integer(1)

    # Kepler (phi, 1, sqrt(phi)) with right angle at base A=(0,0) -> X_1 = (r, r)
    reg_k = CenterSymbolicRegistry("kepler", cache_dir=None)
    x1_k = reg_k.get(1)
    expected_kr = (SQRT_PHI - PHI + 1) / 2
    assert zero_test(x1_k.xy[0] - expected_kr)
    assert zero_test(x1_k.xy[1] - expected_kr)
    assert x1_k.trilinear == (sp.Integer(1), sp.Integer(1), sp.Integer(1))
    assert zero_test(x1_k.bary[0] - PHI)
    assert zero_test(x1_k.bary[1] - 1)
    assert zero_test(x1_k.bary[2] - SQRT_PHI)
    assert zero_test(sum(x1_k.sub_areas) - reg_k.triangle.area)
    assert zero_test(x1_k.search_value - expected_kr)

    reg_m = CenterSymbolicRegistry("kimberling", cache_dir=None)
    x1_m = reg_m.get(1)
    assert x1_m.xy == (sp.Integer(8), sp.Rational(2, 7) * SQRT_35)
    assert x1_m.trilinear == (sp.Integer(1), sp.Integer(1), sp.Integer(1))
    assert x1_m.bary == (sp.Integer(6), sp.Integer(9), sp.Integer(13))
    assert x1_m.sub_areas == (
        sp.Rational(6, 7) * SQRT_35,
        sp.Rational(9, 7) * SQRT_35,
        sp.Rational(13, 7) * SQRT_35,
    )
    assert zero_test(sum(x1_m.sub_areas) - reg_m.triangle.area)
    assert x1_m.search_value == sp.Rational(2, 7) * SQRT_35
    assert reg_m.triangle.Q_r == sp.Rational(20, 7)

    # Pentagon Golden Triangle (phi, phi, 1) -> vertical symmetry axis x = 1/2
    reg_g = CenterSymbolicRegistry("golden", cache_dir=None)
    x1_g = reg_g.get(1)
    assert zero_test(x1_g.xy[0] - sp.Rational(1, 2))
    assert zero_test(x1_g.xy[1] - reg_g.triangle.r)
    assert zero_test(sum(x1_g.sub_areas) - reg_g.triangle.area)

    # Pentagon Golden Gnomon (1, 1, phi) -> vertical symmetry axis x = phi/2
    reg_gn = CenterSymbolicRegistry("gnomon", cache_dir=None)
    x1_gn = reg_gn.get(1)
    assert zero_test(x1_gn.xy[0] - PHI / 2)
    assert zero_test(x1_gn.xy[1] - reg_gn.triangle.r)
    assert zero_test(sum(x1_gn.sub_areas) - reg_gn.triangle.area)

    # Equilateral (2, 2, 2) -> X_1 = (1, sqrt(3)/3), and X_11/X_14/X_16 indeterminate (0:0:0)
    reg_eq = CenterSymbolicRegistry("equilateral", cache_dir=None)
    x1_eq = reg_eq.get(1)
    assert zero_test(x1_eq.xy[0] - 1)
    assert zero_test(x1_eq.xy[1] - sp.sqrt(3) / 3)
    assert reg_eq.get(11).is_indeterminate
    assert reg_eq.get(14).is_indeterminate
    assert reg_eq.get(16).is_indeterminate


@pytest.mark.parametrize(
    "preset",
    ["heronian", "right", "kepler", "kimberling", "golden", "gnomon", "equilateral"],
)
def test_collection_1_algebraic_fields_and_sub_area_partition(preset: str) -> None:
    """Verify exact sub-area partition and quadratic-tower Q(sqrt(3)) detection for X_1..X_19."""
    reg = _cached_registry(preset)
    tri = reg.triangle
    for num in range(1, 20):
        rec = reg.get(num)
        _assert_zero_floats(
            *rec.bary,
            *rec.norm_bary,
            *rec.trilinear,
            *rec.xy,
            *rec.sub_areas,
            rec.search_value,
        )
        if rec.is_indeterminate:
            assert preset == "equilateral" and num in (11, 14, 16)
            continue
        assert zero_test(sum(rec.sub_areas) - tri.area), (
            f"X_{num} on {preset}: sub_areas do not sum to Δ"
        )
        fld = tri.coordinate_field_pretty([*rec.xy, *rec.bary])
        if num in range(13, 19) and preset != "equilateral":
            assert "√3" in fld, f"Expected √3 extension for X_{num} on {preset}, got {fld}"
        elif preset in ("heronian", "right"):
            assert fld == "ℚ", f"Expected rational field ℚ for X_{num} on {preset}, got {fld}"


def test_symbolic_registry_cache_roundtrip_and_kimberling_search_values(
    tmp_path: Path,
) -> None:
    """Verify disk cache srepr round-trip and 12-decimal Kimberling search values."""
    reg = CenterSymbolicRegistry("kimberling", cache_dir=tmp_path)
    warmed = reg.warm_collection_1()
    assert reg.cache_file is not None and reg.cache_file.is_file()

    reg_reloaded = CenterSymbolicRegistry("kimberling", cache_dir=tmp_path)
    for num, pub_val in PUBLISHED_KIMBERLING_SEARCH_VALUES.items():
        rec = warmed[num]
        rec2 = reg_reloaded.get(num)
        _assert_zero_floats(
            *rec2.bary,
            *rec2.norm_bary,
            *rec2.trilinear,
            *rec2.xy,
            *rec2.sub_areas,
            rec2.search_value,
        )
        assert rec2.xy == rec.xy
        assert rec2.bary == rec.bary
        assert rec2.trilinear == rec.trilinear
        assert rec2.search_value == rec.search_value
        comp_val = float(rec2.search_value.evalf(30))
        assert abs(comp_val - pub_val) < 1e-11, (
            f"X_{num}: expected {pub_val:.12f}, got {comp_val:.12f}"
        )


@pytest.mark.parametrize("preset", ["heronian", "right", "kepler", "kimberling"])
def test_x1_model_py_zero_floats_and_central_line_spreads(preset: str) -> None:
    """Build models/x_00001.py on all 4 presets with zero sp.Float and verify Heronian spreads."""
    mod_ns = runpy.run_path(str(MODELS_DIR / "x_00001.py"))
    model = mod_ns["build_model"](preset)
    assert len(model) > 0
    for el in model:
        _assert_zero_floats(el)

    by_id = {info.ID: el for el, info in model.items() if info.ID}
    reg = _cached_registry(preset)
    x1_rec = reg.get(1)
    x1_pt = by_id["X_1"]
    assert zero_test(x1_pt.x - x1_rec.xy[0])
    assert zero_test(x1_pt.y - x1_rec.xy[1])

    if preset == "heronian":
        ab_line = by_id["[ A B ]"]
        nagel_line = by_id["{ 2, 8 }"]
        feuerbach_line = by_id["{ 5, 11 }"]
        oi_line = by_id["{ 3, 40 }"]
        assert line_spread(ab_line, nagel_line) == sp.Integer(0)
        assert line_spread(ab_line, feuerbach_line) == sp.Integer(1)
        assert line_spread(ab_line, oi_line) == sp.Rational(1, 65)


@pytest.mark.parametrize("preset", ["heronian", "right"])
def test_all_19_canonical_constructors_match_symbolic_registry(preset: str) -> None:
    """Verify all 19 Collection 1 Euclidean constructors + auxiliaries match symbolic registry."""
    model = create_model(f"{preset} Constructors Check")
    A, B, C = construct_reference_triangle(model, preset)
    reg = _cached_registry(preset)

    constructors = [
        (1, incenter),
        (2, centroid),
        (3, circumcenter),
        (4, orthocenter),
        (5, nine_point_center),
        (6, symmedian_point),
        (7, gergonne_point),
        (8, nagel_point),
        (9, mittenpunkt),
        (10, spieker_center),
        (11, feuerbach_point),
        (12, harmonic_feuerbach_point),
        (13, fermat_point),
        (14, second_isogonic_center),
        (15, first_isodynamic_point),
        (16, second_isodynamic_point),
        (17, first_napoleon_point),
        (18, second_napoleon_point),
        (19, clawson_point),
        (20, de_longchamps_point),
        (36, circumcircle_inverse_of_incenter),
        (40, bevan_point),
        (75, isotomic_conjugate_of_incenter),
    ]
    for num, fn in constructors:
        pt = fn(model, A, B, C, ID=f"X_{num}")
        _assert_zero_floats(pt)
        rec = reg.get(num)
        assert zero_test(pt.x - rec.xy[0]), f"X_{num} ({preset}) x mismatch"
        assert zero_test(pt.y - rec.xy[1]), f"X_{num} ({preset}) y mismatch"
        assert get_center_concordance(num) is not None

    if preset == "heronian":
        assert reg.get(36).xy == (sp.Integer(-58), sp.Integer(-4))
        assert reg.get(75).xy == (sp.Rational(3915, 587), sp.Rational(2340, 587))
    else:
        # Right (5, 3, 4) with right angle at base A=(0,0): X_4 = X_19 = A and X_3 = midpoint(B, C)
        assert reg.get(4).xy == reg.triangle.A_xy
        assert reg.get(19).xy == reg.triangle.A_xy
        assert reg.get(3).xy == (sp.Integer(2), sp.Rational(3, 2))

    assert len(CANONICAL_CENTER_CONCORDANCE) >= 60


@pytest.mark.parametrize("num", range(1, 20))
def test_collection_1_model_py_zero_floats_and_collinearities(num: int) -> None:
    """Verify every models/x_000NN.py builds cleanly across all 4 presets with exact incidence."""
    model_py = MODELS_DIR / f"x_{num:05d}.py"
    assert model_py.is_file(), f"Missing {model_py}"
    mod_ns = runpy.run_path(str(model_py))

    for preset in ("heronian", "right", "kepler", "kimberling"):
        mdl = mod_ns["build_model"](preset)
        assert len(mdl) > 0
        for el in mdl:
            _assert_zero_floats(el)

        reg = _cached_registry(preset)
        rec = reg.get(num)

        # Find target point X_num (note on Right/Kepler, X_4 and X_19 coincide with right vertex A!)
        target_pt = None
        for el, info in mdl.items():
            if (
                isinstance(el, spg.Point)
                and (info.ID == f"X_{num}" or "target" in (info.classes or set()))
                and zero_test(el.x - rec.xy[0])
                and zero_test(el.y - rec.xy[1])
            ):
                target_pt = el
                break
        if target_pt is None:
            # Coincident with a vertex (e.g. X_4 or X_19 at right-angle vertex A on right/kepler)
            for el, info in mdl.items():
                if (
                    isinstance(el, spg.Point)
                    and info.ID in {"A", "B", "C"}
                    and zero_test(el.x - rec.xy[0])
                    and zero_test(el.y - rec.xy[1])
                ):
                    target_pt = el
                    break
        assert target_pt is not None
        assert zero_test(target_pt.x - rec.xy[0])
        assert zero_test(target_pt.y - rec.xy[1])

        # Verify every incident central line passes strictly through X_num
        for el, info in mdl.items():
            if isinstance(el, spg.Line) and "incident" in (info.classes or set()):
                p1, p2 = el.p1, el.p2
                det = (p1.x - rec.xy[0]) * (p2.y - rec.xy[1]) - (
                    p1.y - rec.xy[1]
                ) * (p2.x - rec.xy[0])
                assert zero_test(det), (
                    f"Line {info.ID} not incident with X_{num} on {preset}"
                )


@pytest.mark.parametrize(
    "preset",
    ["heronian", "right", "kepler", "kimberling", "golden", "gnomon", "equilateral"],
)
def test_symbolic_collection_1_constellation_model(preset: str) -> None:
    """Verify build_symbolic_collection_1_model has zero sp.Float across all 7 presets."""
    mdl = build_symbolic_collection_1_model(preset)
    for el in mdl:
        _assert_zero_floats(el)


def test_collection_1_constellation_and_video_svgs_well_formed() -> None:
    """Validate XML, data-ref, and symbolic_rows across all 7 Collection 1 constellation + 5 video SVGs."""
    coll_svgs = [
        COLL1_DOC_DIR / "c-00001-00019.svg",
        COLL1_DOC_DIR / "c-00001-00019-right.svg",
        COLL1_DOC_DIR / "c-00001-00019-kepler.svg",
        COLL1_DOC_DIR / "c-00001-00019-kimberling.svg",
        COLL1_DOC_DIR / "c-00001-00019-golden.svg",
        COLL1_DOC_DIR / "c-00001-00019-gnomon.svg",
        COLL1_DOC_DIR / "c-00001-00019-equilateral.svg",
    ]
    video_svgs = [
        X1_VIDEO_DIR / "svgs" / "01_primary.svg",
        X1_VIDEO_DIR / "svgs" / "02_coordinates.svg",
        X1_VIDEO_DIR / "svgs" / "03_central_lines.svg",
        X1_VIDEO_DIR / "svgs" / "04_relations.svg",
        X1_VIDEO_DIR / "svgs" / "05_four_triangles.svg",
    ]

    for svg_path in coll_svgs + video_svgs:
        assert svg_path.is_file(), f"Missing SVG: {svg_path}"
        raw = svg_path.read_text(encoding="utf-8")
        root = ET.fromstring(raw)
        refs = [el.attrib["data-ref"] for el in root.iter() if "data-ref" in el.attrib]
        assert refs, f"No data-ref elements found in {svg_path}"

        meta_nodes = [
            el for el in root.iter() if el.attrib.get("class") == "etc-elements-meta"
        ]
        assert len(meta_nodes) == 1, f"Missing .etc-elements-meta in {svg_path}"
        meta = json.loads(meta_nodes[0].text or "{}")
        assert meta, f"Empty .etc-elements-meta JSON in {svg_path}"
        has_symbolic_rows = any(
            bool(entry.get("symbolic_rows"))
            for entry in meta.values()
            if isinstance(entry, dict)
        )
        assert has_symbolic_rows, f"No symbolic_rows in {svg_path}"


def test_collection_1_overview_rst_g_selector_parity() -> None:
    """Verify 100% :g: selector parity and unified Member Centers table on c-00001-00019/index.rst."""
    coll_rst = (COLL1_DOC_DIR / "index.rst").read_text(encoding="utf-8")
    coll_refs = extract_svg_element_refs(COLL1_DOC_DIR / "c-00001-00019.svg")
    targets = _extract_g_targets(coll_rst)
    assert len(targets) >= 25
    for tgt in targets:
        assert tgt in coll_refs, f"c-00001-00019/index.rst unresolved :g:`{tgt}`"
    for num in range(1, 20):
        assert f"X_{num}" in targets, f"X_{num} missing from c-00001-00019/index.rst :g: links"
        assert f":ref:`X_{num} <X_{num}>`" in coll_rst
    assert "<family-c-00001-00019>" in coll_rst


@pytest.mark.parametrize("num", [1, 5, 10, 13, 19])
def test_generalized_plates_api_runtime(num: int) -> None:
    """Exercise plates.py SVG generators directly across circle, rational, and sqrt(3) centers."""
    from geometor.etc.plates import (
        generate_doc_coordinates_svg,
        generate_doc_four_triangles_svg,
        generate_doc_relations_svg,
    )

    coord_svg = generate_doc_coordinates_svg(num)
    ET.fromstring(coord_svg)
    assert "feGaussianBlur" not in coord_svg
    assert 'fill="#ff7043" fill-opacity="0.19"' in coord_svg
    assert 'stroke="#ff7043" stroke-width="5.2"' in coord_svg
    assert 'fill="#e8b85a"' not in coord_svg
    rel_svg, bundle = generate_doc_relations_svg(num)
    ET.fromstring(rel_svg)
    assert f"X_{num}" in bundle.svg_ids
    four_svg = generate_doc_four_triangles_svg(num)
    ET.fromstring(four_svg)
    assert 'fill="#ff7043" fill-opacity="0.14"' in four_svg
    assert 'stroke="#ff7043" stroke-width="2.9"' in four_svg
    assert 'fill="#e8b85a" fill-opacity=' not in four_svg


def test_svg_opt_line_clipping_and_stripping() -> None:
    """Verify analytical line clipping, viewer stripping, and compact thumbnail stripping."""
    import math

    from geometor.etc.svg_opt import (
        clip_infinite_line_to_rect,
        strip_svg_for_thumbnail,
        strip_svg_for_viewer,
    )

    # Analytical slab clipping preserves collinearity and bounds
    seg = clip_infinite_line_to_rect(0.0, 0.0, 0.6, 0.8, -10.0, -10.0, 10.0, 10.0)
    assert seg is not None
    x1, y1, x2, y2 = seg
    assert abs((x2 - x1) * 0.8 - (y2 - y1) * 0.6) < 1e-9
    assert -10.0001 <= x1 <= 10.0001 and -10.0001 <= x2 <= 10.0001
    assert -10.0001 <= y1 <= 10.0001 and -10.0001 <= y2 <= 10.0001

    raw_x1 = (X1_VIDEO_DIR / "svgs" / "01_primary.svg").read_text(encoding="utf-8")
    viewer_svg = strip_svg_for_viewer(raw_x1)
    assert "<style>" not in viewer_svg
    assert "INTERACTIVE_SVG_JS" not in viewer_svg
    assert "scaleViewElements" not in viewer_svg
    assert 'class="etc-elements-meta"' in viewer_svg
    assert 'data-line="' in viewer_svg
    assert 'data-lines-viewbox="' in viewer_svg
    assert len(viewer_svg) < len(raw_x1) * 0.55

    # Verify every clipped <line> stays tightly bounded (no 30,000-unit lines!)
    root_v = ET.fromstring(viewer_svg)
    vb = [float(p) for p in root_v.attrib["viewBox"].split()]
    max_allowed = math.hypot(vb[2], vb[3]) * 3.0
    for el in root_v.iter():
        if el.tag.split("}")[-1] == "line":
            ln_len = math.hypot(
                float(el.attrib["x2"]) - float(el.attrib["x1"]),
                float(el.attrib["y2"]) - float(el.attrib["y1"]),
            )
            assert ln_len <= max_allowed, f"Unclipped line length {ln_len:.1f} > {max_allowed:.1f}"

    # Verify all #points circles share one uniform compact radius (4.8px scale)
    pts_g = next((el for el in root_v.iter() if el.attrib.get("id") == "points"), None)
    assert pts_g is not None
    pt_radii = {
        round(float(c.attrib["r"]), 6)
        for c in pts_g
        if c.tag.split("}")[-1] == "circle"
    }
    assert len(pt_radii) == 1, f"Expected uniform point radius, found {pt_radii}"
    assert root_v.attrib.get("data-target-r-px") == "4.8"

    # Verify thumbnail SVG strips scripts + JSON metadata and keeps compact visual CSS
    thumb_svg = strip_svg_for_thumbnail(raw_x1)
    ET.fromstring(thumb_svg)
    assert "<script" not in thumb_svg
    assert "etc-elements-meta" not in thumb_svg
    assert "<style>" in thumb_svg
    assert len(thumb_svg) < 24_000, f"Thumbnail SVG too large: {len(thumb_svg)} bytes"

    # Verify legacy glow-coord blur filter & oversized halo are stripped from coordinates plate
    raw_coord = (X1_VIDEO_DIR / "svgs" / "02_coordinates.svg").read_text(encoding="utf-8")
    viewer_coord = strip_svg_for_viewer(raw_coord)
    root_c = ET.fromstring(viewer_coord)
    assert "feGaussianBlur" not in viewer_coord
    assert "glow-coord" not in viewer_coord
    plate_radii = {
        round(float(c.attrib["r"]), 3)
        for c in root_c.iter()
        if c.tag.split("}")[-1] == "circle" and "etc-plate-pt" in c.attrib.get("class", "")
    }
    assert len(plate_radii) == 1, f"Expected uniform plate point radius, found {plate_radii}"


def test_x1_video_script_compiles_cleanly() -> None:
    """Verify videos/x-00001/script.scr compiles with exact Heronian and Kimberling data."""
    script_path = X1_VIDEO_DIR / "script.scr"
    script_text = script_path.read_text(encoding="utf-8")
    assert "Anticomplement of | X_10 (Spieker):green" in script_text
    assert "Complement of | X_8 (Nagel):orange" in script_text
    assert "Heronian Triangle | 15 | 13 | 14:gold" in script_text
    assert "2√35 / 7 ≈ 1.690308509457" in script_text

    scenes = compile_scenes_from_script(script_text, X1_VIDEO_DIR / "svgs")
    assert len(scenes) == 3
    subslides = [sub for sc in scenes for sub in sc["subslides"]]
    assert len(subslides) == 7
    assert all(sub.get("clause_html") and sub.get("just_tag") for sub in subslides)


def test_cyclic_coordinate_expansion() -> None:
    """Verify cyclic LaTeX permutation preserves commands/invariants and expands triples accurately."""
    from geometor.etc.tracks import _cyclic_permute_latex, _extract_coordinate_triple

    assert _cyclic_permute_latex(r"\sin 2B + \sin 2C - \sin 2A", 1) == r"\sin 2C + \sin 2A - \sin 2B"
    assert _cyclic_permute_latex(r"\csc A \tan 3A - 2 \sec 3A", 2) == r"\csc C \tan 3C - 2 \sec 3C"
    assert _cyclic_permute_latex(r"S_{A} - S_{\omega}", 1) == r"S_{B} - S_{\omega}"
    assert (
        _cyclic_permute_latex(r"bc[a^{2}(b^{2} + c^{2}) - (b^{2} - c^{2})^{2}]", 1)
        == r"ca[b^{2}(c^{2} + a^{2}) - (c^{2} - a^{2})^{2}]"
    )
    assert (
        _cyclic_permute_latex(r"a^{2}(b^{2} + c^{2} + 4 \sqrt{3} \operatorname{area}(ABC))", 1)
        == r"b^{2}(c^{2} + a^{2} + 4 \sqrt{3} \operatorname{area}(ABC))"
    )
    triple, note = _extract_coordinate_triple(r":math:`\sec A' : :`, where A'B'C' is excentral", lambda s: s)
    assert triple == (":math:`\\sec A'`", ":math:`\\sec B'`", ":math:`\\sec C'`")
    assert "excentral" in note

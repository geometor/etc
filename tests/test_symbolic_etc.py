"""Exact symbolic verification suite for GEOMETOR ETC 4-triangle architecture and X_1."""

from __future__ import annotations

import json
import runpy
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import sympy as sp
from geometor.model import line_spread, zero_test

from geometor.etc import (
    CANONICAL_CENTER_CONCORDANCE,
    CANONICAL_TRIANGLES,
    CenterSymbolicRegistry,
    bevan_point,
    centroid,
    circumcenter,
    circumcircle_inverse_of_incenter,
    construct_reference_triangle,
    create_model,
    de_longchamps_point,
    feuerbach_point,
    gergonne_point,
    get_canonical_triangle,
    get_center_concordance,
    incenter,
    isotomic_conjugate_of_incenter,
    mittenpunkt,
    nagel_point,
    nine_point_center,
    orthocenter,
    spieker_center,
    symmedian_point,
)
from geometor.etc.triangles import PHI, SQRT_35, SQRT_PHI
from geometor.etc.video import compile_scenes_from_script

REPO_ROOT = Path(__file__).resolve().parents[1]
X1_DOC_DIR = REPO_ROOT / "docsrc" / "centers" / "c-00001-00019" / "x-00001"
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


def _assert_zero_floats(*exprs: sp.Basic) -> None:
    for expr in exprs:
        floats = expr.atoms(sp.Float)
        assert not floats, f"Unexpected sp.Float atoms {floats} in {expr!r}"


def test_no_model_setitem_bypass_in_source() -> None:
    """Ensure zero super(Model, ...).__setitem__ validation bypasses remain."""
    src_dir = REPO_ROOT / "src" / "geometor" / "etc"
    for py_path in sorted(src_dir.glob("*.py")):
        content = py_path.read_text(encoding="utf-8")
        assert "super(Model" not in content, f"Found super(Model bypass in {py_path}"


@pytest.mark.parametrize("preset", ["heronian", "right", "kepler", "kimberling"])
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
    # Verify Euclidean side quadrances match exact coordinates of A, B, C
    ax, ay = tri.A_xy
    bx, by = tri.B_xy
    cx, cy = tri.C_xy
    assert zero_test((bx - cx) ** 2 + (by - cy) ** 2 - tri.a**2)
    assert zero_test((cx - ax) ** 2 + (cy - ay) ** 2 - tri.b**2)
    assert zero_test((ax - bx) ** 2 + (ay - by) ** 2 - tri.c**2)
    # Verify signed area matchesshoelace formula
    shoelace_two_area = (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)
    assert zero_test(shoelace_two_area - 2 * tri.area)


def test_x1_exact_symbolic_values_across_four_triangles() -> None:
    """Verify exact closed-form X_1 coordinates, sub-areas, and inradii on all 4 triangles."""
    # 1. Heronian (15, 13, 14) over Q
    reg_h = CenterSymbolicRegistry("heronian", cache_dir=None)
    x1_h = reg_h.get(1)
    assert x1_h.xy == (sp.Integer(6), sp.Integer(4))
    assert x1_h.trilinear == (sp.Integer(1), sp.Integer(1), sp.Integer(1))
    assert x1_h.bary == (sp.Integer(15), sp.Integer(13), sp.Integer(14))
    assert x1_h.sub_areas == (sp.Integer(30), sp.Integer(26), sp.Integer(28))
    assert sum(x1_h.sub_areas) == reg_h.triangle.area == sp.Integer(84)
    assert x1_h.search_value == reg_h.triangle.r == sp.Integer(4)
    assert reg_h.triangle.Q_r == sp.Integer(16)

    # 2. Right (3, 4, 5) over Q
    reg_r = CenterSymbolicRegistry("right", cache_dir=None)
    x1_r = reg_r.get(1)
    assert x1_r.xy == (sp.Integer(3), sp.Integer(1))
    assert x1_r.trilinear == (sp.Integer(1), sp.Integer(1), sp.Integer(1))
    assert x1_r.bary == (sp.Integer(3), sp.Integer(4), sp.Integer(5))
    assert x1_r.sub_areas == (sp.Rational(3, 2), sp.Integer(2), sp.Rational(5, 2))
    assert sum(x1_r.sub_areas) == reg_r.triangle.area == sp.Integer(6)
    assert x1_r.search_value == reg_r.triangle.r == sp.Integer(1)
    assert reg_r.triangle.Q_r == sp.Integer(1)

    # 3. Kepler (1, sqrt(phi), phi) over Q(sqrt(phi))
    reg_k = CenterSymbolicRegistry("kepler", cache_dir=None)
    x1_k = reg_k.get(1)
    expected_kx = (SQRT_PHI + PHI - 1) / 2
    expected_ky = (SQRT_PHI - PHI + 1) / 2
    assert zero_test(x1_k.xy[0] - expected_kx)
    assert zero_test(x1_k.xy[1] - expected_ky)
    assert x1_k.trilinear == (sp.Integer(1), sp.Integer(1), sp.Integer(1))
    assert zero_test(x1_k.bary[0] - 1)
    assert zero_test(x1_k.bary[1] - SQRT_PHI)
    assert zero_test(x1_k.bary[2] - PHI)
    assert zero_test(sum(x1_k.sub_areas) - reg_k.triangle.area)
    assert zero_test(x1_k.search_value - expected_ky)

    # 4. Kimberling (6, 9, 13) over Q(sqrt(35))
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


def test_symbolic_registry_cache_roundtrip_and_kimberling_search_values(
    tmp_path: Path,
) -> None:
    """Verify disk cache srepr round-trip and 12-decimal Kimberling search values."""
    reg = CenterSymbolicRegistry("kimberling", cache_dir=tmp_path)
    warmed = reg.warm_collection_1()
    assert reg.cache_file is not None and reg.cache_file.is_file()

    # Reload from disk into a fresh registry instance
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
    """Build x-00001/model.py on all 4 presets with zero sp.Float and verify Heronian spreads."""
    mod_ns = runpy.run_path(str(X1_DOC_DIR / "model.py"))
    model = mod_ns["build_model"](preset)
    assert len(model) > 0
    for el in model:
        _assert_zero_floats(el)

    by_id = {info.ID: el for el, info in model.items() if info.ID}
    reg = CenterSymbolicRegistry(preset, cache_dir=None)
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


def test_canonical_constructors_match_symbolic_registry_on_heronian() -> None:
    """Verify Euclidean constructors in ops.py match exact symbolic coordinates on Heronian."""
    model = create_model("Heronian Constructors Check")
    A, B, C = construct_reference_triangle(model, "heronian")
    reg = CenterSymbolicRegistry("heronian", cache_dir=None)

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
        (20, de_longchamps_point),
        (36, circumcircle_inverse_of_incenter),
        (40, bevan_point),
        (75, isotomic_conjugate_of_incenter),
    ]
    for num, fn in constructors:
        pt = fn(model, A, B, C, ID=f"X_{num}")
        _assert_zero_floats(pt)
        rec = reg.get(num)
        assert zero_test(pt.x - rec.xy[0]), f"X_{num} x mismatch: {pt.x} != {rec.xy[0]}"
        assert zero_test(pt.y - rec.xy[1]), f"X_{num} y mismatch: {pt.y} != {rec.xy[1]}"

    # Spot-check exact rational coordinates of X_36 and X_75 on Heronian (15, 13, 14)
    assert reg.get(36).xy == (sp.Integer(-58), sp.Integer(-4))
    assert reg.get(75).xy == (sp.Rational(3915, 587), sp.Rational(2340, 587))

    # Verify concordance lookup
    c1 = get_center_concordance(1)
    assert c1 is not None and c1.function_name == "incenter"
    assert 36 in CANONICAL_CENTER_CONCORDANCE
    assert 75 in CANONICAL_CENTER_CONCORDANCE


def test_all_13_x1_svgs_well_formed_and_symbolic_meta() -> None:
    """Validate XML well-formedness, data-ref attributes, and etc-elements-meta JSON."""
    doc_svgs = [
        X1_DOC_DIR / "x-00001.svg",
        X1_DOC_DIR / "x-00001-right.svg",
        X1_DOC_DIR / "x-00001-kepler.svg",
        X1_DOC_DIR / "x-00001-kimberling.svg",
        X1_DOC_DIR / "02_coordinates.svg",
        X1_DOC_DIR / "03_central_lines.svg",
        X1_DOC_DIR / "04_relations.svg",
        X1_DOC_DIR / "05_four_triangles.svg",
    ]
    video_svgs = [
        X1_VIDEO_DIR / "svgs" / "01_primary.svg",
        X1_VIDEO_DIR / "svgs" / "02_coordinates.svg",
        X1_VIDEO_DIR / "svgs" / "03_central_lines.svg",
        X1_VIDEO_DIR / "svgs" / "04_relations.svg",
        X1_VIDEO_DIR / "svgs" / "05_four_triangles.svg",
    ]
    for svg_path in doc_svgs + video_svgs:
        assert svg_path.is_file(), f"Missing SVG: {svg_path}"
        raw = svg_path.read_text(encoding="utf-8")
        root = ET.fromstring(raw)
        refs = [el.attrib["data-ref"] for el in root.iter() if "data-ref" in el.attrib]
        assert refs, f"No data-ref elements found in {svg_path.name}"

        meta_nodes = [
            el for el in root.iter() if el.attrib.get("class") == "etc-elements-meta"
        ]
        assert len(meta_nodes) == 1, f"Missing .etc-elements-meta in {svg_path.name}"
        meta = json.loads(meta_nodes[0].text or "{}")
        assert meta, f"Empty .etc-elements-meta JSON in {svg_path.name}"
        has_symbolic_rows = any(
            bool(entry.get("symbolic_rows"))
            for entry in meta.values()
            if isinstance(entry, dict)
        )
        assert has_symbolic_rows, f"No symbolic_rows in {svg_path.name}"


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

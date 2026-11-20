"""Verification tests for the fast exact algebraic-field evaluator (`field_eval.py`)."""

from __future__ import annotations

import pytest
import sympy as sp
from geometor.model import zero_test

from geometor.etc.field_eval import (
    KEPLER_BIQUAD,
    PENTAGON_BIQUAD,
    BiquadElem,
    QElem,
    QuadElem,
    get_triangle_field,
)
from geometor.etc.symbolic_cache import CenterSymbolicRegistry
from geometor.etc.triangles import CANONICAL_TRIANGLES

ALL_7_TRIANGLES = (
    "heronian",
    "right",
    "kepler",
    "kimberling",
    "golden",
    "gnomon",
    "equilateral",
)


def test_biquadratic_inversion_identities() -> None:
    """Verify O(1) Galois-tower inversion in Q(sqrt(phi)) and Q(tau)."""
    for spec in (KEPLER_BIQUAD, PENTAGON_BIQUAD):
        one = BiquadElem(1, 0, 0, 0, spec)
        for elem in (
            BiquadElem(0, 1, 0, 0, spec),
            BiquadElem(0, 0, 1, 0, spec),
            BiquadElem(1, 2, -3, 5, spec),
            BiquadElem(-7, 3, 11, -2, spec),
        ):
            inv_e = elem.inv()
            assert elem * inv_e == one
            assert inv_e * elem == one


def test_quad_and_sqrt_identities() -> None:
    """Verify exact quadratic arithmetic and exact square-root extraction."""
    q35 = QuadElem(3, 2, 35)
    assert q35 * q35.inv() == QuadElem(1, 0, 35)
    sq = q35 * q35
    rt = sq.sqrt_exact()
    assert rt == q35 or rt == -q35

    # sqrt(3) lifted cleanly from QElem
    rt3 = QElem(3).sqrt_exact()
    assert rt3 * rt3 == QElem(3)


@pytest.mark.parametrize("tri_key", ALL_7_TRIANGLES)
def test_exact_match_collection_1_all_7_triangles(tri_key: str) -> None:
    """Every X_1..X_19 center must match CenterSymbolicRegistry with 0 symbolic error."""
    tf = get_triangle_field(tri_key)
    sym_tri = CANONICAL_TRIANGLES[tri_key]
    sym_reg = CenterSymbolicRegistry(tri_key)

    for num in range(1, 20):
        expected = sym_reg.get(num)
        bary_raw = tf.eval_builtin_exact(num)
        actual = tf.package_exact_bary(bary_raw)

        assert actual.is_indeterminate == expected.is_indeterminate, (
            f"X_{num} on {tri_key}: indeterminate mismatch"
        )
        assert actual.is_ideal == expected.is_ideal, (
            f"X_{num} on {tri_key}: ideal mismatch"
        )
        if not expected.is_finite:
            continue

        assert actual.xy is not None
        ax_sym = sym_tri.simplify(actual.xy[0].to_sympy())
        ay_sym = sym_tri.simplify(actual.xy[1].to_sympy())
        assert zero_test(sym_tri.simplify(ax_sym - expected.xy[0])), (
            f"X_{num} on {tri_key} x mismatch: {ax_sym} != {expected.xy[0]}"
        )
        assert zero_test(sym_tri.simplify(ay_sym - expected.xy[1])), (
            f"X_{num} on {tri_key} y mismatch: {ay_sym} != {expected.xy[1]}"
        )
        assert actual.search_value is not None
        sv_sym = sym_tri.simplify(actual.search_value.to_sympy())
        assert zero_test(sym_tri.simplify(sv_sym - expected.search_value)), (
            f"X_{num} on {tri_key} search mismatch: {sv_sym} != {expected.search_value}"
        )


def test_exact_trig_and_half_angle_evaluation() -> None:
    """Verify exact AST evaluation of trig formulas (X_13, X_19, half-angle tangents)."""
    tf = get_triangle_field("heronian")
    sym_reg = CenterSymbolicRegistry("heronian")

    # X_13 = csc(A + pi/3) trilinears
    b13 = tf.eval_cyclic_exact("csc(A + pi/3)", is_trilinear=True)
    r13 = tf.package_exact_bary(b13)
    e13 = sym_reg.get(13)
    assert r13.xy is not None
    assert zero_test(sp.simplify(r13.xy[0].to_sympy() - e13.xy[0]))
    assert zero_test(sp.simplify(r13.xy[1].to_sympy() - e13.xy[1]))

    # X_19 = tan(A) trilinears (Clawson point)
    b19 = tf.eval_cyclic_exact("tan(A)", is_trilinear=True)
    r19 = tf.package_exact_bary(b19)
    e19 = sym_reg.get(19)
    assert r19.xy is not None
    assert zero_test(sp.simplify(r19.xy[0].to_sympy() - e19.xy[0]))
    assert zero_test(sp.simplify(r19.xy[1].to_sympy() - e19.xy[1]))

    # X_7 = sec(A/2)**2 / a -> cot(A/2) -> Gergonne (bary 1/(s-a) = tan(A/2)/r)
    b7 = tf.eval_cyclic_exact("tan(A/2)", is_trilinear=False)
    r7 = tf.package_exact_bary(b7)
    e7 = sym_reg.get(7)
    assert r7.xy is not None
    assert zero_test(sp.simplify(r7.xy[0].to_sympy() - e7.xy[0]))
    assert zero_test(sp.simplify(r7.xy[1].to_sympy() - e7.xy[1]))

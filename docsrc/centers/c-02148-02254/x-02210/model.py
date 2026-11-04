"""GEOMETOR construction model for X_2210 = X_2-ISOCONJUGATE OF X_335."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02210(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2210 = X_2-ISOCONJUGATE OF X_335 on reference triangle ABC."""
    X_334 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(a**(2) - b*c)', ID="X_334", classes=["center"])
    X_2210 = isogonal_conjugate(model, A, B, C, X_334, ID="X_2210", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_31, X_32, 31, 32, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    central_line(model, X_36, X_58, 36, 58, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_251 = eval_trilinear_point(model, A, B, C, 'a**(2)*csc(A +  omega  )', ID="X_251", classes=["center", "incident"])
    central_line(model, X_42, X_251, 42, 251, incident=True)
    return promote_point_to_top(model, X_2210)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2210 on the given reference triangle."""
    model = create_model('X_2210 = X_2-ISOCONJUGATE OF X_335')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02210(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02210.json"))
    write_center_svg(
        model_acute,
        here / "x-02210.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

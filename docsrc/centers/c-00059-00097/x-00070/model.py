"""GEOMETOR construction model for X_70 = ISOGONAL CONJUGATE OF X_26."""

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
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00070(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_70 = ISOGONAL CONJUGATE OF X_26 on reference triangle ABC."""
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_26", classes=["center"])
    X_70 = isogonal_conjugate(model, A, B, C, X_26, ID="X_70", classes=["selected", "target"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    X_1288 = point_from_barycentrics(model, A, B, C, -0.081215203, 0.1407786, 0.9404366, ID="X_1288", classes=["center", "incident"])
    central_line(model, X_74, X_1288, 74, 1288, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1594 = eval_trilinear_point(model, A, B, C, 'sec(A) + 2*cos(B - C)', ID="X_1594", classes=["center", "incident"])
    central_line(model, X_6, X_1594, 6, 1594, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_1899 = eval_trilinear_point(model, A, B, C, '2*b*c - a*b*sec(B) - a*c*sec(C)', ID="X_1899", classes=["center", "incident"])
    central_line(model, X_54, X_1899, 54, 1899, incident=True)
    return promote_point_to_top(model, X_70)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_70 on the given reference triangle."""
    model = create_model('X_70 = ISOGONAL CONJUGATE OF X_26')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00070(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00070.json"))
    write_center_svg(
        model_acute,
        here / "x-00070.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

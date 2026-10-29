"""GEOMETOR construction model for X(733) = EVEN (- 2, 2) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00733(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(733) = EVEN (- 2, 2) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_732 = eval_trilinear_point(model, A, B, C, 'a**(-3)*(b**(2)+ c**(2)) - a**(1)*(b**(-2)+ c**(-2))', ID="X(732)", classes=["center"])
    X_733 = isogonal_conjugate(model, A, B, C, X_732, ID="X(733)", classes=["selected", "target"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X(83)", classes=["center", "incident"])
    central_line(model, X_39, X_83, 39, 83, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_251 = eval_trilinear_point(model, A, B, C, 'a**(2)*csc(A + omega )', ID="X(251)", classes=["center", "incident"])
    central_line(model, X_110, X_251, 110, 251, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_689 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(4) - c**(4)))', ID="X(689)", classes=["center", "incident"])
    central_line(model, X_2, X_689, 2, 689, incident=True)
    return promote_point_to_top(model, X_733)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(733) on the given reference triangle."""
    model = create_model('X(733) = EVEN (- 2, 2) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00733(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00733.json"))
    write_center_svg(
        model_acute,
        here / "x-00733.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

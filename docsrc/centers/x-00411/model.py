"""GEOMETOR construction model for X(411) = EULER X(21)-2nd-SUBSTITUTION POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00411(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(411) = EULER X(21)-2nd-SUBSTITUTION POINT on reference triangle ABC."""
    X_411 = eval_barycentric_point(model, A, B, C, 'a*(a**(6) - a**(5)*b - 2*a**(4)*b**(2) + 2*a**(3)*b**(3) + a**(2)*b**(4) - a*b**(5) - a**(5)*c - a**(4)*b*c + a*b**(4)*c + b**(5)*c - 2*a**(4)*c**(2) + 2*a**(2)*b**(2)*c**(2) + 2*a**(3)*c**(3) - 2*b**(3)*c**(3) + a**(2)*c**(4) + a*b*c**(4) - a*c**(5) + b*c**(5))', ID="X(411)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X(78)", classes=["center", "incident"])
    central_line(model, X_40, X_78, 40, 78, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X(35)", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X(516)", classes=["center", "incident"])
    central_line(model, X_35, X_516, 35, 516, incident=True)
    return promote_point_to_top(model, X_411)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(411) on the given reference triangle."""
    model = create_model('X(411) = EULER X(21)-2nd-SUBSTITUTION POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00411(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00411.json"))
    write_center_svg(
        model_acute,
        here / "x-00411.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

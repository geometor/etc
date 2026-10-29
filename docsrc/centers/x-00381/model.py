"""GEOMETOR construction model for X(381) = MIDPOINT OF X(2) AND X(4)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00381(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(381) = MIDPOINT OF X(2) AND X(4) on reference triangle ABC."""
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X(376)", classes=["center"])
    X_381 = complement(model, A, B, C, X_376, ID="X(381)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center", "incident"])
    central_line(model, X_6, X_13, 6, 13, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    X_156 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(8) - 3*a**(6)*(b**(2) + c**(2)) + a**(4)*(3*b**(4) + 2*b**(2)*c**(2) + 3*c**(4)) - a**(2)*(b**(6) + c**(6)) + b**(2)*c**(2)*(b**(2) - c**(2))**(2))', ID="X(156)", classes=["center", "incident"])
    central_line(model, X_54, X_156, 54, 156, incident=True)
    return promote_point_to_top(model, X_381)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(381) on the given reference triangle."""
    model = create_model('X(381) = MIDPOINT OF X(2) AND X(4)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00381(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00381.json"))
    write_center_svg(
        model_acute,
        here / "x-00381.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

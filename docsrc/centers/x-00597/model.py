"""GEOMETOR construction model for X(597) = MIDPOINT OF X(2) AND X(6)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    midpoint,
    nine_point_center_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00597(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(597) = MIDPOINT OF X(2) AND X(6) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_597 = midpoint(model, X_2, X_6, ID="X(597)", classes=["selected", "target"], guide=False)
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A- omega )', ID="X(182)", classes=["center", "incident"])
    central_line(model, X_30, X_182, 30, 182, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_542 = eval_barycentric_point(model, A, B, C, '2*a**(6) - 2*a**(4)*(b**(2) + c**(2)) + a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2))', ID="X(542)", classes=["center", "incident"])
    central_line(model, X_5, X_542, 5, 542, incident=True)
    return promote_point_to_top(model, X_597)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(597) on the given reference triangle."""
    model = create_model('X(597) = MIDPOINT OF X(2) AND X(6)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00597(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00597.json"))
    write_center_svg(
        model_acute,
        here / "x-00597.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

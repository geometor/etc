"""GEOMETOR construction model for X_2097 = REFLECTION OF X_6 IN X_57."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02097(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2097 = REFLECTION OF X_6 IN X_57 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center"])
    X_329 = eval_trilinear_point(model, A, B, C, '( -1 - cos(A) + cos(B) + cos(C))*(csc(A))', ID="X_329", classes=["center"])
    central_line(model, X_6, X_57, 6, 57)
    central_line(model, X_141, X_329, 141, 329)
    X_2097 = intersect_lines(model, X_6, X_57, X_141, X_329, ID="X_2097", classes=["selected", "target"])
    X_527 = eval_barycentric_point(model, A, B, C, '2*a**(2) - a*(b + c) - (b - c)**(2)', ID="X_527", classes=["center", "incident"])
    X_599 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - 2*b**(2) - 2*c**(2))', ID="X_599", classes=["center", "incident"])
    central_line(model, X_527, X_599, 527, 599, incident=True)
    return promote_point_to_top(model, X_2097)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2097 on the given reference triangle."""
    model = create_model('X_2097 = REFLECTION OF X_6 IN X_57')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02097(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02097.json"))
    write_center_svg(
        model_acute,
        here / "x-02097.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

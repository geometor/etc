"""GEOMETOR construction model for X_2696 = SR(X_74, X_111)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_02696(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2696 = SR(X_74, X_111) on reference triangle ABC."""
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center"])
    X_524 = eval_trilinear_point(model, A, B, C, '(2*a**(2) - b**(2) - c**(2))/a', ID="X_524", classes=["center"])
    central_line(model, X_30, X_111, 30, 111)
    central_line(model, X_74, X_524, 74, 524)
    X_2696 = intersect_lines(model, X_30, X_111, X_74, X_524, ID="X_2696", classes=["selected", "target"])
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X_376", classes=["center", "incident"])
    X_842 = eval_barycentric_point(model, A, B, C, 'a**(2)/(2*a**(6) - 2*a**(4)*(b**(2) + c**(2)) + a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X_842", classes=["center", "incident"])
    central_line(model, X_376, X_842, 376, 842, incident=True)
    return promote_point_to_top(model, X_2696)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2696 on the given reference triangle."""
    model = create_model('X_2696 = SR(X_74, X_111)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02696(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02696.json"))
    write_center_svg(
        model_acute,
        here / "x-02696.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

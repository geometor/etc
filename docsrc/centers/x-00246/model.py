"""GEOMETOR construction model for X(246) = X(3)-LINE CONJUGATE OF X(110)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00246(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(246) = X(3)-LINE CONJUGATE OF X(110) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X(125)", classes=["center"])
    central_line(model, X_3, X_74, 3, 74)
    central_line(model, X_115, X_125, 115, 125)
    X_246 = intersect_lines(model, X_3, X_74, X_115, X_125, ID="X(246)", classes=["selected", "target"])
    return promote_point_to_top(model, X_246)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(246) on the given reference triangle."""
    model = create_model('X(246) = X(3)-LINE CONJUGATE OF X(110)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00246(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00246.json"))
    write_center_svg(
        model_acute,
        here / "x-00246.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

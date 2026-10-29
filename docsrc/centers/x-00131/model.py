"""GEOMETOR construction model for X(131) = INTERSECTION OF LINES X(3)X(125) AND X(4)X(135)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00131(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(131) = INTERSECTION OF LINES X(3)X(125) AND X(4)X(135) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X(125)", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_135 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sin(2*B))/(sec(2*C) - sec(2*A)) + (sin(2*C))/(sec(2*A) - sec(2*B)))', ID="X(135)", classes=["center"])
    central_line(model, X_3, X_125, 3, 125)
    central_line(model, X_4, X_135, 4, 135)
    X_131 = intersect_lines(model, X_3, X_125, X_4, X_135, ID="X(131)", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_136 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2))/(a**(2) - b**(2) - c**(2))', ID="X(136)", classes=["center", "incident"])
    central_line(model, X_5, X_136, 5, 136, incident=True)
    return promote_point_to_top(model, X_131)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(131) on the given reference triangle."""
    model = create_model('X(131) = INTERSECTION OF LINES X(3)X(125) AND X(4)X(135)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00131(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00131.json"))
    write_center_svg(
        model_acute,
        here / "x-00131.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

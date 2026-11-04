"""GEOMETOR construction model for X_2158 = X_2-ISOCONJUGATE OF X_26."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02158(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2158 = X_2-ISOCONJUGATE OF X_26 on reference triangle ABC."""
    X_70 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_70", classes=["center"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center"])
    X_2083 = eval_trilinear_point(model, A, B, C, '((tan(B))**(2) + (tan(C))**(2))*tan(A)', ID="X_2083", classes=["center"])
    X_2148 = eval_trilinear_point(model, A, B, C, 'a*sec(B - C)', ID="X_2148", classes=["center"])
    central_line(model, X_70, X_71, 70, 71)
    central_line(model, X_2083, X_2148, 2083, 2148)
    X_2158 = intersect_lines(model, X_70, X_71, X_2083, X_2148, ID="X_2158", classes=["selected", "target"])
    X_1288 = point_from_barycentrics(model, A, B, C, -0.081215203, 0.1407786, 0.9404366, ID="X_1288", classes=["center", "incident"])
    X_2249 = point_from_barycentrics(model, A, B, C, 0.36268412, 1.1224488, -0.48513296, ID="X_2249", classes=["center", "incident"])
    central_line(model, X_1288, X_2249, 1288, 2249, incident=True)
    return promote_point_to_top(model, X_2158)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2158 on the given reference triangle."""
    model = create_model('X_2158 = X_2-ISOCONJUGATE OF X_26')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02158(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02158.json"))
    write_center_svg(
        model_acute,
        here / "x-02158.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

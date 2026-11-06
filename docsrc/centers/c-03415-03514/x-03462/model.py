"""GEOMETOR construction model for X_3462 = X_5-CEVA CONJUGATE OF X_4."""

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
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03462(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3462 = X_5-CEVA CONJUGATE OF X_4 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_1075 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sec(B))**(2) + (sec(C))**(2) - (sec(A))**(2))', ID="X_1075", classes=["center"])
    central_line(model, X_4, X_54, 4, 54)
    central_line(model, X_2, X_1075, 2, 1075)
    X_3462 = intersect_lines(model, X_4, X_54, X_2, X_1075, ID="X_3462", classes=["selected", "target"])
    X_233 = eval_trilinear_point(model, A, B, C, '(b*cos(C - A) + c*cos(B - A))*cos(B - C)', ID="X_233", classes=["center", "incident"])
    X_1249 = eval_trilinear_point(model, A, B, C, '(tan(A))*(cos(A) - cos(B)*cos(C))', ID="X_1249", classes=["center", "incident"])
    central_line(model, X_233, X_1249, 233, 1249, incident=True)
    return promote_point_to_top(model, X_3462)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3462 on the given reference triangle."""
    model = create_model('X_3462 = X_5-CEVA CONJUGATE OF X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03462(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03462.json"))
    write_center_svg(
        model_acute,
        here / "x-03462.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

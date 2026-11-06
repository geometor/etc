"""GEOMETOR construction model for X_3351 = X_2-CEVA CONJUGATE OF X_3342."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03351(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3351 = X_2-CEVA CONJUGATE OF X_3342 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_282 = eval_trilinear_point(model, A, B, C, '(cot(A/2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X_282", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_1073 = eval_trilinear_point(model, A, B, C, '((cot(A))/(cos(A) - cos(B)*cos(C)))', ID="X_1073", classes=["center"])
    central_line(model, X_4, X_282, 4, 282)
    central_line(model, X_57, X_1073, 57, 1073)
    X_3351 = intersect_lines(model, X_4, X_282, X_57, X_1073, ID="X_3351", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3344 = point_from_barycentrics(model, A, B, C, 0.41191386, 0.36788863, 0.22019751, ID="X_3344", classes=["center", "incident"])
    central_line(model, X_1, X_3344, 1, 3344, incident=True)
    return promote_point_to_top(model, X_3351)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3351 on the given reference triangle."""
    model = create_model('X_3351 = X_2-CEVA CONJUGATE OF X_3342')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03351(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03351.json"))
    write_center_svg(
        model_acute,
        here / "x-03351.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

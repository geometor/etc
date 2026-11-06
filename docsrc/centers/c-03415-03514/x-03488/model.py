"""GEOMETOR construction model for X_3488 = INTERSECTION OF LINES X_1X_4 AND X_8X_405."""

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
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03488(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3488 = INTERSECTION OF LINES X_1X_4 AND X_8X_405 on reference triangle ABC."""
    X_1056 = eval_trilinear_point(model, A, B, C, '(2 + cos(B)*cos(C))', ID="X_1056", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3488 = reflection_in_point(model, X_1056, X_1, ID="X_3488", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_405 = eval_trilinear_point(model, A, B, C, 'b*c*(a + b + c) + a*b*c*cos(A)', ID="X_405", classes=["center", "incident"])
    central_line(model, X_8, X_405, 8, 405, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X_376", classes=["center", "incident"])
    central_line(model, X_57, X_376, 57, 376, incident=True)
    return promote_point_to_top(model, X_3488)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3488 on the given reference triangle."""
    model = create_model('X_3488 = INTERSECTION OF LINES X_1X_4 AND X_8X_405')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03488(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03488.json"))
    write_center_svg(
        model_acute,
        here / "x-03488.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

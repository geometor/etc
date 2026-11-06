"""GEOMETOR construction model for X_3303 = INTERSECTION OF LINES X_1X_3 AND X_496X_498."""

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
    incenter_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03303(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3303 = INTERSECTION OF LINES X_1X_3 AND X_496X_498 on reference triangle ABC."""
    X_3303 = eval_trilinear_point(model, A, B, C, '3 + cos(A)', ID="X_3303", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_344 = eval_trilinear_point(model, A, B, C, '((csc(A/2))**(2))*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4))', ID="X_344", classes=["center", "incident"])
    central_line(model, X_8, X_344, 8, 344, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_497 = eval_trilinear_point(model, A, B, C, '1 - cos(B)*cos(C)', ID="X_497", classes=["center", "incident"])
    central_line(model, X_12, X_497, 12, 497, incident=True)
    return promote_point_to_top(model, X_3303)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3303 on the given reference triangle."""
    model = create_model('X_3303 = INTERSECTION OF LINES X_1X_3 AND X_496X_498')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03303(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03303.json"))
    write_center_svg(
        model_acute,
        here / "x-03303.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

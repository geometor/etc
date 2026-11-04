"""GEOMETOR construction model for X_1071 = INTERSECTION OF LINES X_1X_84 AND X_4X_7."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01071(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1071 = INTERSECTION OF LINES X_1X_84 AND X_4X_7 on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center"])
    X_1071 = crosspoint(model, A, B, C, X_7, X_63, ID="X_1071", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_4, X_7, 4, 7, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_6, X_63, 6, 63, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center", "incident"])
    central_line(model, X_1, X_84, 1, 84, incident=True)
    return promote_point_to_top(model, X_1071)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1071 on the given reference triangle."""
    model = create_model('X_1071 = INTERSECTION OF LINES X_1X_84 AND X_4X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01071(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01071.json"))
    write_center_svg(
        model_acute,
        here / "x-01071.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

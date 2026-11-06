"""GEOMETOR construction model for X_3350 = INTERSECTION OF LINES X_3X_2131 AND X_4X_1073."""

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
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03350(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3350 = INTERSECTION OF LINES X_3X_2131 AND X_4X_1073 on reference triangle ABC."""
    X_3349 = point_from_barycentrics(model, A, B, C, 0.30966513, 0.33289879, 0.35743608, ID="X_3349", classes=["center"])
    X_3350 = isogonal_conjugate(model, A, B, C, X_3349, ID="X_3350", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_1073 = eval_trilinear_point(model, A, B, C, '((cot(A))/(cos(A) - cos(B)*cos(C)))', ID="X_1073", classes=["center", "incident"])
    central_line(model, X_4, X_1073, 4, 1073, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_2131 = point_from_barycentrics(model, A, B, C, 0.36616655, 0.37250097, 0.26133249, ID="X_2131", classes=["center", "incident"])
    central_line(model, X_3, X_2131, 3, 2131, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_3344 = point_from_barycentrics(model, A, B, C, 0.41191386, 0.36788863, 0.22019751, ID="X_3344", classes=["center", "incident"])
    central_line(model, X_6, X_3344, 6, 3344, incident=True)
    return promote_point_to_top(model, X_3350)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3350 on the given reference triangle."""
    model = create_model('X_3350 = INTERSECTION OF LINES X_3X_2131 AND X_4X_1073')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03350(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03350.json"))
    write_center_svg(
        model_acute,
        here / "x-03350.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

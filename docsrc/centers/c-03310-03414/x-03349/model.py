"""GEOMETOR construction model for X_3349 = INTERSECTION OF LINES X_3X_2130 AND X_4X_2131."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03349(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3349 = INTERSECTION OF LINES X_3X_2130 AND X_4X_2131 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2130 = point_from_barycentrics(model, A, B, C, 0.19373197, 0.27423005, 0.53203798, ID="X_2130", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_2131 = point_from_barycentrics(model, A, B, C, 0.36616655, 0.37250097, 0.26133249, ID="X_2131", classes=["center"])
    central_line(model, X_3, X_2130, 3, 2130)
    central_line(model, X_4, X_2131, 4, 2131)
    X_3349 = intersect_lines(model, X_3, X_2130, X_4, X_2131, ID="X_3349", classes=["selected", "target"])
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_223", classes=["center", "incident"])
    X_3341 = point_from_barycentrics(model, A, B, C, 0.05793173, 0.086051457, 0.85601681, ID="X_3341", classes=["center", "incident"])
    central_line(model, X_223, X_3341, 223, 3341, incident=True)
    return promote_point_to_top(model, X_3349)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3349 on the given reference triangle."""
    model = create_model('X_3349 = INTERSECTION OF LINES X_3X_2130 AND X_4X_2131')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03349(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03349.json"))
    write_center_svg(
        model_acute,
        here / "x-03349.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

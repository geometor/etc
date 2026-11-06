"""GEOMETOR construction model for X_3545 = EULER LINE INTERCEPT OF LINE X_11X_1056."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03545(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3545 = EULER LINE INTERCEPT OF LINE X_11X_1056 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_3524 = eval_trilinear_point(model, A, B, C, '3*cos(A) + sin(B)*sin(C)', ID="X_3524", classes=["center"])
    X_3545 = midpoint(model, X_4, X_3524, ID="X_3545", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    X_671 = eval_trilinear_point(model, A, B, C, '1/(a*(2*a**(2) - b**(2) - c**(2)))', ID="X_671", classes=["center", "incident"])
    central_line(model, X_114, X_671, 114, 671, incident=True)
    X_262 = eval_trilinear_point(model, A, B, C, 'sec(A -  omega  )', ID="X_262", classes=["center", "incident"])
    X_538 = point_from_barycentrics(model, A, B, C, -0.75777793, 0.11558409, 0.64219384, ID="X_538", classes=["center", "incident"])
    central_line(model, X_262, X_538, 262, 538, incident=True)
    return promote_point_to_top(model, X_3545)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3545 on the given reference triangle."""
    model = create_model('X_3545 = EULER LINE INTERCEPT OF LINE X_11X_1056')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03545(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03545.json"))
    write_center_svg(
        model_acute,
        here / "x-03545.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

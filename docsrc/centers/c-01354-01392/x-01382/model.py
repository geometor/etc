"""GEOMETOR construction model for X_1382 = 2nd INTERCEPT OF LINE X_1X_3 AND CIRCUMCIRCLE."""

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
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01382(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1382 = 2nd INTERCEPT OF LINE X_1X_3 AND CIRCUMCIRCLE on reference triangle ABC."""
    X_1381 = eval_trilinear_point(model, A, B, C, '(r + ( OI  - R)*cos(A))', ID="X_1381", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_1382 = reflection_in_point(model, X_1381, X_3, ID="X_1382", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    return promote_point_to_top(model, X_1382)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1382 on the given reference triangle."""
    model = create_model('X_1382 = 2nd INTERCEPT OF LINE X_1X_3 AND CIRCUMCIRCLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01382(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01382.json"))
    write_center_svg(
        model_acute,
        here / "x-01382.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

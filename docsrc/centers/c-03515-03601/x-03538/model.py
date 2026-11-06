"""GEOMETOR construction model for X_3538 = EULER LINE INTERCEPT OF LINE X_1038X_1056."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03538(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3538 = EULER LINE INTERCEPT OF LINE X_1038X_1056 on reference triangle ABC."""
    X_3538 = eval_trilinear_point(model, A, B, C, '(cos(B)*cos(C) - 2*sec(B)*sec(C))', ID="X_3538", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_1038 = eval_trilinear_point(model, A, B, C, 'cos(A) + cos(A)*cos(B)*cos(C)', ID="X_1038", classes=["center", "incident"])
    X_1056 = eval_trilinear_point(model, A, B, C, '(2 + cos(B)*cos(C))', ID="X_1056", classes=["center", "incident"])
    central_line(model, X_1038, X_1056, 1038, 1056, incident=True)
    X_1040 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(A)*cos(B)*cos(C)', ID="X_1040", classes=["center", "incident"])
    X_1058 = eval_trilinear_point(model, A, B, C, '(2 - cos(B)*cos(C))', ID="X_1058", classes=["center", "incident"])
    central_line(model, X_1040, X_1058, 1040, 1058, incident=True)
    return promote_point_to_top(model, X_3538)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3538 on the given reference triangle."""
    model = create_model('X_3538 = EULER LINE INTERCEPT OF LINE X_1038X_1056')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03538(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03538.json"))
    write_center_svg(
        model_acute,
        here / "x-03538.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

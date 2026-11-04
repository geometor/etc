"""GEOMETOR construction model for X_1904 = ZOSMA TRANSFORM OF X_1468."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01904(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1904 = ZOSMA TRANSFORM OF X_1468 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_968 = eval_trilinear_point(model, A, B, C, 'a**(2) - 2*a*(b + c) - (b + c)**(2)', ID="X_968", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_12, X_968, 12, 968)
    X_1904 = intersect_lines(model, X_2, X_3, X_12, X_968, ID="X_1904", classes=["selected", "target"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    X_1039 = eval_trilinear_point(model, A, B, C, '(1/(cos(A) + cos(A)*cos(B)*cos(C)))', ID="X_1039", classes=["center", "incident"])
    central_line(model, X_80, X_1039, 80, 1039, incident=True)
    return promote_point_to_top(model, X_1904)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1904 on the given reference triangle."""
    model = create_model('X_1904 = ZOSMA TRANSFORM OF X_1468')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01904(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01904.json"))
    write_center_svg(
        model_acute,
        here / "x-01904.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

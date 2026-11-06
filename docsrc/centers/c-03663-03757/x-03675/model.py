"""GEOMETOR construction model for X_3675 = X_1026com(INTOUCH TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03675(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3675 = X_1026com(INTOUCH TRIANGLE) on reference triangle ABC."""
    X_3675 = eval_barycentric_point(model, A, B, C, 'a*(b - c)**(2)*(b**(2) + c**(2) - a*b - a*c)', ID="X_3675", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X_665", classes=["center", "incident"])
    central_line(model, X_244, X_665, 244, 665, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_1111 = eval_trilinear_point(model, A, B, C, '(((b - c)/a)**(2))', ID="X_1111", classes=["center", "incident"])
    central_line(model, X_11, X_1111, 11, 1111, incident=True)
    return promote_point_to_top(model, X_3675)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3675 on the given reference triangle."""
    model = create_model('X_3675 = X_1026com(INTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03675(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03675.json"))
    write_center_svg(
        model_acute,
        here / "x-03675.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_2095 = REFLECTION OF X_3 IN X_57."""

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
    incenter_of,
    intersect_lines,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02095(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2095 = REFLECTION OF X_3 IN X_57 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_329 = eval_trilinear_point(model, A, B, C, '( -1 - cos(A) + cos(B) + cos(C))*(csc(A))', ID="X_329", classes=["center"])
    central_line(model, X_1, X_3, 1, 3)
    central_line(model, X_5, X_329, 5, 329)
    X_2095 = intersect_lines(model, X_1, X_3, X_5, X_329, ID="X_2095", classes=["selected", "target"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center", "incident"])
    X_527 = eval_barycentric_point(model, A, B, C, '2*a**(2) - a*(b + c) - (b - c)**(2)', ID="X_527", classes=["center", "incident"])
    central_line(model, X_381, X_527, 381, 527, incident=True)
    return promote_point_to_top(model, X_2095)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2095 on the given reference triangle."""
    model = create_model('X_2095 = REFLECTION OF X_3 IN X_57')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02095(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02095.json"))
    write_center_svg(
        model_acute,
        here / "x-02095.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

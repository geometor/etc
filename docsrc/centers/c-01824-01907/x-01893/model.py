"""GEOMETOR construction model for X_1893 = ZOSMA TRANSFORM OF X_991."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01893(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1893 = ZOSMA TRANSFORM OF X_991 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    central_line(model, X_4, X_7, 4, 7)
    central_line(model, X_12, X_37, 12, 37)
    X_1893 = intersect_lines(model, X_4, X_7, X_12, X_37, ID="X_1893", classes=["selected", "target"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    X_430 = eval_barycentric_point(model, A, B, C, '(b + c) * (2*a + b + c) * (-a**(2) + b**(2) - c**(2)) * (a**(2) + b**(2) - c**(2))', ID="X_430", classes=["center", "incident"])
    central_line(model, X_226, X_430, 226, 430, incident=True)
    return promote_point_to_top(model, X_1893)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1893 on the given reference triangle."""
    model = create_model('X_1893 = ZOSMA TRANSFORM OF X_991')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01893(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01893.json"))
    write_center_svg(
        model_acute,
        here / "x-01893.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

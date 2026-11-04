"""GEOMETOR construction model for X_1301 = COLLINGS TRANSFORM OF X_235."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01301(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1301 = COLLINGS TRANSFORM OF X_235 on reference triangle ABC."""
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_122 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A) - cos(B)*cos(C))*(cot(A))**(2)', ID="X_122", classes=["center"])
    central_line(model, X_24, X_64, 24, 64)
    central_line(model, X_4, X_122, 4, 122)
    X_1301 = intersect_lines(model, X_24, X_64, X_4, X_122, ID="X_1301", classes=["selected", "target"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X_98", classes=["center", "incident"])
    X_459 = eval_trilinear_point(model, A, B, C, '(sec(A))/(tan(B) + tan(C) - tan(A))', ID="X_459", classes=["center", "incident"])
    central_line(model, X_98, X_459, 98, 459, incident=True)
    return promote_point_to_top(model, X_1301)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1301 on the given reference triangle."""
    model = create_model('X_1301 = COLLINGS TRANSFORM OF X_235')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01301(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01301.json"))
    write_center_svg(
        model_acute,
        here / "x-01301.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_1789 = INVERSE MIMOSA TRANSFORM OF X_5."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01789(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1789 = INVERSE MIMOSA TRANSFORM OF X_5 on reference triangle ABC."""
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center"])
    central_line(model, X_21, X_36, 21, 36)
    central_line(model, X_3, X_125, 3, 125)
    X_1789 = intersect_lines(model, X_21, X_36, X_3, X_125, ID="X_1789", classes=["selected", "target"])
    return promote_point_to_top(model, X_1789)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1789 on the given reference triangle."""
    model = create_model('X_1789 = INVERSE MIMOSA TRANSFORM OF X_5')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01789(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01789.json"))
    write_center_svg(
        model_acute,
        here / "x-01789.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

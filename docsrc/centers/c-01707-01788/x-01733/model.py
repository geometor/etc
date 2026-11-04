"""GEOMETOR construction model for X_1733 = MIMOSA TRANSFORM OF X_98."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01733(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1733 = MIMOSA TRANSFORM OF X_98 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X_91", classes=["center"])
    central_line(model, X_1, X_75, 1, 75)
    central_line(model, X_19, X_91, 19, 91)
    X_1733 = intersect_lines(model, X_1, X_75, X_19, X_91, ID="X_1733", classes=["selected", "target"])
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A +  omega  )', ID="X_240", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_240, X_522, 240, 522, incident=True)
    return promote_point_to_top(model, X_1733)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1733 on the given reference triangle."""
    model = create_model('X_1733 = MIMOSA TRANSFORM OF X_98')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01733(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01733.json"))
    write_center_svg(
        model_acute,
        here / "x-01733.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

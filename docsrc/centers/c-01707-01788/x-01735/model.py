"""GEOMETOR construction model for X_1735 = MIMOSA TRANSFORM OF X_102."""

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
    intersect_lines,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01735(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1735 = MIMOSA TRANSFORM OF X_102 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A + omega )', ID="X_240", classes=["center"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center"])
    central_line(model, X_1, X_3, 1, 3)
    central_line(model, X_240, X_522, 240, 522)
    X_1735 = intersect_lines(model, X_1, X_3, X_240, X_522, ID="X_1735", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_1074 = eval_trilinear_point(model, A, B, C, '(cos(A) + (cos(B))**(2)*cos(C) + cos(B)*(cos(C))**(2))', ID="X_1074", classes=["center", "incident"])
    central_line(model, X_10, X_1074, 10, 1074, incident=True)
    return promote_point_to_top(model, X_1735)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1735 on the given reference triangle."""
    model = create_model('X_1735 = MIMOSA TRANSFORM OF X_102')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01735(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01735.json"))
    write_center_svg(
        model_acute,
        here / "x-01735.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

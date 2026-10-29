"""GEOMETOR construction model for X(10) = SPIEKER CENTER."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00010(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(10) = SPIEKER CENTER on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    central_line(model, X_1, X_2, 1, 2)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    central_line(model, X_4, X_9, 4, 9)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X(35)", classes=["center"])
    central_line(model, X_21, X_35, 21, 35)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["selected", "target"], draw_circle=True)
    return promote_point_to_top(model, X_10)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(10) on the given reference triangle."""
    model = create_model('X(10) = SPIEKER CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00010(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00010.json"))
    write_center_svg(
        model_acute,
        here / "x-00010.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

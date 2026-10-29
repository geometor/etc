"""GEOMETOR construction model for X(377) = EULER LINE INTERCEPT OF LINE X(7)X(8)."""

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
    gergonne_point_of,
    intersect_lines,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00377(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(377) = EULER LINE INTERCEPT OF LINE X(7)X(8) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_7, X_8, 7, 8)
    X_377 = intersect_lines(model, X_2, X_3, X_7, X_8, ID="X(377)", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X(46)", classes=["center", "incident"])
    central_line(model, X_10, X_46, 10, 46, incident=True)
    return promote_point_to_top(model, X_377)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(377) on the given reference triangle."""
    model = create_model('X(377) = EULER LINE INTERCEPT OF LINE X(7)X(8)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00377(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00377.json"))
    write_center_svg(
        model_acute,
        here / "x-00377.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

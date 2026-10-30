"""GEOMETOR construction model for X(993) = MIDPOINT OF X(1) AND X(63)."""

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
    incenter_of,
    intersect_lines,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00993(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(993) = MIDPOINT OF X(1) AND X(63) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center"])
    central_line(model, X_3, X_10, 3, 10)
    central_line(model, X_1, X_21, 1, 21)
    X_993 = intersect_lines(model, X_3, X_10, X_1, X_21, ID="X(993)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    central_line(model, X_2, X_36, 2, 36, incident=True)
    return promote_point_to_top(model, X_993)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(993) on the given reference triangle."""
    model = create_model('X(993) = MIDPOINT OF X(1) AND X(63)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00993(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00993.json"))
    write_center_svg(
        model_acute,
        here / "x-00993.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

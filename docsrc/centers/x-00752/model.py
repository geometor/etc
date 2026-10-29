"""GEOMETOR construction model for X(752) = EVEN (0, 3) INFINITY POINT."""

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
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00752(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(752) = EVEN (0, 3) INFINITY POINT on reference triangle ABC."""
    X_752 = eval_trilinear_point(model, A, B, C, 'a **(-1)*(b**(3) + c**(3)) - a**(2)*(b**(0) + c**(0))', ID="X(752)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    central_line(model, X_2, X_31, 2, 31, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    central_line(model, X_10, X_44, 10, 44, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_320 = eval_trilinear_point(model, A, B, C, '(1 - 2*cos(A))/a**(2)', ID="X(320)", classes=["center", "incident"])
    central_line(model, X_1, X_320, 1, 320, incident=True)
    return promote_point_to_top(model, X_752)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(752) on the given reference triangle."""
    model = create_model('X(752) = EVEN (0, 3) INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00752(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00752.json"))
    write_center_svg(
        model_acute,
        here / "x-00752.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

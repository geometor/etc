"""GEOMETOR construction model for X(474) = EULER LINE INTERCEPT OF LINE X(10)X(56)."""

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
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00474(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(474) = EULER LINE INTERCEPT OF LINE X(10)X(56) on reference triangle ABC."""
    X_474 = eval_trilinear_point(model, A, B, C, 'cos(A) - (a + b + c)/a', ID="X(474)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    central_line(model, X_10, X_56, 10, 56, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X(72)", classes=["center", "incident"])
    central_line(model, X_57, X_72, 57, 72, incident=True)
    return promote_point_to_top(model, X_474)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(474) on the given reference triangle."""
    model = create_model('X(474) = EULER LINE INTERCEPT OF LINE X(10)X(56)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00474(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00474.json"))
    write_center_svg(
        model_acute,
        here / "x-00474.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

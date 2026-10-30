"""GEOMETOR construction model for X(679) = ISOGONAL CONJUGATE OF X(678)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00679(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(679) = ISOGONAL CONJUGATE OF X(678) on reference triangle ABC."""
    X_678 = point_from_barycentrics(model, A, B, C, 0.41666649, 6.9999877e-07, 0.58333281, ID="X(678)", classes=["center"])
    X_679 = isogonal_conjugate(model, A, B, C, X_678, ID="X(679)", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X(88)", classes=["center", "incident"])
    central_line(model, X_44, X_88, 44, 88, incident=True)
    X_320 = eval_trilinear_point(model, A, B, C, '(1 - 2*cos(A))/a**(2)', ID="X(320)", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X(519)", classes=["center", "incident"])
    central_line(model, X_320, X_519, 320, 519, incident=True)
    return promote_point_to_top(model, X_679)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(679) on the given reference triangle."""
    model = create_model('X(679) = ISOGONAL CONJUGATE OF X(678)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00679(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00679.json"))
    write_center_svg(
        model_acute,
        here / "x-00679.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

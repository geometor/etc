"""GEOMETOR construction model for X(519) = ISOGONAL CONJUGATE OF X(106)."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00519(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(519) = ISOGONAL CONJUGATE OF X(106) on reference triangle ABC."""
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X(106)", classes=["center"])
    X_519 = isogonal_conjugate(model, A, B, C, X_106, ID="X(519)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    central_line(model, X_36, X_100, 36, 100, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X(376)", classes=["center", "incident"])
    central_line(model, X_40, X_376, 40, 376, incident=True)
    return promote_point_to_top(model, X_519)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(519) on the given reference triangle."""
    model = create_model('X(519) = ISOGONAL CONJUGATE OF X(106)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00519(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00519.json"))
    write_center_svg(
        model_acute,
        here / "x-00519.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

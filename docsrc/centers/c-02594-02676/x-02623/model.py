"""GEOMETOR construction model for X_2623 = BARYCENTRIC PRODUCT OF PU(73)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02623(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2623 = BARYCENTRIC PRODUCT OF PU(73) on reference triangle ABC."""
    X_2623 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(B - C)', ID="X_2623", classes=["selected", "target"])
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X_50", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X_647", classes=["center", "incident"])
    central_line(model, X_50, X_647, 50, 647, incident=True)
    X_323 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*(csc(A))**(2)', ID="X_323", classes=["center", "incident"])
    X_401 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))*(csc(A))', ID="X_401", classes=["center", "incident"])
    central_line(model, X_323, X_401, 323, 401, incident=True)
    return promote_point_to_top(model, X_2623)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2623 on the given reference triangle."""
    model = create_model('X_2623 = BARYCENTRIC PRODUCT OF PU(73)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02623(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02623.json"))
    write_center_svg(
        model_acute,
        here / "x-02623.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

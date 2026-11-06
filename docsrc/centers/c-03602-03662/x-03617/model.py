"""GEOMETOR construction model for X_3617 = H(X_1; M, -2)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_03617(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3617 = H(X_1; M, -2) on reference triangle ABC."""
    X_3617 = eval_trilinear_point(model, A, B, C, 'b*c*(a - 3*b - 3*c)', ID="X_3617", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_355 = eval_trilinear_point(model, A, B, C, 'a*cos(A) - (b + c)*cos(B - C)', ID="X_355", classes=["center", "incident"])
    central_line(model, X_20, X_355, 20, 355, incident=True)
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X_45", classes=["center", "incident"])
    X_346 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)**(2)', ID="X_346", classes=["center", "incident"])
    central_line(model, X_45, X_346, 45, 346, incident=True)
    return promote_point_to_top(model, X_3617)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3617 on the given reference triangle."""
    model = create_model('X_3617 = H(X_1; M, -2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03617(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03617.json"))
    write_center_svg(
        model_acute,
        here / "x-03617.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

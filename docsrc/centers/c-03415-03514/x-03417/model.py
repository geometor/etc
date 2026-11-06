"""GEOMETOR construction model for X_3417 = X_1-VERTEX CONJUGATE OF X_4."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03417(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3417 = X_1-VERTEX CONJUGATE OF X_4 on reference triangle ABC."""
    X_355 = eval_trilinear_point(model, A, B, C, 'a*cos(A) - (b + c)*cos(B - C)', ID="X_355", classes=["center"])
    X_3417 = isogonal_conjugate(model, A, B, C, X_355, ID="X_3417", classes=["selected", "target"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_24, X_56, 24, 56, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    central_line(model, X_36, X_47, 36, 47, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_573 = eval_trilinear_point(model, A, B, C, 'cos(A + U)', ID="X_573", classes=["center", "incident"])
    central_line(model, X_48, X_573, 48, 573, incident=True)
    return promote_point_to_top(model, X_3417)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3417 on the given reference triangle."""
    model = create_model('X_3417 = X_1-VERTEX CONJUGATE OF X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03417(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03417.json"))
    write_center_svg(
        model_acute,
        here / "x-03417.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

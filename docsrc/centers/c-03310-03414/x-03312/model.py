"""GEOMETOR construction model for X_3312 = INTERSECTION OF LINES X_3X_6 AND X_4X_1132."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03312(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3312 = INTERSECTION OF LINES X_3X_6 AND X_4X_1132 on reference triangle ABC."""
    X_3312 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*sin(A)', ID="X_3312", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_589 = eval_trilinear_point(model, A, B, C, '(a/(a**(2) - 4*area ))', ID="X_589", classes=["center", "incident"])
    central_line(model, X_25, X_589, 25, 589, incident=True)
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center", "incident"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A +  pi  /4)', ID="X_486", classes=["center", "incident"])
    central_line(model, X_381, X_486, 381, 486, incident=True)
    return promote_point_to_top(model, X_3312)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3312 on the given reference triangle."""
    model = create_model('X_3312 = INTERSECTION OF LINES X_3X_6 AND X_4X_1132')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03312(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03312.json"))
    write_center_svg(
        model_acute,
        here / "x-03312.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

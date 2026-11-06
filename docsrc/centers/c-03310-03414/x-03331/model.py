"""GEOMETOR construction model for X_3331 = INTERSECTION OF LINES X_4X_6 AND X_187X_237."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03331(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3331 = INTERSECTION OF LINES X_4X_6 AND X_187X_237 on reference triangle ABC."""
    X_3331 = eval_trilinear_point(model, A, B, C, '((csc(B)*cos(C))*(sin(2*A) - sin(2*B)) - (csc(C)*cos(B))*(sin(2*C) - sin(2*A)))', ID="X_3331", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A +  omega  )', ID="X_237", classes=["center", "incident"])
    central_line(model, X_187, X_237, 187, 237, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_1625 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2)) / (b**(2) - c**(2))', ID="X_1625", classes=["center", "incident"])
    central_line(model, X_30, X_1625, 30, 1625, incident=True)
    return promote_point_to_top(model, X_3331)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3331 on the given reference triangle."""
    model = create_model('X_3331 = INTERSECTION OF LINES X_4X_6 AND X_187X_237')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03331(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03331.json"))
    write_center_svg(
        model_acute,
        here / "x-03331.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

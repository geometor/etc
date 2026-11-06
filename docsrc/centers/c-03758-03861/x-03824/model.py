"""GEOMETOR construction model for X_3824 = X_3671com(3rd EULER TRIANGLE)."""

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
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03824(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3824 = X_3671com(3rd EULER TRIANGLE) on reference triangle ABC."""
    X_3824 = eval_barycentric_point(model, A, B, C, '((a + 2*b + 2*c)*(b**(3) + c**(3) - a**(2)*b - a**(2)*c - 2*a*b*c - b**(2)*c - b*c**(2)))', ID="X_3824", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center", "incident"])
    central_line(model, X_5, X_142, 5, 142, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_1125 = eval_trilinear_point(model, A, B, C, '(2*a+b+c)/a', ID="X_1125", classes=["center", "incident"])
    central_line(model, X_30, X_1125, 30, 1125, incident=True)
    X_442 = point_from_barycentrics(model, A, B, C, 0.3215734, 0.32603406, 0.35239254, ID="X_442", classes=["center", "incident"])
    X_942 = eval_trilinear_point(model, A, B, C, '2*a*b*c + (b + c)*(a - b + c)*(a + b -c)', ID="X_942", classes=["center", "incident"])
    central_line(model, X_442, X_942, 442, 942, incident=True)
    return promote_point_to_top(model, X_3824)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3824 on the given reference triangle."""
    model = create_model('X_3824 = X_3671com(3rd EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03824(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03824.json"))
    write_center_svg(
        model_acute,
        here / "x-03824.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

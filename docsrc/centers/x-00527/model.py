"""GEOMETOR construction model for X(527) = DIRECTION OF VECTOR AX + BX + CX, where X = X(7)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00527(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(527) = DIRECTION OF VECTOR AX + BX + CX, where X = X(7) on reference triangle ABC."""
    X_527 = eval_barycentric_point(model, A, B, C, '2*a**(2) - a*(b + c) - (b - c)**(2)', ID="X(527)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    X_320 = eval_trilinear_point(model, A, B, C, '(1 - 2*cos(A))/a**(2)', ID="X(320)", classes=["center", "incident"])
    central_line(model, X_190, X_320, 190, 320, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_527)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(527) on the given reference triangle."""
    model = create_model('X(527) = DIRECTION OF VECTOR AX + BX + CX, where X = X(7)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00527(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00527.json"))
    write_center_svg(
        model_acute,
        here / "x-00527.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

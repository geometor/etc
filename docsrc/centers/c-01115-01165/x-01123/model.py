"""GEOMETOR construction model for X_1123 = PAASCHE POINT."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01123(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1123 = PAASCHE POINT on reference triangle ABC."""
    X_1123 = eval_trilinear_point(model, A, B, C, '1/(1 +sin(A))', ID="X_1123", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_158 = eval_trilinear_point(model, A, B, C, '(sec(A))**(2)', ID="X_158", classes=["center", "incident"])
    central_line(model, X_37, X_158, 37, 158, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_482 = eval_trilinear_point(model, A, B, C, '1 + 2*sec(A/2)*cos(B/2)*cos(C/2)', ID="X_482", classes=["center", "incident"])
    central_line(model, X_57, X_482, 57, 482, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_586 = eval_trilinear_point(model, A, B, C, '((2*area*(1/b + 1/c - 1/a) + a - b - c)/a)', ID="X_586", classes=["center", "incident"])
    central_line(model, X_2, X_586, 2, 586, incident=True)
    return promote_point_to_top(model, X_1123)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1123 on the given reference triangle."""
    model = create_model('X_1123 = PAASCHE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01123(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01123.json"))
    write_center_svg(
        model_acute,
        here / "x-01123.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

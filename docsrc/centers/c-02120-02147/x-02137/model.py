"""GEOMETOR construction model for X_2137 = ISOGONAL CONJUGATE OF X_2136."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02137(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2137 = ISOGONAL CONJUGATE OF X_2136 on reference triangle ABC."""
    X_2136 = eval_barycentric_point(model, A, B, C, 'a*(a**(2)+2*(b+c)*a+b**(2)-6*b*c+c**(2)) * (-a+b+c)', ID="X_2136", classes=["center"])
    X_2137 = isogonal_conjugate(model, A, B, C, X_2136, ID="X_2137", classes=["selected", "target"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_57, X_145, 57, 145, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_1743 = eval_trilinear_point(model, A, B, C, '3*a - b - c', ID="X_1743", classes=["center", "incident"])
    central_line(model, X_56, X_1743, 56, 1743, incident=True)
    X_1407 = eval_trilinear_point(model, A, B, C, '(1 - cos(A))*(1 - cos(A) + cos(B) + cos(C))', ID="X_1407", classes=["center", "incident"])
    X_1420 = eval_trilinear_point(model, A, B, C, '3*cos(A) + cos(B) + cos(C) - 3', ID="X_1420", classes=["center", "incident"])
    central_line(model, X_1407, X_1420, 1407, 1420, incident=True)
    return promote_point_to_top(model, X_2137)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2137 on the given reference triangle."""
    model = create_model('X_2137 = ISOGONAL CONJUGATE OF X_2136')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02137(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02137.json"))
    write_center_svg(
        model_acute,
        here / "x-02137.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

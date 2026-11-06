"""GEOMETOR construction model for X_3800 = X_512com[INVERSE(nT(a², a² + b²))]."""

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


def construct_x_03800(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3800 = X_512com[INVERSE(nT(a², a² + b²))] on reference triangle ABC."""
    X_907 = eval_trilinear_point(model, A, B, C, '(a/((b**(2) - c**(2))*(3*a**(2) + b**(2) + c**(2))))', ID="X_907", classes=["center"])
    X_3800 = isogonal_conjugate(model, A, B, C, X_907, ID="X_3800", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_419 = eval_barycentric_point(model, A, B, C, '(a**(2) - b*c) * (a**(2) + b*c) * (a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2))', ID="X_419", classes=["center", "incident"])
    X_2501 = eval_trilinear_point(model, A, B, C, 'tan(A)*sin(B - C)', ID="X_2501", classes=["center", "incident"])
    central_line(model, X_419, X_2501, 419, 2501, incident=True)
    X_879 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))/(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X_879", classes=["center", "incident"])
    X_3527 = eval_trilinear_point(model, A, B, C, '(1/(cos(A) + sin(B)*sin(C)))', ID="X_3527", classes=["center", "incident"])
    central_line(model, X_879, X_3527, 879, 3527, incident=True)
    return promote_point_to_top(model, X_3800)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3800 on the given reference triangle."""
    model = create_model('X_3800 = X_512com[INVERSE(nT(a², a² + b²))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03800(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03800.json"))
    write_center_svg(
        model_acute,
        here / "x-03800.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

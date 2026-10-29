"""GEOMETOR construction model for X(296) = ISOGONAL CONJUGATE OF X(243)."""

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
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00296(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(296) = ISOGONAL CONJUGATE OF X(243) on reference triangle ABC."""
    X_243 = eval_barycentric_point(model, A, B, C, '(a - b - c)*(a**(4) - a**(2)*(b**(2) - b*c + c**(2)) - b*c*(b - c)**(2))/(a**(2) - b**(2) - c**(2))', ID="X(243)", classes=["center"])
    X_296 = isogonal_conjugate(model, A, B, C, X_243, ID="X(296)", classes=["selected", "target"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center", "incident"])
    central_line(model, X_29, X_65, 29, 65, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X(185)", classes=["center", "incident"])
    central_line(model, X_1, X_185, 1, 185, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X(284)", classes=["center", "incident"])
    central_line(model, X_109, X_284, 109, 284, incident=True)
    return promote_point_to_top(model, X_296)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(296) on the given reference triangle."""
    model = create_model('X(296) = ISOGONAL CONJUGATE OF X(243)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00296(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00296.json"))
    write_center_svg(
        model_acute,
        here / "x-00296.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

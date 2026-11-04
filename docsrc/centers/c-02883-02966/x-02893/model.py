"""GEOMETOR construction model for X_2893 = ANTICOMPLEMENTARY CONJUGATE OF X_63."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02893(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2893 = ANTICOMPLEMENTARY CONJUGATE OF X_63 on reference triangle ABC."""
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center"])
    X_2893 = anticomplement(model, A, B, C, X_284, ID="X_2893", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_4, X_69, 4, 69, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_150 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) + a*(b*c**(2) +c*b**(2) - b**(3) - c**(3)) - b*c*(a**(2) + b**(2) + c**(2)) + (b + c)*a**(3)))', ID="X_150", classes=["center", "incident"])
    central_line(model, X_75, X_150, 75, 150, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_272 = eval_trilinear_point(model, A, B, C, '(1/((sin(A) + sin(A - B) + sin(A - C))*(sin(B) + sin(C))))', ID="X_272", classes=["center", "incident"])
    central_line(model, X_2, X_272, 2, 272, incident=True)
    return promote_point_to_top(model, X_2893)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2893 on the given reference triangle."""
    model = create_model('X_2893 = ANTICOMPLEMENTARY CONJUGATE OF X_63')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02893(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02893.json"))
    write_center_svg(
        model_acute,
        here / "x-02893.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

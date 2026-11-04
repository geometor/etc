"""GEOMETOR construction model for X_2811 = ISOGONAL CONJUGATE OF X_2727."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02811(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2811 = ISOGONAL CONJUGATE OF X_2727 on reference triangle ABC."""
    X_2727 = point_from_barycentrics(model, A, B, C, -0.14177039, 0.3057906, 0.83597979, ID="X_2727", classes=["center"])
    X_2811 = isogonal_conjugate(model, A, B, C, X_2727, ID="X_2811", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    central_line(model, X_101, X_107, 101, 107, incident=True)
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X_116", classes=["center", "incident"])
    X_122 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A) - cos(B)*cos(C))*(cot(A))**(2)', ID="X_122", classes=["center", "incident"])
    central_line(model, X_116, X_122, 116, 122, incident=True)
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center", "incident"])
    X_133 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sin(2*B) - sin(2*C))**(2) + (sin(2*A))*(sin(2*B)) + (sin(2*A))*(sin(2*C)) - 2*(sin(2*B))*(sin(2*C)))*(2*sin(2*A) - sin(2*B) - sin(2*C))', ID="X_133", classes=["center", "incident"])
    central_line(model, X_118, X_133, 118, 133, incident=True)
    return promote_point_to_top(model, X_2811)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2811 on the given reference triangle."""
    model = create_model('X_2811 = ISOGONAL CONJUGATE OF X_2727')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02811(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02811.json"))
    write_center_svg(
        model_acute,
        here / "x-02811.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

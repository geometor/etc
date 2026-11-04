"""GEOMETOR construction model for X_2822 = ISOGONAL CONJUGATE OF X_2738."""

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


def construct_x_02822(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2822 = ISOGONAL CONJUGATE OF X_2738 on reference triangle ABC."""
    X_2738 = point_from_barycentrics(model, A, B, C, 1.0098259, 0.48587606, -0.49570201, ID="X_2738", classes=["center"])
    X_2822 = isogonal_conjugate(model, A, B, C, X_2738, ID="X_2822", classes=["selected", "target"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    central_line(model, X_27, X_103, 27, 103, incident=True)
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center", "incident"])
    X_122 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A) - cos(B)*cos(C))*(cot(A))**(2)', ID="X_122", classes=["center", "incident"])
    central_line(model, X_118, X_122, 118, 122, incident=True)
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X_116", classes=["center", "incident"])
    X_133 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sin(2*B) - sin(2*C))**(2) + (sin(2*A))*(sin(2*B)) + (sin(2*A))*(sin(2*C)) - 2*(sin(2*B))*(sin(2*C)))*(2*sin(2*A) - sin(2*B) - sin(2*C))', ID="X_133", classes=["center", "incident"])
    central_line(model, X_116, X_133, 116, 133, incident=True)
    return promote_point_to_top(model, X_2822)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2822 on the given reference triangle."""
    model = create_model('X_2822 = ISOGONAL CONJUGATE OF X_2738')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02822(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02822.json"))
    write_center_svg(
        model_acute,
        here / "x-02822.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

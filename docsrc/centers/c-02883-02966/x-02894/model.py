"""GEOMETOR construction model for X_2894 = ANTICOMPLEMENTARY CONJUGATE OF X_72."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02894(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2894 = ANTICOMPLEMENTARY CONJUGATE OF X_72 on reference triangle ABC."""
    X_943 = eval_trilinear_point(model, A, B, C, '(1/(2*a*b*c + (b + c)*(a - b + c)*(a + b - c)))', ID="X_943", classes=["center"])
    X_2894 = anticomplement(model, A, B, C, X_943, ID="X_2894", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_144 = eval_trilinear_point(model, A, B, C, '(csc(A))*(tan(B/2) + tan(C/2) - tan(A/2))', ID="X_144", classes=["center", "incident"])
    central_line(model, X_4, X_144, 4, 144, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_149 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(3) + c**(3) - a**(3) + (a**(2) - b*c)*(b + c) + a*(b*c - b**(2) - c**(2))))', ID="X_149", classes=["center", "incident"])
    central_line(model, X_21, X_149, 21, 149, incident=True)
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    X_377 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) - 2*b**(2)*c**(2) - 2*a*b*c*(a + b + c)))', ID="X_377", classes=["center", "incident"])
    central_line(model, X_145, X_377, 145, 377, incident=True)
    return promote_point_to_top(model, X_2894)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2894 on the given reference triangle."""
    model = create_model('X_2894 = ANTICOMPLEMENTARY CONJUGATE OF X_72')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02894(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02894.json"))
    write_center_svg(
        model_acute,
        here / "x-02894.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

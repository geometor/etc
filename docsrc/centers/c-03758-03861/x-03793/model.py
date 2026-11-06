"""GEOMETOR construction model for X_3793 = X_625com[INVERSE(nT(a², a² - c²))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03793(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3793 = X_625com[INVERSE(nT(a², a² - c²))] on reference triangle ABC."""
    X_3793 = eval_barycentric_point(model, A, B, C, '(3*a**(2)+b**(2)+c**(2)) * (2*a**(2)-b**(2)-c**(2))', ID="X_3793", classes=["selected", "target"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center", "incident"])
    central_line(model, X_32, X_141, 32, 141, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_148 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - (b**(2) - c**(2))**(2) + b**(2)*c**(2) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X_148", classes=["center", "incident"])
    central_line(model, X_30, X_148, 30, 148, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_193 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cot(B) + cot(C) - cot(A))', ID="X_193", classes=["center", "incident"])
    central_line(model, X_3, X_193, 3, 193, incident=True)
    return promote_point_to_top(model, X_3793)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3793 on the given reference triangle."""
    model = create_model('X_3793 = X_625com[INVERSE(nT(a², a² - c²))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03793(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03793.json"))
    write_center_svg(
        model_acute,
        here / "x-03793.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

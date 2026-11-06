"""GEOMETOR construction model for X_3324 = INCIRCLE TRANSFORM T(X_822)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03324(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3324 = INCIRCLE TRANSFORM T(X_822) on reference triangle ABC."""
    X_3324 = eval_barycentric_point(model, A, B, C, '((b + c)**(2)*(a**(6) - a**(4)*(2*b**(2) - 3*b*c + 2*c**(2)) + a**(2)*(b - c)**(2)*(b**(2) + c**(2)) - b*c*(b**(2) - c**(2))**(2))**(2)/(b + c - a))', ID="X_3324", classes=["selected", "target"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_122 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A) - cos(B)*cos(C))*(cot(A))**(2)', ID="X_122", classes=["center", "incident"])
    central_line(model, X_12, X_122, 12, 122, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    central_line(model, X_56, X_107, 56, 107, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1294 = eval_barycentric_point(model, A, B, C, '1/(a**(6)*(b**(2) + c**(2)) - a**(4)*(3*b**(4) - 4*b**(2)*c**(2) + 3*c**(4)) + 3*a**(2)*(b**(2) - c**(2))**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2)*(b**(4) + 4*b**(2)*c**(2) + c**(4)))', ID="X_1294", classes=["center", "incident"])
    central_line(model, X_55, X_1294, 55, 1294, incident=True)
    return promote_point_to_top(model, X_3324)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3324 on the given reference triangle."""
    model = create_model('X_3324 = INCIRCLE TRANSFORM T(X_822)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03324(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03324.json"))
    write_center_svg(
        model_acute,
        here / "x-03324.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

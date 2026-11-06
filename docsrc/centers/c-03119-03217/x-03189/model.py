"""GEOMETOR construction model for X_3189 = X_27-CEVA CONJUGATE OF X_9."""

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
    nagel_point_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03189(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3189 = X_27-CEVA CONJUGATE OF X_9 on reference triangle ABC."""
    X_2550 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c + a*cos(B)*cos(C)))', ID="X_2550", classes=["center"])
    X_3174 = eval_barycentric_point(model, A, B, C, '(a*( b + c - a)*(a**(3) - 3*a**(2)*b - 3*a**(2)*c + a*(3*b**(2) - 2*b*c + 3*c**(2)) - (b + c)*(b - c)**(2)))', ID="X_3174", classes=["center"])
    X_3189 = reflection_in_point(model, X_2550, X_3174, ID="X_3189", classes=["selected", "target"], guide=False)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_8, X_21, 8, 21, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center", "incident"])
    central_line(model, X_1, X_142, 1, 142, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_65, X_145, 65, 145, incident=True)
    return promote_point_to_top(model, X_3189)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3189 on the given reference triangle."""
    model = create_model('X_3189 = X_27-CEVA CONJUGATE OF X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03189(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03189.json"))
    write_center_svg(
        model_acute,
        here / "x-03189.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_2916 = TANGENTIAL-ISOGONAL CONJUGATE OF X_2."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02916(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2916 = TANGENTIAL-ISOGONAL CONJUGATE OF X_2 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1176 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a**(2))/(b**(2) + c**(2))', ID="X_1176", classes=["center"])
    X_2916 = reflection_in_point(model, X_6, X_1176, ID="X_2916", classes=["selected", "target"], guide=False)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    central_line(model, X_6, X_22, 6, 22, incident=True)
    X_195 = eval_trilinear_point(model, A, B, C, 'a*(a**(8) + b**(8) + c**(8) - 4*a**(6)*(b**(2) + c**(2)) + a**(4)*(6*b**(4) + 6*c**(4) + 5*b**(2)*c**(2)) - a**(2)*(4*b**(6) + 4*c**(6) - b**(4)*c**(2) - b**(2)*c**(4)) - 2*b**(2)*c**(2)*(b**(4) + c**(4) - b**(2)*c**(2)))', ID="X_195", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_195, X_511, 195, 511, incident=True)
    X_159 = eval_trilinear_point(model, A, B, C, '(a*((a**(2) + b**(2) + c**(2))*sin(2*A) + (c**(2) - b**(2) - a**(2))*sin(2*B) + (b**(2) - c**(2) - a**(2))*sin(2*C)))', ID="X_159", classes=["center", "incident"])
    X_599 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - 2*b**(2) - 2*c**(2))', ID="X_599", classes=["center", "incident"])
    central_line(model, X_159, X_599, 159, 599, incident=True)
    return promote_point_to_top(model, X_2916)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2916 on the given reference triangle."""
    model = create_model('X_2916 = TANGENTIAL-ISOGONAL CONJUGATE OF X_2')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02916(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02916.json"))
    write_center_svg(
        model_acute,
        here / "x-02916.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

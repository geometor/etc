"""GEOMETOR construction model for X_3421 = ISOGONAL CONJUGATE OF X_3420."""

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
    midpoint,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03421(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3421 = ISOGONAL CONJUGATE OF X_3420 on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_329 = eval_trilinear_point(model, A, B, C, '( -1 - cos(A) + cos(B) + cos(C))*(csc(A))', ID="X_329", classes=["center"])
    X_3421 = midpoint(model, X_8, X_329, ID="X_3421", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_4, X_8, 4, 8, incident=True)
    X_144 = eval_trilinear_point(model, A, B, C, '(csc(A))*(tan(B/2) + tan(C/2) - tan(A/2))', ID="X_144", classes=["center", "incident"])
    X_153 = eval_barycentric_point(model, A, B, C, 'a**(7) - a**(6)*(b + c) - a**(5)*(b**(2) - 7*b*c + c**(2)) + a**(4)*(b + c)*(b**(2) - 6*b*c + c**(2)) - a**(3)*(b**(4) + 2*b**(3)*c - 10*b**(2)*c**(2) + 2*b*c**(3) + c**(4)) + a**(2)*(b - c)**(2)*(b + c)*(b**(2) + 6*b*c + c**(2)) + a*(b**(2) - c**(2))**(2)*(b**(2) - 5*b*c + c**(2)) - (b - c)**(4)*(b + c)**(3)', ID="X_153", classes=["center", "incident"])
    central_line(model, X_144, X_153, 144, 153, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_388 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) + (b + c)**(2))/(b + c - a)', ID="X_388", classes=["center", "incident"])
    central_line(model, X_57, X_388, 57, 388, incident=True)
    return promote_point_to_top(model, X_3421)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3421 on the given reference triangle."""
    model = create_model('X_3421 = ISOGONAL CONJUGATE OF X_3420')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03421(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03421.json"))
    write_center_svg(
        model_acute,
        here / "x-03421.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

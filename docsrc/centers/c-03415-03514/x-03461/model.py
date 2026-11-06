"""GEOMETOR construction model for X_3461 = ISOGONAL CONJUGATE OF X_3460."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03461(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3461 = ISOGONAL CONJUGATE OF X_3460 on reference triangle ABC."""
    X_3460 = point_from_barycentrics(model, A, B, C, 0.29060152, 0.26847785, 0.44092064, ID="X_3460", classes=["center"])
    X_3461 = isogonal_conjugate(model, A, B, C, X_3460, ID="X_3461", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2120 = point_from_barycentrics(model, A, B, C, 0.30475192, 0.22664215, 0.46860594, ID="X_2120", classes=["center", "incident"])
    central_line(model, X_1, X_2120, 1, 2120, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_2595 = eval_trilinear_point(model, A, B, C, '(cos(A - B)*cos(A - C) + (cos(B - C))**(2))', ID="X_2595", classes=["center", "incident"])
    central_line(model, X_5, X_2595, 5, 2595, incident=True)
    X_195 = eval_trilinear_point(model, A, B, C, 'a*(a**(8) + b**(8) + c**(8) - 4*a**(6)*(b**(2) + c**(2)) + a**(4)*(6*b**(4) + 6*c**(4) + 5*b**(2)*c**(2)) - a**(2)*(4*b**(6) + 4*c**(6) - b**(4)*c**(2) - b**(2)*c**(4)) - 2*b**(2)*c**(2)*(b**(4) + c**(4) - b**(2)*c**(2)))', ID="X_195", classes=["center", "incident"])
    X_3468 = eval_trilinear_point(model, A, B, C, '2 - sec(A) + sec(B) + sec(C)', ID="X_3468", classes=["center", "incident"])
    central_line(model, X_195, X_3468, 195, 3468, incident=True)
    return promote_point_to_top(model, X_3461)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3461 on the given reference triangle."""
    model = create_model('X_3461 = ISOGONAL CONJUGATE OF X_3460')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03461(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03461.json"))
    write_center_svg(
        model_acute,
        here / "x-03461.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

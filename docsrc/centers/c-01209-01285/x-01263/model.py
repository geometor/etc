"""GEOMETOR construction model for X_1263 = ISOGONAL CONJUGATE OF X_1157."""

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
    isogonal_conjugate,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01263(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1263 = ISOGONAL CONJUGATE OF X_1157 on reference triangle ABC."""
    X_1157 = eval_trilinear_point(model, A, B, C, '4*cos(A) + cos(3*A)*sec(A)*sec(B - C)', ID="X_1157", classes=["center"])
    X_1263 = isogonal_conjugate(model, A, B, C, X_1157, ID="X_1263", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_128 = eval_trilinear_point(model, A, B, C, '((sec(A))*(cos(2*B) + cos(2*C))*(1 + 2*cos(2*A))*(cos(2*A) + 2*cos(2*B)*cos(2*C)))', ID="X_128", classes=["center", "incident"])
    central_line(model, X_5, X_128, 5, 128, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_195 = eval_trilinear_point(model, A, B, C, 'a*(a**(8) + b**(8) + c**(8) - 4*a**(6)*(b**(2) + c**(2)) + a**(4)*(6*b**(4) + 6*c**(4) + 5*b**(2)*c**(2)) - a**(2)*(4*b**(6) + 4*c**(6) - b**(4)*c**(2) - b**(2)*c**(4)) - 2*b**(2)*c**(2)*(b**(4) + c**(4) - b**(2)*c**(2)))', ID="X_195", classes=["center", "incident"])
    central_line(model, X_4, X_195, 4, 195, incident=True)
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    X_930 = eval_barycentric_point(model, A, B, C, '1/((b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) - b**(2)*c**(2)))', ID="X_930", classes=["center", "incident"])
    central_line(model, X_140, X_930, 140, 930, incident=True)
    return promote_point_to_top(model, X_1263)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1263 on the given reference triangle."""
    model = create_model('X_1263 = ISOGONAL CONJUGATE OF X_1157')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01263(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01263.json"))
    write_center_svg(
        model_acute,
        here / "x-01263.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

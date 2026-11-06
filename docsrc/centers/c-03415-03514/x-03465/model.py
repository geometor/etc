"""GEOMETOR construction model for X_3465 = X_30-CEVA CONJUGATE OF X_484."""

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
    orthocenter_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03465(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3465 = X_30-CEVA CONJUGATE OF X_484 on reference triangle ABC."""
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center"])
    X_2222 = eval_barycentric_point(model, A, B, C, 'a*(a - b)*(a - c)*(a - b + c)*(a + b - c)*(a**(2) - b**(2) + c**(2) - a*c)*(a**(2) - c**(2) + b**(2) - a*b)', ID="X_2222", classes=["center"])
    X_3465 = reflection_in_point(model, X_484, X_2222, ID="X_3465", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_228 = eval_trilinear_point(model, A, B, C, '(sin(2*A))*(sin(B) + sin(C))', ID="X_228", classes=["center", "incident"])
    central_line(model, X_35, X_228, 35, 228, incident=True)
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_74, X_484, 74, 484, incident=True)
    return promote_point_to_top(model, X_3465)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3465 on the given reference triangle."""
    model = create_model('X_3465 = X_30-CEVA CONJUGATE OF X_484')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03465(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03465.json"))
    write_center_svg(
        model_acute,
        here / "x-03465.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

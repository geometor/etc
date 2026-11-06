"""GEOMETOR construction model for X_3891 = X_2887com[INVERSE(n(3rd EULER TRIANGLE))]."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03891(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3891 = X_2887com[INVERSE(n(3rd EULER TRIANGLE))] on reference triangle ABC."""
    X_3891 = eval_barycentric_point(model, A, B, C, '(a**(3) + a*b**(2) + a*c**(2) - b**(2)*c - b*c**(2))', ID="X_3891", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_1, X_321, 1, 321, incident=True)
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    X_388 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) + (b + c)**(2))/(b + c - a)', ID="X_388", classes=["center", "incident"])
    central_line(model, X_145, X_388, 145, 388, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_726 = eval_trilinear_point(model, A, B, C, '(a **(-3)*(b **(-1) + c **(-1)) - a **(-2)*(b **(-2) + c **(-2)))', ID="X_726", classes=["center", "incident"])
    central_line(model, X_31, X_726, 31, 726, incident=True)
    return promote_point_to_top(model, X_3891)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3891 on the given reference triangle."""
    model = create_model('X_3891 = X_2887com[INVERSE(n(3rd EULER TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03891(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03891.json"))
    write_center_svg(
        model_acute,
        here / "x-03891.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

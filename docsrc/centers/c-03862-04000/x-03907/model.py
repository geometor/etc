"""GEOMETOR construction model for X_3907 = X_512com[INVERSE(n(3rd EULER TRIANGLE))]."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03907(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3907 = X_512com[INVERSE(n(3rd EULER TRIANGLE))] on reference triangle ABC."""
    X_3907 = eval_barycentric_point(model, A, B, C, '((b - c)*(b + c - a)*(a**(2) + b*c))', ID="X_3907", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_810 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*((cos(B))**(2) - (cos(C))**(2))', ID="X_810", classes=["center", "incident"])
    central_line(model, X_1, X_810, 1, 810, incident=True)
    X_1027 = eval_trilinear_point(model, A, B, C, '((b - c)/(b**(2) + c**(2) - a*(b + c)))', ID="X_1027", classes=["center", "incident"])
    X_1222 = point_from_barycentrics(model, A, B, C, 0.3683818, 0.31991051, 0.31170768, ID="X_1222", classes=["center", "incident"])
    central_line(model, X_1027, X_1222, 1027, 1222, incident=True)
    return promote_point_to_top(model, X_3907)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3907 on the given reference triangle."""
    model = create_model('X_3907 = X_512com[INVERSE(n(3rd EULER TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03907(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03907.json"))
    write_center_svg(
        model_acute,
        here / "x-03907.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

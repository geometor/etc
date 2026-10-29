"""GEOMETOR construction model for X(911) = POINT ADHARA."""

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


def construct_x_00911(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(911) = POINT ADHARA on reference triangle ABC."""
    X_911 = eval_barycentric_point(model, A, B, C, 'a**(3) / (2*a**(3) - a**(2)*(b + c) - (b - c)**(2)*(b + c))', ID="X(911)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_3, X_101, 3, 101, incident=True)
    X_241 = eval_trilinear_point(model, A, B, C, '(b**(2) + c**(2) - a*b - a*c)/(a - b - c)', ID="X(241)", classes=["center", "incident"])
    X_294 = eval_trilinear_point(model, A, B, C, '(b + c - a)/(b**(2)+ c**(2)- a*b - a*c)', ID="X(294)", classes=["center", "incident"])
    central_line(model, X_241, X_294, 241, 294, incident=True)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["center", "incident"])
    X_603 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A))', ID="X(603)", classes=["center", "incident"])
    central_line(model, X_41, X_603, 41, 603, incident=True)
    return promote_point_to_top(model, X_911)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(911) on the given reference triangle."""
    model = create_model('X(911) = POINT ADHARA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00911(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00911.json"))
    write_center_svg(
        model_acute,
        here / "x-00911.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

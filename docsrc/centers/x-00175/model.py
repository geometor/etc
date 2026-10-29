"""GEOMETOR construction model for X(175) = ISOPERIMETRIC POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00175(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(175) = ISOPERIMETRIC POINT on reference triangle ABC."""
    X_175 = eval_trilinear_point(model, A, B, C, '-1 + sec(A/2)*cos(B/2)*cos(C/2)', ID="X(175)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X(174)", classes=["center", "incident"])
    X_483 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(A/2))', ID="X(483)", classes=["center", "incident"])
    central_line(model, X_174, X_483, 174, 483, incident=True)
    X_490 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + csc(A)*sin(B)*sin(C)) - cos(B)*cos(C)', ID="X(490)", classes=["center", "incident"])
    X_664 = eval_trilinear_point(model, A, B, C, '1/(a*(b - c)*(b + c - a))', ID="X(664)", classes=["center", "incident"])
    central_line(model, X_490, X_664, 490, 664, incident=True)
    return promote_point_to_top(model, X_175)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(175) on the given reference triangle."""
    model = create_model('X(175) = ISOPERIMETRIC POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00175(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00175.json"))
    write_center_svg(
        model_acute,
        here / "x-00175.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

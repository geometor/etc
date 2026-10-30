"""GEOMETOR construction model for X(26) = CIRCUMCENTER OF THE TANGENTIAL TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00026(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(26) = CIRCUMCENTER OF THE TANGENTIAL TRIANGLE on reference triangle ABC."""
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X(26)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_143 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(2*C - 2*A) + cos(2*A - 2*B))', ID="X(143)", classes=["center", "incident"])
    central_line(model, X_6, X_143, 6, 143, incident=True)
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X(68)", classes=["center", "incident"])
    X_161 = point_from_barycentrics(model, A, B, C, 1.6755479, 1.8002951, -2.475843, ID="X(161)", classes=["center", "incident"])
    central_line(model, X_68, X_161, 68, 161, incident=True)
    return promote_point_to_top(model, X_26)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(26) on the given reference triangle."""
    model = create_model('X(26) = CIRCUMCENTER OF THE TANGENTIAL TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00026(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00026.json"))
    write_center_svg(
        model_acute,
        here / "x-00026.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

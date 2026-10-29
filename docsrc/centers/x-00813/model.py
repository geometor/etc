"""GEOMETOR construction model for X(813) = o-(- 1, 1) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00813(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(813) = o-(- 1, 1) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_812 = eval_trilinear_point(model, A, B, C, 'a **(-2)*(b**(1) - c**(1)) + a**(0)*(b **(-1) - c **(-1))', ID="X(812)", classes=["center"])
    X_813 = isogonal_conjugate(model, A, B, C, X_812, ID="X(813)", classes=["selected", "target"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X(105)", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X(238)", classes=["center", "incident"])
    central_line(model, X_105, X_238, 105, 238, incident=True)
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X(103)", classes=["center", "incident"])
    X_295 = eval_trilinear_point(model, A, B, C, '(cos(A))/(a**(2) - b*c)', ID="X(295)", classes=["center", "incident"])
    central_line(model, X_103, X_295, 103, 295, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X(106)", classes=["center", "incident"])
    X_292 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) - b*c)', ID="X(292)", classes=["center", "incident"])
    central_line(model, X_106, X_292, 106, 292, incident=True)
    return promote_point_to_top(model, X_813)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(813) on the given reference triangle."""
    model = create_model('X(813) = o-(- 1, 1) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00813(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00813.json"))
    write_center_svg(
        model_acute,
        here / "x-00813.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

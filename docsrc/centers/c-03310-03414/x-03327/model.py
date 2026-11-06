"""GEOMETOR construction model for X_3327 = INCIRCLE TRANSFORM T(X_2290)."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03327(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3327 = INCIRCLE TRANSFORM T(X_2290) on reference triangle ABC."""
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_128 = eval_trilinear_point(model, A, B, C, '((sec(A))*(cos(2*B) + cos(2*C))*(1 + 2*cos(2*A))*(cos(2*A) + 2*cos(2*B)*cos(2*C)))', ID="X_128", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    X_930 = eval_barycentric_point(model, A, B, C, '1/((b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) - b**(2)*c**(2)))', ID="X_930", classes=["center"])
    central_line(model, X_12, X_128, 12, 128)
    central_line(model, X_55, X_930, 55, 930)
    X_3327 = intersect_lines(model, X_12, X_128, X_55, X_930, ID="X_3327", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_1141 = eval_trilinear_point(model, A, B, C, 'b*c/(16*D**(2) + (a**(2)+c**(2)-b**(2))*(a**(2)+b**(2)-c**(2)))*(16*D**(2) - 3*(b**(2)+c**(2)-a**(2))**(2))', ID="X_1141", classes=["center", "incident"])
    central_line(model, X_56, X_1141, 56, 1141, incident=True)
    return promote_point_to_top(model, X_3327)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3327 on the given reference triangle."""
    model = create_model('X_3327 = INCIRCLE TRANSFORM T(X_2290)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03327(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03327.json"))
    write_center_svg(
        model_acute,
        here / "x-03327.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

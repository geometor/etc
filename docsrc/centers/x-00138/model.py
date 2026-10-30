"""GEOMETOR construction model for X(138) = X(111)-OF-ORTHIC-TRIANGLE."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00138(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(138) = X(111)-OF-ORTHIC-TRIANGLE on reference triangle ABC."""
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center"])
    X_130 = point_from_barycentrics(model, A, B, C, 0.33794961, 0.64021524, 0.021835148, ID="X(130)", classes=["center"])
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X(53)", classes=["center"])
    X_137 = point_from_barycentrics(model, A, B, C, 0.1354431, 0.64976082, 0.21479608, ID="X(137)", classes=["center"])
    central_line(model, X_51, X_130, 51, 130)
    central_line(model, X_53, X_137, 53, 137)
    X_138 = intersect_lines(model, X_51, X_130, X_53, X_137, ID="X(138)", classes=["selected", "target"])
    X_122 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(a**(2) - b**(2) - c**(2))**(2)*(3*a**(4) - 2*a**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2))', ID="X(122)", classes=["center", "incident"])
    X_233 = eval_trilinear_point(model, A, B, C, '(b*cos(C - A) + c*cos(B - A))*cos(B - C)', ID="X(233)", classes=["center", "incident"])
    central_line(model, X_122, X_233, 122, 233, incident=True)
    return promote_point_to_top(model, X_138)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(138) on the given reference triangle."""
    model = create_model('X(138) = X(111)-OF-ORTHIC-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00138(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00138.json"))
    write_center_svg(
        model_acute,
        here / "x-00138.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

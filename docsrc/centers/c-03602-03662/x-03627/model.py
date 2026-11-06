"""GEOMETOR construction model for X_3627 = H⁻¹(X_3; M,-1/2)."""

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
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03627(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3627 = H⁻¹(X_3; M,-1/2) on reference triangle ABC."""
    X_3627 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(b**(2) + c**(2) - 4*a**(2)) + 3*(b**(2) - c**(2))**(2))', ID="X_3627", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_143 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(2*C - 2*A) + cos(2*A - 2*B))', ID="X_143", classes=["center", "incident"])
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center", "incident"])
    central_line(model, X_143, X_185, 143, 185, incident=True)
    X_156 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(8) - 3*a**(6)*(b**(2) + c**(2)) + a**(4)*(3*b**(4) + 2*b**(2)*c**(2) + 3*c**(4)) - a**(2)*(b**(6) + c**(6)) + b**(2)*c**(2)*(b**(2) - c**(2))**(2))', ID="X_156", classes=["center", "incident"])
    X_1514 = point_from_barycentrics(model, A, B, C, -0.40927419, -0.46693548, 1.8762097, ID="X_1514", classes=["center", "incident"])
    central_line(model, X_156, X_1514, 156, 1514, incident=True)
    return promote_point_to_top(model, X_3627)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3627 on the given reference triangle."""
    model = create_model('X_3627 = H⁻¹(X_3; M,-1/2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03627(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03627.json"))
    write_center_svg(
        model_acute,
        here / "x-03627.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

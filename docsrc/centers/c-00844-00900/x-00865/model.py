"""GEOMETOR construction model for X_865 = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X_512."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00865(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_865 = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X_512 on reference triangle ABC."""
    X_865 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*(csc(C))**(2)*sin(C - A)*csc(A - B) - sin(2*C)*(csc(B))**(2)*sin(B - A)*csc(A - C))', ID="X_865", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_351 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(2) + c**(2) - 2*a**(2)))', ID="X_351", classes=["center", "incident"])
    X_888 = eval_barycentric_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))*(a**(2)*b**(2) + a**(2)*c**(2) - 2*b**(2)*c**(2))', ID="X_888", classes=["center", "incident"])
    central_line(model, X_351, X_888, 351, 888, incident=True)
    return promote_point_to_top(model, X_865)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_865 on the given reference triangle."""
    model = create_model('X_865 = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X_512')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00865(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00865.json"))
    write_center_svg(
        model_acute,
        here / "x-00865.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

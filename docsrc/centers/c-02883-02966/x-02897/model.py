"""GEOMETOR construction model for X_2897 = ANTICOMPLEMENTARY CONJUGATE OF X_92."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02897(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2897 = ANTICOMPLEMENTARY CONJUGATE OF X_92 on reference triangle ABC."""
    X_1172 = point_from_barycentrics(model, A, B, C, 0.14979394, 0.23060383, 0.61960222, ID="X_1172", classes=["center"])
    X_2897 = anticomplement(model, A, B, C, X_1172, ID="X_2897", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    central_line(model, X_20, X_64, 20, 64, incident=True)
    X_153 = eval_barycentric_point(model, A, B, C, 'a**(7) - a**(6)*(b + c) - a**(5)*(b**(2) - 7*b*c + c**(2)) + a**(4)*(b + c)*(b**(2) - 6*b*c + c**(2)) - a**(3)*(b**(4) + 2*b**(3)*c - 10*b**(2)*c**(2) + 2*b*c**(3) + c**(4)) + a**(2)*(b - c)**(2)*(b + c)*(b**(2) + 6*b*c + c**(2)) + a*(b**(2) - c**(2))**(2)*(b**(2) - 5*b*c + c**(2)) - (b - c)**(4)*(b + c)**(3)', ID="X_153", classes=["center", "incident"])
    X_322 = eval_trilinear_point(model, A, B, C, '((-1 - cos(A) + cos(B) + cos(C))*(csc(A))**(2))', ID="X_322", classes=["center", "incident"])
    central_line(model, X_153, X_322, 153, 322, incident=True)
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    X_347 = point_from_barycentrics(model, A, B, C, 0.57303371, 0.49438202, -0.06741573, ID="X_347", classes=["center", "incident"])
    central_line(model, X_145, X_347, 145, 347, incident=True)
    return promote_point_to_top(model, X_2897)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2897 on the given reference triangle."""
    model = create_model('X_2897 = ANTICOMPLEMENTARY CONJUGATE OF X_92')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02897(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02897.json"))
    write_center_svg(
        model_acute,
        here / "x-02897.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

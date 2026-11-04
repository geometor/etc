"""GEOMETOR construction model for X_1619 = TCC-PERSPECTOR OF X_63."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01619(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1619 = TCC-PERSPECTOR OF X_63 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center"])
    central_line(model, X_3, X_64, 3, 64)
    central_line(model, X_22, X_69, 22, 69)
    X_1619 = intersect_lines(model, X_3, X_64, X_22, X_69, ID="X_1619", classes=["selected", "target"])
    X_161 = eval_trilinear_point(model, A, B, C, '(a*((a**(2) + b**(2) + c**(2))*(sin(2*A))**(2) + (c**(2) - b**(2) - a**(2))*(sin(2*B))**(2) + (b**(2) - c**(2) - a**(2))*(sin(2*C))**(2)))', ID="X_161", classes=["center", "incident"])
    X_542 = eval_barycentric_point(model, A, B, C, '2*a**(6) - 2*a**(4)*(b**(2) + c**(2)) + a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2))', ID="X_542", classes=["center", "incident"])
    central_line(model, X_161, X_542, 161, 542, incident=True)
    return promote_point_to_top(model, X_1619)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1619 on the given reference triangle."""
    model = create_model('X_1619 = TCC-PERSPECTOR OF X_63')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01619(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01619.json"))
    write_center_svg(
        model_acute,
        here / "x-01619.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

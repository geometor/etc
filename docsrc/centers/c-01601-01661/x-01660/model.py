"""GEOMETOR construction model for X_1660 = 1st GRINBERG MIDPOINTS PERSPECTOR."""

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
    midpoint,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01660(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1660 = 1st GRINBERG MIDPOINTS PERSPECTOR on reference triangle ABC."""
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center"])
    X_1619 = point_from_barycentrics(model, A, B, C, 1.6442071, 2.1299263, -2.7741334, ID="X_1619", classes=["center"])
    X_1660 = midpoint(model, X_394, X_1619, ID="X_1660", classes=["selected", "target"], guide=False)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_6, X_25, 6, 25, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_156 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(8) - 3*a**(6)*(b**(2) + c**(2)) + a**(4)*(3*b**(4) + 2*b**(2)*c**(2) + 3*c**(4)) - a**(2)*(b**(6) + c**(6)) + b**(2)*c**(2)*(b**(2) - c**(2))**(2))', ID="X_156", classes=["center", "incident"])
    central_line(model, X_30, X_156, 30, 156, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_1370 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2)/(a**(2) - b**(2) + c**(2)) + c**(2)/(a**(2) + b**(2) - c**(2)) - a**(2)/(- a**(2) + b**(2) + c**(2))))', ID="X_1370", classes=["center", "incident"])
    central_line(model, X_110, X_1370, 110, 1370, incident=True)
    return promote_point_to_top(model, X_1660)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1660 on the given reference triangle."""
    model = create_model('X_1660 = 1st GRINBERG MIDPOINTS PERSPECTOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01660(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01660.json"))
    write_center_svg(
        model_acute,
        here / "x-01660.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

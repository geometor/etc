"""GEOMETOR construction model for X_1603 = TCC-PERSPECTOR OF X_8."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01603(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1603 = TCC-PERSPECTOR OF X_8 on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_197 = eval_trilinear_point(model, A, B, C, 'a*(-a**(2)*tan(A/2) + b**(2)*tan(B/2) + c**(2)*tan(C/2))', ID="X_197", classes=["center"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center"])
    X_1324 = eval_trilinear_point(model, A, B, C, '(a*(a**(5) - b**(5) - c**(5) + a**(3)*b*c - b**(3)*c*a - c**(3)*a*b + a**(2)*b**(2)*(b - a) + a**(2)*c**(2)*(c - a) + b**(2)*c**(2)*(b + c)))', ID="X_1324", classes=["center"])
    central_line(model, X_8, X_197, 8, 197)
    central_line(model, X_24, X_1324, 24, 1324)
    X_1603 = intersect_lines(model, X_8, X_197, X_24, X_1324, ID="X_1603", classes=["selected", "target"])
    return promote_point_to_top(model, X_1603)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1603 on the given reference triangle."""
    model = create_model('X_1603 = TCC-PERSPECTOR OF X_8')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01603(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01603.json"))
    write_center_svg(
        model_acute,
        here / "x-01603.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_1715 = MIMOSA TRANSFORM OF X_29."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01715(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1715 = MIMOSA TRANSFORM OF X_29 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center"])
    X_851 = eval_trilinear_point(model, A, B, C, 'sin(2*B)*sin(C - A) + sin(2*C)*sin(B - A)', ID="X_851", classes=["center"])
    central_line(model, X_1, X_3, 1, 3)
    central_line(model, X_185, X_851, 185, 851)
    X_1715 = intersect_lines(model, X_1, X_3, X_185, X_851, ID="X_1715", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_1158 = eval_trilinear_point(model, A, B, C, 'a**(6) - b**(6) - c**(6) + b**(2)*c**(2)*(b**(2) + c**(2)) + 3*a**(2)*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2)) + 2*a*b*c*(a**(3) - b**(3) - c**(3) - a*b*c + (a**(2) + b*c)*(b + c) - a*b**(2) - a*c**(2))', ID="X_1158", classes=["center", "incident"])
    central_line(model, X_19, X_1158, 19, 1158, incident=True)
    return promote_point_to_top(model, X_1715)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1715 on the given reference triangle."""
    model = create_model('X_1715 = MIMOSA TRANSFORM OF X_29')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01715(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01715.json"))
    write_center_svg(
        model_acute,
        here / "x-01715.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_3143 = X_111-CEVA CONJUGATE OF X_523."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03143(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3143 = X_111-CEVA CONJUGATE OF X_523 on reference triangle ABC."""
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center"])
    X_3143 = ceva_conjugate(model, A, B, C, X_111, X_523, ID="X_3143", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_804 = eval_trilinear_point(model, A, B, C, 'a **(-3)*(b**(2) - c**(2)) + a**(1)*(b **(-2) - c **(-2))', ID="X_804", classes=["center", "incident"])
    central_line(model, X_115, X_804, 115, 804, incident=True)
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    X_2780 = point_from_barycentrics(model, A, B, C, -0.65368728, -0.09685402, 0.7505413, ID="X_2780", classes=["center", "incident"])
    central_line(model, X_125, X_2780, 125, 2780, incident=True)
    return promote_point_to_top(model, X_3143)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3143 on the given reference triangle."""
    model = create_model('X_3143 = X_111-CEVA CONJUGATE OF X_523')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03143(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03143.json"))
    write_center_svg(
        model_acute,
        here / "x-03143.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

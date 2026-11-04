"""GEOMETOR construction model for X_1594 = RIGBY-LALESCU ORTHOPOLE."""

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
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01594(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1594 = RIGBY-LALESCU ORTHOPOLE on reference triangle ABC."""
    X_933 = eval_trilinear_point(model, A, B, C, 'sec(A)*csc(2*B - 2*C)', ID="X_933", classes=["center"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center"])
    X_1594 = ceva_conjugate(model, A, B, C, X_933, X_523, ID="X_1594", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_70 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_70", classes=["center", "incident"])
    central_line(model, X_6, X_70, 6, 70, incident=True)
    X_128 = eval_trilinear_point(model, A, B, C, '((sec(A))*(cos(2*B) + cos(2*C))*(1 + 2*cos(2*A))*(cos(2*A) + 2*cos(2*B)*cos(2*C)))', ID="X_128", classes=["center", "incident"])
    X_136 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2))/(a**(2) - b**(2) - c**(2))', ID="X_136", classes=["center", "incident"])
    central_line(model, X_128, X_136, 128, 136, incident=True)
    return promote_point_to_top(model, X_1594)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1594 on the given reference triangle."""
    model = create_model('X_1594 = RIGBY-LALESCU ORTHOPOLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01594(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01594.json"))
    write_center_svg(
        model_acute,
        here / "x-01594.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

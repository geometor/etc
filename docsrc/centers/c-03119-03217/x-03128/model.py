"""GEOMETOR construction model for X_3128 = X_4-CEVA CONJUGATE OF X_1163."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03128(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3128 = X_4-CEVA CONJUGATE OF X_1163 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1163 = eval_trilinear_point(model, A, B, C, '(( area - a**(2))*(2*area - b**(2) - c**(2))/(a*(b**(2) + c**(2) - a**(2))))', ID="X_1163", classes=["center"])
    X_3128 = ceva_conjugate(model, A, B, C, X_4, X_1163, ID="X_3128", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_1164 = eval_trilinear_point(model, A, B, C, '(( area + a**(2))*(2*area - b**(2) - c**(2))/(a*(b**(2) + c**(2) - a**(2))))', ID="X_1164", classes=["center", "incident"])
    central_line(model, X_1163, X_1164, 1163, 1164, incident=True)
    X_1588 = eval_trilinear_point(model, A, B, C, '(sin(A) - cos(B)*cos(C))', ID="X_1588", classes=["center", "incident"])
    X_1899 = eval_trilinear_point(model, A, B, C, '2*b*c - a*b*sec(B) - a*c*sec(C)', ID="X_1899", classes=["center", "incident"])
    central_line(model, X_1588, X_1899, 1588, 1899, incident=True)
    return promote_point_to_top(model, X_3128)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3128 on the given reference triangle."""
    model = create_model('X_3128 = X_4-CEVA CONJUGATE OF X_1163')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03128(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03128.json"))
    write_center_svg(
        model_acute,
        here / "x-03128.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_1992 = ORTHOCORRESPONDENT OF X_2."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    midpoint,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01992(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1992 = ORTHOCORRESPONDENT OF X_2 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_193 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cot(B) + cot(C) - cot(A))', ID="X_193", classes=["center"])
    X_1992 = midpoint(model, X_2, X_193, ID="X_1992", classes=["selected", "target"], guide=False)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_145, X_190, 145, 190, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_542 = eval_barycentric_point(model, A, B, C, '2*a**(6) - 2*a**(4)*(b**(2) + c**(2)) + a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2))', ID="X_542", classes=["center", "incident"])
    central_line(model, X_4, X_542, 4, 542, incident=True)
    return promote_point_to_top(model, X_1992)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1992 on the given reference triangle."""
    model = create_model('X_1992 = ORTHOCORRESPONDENT OF X_2')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01992(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01992.json"))
    write_center_svg(
        model_acute,
        here / "x-01992.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

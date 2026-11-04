"""GEOMETOR construction model for X_1999 = ORTHOCORRESPONDENT OF X_10."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01999(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1999 = ORTHOCORRESPONDENT OF X_10 on reference triangle ABC."""
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center"])
    X_894 = eval_trilinear_point(model, A, B, C, '(a**(2) + b*c)/a', ID="X_894", classes=["center"])
    X_1999 = ceva_conjugate(model, A, B, C, X_65, X_894, ID="X_1999", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X_192", classes=["center", "incident"])
    central_line(model, X_63, X_192, 63, 192, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_312 = eval_trilinear_point(model, A, B, C, '(b + c - a)*b**(2)*c**(2)', ID="X_312", classes=["center", "incident"])
    central_line(model, X_6, X_312, 6, 312, incident=True)
    return promote_point_to_top(model, X_1999)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1999 on the given reference triangle."""
    model = create_model('X_1999 = ORTHOCORRESPONDENT OF X_10')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01999(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01999.json"))
    write_center_svg(
        model_acute,
        here / "x-01999.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

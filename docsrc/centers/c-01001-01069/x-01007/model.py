"""GEOMETOR construction model for X_1007 = INTERCEPT OF LINES X_2X_6 AND X_4X_99."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01007(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1007 = INTERCEPT OF LINES X_2X_6 AND X_4X_99 on reference triangle ABC."""
    X_1007 = eval_trilinear_point(model, A, B, C, '(b*c*(a**(4) - 4*a**(2)*(b**(2) + c**(2)) + 3*b**(4) - 2*b**(2)*c**(2) + 3*c**(4)))', ID="X_1007", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    central_line(model, X_4, X_99, 4, 99, incident=True)
    X_305 = eval_trilinear_point(model, A, B, C, 'b**(4)*c**(4)*cos(A)', ID="X_305", classes=["center", "incident"])
    X_311 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*cos(B - C)', ID="X_311", classes=["center", "incident"])
    central_line(model, X_305, X_311, 305, 311, incident=True)
    return promote_point_to_top(model, X_1007)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1007 on the given reference triangle."""
    model = create_model('X_1007 = INTERCEPT OF LINES X_2X_6 AND X_4X_99')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01007(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01007.json"))
    write_center_svg(
        model_acute,
        here / "x-01007.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

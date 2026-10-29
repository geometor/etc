"""GEOMETOR construction model for X(340) = ISOTOMIC CONJUGATE OF X(265)."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00340(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(340) = ISOTOMIC CONJUGATE OF X(265) on reference triangle ABC."""
    X_340 = eval_barycentric_point(model, A, B, C, '((a**(2) - b**(2) - c**(2))**(2) - b**(2)*c**(2))/(b**(2) + c**(2) - a**(2))', ID="X(340)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    central_line(model, X_4, X_69, 4, 69, incident=True)
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X(95)", classes=["center", "incident"])
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X(140)", classes=["center", "incident"])
    central_line(model, X_95, X_140, 95, 140, incident=True)
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(67)", classes=["center", "incident"])
    X_290 = eval_barycentric_point(model, A, B, C, 'csc(A)*sec(A + omega )', ID="X(290)", classes=["center", "incident"])
    central_line(model, X_67, X_290, 67, 290, incident=True)
    return promote_point_to_top(model, X_340)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(340) on the given reference triangle."""
    model = create_model('X(340) = ISOTOMIC CONJUGATE OF X(265)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00340(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00340.json"))
    write_center_svg(
        model_acute,
        here / "x-00340.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

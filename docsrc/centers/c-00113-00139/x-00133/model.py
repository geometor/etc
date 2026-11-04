"""GEOMETOR construction model for X_133 = INTERSECTION OF LINES X_4X_74 AND X_5X_122."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00133(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_133 = INTERSECTION OF LINES X_4X_74 AND X_5X_122 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center"])
    X_133 = midpoint(model, X_4, X_107, ID="X_133", classes=["selected", "target"], guide=False)
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_4, X_74, 4, 74, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_122 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A) - cos(B)*cos(C))*(cot(A))**(2)', ID="X_122", classes=["center", "incident"])
    central_line(model, X_5, X_122, 5, 122, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    central_line(model, X_53, X_115, 53, 115, incident=True)
    return promote_point_to_top(model, X_133)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_133 on the given reference triangle."""
    model = create_model('X_133 = INTERSECTION OF LINES X_4X_74 AND X_5X_122')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00133(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00133.json"))
    write_center_svg(
        model_acute,
        here / "x-00133.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

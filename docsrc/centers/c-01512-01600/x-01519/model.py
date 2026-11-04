"""GEOMETOR construction model for X_1519 = ORTHOJOIN OF X_9."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01519(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1519 = ORTHOJOIN OF X_9 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_119 = eval_trilinear_point(model, A, B, C, '(csc(A))*(-1 + cos(B) + cos(C))*(sin(2*B) + sin(2*C) + 2*(-1 + cos(A))*(sin(B) + sin(C)))', ID="X_119", classes=["center"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center"])
    central_line(model, X_1, X_4, 1, 4)
    central_line(model, X_119, X_517, 119, 517)
    X_1519 = intersect_lines(model, X_1, X_4, X_119, X_517, ID="X_1519", classes=["selected", "target"])
    X_499 = eval_trilinear_point(model, A, B, C, '1 - 2*sin(B)*sin(C)', ID="X_499", classes=["center", "incident"])
    X_1158 = eval_trilinear_point(model, A, B, C, 'a**(6) - b**(6) - c**(6) + b**(2)*c**(2)*(b**(2) + c**(2)) + 3*a**(2)*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2)) + 2*a*b*c*(a**(3) - b**(3) - c**(3) - a*b*c + (a**(2) + b*c)*(b + c) - a*b**(2) - a*c**(2))', ID="X_1158", classes=["center", "incident"])
    central_line(model, X_499, X_1158, 499, 1158, incident=True)
    return promote_point_to_top(model, X_1519)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1519 on the given reference triangle."""
    model = create_model('X_1519 = ORTHOJOIN OF X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01519(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01519.json"))
    write_center_svg(
        model_acute,
        here / "x-01519.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

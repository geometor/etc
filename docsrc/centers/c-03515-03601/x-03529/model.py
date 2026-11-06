"""GEOMETOR construction model for X_3529 = EULER LINE INTERCEPT OF LINE X_516X_944."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03529(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3529 = EULER LINE INTERCEPT OF LINE X_516X_944 on reference triangle ABC."""
    X_382 = eval_trilinear_point(model, A, B, C, 'cos(A) - 4*cos(B)*cos(C)', ID="X_382", classes=["center"])
    X_3529 = anticomplement(model, A, B, C, X_382, ID="X_3529", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    X_944 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a**(4) - 2*a**(3)*(b + c) + (b - c)**(2)*(2*a*b + 2*a*c - 2*b*c - b**(2) - c**(2) - 2*a**(2)))', ID="X_944", classes=["center", "incident"])
    central_line(model, X_516, X_944, 516, 944, incident=True)
    X_1056 = eval_trilinear_point(model, A, B, C, '(2 + cos(B)*cos(C))', ID="X_1056", classes=["center", "incident"])
    X_3303 = eval_trilinear_point(model, A, B, C, '3 + cos(A)', ID="X_3303", classes=["center", "incident"])
    central_line(model, X_1056, X_3303, 1056, 3303, incident=True)
    return promote_point_to_top(model, X_3529)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3529 on the given reference triangle."""
    model = create_model('X_3529 = EULER LINE INTERCEPT OF LINE X_516X_944')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03529(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03529.json"))
    write_center_svg(
        model_acute,
        here / "x-03529.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

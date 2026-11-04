"""GEOMETOR construction model for X_1487 = NAPOLEON CEVAPOINT."""

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
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01487(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1487 = NAPOLEON CEVAPOINT on reference triangle ABC."""
    X_1487 = eval_trilinear_point(model, A, B, C, '((csc(A))/((3 - cot(B)*cot(C))*(3 - (cot(A))**(2))))', ID="X_1487", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_252 = eval_trilinear_point(model, A, B, C, '(sec(B - C)/(1 - 2*cos(2*A)))', ID="X_252", classes=["center", "incident"])
    central_line(model, X_4, X_252, 4, 252, incident=True)
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    X_930 = eval_barycentric_point(model, A, B, C, '1/((b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) - b**(2)*c**(2)))', ID="X_930", classes=["center", "incident"])
    central_line(model, X_140, X_930, 140, 930, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_1173 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(4) - 3*a**(2)*(b**(2) + c**(2)) + (b**(2) - c**(2))**(2))', ID="X_1173", classes=["center", "incident"])
    central_line(model, X_5, X_1173, 5, 1173, incident=True)
    return promote_point_to_top(model, X_1487)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1487 on the given reference triangle."""
    model = create_model('X_1487 = NAPOLEON CEVAPOINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01487(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01487.json"))
    write_center_svg(
        model_acute,
        here / "x-01487.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

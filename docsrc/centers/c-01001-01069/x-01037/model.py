"""GEOMETOR construction model for X_1037 = CEVAPOINT OF X_55 AND X_56."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01037(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1037 = CEVAPOINT OF X_55 AND X_56 on reference triangle ABC."""
    X_497 = eval_trilinear_point(model, A, B, C, '1 - cos(B)*cos(C)', ID="X_497", classes=["center"])
    X_1037 = isogonal_conjugate(model, A, B, C, X_497, ID="X_1037", classes=["selected", "target"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_55, X_77, 55, 77, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    central_line(model, X_56, X_78, 56, 78, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    X_388 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) + (b + c)**(2))/(b + c - a)', ID="X_388", classes=["center", "incident"])
    central_line(model, X_29, X_388, 29, 388, incident=True)
    return promote_point_to_top(model, X_1037)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1037 on the given reference triangle."""
    model = create_model('X_1037 = CEVAPOINT OF X_55 AND X_56')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01037(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01037.json"))
    write_center_svg(
        model_acute,
        here / "x-01037.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

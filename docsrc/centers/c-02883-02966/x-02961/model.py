"""GEOMETOR construction model for X_2961 = EXCENTRAL-ISOGONAL CONJUGATE OF X_200."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02961(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2961 = EXCENTRAL-ISOGONAL CONJUGATE OF X_200 on reference triangle ABC."""
    X_497 = eval_trilinear_point(model, A, B, C, '1 - cos(B)*cos(C)', ID="X_497", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2961 = ceva_conjugate(model, A, B, C, X_497, X_1, ID="X_2961", classes=["selected", "target"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_40, X_238, 40, 238, incident=True)
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    central_line(model, X_46, X_516, 46, 516, incident=True)
    X_1037 = eval_trilinear_point(model, A, B, C, '(1/(1 - cos(B)*cos(C)))', ID="X_1037", classes=["center", "incident"])
    central_line(model, X_1, X_1037, 1, 1037, incident=True)
    return promote_point_to_top(model, X_2961)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2961 on the given reference triangle."""
    model = create_model('X_2961 = EXCENTRAL-ISOGONAL CONJUGATE OF X_200')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02961(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02961.json"))
    write_center_svg(
        model_acute,
        here / "x-02961.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

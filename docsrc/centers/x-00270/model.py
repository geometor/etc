"""GEOMETOR construction model for X(270) = ISOGONAL CONJUGATE OF X(201)."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00270(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(270) = ISOGONAL CONJUGATE OF X(201) on reference triangle ABC."""
    X_201 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(B - C))', ID="X(201)", classes=["center"])
    X_270 = isogonal_conjugate(model, A, B, C, X_201, ID="X(270)", classes=["selected", "target"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X(27)", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    central_line(model, X_27, X_58, 27, 58, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X(28)", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X(60)", classes=["center", "incident"])
    central_line(model, X_28, X_60, 28, 60, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X(162)", classes=["center", "incident"])
    central_line(model, X_4, X_162, 4, 162, incident=True)
    return promote_point_to_top(model, X_270)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(270) on the given reference triangle."""
    model = create_model('X(270) = ISOGONAL CONJUGATE OF X(201)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00270(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00270.json"))
    write_center_svg(
        model_acute,
        here / "x-00270.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

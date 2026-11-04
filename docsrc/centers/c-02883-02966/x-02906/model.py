"""GEOMETOR construction model for X_2906 = ORTHIC-ISOGONAL CONJUGATE OF X_28."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02906(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2906 = ORTHIC-ISOGONAL CONJUGATE OF X_28 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center"])
    X_2906 = ceva_conjugate(model, A, B, C, X_4, X_28, ID="X_2906", classes=["selected", "target"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_28, X_60, 28, 60, incident=True)
    X_193 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cot(B) + cot(C) - cot(A))', ID="X_193", classes=["center", "incident"])
    X_406 = eval_trilinear_point(model, A, B, C, '(b*c*(a + b + c) + a*b*c*sec(A))', ID="X_406", classes=["center", "incident"])
    central_line(model, X_193, X_406, 193, 406, incident=True)
    X_1029 = eval_trilinear_point(model, A, B, C, '(1/(a + 2*(a + b + c)*cos(A)))', ID="X_1029", classes=["center", "incident"])
    central_line(model, X_4, X_1029, 4, 1029, incident=True)
    return promote_point_to_top(model, X_2906)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2906 on the given reference triangle."""
    model = create_model('X_2906 = ORTHIC-ISOGONAL CONJUGATE OF X_28')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02906(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02906.json"))
    write_center_svg(
        model_acute,
        here / "x-02906.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_2907 = ORTHIC-ISOGONAL CONJUGATE OF X_29."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02907(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2907 = ORTHIC-ISOGONAL CONJUGATE OF X_29 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center"])
    X_2907 = ceva_conjugate(model, A, B, C, X_4, X_29, ID="X_2907", classes=["selected", "target"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    central_line(model, X_27, X_239, 27, 239, incident=True)
    X_270 = eval_trilinear_point(model, A, B, C, '(sec(A))/(1 + cos(B - C))', ID="X_270", classes=["center", "incident"])
    central_line(model, X_29, X_270, 29, 270, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_415 = eval_barycentric_point(model, A, B, C, '(a + b) * (a + c) * (a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2)) * (a**(3) - 2*a**(2)*b + b**(3) - 2*a**(2)*c + a*b*c + c**(3))', ID="X_415", classes=["center", "incident"])
    central_line(model, X_1, X_415, 1, 415, incident=True)
    return promote_point_to_top(model, X_2907)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2907 on the given reference triangle."""
    model = create_model('X_2907 = ORTHIC-ISOGONAL CONJUGATE OF X_29')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02907(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02907.json"))
    write_center_svg(
        model_acute,
        here / "x-02907.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

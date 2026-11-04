"""GEOMETOR construction model for X_2905 = ORTHIC-ISOGONAL CONJUGATE OF X_27."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02905(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2905 = ORTHIC-ISOGONAL CONJUGATE OF X_27 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center"])
    X_2905 = ceva_conjugate(model, A, B, C, X_4, X_27, ID="X_2905", classes=["selected", "target"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    central_line(model, X_27, X_86, 27, 86, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    X_242 = eval_trilinear_point(model, A, B, C, '((sec(A))*((sin(A))**(2) - sin(B)*sin(C)))', ID="X_242", classes=["center", "incident"])
    central_line(model, X_29, X_242, 29, 242, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_423 = eval_barycentric_point(model, A, B, C, '(a + b) * (a + c) * (a**(2) + b**(2) - c**(2)) * (a**(2) + a*b - b**(2) + a*c - b*c - c**(2)) * (a**(2) - b**(2) + c**(2))', ID="X_423", classes=["center", "incident"])
    central_line(model, X_19, X_423, 19, 423, incident=True)
    return promote_point_to_top(model, X_2905)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2905 on the given reference triangle."""
    model = create_model('X_2905 = ORTHIC-ISOGONAL CONJUGATE OF X_27')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02905(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02905.json"))
    write_center_svg(
        model_acute,
        here / "x-02905.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

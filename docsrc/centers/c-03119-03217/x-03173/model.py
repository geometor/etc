"""GEOMETOR construction model for X_3173 = X_7-CEVA CONJUGATE OF X_3."""

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
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03173(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3173 = X_7-CEVA CONJUGATE OF X_3 on reference triangle ABC."""
    X_3173 = eval_barycentric_point(model, A, B, C, '(a**(2)*(b**(2) + c**(2) - a**(2))*(a**(3) - a**(2)*b - a**(2)*c - a*(b + c)**(2) + (b + c)*(b**(2) + c**(2)))/(b + c - a))', ID="X_3173", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_90 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A))', ID="X_90", classes=["center", "incident"])
    central_line(model, X_1, X_90, 1, 90, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_63, X_77, 63, 77, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_6, X_226, 6, 226, incident=True)
    return promote_point_to_top(model, X_3173)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3173 on the given reference triangle."""
    model = create_model('X_3173 = X_7-CEVA CONJUGATE OF X_3')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03173(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03173.json"))
    write_center_svg(
        model_acute,
        here / "x-03173.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

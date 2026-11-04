"""GEOMETOR construction model for X_1265 = ISOTOMIC CONJUGATE OF X_1119."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01265(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1265 = ISOTOMIC CONJUGATE OF X_1119 on reference triangle ABC."""
    X_1265 = eval_trilinear_point(model, A, B, C, '((cos(A))*((csc(A/2))**(4)))', ID="X_1265", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    central_line(model, X_69, X_72, 69, 72, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_20, X_190, 20, 190, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    central_line(model, X_8, X_210, 8, 210, incident=True)
    return promote_point_to_top(model, X_1265)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1265 on the given reference triangle."""
    model = create_model('X_1265 = ISOTOMIC CONJUGATE OF X_1119')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01265(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01265.json"))
    write_center_svg(
        model_acute,
        here / "x-01265.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_2188 = X_2-ISOCONJUGATE OF X_196."""

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


def construct_x_02188(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2188 = X_2-ISOCONJUGATE OF X_196 on reference triangle ABC."""
    X_342 = eval_trilinear_point(model, A, B, C, '((csc(2*A)*tan(A/2))*(1 + cos(A) - cos(B) - cos(C)))', ID="X_342", classes=["center"])
    X_2188 = isogonal_conjugate(model, A, B, C, X_342, ID="X_2188", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_48, X_55, 48, 55, incident=True)
    X_282 = eval_trilinear_point(model, A, B, C, '(cot(A/2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X_282", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    central_line(model, X_282, X_284, 282, 284, incident=True)
    X_212 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(A))', ID="X_212", classes=["center", "incident"])
    X_577 = eval_trilinear_point(model, A, B, C, 'sin(A)*(cos(A))**(2)', ID="X_577", classes=["center", "incident"])
    central_line(model, X_212, X_577, 212, 577, incident=True)
    return promote_point_to_top(model, X_2188)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2188 on the given reference triangle."""
    model = create_model('X_2188 = X_2-ISOCONJUGATE OF X_196')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02188(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02188.json"))
    write_center_svg(
        model_acute,
        here / "x-02188.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

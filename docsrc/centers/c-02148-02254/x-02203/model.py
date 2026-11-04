"""GEOMETOR construction model for X_2203 = X_2-ISOCONJUGATE OF X_306."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02203(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2203 = X_2-ISOCONJUGATE OF X_306 on reference triangle ABC."""
    X_2203 = eval_trilinear_point(model, A, B, C, 'a**(2)/((a**(2) - b**(2) - c**(2))*(b + c))', ID="X_2203", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_6, X_25, 6, 25, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_28, X_60, 28, 60, incident=True)
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    X_739 = eval_trilinear_point(model, A, B, C, '1/(a**(-2)*(b**(0) + c**(0)) - a **(-1)*(b **(-1) + c **(-1)))', ID="X_739", classes=["center", "incident"])
    central_line(model, X_112, X_739, 112, 739, incident=True)
    return promote_point_to_top(model, X_2203)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2203 on the given reference triangle."""
    model = create_model('X_2203 = X_2-ISOCONJUGATE OF X_306')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02203(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02203.json"))
    write_center_svg(
        model_acute,
        here / "x-02203.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

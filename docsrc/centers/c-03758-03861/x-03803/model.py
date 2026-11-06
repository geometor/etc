"""GEOMETOR construction model for X_3803 = X_905com[INVERSE(nT(a², a² + c²))]."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03803(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3803 = X_905com[INVERSE(nT(a², a² + c²))] on reference triangle ABC."""
    X_3803 = eval_barycentric_point(model, A, B, C, '(a*(b - c)*(3*a**(2) + b**(2) + c**(2)))', ID="X_3803", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_36, X_238, 36, 238, incident=True)
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center", "incident"])
    X_830 = eval_trilinear_point(model, A, B, C, '(a**(0)*(b**(3) - c**(3)) + a**(2)*(b**(1) - c**(1)))', ID="X_830", classes=["center", "incident"])
    central_line(model, X_650, X_830, 650, 830, incident=True)
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center", "incident"])
    X_3309 = eval_trilinear_point(model, A, B, C, '(b - c)*(a**(2) + b**(2) + c**(2) - 2*a*b - 2*a*c)', ID="X_3309", classes=["center", "incident"])
    central_line(model, X_649, X_3309, 649, 3309, incident=True)
    return promote_point_to_top(model, X_3803)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3803 on the given reference triangle."""
    model = create_model('X_3803 = X_905com[INVERSE(nT(a², a² + c²))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03803(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03803.json"))
    write_center_svg(
        model_acute,
        here / "x-03803.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

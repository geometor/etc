"""GEOMETOR construction model for X_3328 = INCIRCLE TRANSFORM T(X_2291)."""

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
    gergonne_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03328(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3328 = INCIRCLE TRANSFORM T(X_2291) on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_1638 = eval_barycentric_point(model, A, B, C, '(b - c)*(2*a**(2) - b**(2) - c**(2) - a*b - a*c + 2*b*c)', ID="X_1638", classes=["center"])
    X_3328 = ceva_conjugate(model, A, B, C, X_7, X_1638, ID="X_3328", classes=["selected", "target"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1308 = point_from_barycentrics(model, A, B, C, -0.069444444, 0.91666667, 0.15277778, ID="X_1308", classes=["center", "incident"])
    central_line(model, X_55, X_1308, 55, 1308, incident=True)
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    X_1317 = eval_trilinear_point(model, A, B, C, '(b*c*(c + a - b)*(a + b - c)*(b + c - 2*a)**(2))', ID="X_1317", classes=["center", "incident"])
    central_line(model, X_516, X_1317, 516, 1317, incident=True)
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    X_1362 = point_from_barycentrics(model, A, B, C, 0.28344671, 0.0054421769, 0.71111111, ID="X_1362", classes=["center", "incident"])
    central_line(model, X_517, X_1362, 517, 1362, incident=True)
    return promote_point_to_top(model, X_3328)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3328 on the given reference triangle."""
    model = create_model('X_3328 = INCIRCLE TRANSFORM T(X_2291)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03328(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03328.json"))
    write_center_svg(
        model_acute,
        here / "x-03328.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

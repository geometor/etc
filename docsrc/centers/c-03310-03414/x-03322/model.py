"""GEOMETOR construction model for X_3322 = INCIRCLE TRANSFORM T(X_665)."""

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
    gergonne_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03322(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3322 = INCIRCLE TRANSFORM T(X_665) on reference triangle ABC."""
    X_3322 = eval_barycentric_point(model, A, B, C, '((2*a**(3) - 2*a**(2)*(b + c) + a*(b**(2) + c**(2)) - (b + c)*(b - c)**(2))**(2)/(b + c - a))', ID="X_3322", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_840 = point_from_barycentrics(model, A, B, C, 0.66666667, -0.32, 0.65333333, ID="X_840", classes=["center", "incident"])
    central_line(model, X_7, X_840, 7, 840, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_1308 = point_from_barycentrics(model, A, B, C, -0.069444444, 0.91666667, 0.15277778, ID="X_1308", classes=["center", "incident"])
    central_line(model, X_56, X_1308, 56, 1308, incident=True)
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    X_1155 = eval_trilinear_point(model, A, B, C, '(cos(B) + cos(C) - 2*cos(A))', ID="X_1155", classes=["center", "incident"])
    central_line(model, X_516, X_1155, 516, 1155, incident=True)
    return promote_point_to_top(model, X_3322)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3322 on the given reference triangle."""
    model = create_model('X_3322 = INCIRCLE TRANSFORM T(X_665)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03322(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03322.json"))
    write_center_svg(
        model_acute,
        here / "x-03322.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_3271 = CROSSSUM OF X_2 AND X_100."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03271(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3271 = CROSSSUM OF X_2 AND X_100 on reference triangle ABC."""
    X_3271 = eval_trilinear_point(model, A, B, C, 'a*(b - c)**(2)*(b + c - a)', ID="X_3271", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_31, X_51, 31, 51, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_124 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(b - c)**(2)*((b + c)*(b**(2) + c**(2) - a**(2) - b*c) + a*b*c))', ID="X_124", classes=["center", "incident"])
    central_line(model, X_11, X_124, 11, 124, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_646 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(a**(2)*(b - c)))', ID="X_646", classes=["center", "incident"])
    central_line(model, X_8, X_646, 8, 646, incident=True)
    return promote_point_to_top(model, X_3271)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3271 on the given reference triangle."""
    model = create_model('X_3271 = CROSSSUM OF X_2 AND X_100')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03271(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03271.json"))
    write_center_svg(
        model_acute,
        here / "x-03271.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

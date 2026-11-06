"""GEOMETOR construction model for X_3319 = INCIRCLE TRANSFORM T(X_654)."""

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
    feuerbach_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03319(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3319 = INCIRCLE TRANSFORM T(X_654) on reference triangle ABC."""
    X_3319 = eval_barycentric_point(model, A, B, C, '((2*a**(4) - 2*a**(3)*(b + c) - a**(2)*(b**(2) - 4*b*c + c**(2)) + 2*a*(b + c)*(b - c)**(2) - (b**(2) - c**(2))**(2))**(2)/(b + c - a))', ID="X_3319", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center", "incident"])
    central_line(model, X_11, X_515, 11, 515, incident=True)
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    X_1317 = eval_trilinear_point(model, A, B, C, '(b*c*(c + a - b)*(a + b - c)*(b + c - 2*a)**(2))', ID="X_1317", classes=["center", "incident"])
    central_line(model, X_522, X_1317, 522, 1317, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_1361 = point_from_barycentrics(model, A, B, C, 0.19480519, 0.041558442, 0.76363636, ID="X_1361", classes=["center", "incident"])
    central_line(model, X_513, X_1361, 513, 1361, incident=True)
    return promote_point_to_top(model, X_3319)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3319 on the given reference triangle."""
    model = create_model('X_3319 = INCIRCLE TRANSFORM T(X_654)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03319(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03319.json"))
    write_center_svg(
        model_acute,
        here / "x-03319.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

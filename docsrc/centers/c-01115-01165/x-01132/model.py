"""GEOMETOR construction model for X_1132 = ARCTAN(-2) KIEPERT POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01132(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1132 = ARCTAN(-2) KIEPERT POINT on reference triangle ABC."""
    X_1132 = eval_trilinear_point(model, A, B, C, '1/(sin(A) - 2*cos(A))', ID="X_1132", classes=["selected", "target"])
    X_176 = eval_trilinear_point(model, A, B, C, '1 + sec(A/2)*cos(B/2)*cos(C/2)', ID="X_176", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_176, X_226, 176, 226, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_489 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 - csc(A)*sin(B)*sin(C)) - cos(B)*cos(C))', ID="X_489", classes=["center", "incident"])
    central_line(model, X_2, X_489, 2, 489, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A + pi /4)', ID="X_486", classes=["center", "incident"])
    central_line(model, X_20, X_486, 20, 486, incident=True)
    return promote_point_to_top(model, X_1132)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1132 on the given reference triangle."""
    model = create_model('X_1132 = ARCTAN(-2) KIEPERT POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01132(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01132.json"))
    write_center_svg(
        model_acute,
        here / "x-01132.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

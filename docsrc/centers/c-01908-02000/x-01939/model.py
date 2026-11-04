"""GEOMETOR construction model for X_1939 = MIDPOINT OF PU(15)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_01939(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1939 = MIDPOINT OF PU(15) on reference triangle ABC."""
    X_1939 = eval_trilinear_point(model, A, B, C, '((a*cos(B) + b*cos(C) + c*cos(A))*cos(C) + (a*cos(C) + b*cos(A) + c*cos(B))*cos(B))', ID="X_1939", classes=["selected", "target"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center", "incident"])
    central_line(model, X_65, X_650, 65, 650, incident=True)
    X_169 = eval_trilinear_point(model, A, B, C, '- (sin(A))*(cos(A/2))**(2) + (sin(B))*(cos(B/2))**(2) + (sin(C))*(cos(C/2))**(2)', ID="X_169", classes=["center", "incident"])
    X_1575 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2)) - b*c*(b + c)', ID="X_1575", classes=["center", "incident"])
    central_line(model, X_169, X_1575, 169, 1575, incident=True)
    X_1385 = eval_trilinear_point(model, A, B, C, '16*( area )**(2) + a*(a + b + c)*(b**(2) + c**(2) - a**(2))', ID="X_1385", classes=["center", "incident"])
    X_2649 = eval_trilinear_point(model, A, B, C, '((a*(cos(B) + cos(A)) + b*(cos(C) + cos(B)) + c*(cos(A) + cos(C)))*(cos(C) + cos(A)) + (a*(cos(C) + cos(A)) + b*(cos(A) + cos(B)) + c*(cos(B) + cos(C)))*(cos(B) + cos(A)))', ID="X_2649", classes=["center", "incident"])
    central_line(model, X_1385, X_2649, 1385, 2649, incident=True)
    return promote_point_to_top(model, X_1939)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1939 on the given reference triangle."""
    model = create_model('X_1939 = MIDPOINT OF PU(15)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01939(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01939.json"))
    write_center_svg(
        model_acute,
        here / "x-01939.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

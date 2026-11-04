"""GEOMETOR construction model for X_2677 = RS(X_74, X_100)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02677(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2677 = RS(X_74, X_100) on reference triangle ABC."""
    X_119 = eval_trilinear_point(model, A, B, C, '(csc(A))*(-1 + cos(B) + cos(C))*(sin(2*B) + sin(2*C) + 2*(-1 + cos(A))*(sin(B) + sin(C)))', ID="X_119", classes=["center"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center"])
    central_line(model, X_119, X_517, 119, 517)
    central_line(model, X_125, X_523, 125, 523)
    X_2677 = intersect_lines(model, X_119, X_517, X_125, X_523, ID="X_2677", classes=["selected", "target"])
    X_673 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2) - a*(b + c))', ID="X_673", classes=["center", "incident"])
    X_2481 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2)/(b**(2) + c**(2) - a*b - a*c))', ID="X_2481", classes=["center", "incident"])
    central_line(model, X_673, X_2481, 673, 2481, incident=True)
    return promote_point_to_top(model, X_2677)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2677 on the given reference triangle."""
    model = create_model('X_2677 = RS(X_74, X_100)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02677(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02677.json"))
    write_center_svg(
        model_acute,
        here / "x-02677.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

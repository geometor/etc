"""GEOMETOR construction model for X_2682 = RS(X_98, X_110)."""

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


def construct_x_02682(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2682 = RS(X_98, X_110) on reference triangle ABC."""
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center"])
    central_line(model, X_30, X_113, 30, 113)
    central_line(model, X_115, X_512, 115, 512)
    X_2682 = intersect_lines(model, X_30, X_113, X_115, X_512, ID="X_2682", classes=["selected", "target"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    X_1499 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))*(b**(2) + c**(2) - 5*a**(2))', ID="X_1499", classes=["center", "incident"])
    central_line(model, X_125, X_1499, 125, 1499, incident=True)
    return promote_point_to_top(model, X_2682)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2682 on the given reference triangle."""
    model = create_model('X_2682 = RS(X_98, X_110)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02682(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02682.json"))
    write_center_svg(
        model_acute,
        here / "x-02682.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

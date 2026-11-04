"""GEOMETOR construction model for X_2861 = SM(X_100, X_104)."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02861(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2861 = SM(X_100, X_104) on reference triangle ABC."""
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center"])
    X_693 = eval_trilinear_point(model, A, B, C, '(b - c)/a**(2)', ID="X_693", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_908 = eval_barycentric_point(model, A, B, C, 'cos(B) + cos(C) - 1', ID="X_908", classes=["center"])
    central_line(model, X_104, X_693, 104, 693)
    central_line(model, X_101, X_908, 101, 908)
    X_2861 = intersect_lines(model, X_104, X_693, X_101, X_908, ID="X_2861", classes=["selected", "target"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center", "incident"])
    X_1309 = eval_trilinear_point(model, A, B, C, '(csc(2*A))/(4*((sin(B))**(2) - (sin(C))**(2))*cos(B)*cos(C) + (sin(B))**(2)*cos(B) - (sin(C))**(2)*cos(C))', ID="X_1309", classes=["center", "incident"])
    central_line(model, X_264, X_1309, 264, 1309, incident=True)
    return promote_point_to_top(model, X_2861)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2861 on the given reference triangle."""
    model = create_model('X_2861 = SM(X_100, X_104)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02861(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02861.json"))
    write_center_svg(
        model_acute,
        here / "x-02861.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

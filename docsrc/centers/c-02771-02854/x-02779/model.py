"""GEOMETOR construction model for X_2779 = ISOGONAL CONJUGATE OF X_2695."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02779(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2779 = ISOGONAL CONJUGATE OF X_2695 on reference triangle ABC."""
    X_2695 = point_from_barycentrics(model, A, B, C, 1.0416626, 0.24738514, -0.28904774, ID="X_2695", classes=["center"])
    X_2779 = isogonal_conjugate(model, A, B, C, X_2695, ID="X_2779", classes=["selected", "target"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X_73", classes=["center", "incident"])
    central_line(model, X_35, X_73, 35, 73, incident=True)
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_102, X_110, 102, 110, incident=True)
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    X_124 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(b - c)**(2)*((b + c)*(b**(2) + c**(2) - a**(2) - b*c) + a*b*c))', ID="X_124", classes=["center", "incident"])
    central_line(model, X_113, X_124, 113, 124, incident=True)
    return promote_point_to_top(model, X_2779)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2779 on the given reference triangle."""
    model = create_model('X_2779 = ISOGONAL CONJUGATE OF X_2695')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02779(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02779.json"))
    write_center_svg(
        model_acute,
        here / "x-02779.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

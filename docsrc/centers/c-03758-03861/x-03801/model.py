"""GEOMETOR construction model for X_3801 = X_2533com[INVERSE(nT(-bc, b²))]."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03801(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3801 = X_2533com[INVERSE(nT(-bc, b²))] on reference triangle ABC."""
    X_3801 = eval_barycentric_point(model, A, B, C, '((b**(2) - c**(2))*(b**(2) + c**(2) - b*c))', ID="X_3801", classes=["selected", "target"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    X_659 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c)*(b - c)', ID="X_659", classes=["center", "incident"])
    central_line(model, X_514, X_659, 514, 659, incident=True)
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    X_656 = eval_trilinear_point(model, A, B, C, 'tan(B) - tan(C)', ID="X_656", classes=["center", "incident"])
    central_line(model, X_523, X_656, 523, 656, incident=True)
    X_826 = eval_trilinear_point(model, A, B, C, 'a **(-1)*(b**(4) - c**(4)) + a**(3)*(b**(0) - c**(0))', ID="X_826", classes=["center", "incident"])
    X_1089 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2)*(b + c)**(2))', ID="X_1089", classes=["center", "incident"])
    central_line(model, X_826, X_1089, 826, 1089, incident=True)
    return promote_point_to_top(model, X_3801)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3801 on the given reference triangle."""
    model = create_model('X_3801 = X_2533com[INVERSE(nT(-bc, b²))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03801(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03801.json"))
    write_center_svg(
        model_acute,
        here / "x-03801.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

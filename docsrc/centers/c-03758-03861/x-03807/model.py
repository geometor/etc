"""GEOMETOR construction model for X_3807 = X_2525com[INVERSE(nT(bc, b²))]."""

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


def construct_x_03807(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3807 = X_2525com[INVERSE(nT(bc, b²))] on reference triangle ABC."""
    X_3807 = eval_barycentric_point(model, A, B, C, '((a - b)*(a - c)*(b**(2) + c**(2) + b*c))', ID="X_3807", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_100, X_190, 100, 190, incident=True)
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    X_668 = eval_trilinear_point(model, A, B, C, '1/(a**(2)*(b - c))', ID="X_668", classes=["center", "incident"])
    central_line(model, X_514, X_668, 514, 668, incident=True)
    return promote_point_to_top(model, X_3807)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3807 on the given reference triangle."""
    model = create_model('X_3807 = X_2525com[INVERSE(nT(bc, b²))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03807(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03807.json"))
    write_center_svg(
        model_acute,
        here / "x-03807.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

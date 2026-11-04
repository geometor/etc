"""GEOMETOR construction model for X_2419 = GIBERT-SIMSON TRANSFORM OF X_1297."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02419(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2419 = GIBERT-SIMSON TRANSFORM OF X_1297 on reference triangle ABC."""
    X_253 = eval_trilinear_point(model, A, B, C, '((csc(A))/(tan(B) + tan(C) - tan(A)))', ID="X_253", classes=["center"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center"])
    X_1297 = eval_trilinear_point(model, A, B, C, '(a/(b**(6) + c**(6) - 2*a**(6) + a**(4)*b**(2) + a**(4)*c**(2) - b**(4)*c**(2) - b**(2)*c**(4)))', ID="X_1297", classes=["center"])
    X_2373 = point_from_barycentrics(model, A, B, C, 0.69246829, 0.98040184, -0.67287013, ID="X_2373", classes=["center"])
    central_line(model, X_253, X_523, 253, 523)
    central_line(model, X_1297, X_2373, 1297, 2373)
    X_2419 = intersect_lines(model, X_253, X_523, X_1297, X_2373, ID="X_2419", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_2435 = point_from_barycentrics(model, A, B, C, -2.0119632, 2.7150562, 0.29690708, ID="X_2435", classes=["center", "incident"])
    central_line(model, X_69, X_2435, 69, 2435, incident=True)
    return promote_point_to_top(model, X_2419)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2419 on the given reference triangle."""
    model = create_model('X_2419 = GIBERT-SIMSON TRANSFORM OF X_1297')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02419(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02419.json"))
    write_center_svg(
        model_acute,
        here / "x-02419.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

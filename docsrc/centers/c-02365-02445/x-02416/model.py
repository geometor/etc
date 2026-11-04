"""GEOMETOR construction model for X_2416 = GIBERT-SIMSON TRANSFORM OF X_1294."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02416(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2416 = GIBERT-SIMSON TRANSFORM OF X_1294 on reference triangle ABC."""
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center"])
    X_1073 = eval_trilinear_point(model, A, B, C, '((cot(A))/(cos(A) - cos(B)*cos(C)))', ID="X_1073", classes=["center"])
    X_1294 = eval_barycentric_point(model, A, B, C, '1/(a**(6)*(b**(2) + c**(2)) - a**(4)*(3*b**(4) - 4*b**(2)*c**(2) + 3*c**(4)) + 3*a**(2)*(b**(2) - c**(2))**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2)*(b**(4) + 4*b**(2)*c**(2) + c**(4)))', ID="X_1294", classes=["center"])
    X_1297 = eval_trilinear_point(model, A, B, C, '(a/(b**(6) + c**(6) - 2*a**(6) + a**(4)*b**(2) + a**(4)*c**(2) - b**(4)*c**(2) - b**(2)*c**(4)))', ID="X_1297", classes=["center"])
    central_line(model, X_525, X_1073, 525, 1073)
    central_line(model, X_1294, X_1297, 1294, 1297)
    X_2416 = intersect_lines(model, X_525, X_1073, X_1294, X_1297, ID="X_2416", classes=["selected", "target"])
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    X_2430 = point_from_barycentrics(model, A, B, C, -7.9968774, 8.569498, 0.42737949, ID="X_2430", classes=["center", "incident"])
    central_line(model, X_394, X_2430, 394, 2430, incident=True)
    return promote_point_to_top(model, X_2416)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2416 on the given reference triangle."""
    model = create_model('X_2416 = GIBERT-SIMSON TRANSFORM OF X_1294')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02416(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02416.json"))
    write_center_svg(
        model_acute,
        here / "x-02416.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

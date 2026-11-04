"""GEOMETOR construction model for X_2399 = GIBERT-SIMSON TRANSFORM OF X_102."""

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


def construct_x_02399(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2399 = GIBERT-SIMSON TRANSFORM OF X_102 on reference triangle ABC."""
    X_189 = eval_trilinear_point(model, A, B, C, 'b*c/(cos(B) + cos(C) - cos(A) - 1)', ID="X_189", classes=["center"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center"])
    X_1311 = eval_barycentric_point(model, A, B, C, '1/(a**(2)*(b**(2) + c**(2)) - a*b*c*(b + c) - (b - c)**(2)*(b**(2) + b*c + c**(2)))', ID="X_1311", classes=["center"])
    central_line(model, X_189, X_514, 189, 514)
    central_line(model, X_102, X_1311, 102, 1311)
    X_2399 = intersect_lines(model, X_189, X_514, X_102, X_1311, ID="X_2399", classes=["selected", "target"])
    X_333 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)/(b + c)', ID="X_333", classes=["center", "incident"])
    X_2432 = point_from_barycentrics(model, A, B, C, -0.48835462, 1.2306536, 0.25770098, ID="X_2432", classes=["center", "incident"])
    central_line(model, X_333, X_2432, 333, 2432, incident=True)
    return promote_point_to_top(model, X_2399)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2399 on the given reference triangle."""
    model = create_model('X_2399 = GIBERT-SIMSON TRANSFORM OF X_102')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02399(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02399.json"))
    write_center_svg(
        model_acute,
        here / "x-02399.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X(845) = X(165)X(166)∩X(173)X(503)."""

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


def construct_x_00845(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(845) = X(165)X(166)∩X(173)X(503) on reference triangle ABC."""
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X(165)", classes=["center"])
    X_166 = eval_trilinear_point(model, A, B, C, '(tan(A/2))/(cos(B/2) + cos(C/2) - cos(A/2)) - (tan(B/2))/(cos(C/2) + cos(A/2) - cos(B/2)) - (tan(C/2))/(cos(A/2) + cos(B/2) - cos(C/2))', ID="X(166)", classes=["center"])
    X_164 = eval_trilinear_point(model, A, B, C, 'sin(B/2) + sin(C/2) - sin(A/2)', ID="X(164)", classes=["center"])
    X_362 = eval_trilinear_point(model, A, B, C, 'b*cos(B/2) + c*cos(C/2) - a*cos(A/2)', ID="X(362)", classes=["center"])
    central_line(model, X_165, X_166, 165, 166)
    central_line(model, X_164, X_362, 164, 362)
    X_845 = intersect_lines(model, X_165, X_166, X_164, X_362, ID="X(845)", classes=["selected", "target"])
    return promote_point_to_top(model, X_845)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(845) on the given reference triangle."""
    model = create_model('X(845) = X(165)X(166)∩X(173)X(503)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00845(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00845.json"))
    write_center_svg(
        model_acute,
        here / "x-00845.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

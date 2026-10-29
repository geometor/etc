"""GEOMETOR construction model for X(166) = GERGONNE POINT OF EXCENTRAL TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00166(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(166) = GERGONNE POINT OF EXCENTRAL TRIANGLE on reference triangle ABC."""
    X_166 = eval_trilinear_point(model, A, B, C, '(tan(A/2))/(cos(B/2) + cos(C/2) - cos(A/2)) - (tan(B/2))/(cos(C/2) + cos(A/2) - cos(B/2)) - (tan(C/2))/(cos(A/2) + cos(B/2) - cos(C/2))', ID="X(166)", classes=["selected", "target"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X(165)", classes=["center", "incident"])
    X_168 = eval_trilinear_point(model, A, B, C, 'sin(A) - sin(B) - sin(C) + 2*(cos(A/2) + sin(B/2 - A/2) + sin(C/2 - A/2))', ID="X(168)", classes=["center", "incident"])
    central_line(model, X_165, X_168, 165, 168, incident=True)
    X_167 = point_from_barycentrics(model, A, B, C, 0.58849841, 0.49152493, -0.080023337, ID="X(167)", classes=["center", "incident"])
    X_188 = eval_trilinear_point(model, A, B, C, 'csc(A/2)', ID="X(188)", classes=["center", "incident"])
    central_line(model, X_167, X_188, 167, 188, incident=True)
    return promote_point_to_top(model, X_166)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(166) on the given reference triangle."""
    model = create_model('X(166) = GERGONNE POINT OF EXCENTRAL TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00166(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00166.json"))
    write_center_svg(
        model_acute,
        here / "x-00166.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

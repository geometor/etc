"""GEOMETOR construction model for X(905) = POINT ACHERNAR."""

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


def construct_x_00905(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(905) = POINT ACHERNAR on reference triangle ABC."""
    X_905 = eval_trilinear_point(model, A, B, C, '(b - c)*cot(A)', ID="X(905)", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X(238)", classes=["center", "incident"])
    central_line(model, X_36, X_238, 36, 238, incident=True)
    X_241 = eval_trilinear_point(model, A, B, C, '(b**(2) + c**(2) - a*b - a*c)/(a - b - c)', ID="X(241)", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X(514)", classes=["center", "incident"])
    central_line(model, X_241, X_514, 241, 514, incident=True)
    X_441 = point_from_barycentrics(model, A, B, C, 0.74590002, 0.58940921, -0.33530923, ID="X(441)", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X(525)", classes=["center", "incident"])
    central_line(model, X_441, X_525, 441, 525, incident=True)
    return promote_point_to_top(model, X_905)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(905) on the given reference triangle."""
    model = create_model('X(905) = POINT ACHERNAR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00905(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00905.json"))
    write_center_svg(
        model_acute,
        here / "x-00905.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

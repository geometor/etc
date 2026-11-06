"""GEOMETOR construction model for X_3977 = X_902com[INVERSE(n(TANGENTIAL TRIANGLE))]."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03977(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3977 = X_902com[INVERSE(n(TANGENTIAL TRIANGLE))] on reference triangle ABC."""
    X_3977 = eval_barycentric_point(model, A, B, C, '((b + c - 2*a)*(b**(2) + c**(2) - a**(2)))', ID="X_3977", classes=["selected", "target"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_63, X_69, 63, 69, incident=True)
    X_441 = point_from_barycentrics(model, A, B, C, 0.74590002, 0.58940921, -0.33530923, ID="X_441", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_441, X_525, 441, 525, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    X_908 = eval_barycentric_point(model, A, B, C, 'cos(B) + cos(C) - 1', ID="X_908", classes=["center", "incident"])
    central_line(model, X_190, X_908, 190, 908, incident=True)
    return promote_point_to_top(model, X_3977)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3977 on the given reference triangle."""
    model = create_model('X_3977 = X_902com[INVERSE(n(TANGENTIAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03977(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03977.json"))
    write_center_svg(
        model_acute,
        here / "x-03977.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_3936 = X_902com[INVERSE(n(INCENTRAL TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03936(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3936 = X_902com[INVERSE(n(INCENTRAL TRIANGLE))] on reference triangle ABC."""
    X_3936 = eval_barycentric_point(model, A, B, C, '((b + c)*(b**(2) + c**(2) - a**(2) - b*c))', ID="X_3936", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_442 = point_from_barycentrics(model, A, B, C, 0.3215734, 0.32603406, 0.35239254, ID="X_442", classes=["center", "incident"])
    central_line(model, X_8, X_442, 8, 442, incident=True)
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    X_306 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2))*(b + c)*cos(A)', ID="X_306", classes=["center", "incident"])
    central_line(model, X_226, X_306, 226, 306, incident=True)
    return promote_point_to_top(model, X_3936)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3936 on the given reference triangle."""
    model = create_model('X_3936 = X_902com[INVERSE(n(INCENTRAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03936(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03936.json"))
    write_center_svg(
        model_acute,
        here / "x-03936.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

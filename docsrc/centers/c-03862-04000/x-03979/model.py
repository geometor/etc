"""GEOMETOR construction model for X_3979 = X_3750com[INVERSE(n(INTOUCH TRIANGLE))]."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03979(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3979 = X_3750com[INVERSE(n(INTOUCH TRIANGLE))] on reference triangle ABC."""
    X_3979 = eval_barycentric_point(model, A, B, C, '(a*(a**(2) + b**(2) + c**(2) - 3*a*b - 3*a*c - b*c))', ID="X_3979", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    X_846 = eval_trilinear_point(model, A, B, C, '(- a**(2) + b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_846", classes=["center", "incident"])
    central_line(model, X_518, X_846, 518, 846, incident=True)
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center", "incident"])
    X_1054 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2) - a**(2) - 3*b*c + a*b + a*c', ID="X_1054", classes=["center", "incident"])
    central_line(model, X_354, X_1054, 354, 1054, incident=True)
    return promote_point_to_top(model, X_3979)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3979 on the given reference triangle."""
    model = create_model('X_3979 = X_3750com[INVERSE(n(INTOUCH TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03979(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03979.json"))
    write_center_svg(
        model_acute,
        here / "x-03979.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_3337 = INTERSECTION OF LINES X_1X_3 AND X_7X_499."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03337(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3337 = INTERSECTION OF LINES X_1X_3 AND X_7X_499 on reference triangle ABC."""
    X_3337 = eval_trilinear_point(model, A, B, C, '((a - b + c)*(a + b - c)*(a + b + c) + a*b*c)', ID="X_3337", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center", "incident"])
    central_line(model, X_11, X_79, 11, 79, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_229 = point_from_barycentrics(model, A, B, C, 0.21061481, 0.29086323, 0.49852195, ID="X_229", classes=["center", "incident"])
    central_line(model, X_58, X_229, 58, 229, incident=True)
    return promote_point_to_top(model, X_3337)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3337 on the given reference triangle."""
    model = create_model('X_3337 = INTERSECTION OF LINES X_1X_3 AND X_7X_499')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03337(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03337.json"))
    write_center_svg(
        model_acute,
        here / "x-03337.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

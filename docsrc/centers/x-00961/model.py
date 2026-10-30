"""GEOMETOR construction model for X(961) = ISOGONAL CONJUGATE OF X(960)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00961(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(961) = ISOGONAL CONJUGATE OF X(960) on reference triangle ABC."""
    X_960 = point_from_barycentrics(model, A, B, C, 0.3968254, 0.34761905, 0.25555556, ID="X(960)", classes=["center"])
    X_961 = isogonal_conjugate(model, A, B, C, X_960, ID="X(961)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center", "incident"])
    central_line(model, X_2, X_12, 2, 12, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center", "incident"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X(81)", classes=["center", "incident"])
    central_line(model, X_65, X_81, 65, 81, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X(108)", classes=["center", "incident"])
    X_429 = point_from_barycentrics(model, A, B, C, 0.15845522, 0.2247883, 0.61675648, ID="X(429)", classes=["center", "incident"])
    central_line(model, X_108, X_429, 108, 429, incident=True)
    return promote_point_to_top(model, X_961)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(961) on the given reference triangle."""
    model = create_model('X(961) = ISOGONAL CONJUGATE OF X(960)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00961(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00961.json"))
    write_center_svg(
        model_acute,
        here / "x-00961.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

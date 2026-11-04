"""GEOMETOR construction model for X_2860 = SM(X_100, X_101)."""

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


def construct_x_02860(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2860 = SM(X_100, X_101) on reference triangle ABC."""
    X_2860 = point_from_barycentrics(model, A, B, C, -0.15806766, 0.69849469, 0.45957297, ID="X_2860", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_693 = eval_trilinear_point(model, A, B, C, '(b - c)/a**(2)', ID="X_693", classes=["center", "incident"])
    central_line(model, X_101, X_693, 101, 693, incident=True)
    return promote_point_to_top(model, X_2860)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2860 on the given reference triangle."""
    model = create_model('X_2860 = SM(X_100, X_101)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02860(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02860.json"))
    write_center_svg(
        model_acute,
        here / "x-02860.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

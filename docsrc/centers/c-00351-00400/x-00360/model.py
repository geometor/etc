"""GEOMETOR construction model for X_360 = HOFSTADTER ZERO POINT."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00360(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_360 = HOFSTADTER ZERO POINT on reference triangle ABC."""
    X_359 = eval_trilinear_point(model, A, B, C, 'a/A', ID="X_359", classes=["center"])
    X_360 = isogonal_conjugate(model, A, B, C, X_359, ID="X_360", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_1115 = eval_trilinear_point(model, A, B, C, '( pi  - A)/a', ID="X_1115", classes=["center", "incident"])
    central_line(model, X_2, X_1115, 2, 1115, incident=True)
    return promote_point_to_top(model, X_360)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_360 on the given reference triangle."""
    model = create_model('X_360 = HOFSTADTER ZERO POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00360(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00360.json"))
    write_center_svg(
        model_acute,
        here / "x-00360.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

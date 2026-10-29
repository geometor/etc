"""GEOMETOR construction model for X(486) = INNER VECTEN POINT."""

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
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00486(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(486) = INNER VECTEN POINT on reference triangle ABC."""
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A + pi /4)', ID="X(372)", classes=["center"])
    X_486 = isogonal_conjugate(model, A, B, C, X_372, ID="X(486)", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_5, X_6, 5, 6, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A - pi /4)', ID="X(371)", classes=["center", "incident"])
    central_line(model, X_2, X_371, 2, 371, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    central_line(model, X_4, X_372, 4, 372, incident=True)
    return promote_point_to_top(model, X_486)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(486) on the given reference triangle."""
    model = create_model('X(486) = INNER VECTEN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00486(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00486.json"))
    write_center_svg(
        model_acute,
        here / "x-00486.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X(54) = KOSNITA POINT."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00054(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(54) = KOSNITA POINT on reference triangle ABC."""
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_54 = isogonal_conjugate(model, A, B, C, X_5, ID="X(54)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X(24)", classes=["center", "incident"])
    central_line(model, X_6, X_24, 6, 24, incident=True)
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X(49)", classes=["center", "incident"])
    central_line(model, X_5, X_49, 5, 49, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X(68)", classes=["center", "incident"])
    central_line(model, X_2, X_68, 2, 68, incident=True)
    return promote_point_to_top(model, X_54)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(54) on the given reference triangle."""
    model = create_model('X(54) = KOSNITA POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00054(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00054.json"))
    write_center_svg(
        model_acute,
        here / "x-00054.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

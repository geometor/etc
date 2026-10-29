"""GEOMETOR construction model for X(89) = ISOGONAL CONJUGATE OF X(45)."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00089(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(89) = ISOGONAL CONJUGATE OF X(45) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center"])
    central_line(model, X_2, X_44, 2, 44)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_88 = point_from_barycentrics(model, A, B, C, -0, 1, -0, ID="X(88)", classes=["center"])
    central_line(model, X_6, X_88, 6, 88)
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X(45)", classes=["center"])
    X_89 = isogonal_conjugate(model, A, B, C, X_45, ID="X(89)", classes=["selected", "target"])
    return promote_point_to_top(model, X_89)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(89) on the given reference triangle."""
    model = create_model('X(89) = ISOGONAL CONJUGATE OF X(45)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00089(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00089.json"))
    write_center_svg(
        model_acute,
        here / "x-00089.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X(88) = ISOGONAL CONJUGATE OF X(44)."""

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
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00088(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(88) = ISOGONAL CONJUGATE OF X(44) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X(45)", classes=["center"])
    central_line(model, X_2, X_45, 2, 45)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_89 = eval_trilinear_point(model, A, B, C, '1/(2*b + 2*c - a)', ID="X(89)", classes=["center"])
    central_line(model, X_6, X_89, 6, 89)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center"])
    central_line(model, X_1, X_100, 1, 100)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center"])
    X_88 = isogonal_conjugate(model, A, B, C, X_44, ID="X(88)", classes=["selected", "target"])
    return promote_point_to_top(model, X_88)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(88) on the given reference triangle."""
    model = create_model('X(88) = ISOGONAL CONJUGATE OF X(44)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00088(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00088.json"))
    write_center_svg(
        model_acute,
        here / "x-00088.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

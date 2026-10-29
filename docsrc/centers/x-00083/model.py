"""GEOMETOR construction model for X(83) = CEVAPOINT OF CENTROID AND SYMMEDIAN POINT."""

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
    spieker_center_of,
    symmedian_point_of,
    tangential_triangle,
)
from geometor.etc.render import write_center_svg


def construct_x_00083(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(83) = CEVAPOINT OF CENTROID AND SYMMEDIAN POINT on reference triangle ABC."""
    tangential_triangle(model, A, B, C)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center"])
    central_line(model, X_2, X_32, 2, 32)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center"])
    central_line(model, X_6, X_76, 6, 76)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X(82)", classes=["center"])
    central_line(model, X_10, X_82, 10, 82)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center"])
    X_83 = isogonal_conjugate(model, A, B, C, X_39, ID="X(83)", classes=["selected", "target"])
    return promote_point_to_top(model, X_83)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(83) on the given reference triangle."""
    model = create_model('X(83) = CEVAPOINT OF CENTROID AND SYMMEDIAN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00083(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00083.json"))
    write_center_svg(
        model_acute,
        here / "x-00083.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

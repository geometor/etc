"""GEOMETOR construction model for X_1186 = 2nd SARAGOSSA POINT OF X_32."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01186(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1186 = 2nd SARAGOSSA POINT OF X_32 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center"])
    central_line(model, X_6, X_76, 6, 76)
    central_line(model, X_32, X_184, 32, 184)
    X_1186 = intersect_lines(model, X_6, X_76, X_32, X_184, ID="X_1186", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_1207 = point_from_barycentrics(model, A, B, C, 0.23796853, 0.33081949, 0.43121198, ID="X_1207", classes=["center", "incident"])
    central_line(model, X_2, X_1207, 2, 1207, incident=True)
    return promote_point_to_top(model, X_1186)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1186 on the given reference triangle."""
    model = create_model('X_1186 = 2nd SARAGOSSA POINT OF X_32')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01186(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01186.json"))
    write_center_svg(
        model_acute,
        here / "x-01186.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

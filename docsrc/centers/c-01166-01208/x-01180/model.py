"""GEOMETOR construction model for X_1180 = 2nd SARAGOSSA POINT OF X_2."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01180(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1180 = 2nd SARAGOSSA POINT OF X_2 on reference triangle ABC."""
    X_1180 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) + b**(2)*c**(2) + c**(2)*a**(2) + a**(2)*b**(2))', ID="X_1180", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    central_line(model, X_6, X_22, 6, 22, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_2, X_39, 2, 39, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_907 = eval_trilinear_point(model, A, B, C, '(a/((b**(2) - c**(2))*(3*a**(2) + b**(2) + c**(2))))', ID="X_907", classes=["center", "incident"])
    central_line(model, X_111, X_907, 111, 907, incident=True)
    return promote_point_to_top(model, X_1180)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1180 on the given reference triangle."""
    model = create_model('X_1180 = 2nd SARAGOSSA POINT OF X_2')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01180(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01180.json"))
    write_center_svg(
        model_acute,
        here / "x-01180.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

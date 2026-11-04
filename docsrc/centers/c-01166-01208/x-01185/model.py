"""GEOMETOR construction model for X_1185 = 2nd SARAGOSSA POINT OF X_31."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01185(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1185 = 2nd SARAGOSSA POINT OF X_31 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    central_line(model, X_2, X_6, 2, 6)
    central_line(model, X_31, X_32, 31, 32)
    X_1185 = intersect_lines(model, X_2, X_6, X_31, X_32, ID="X_1185", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1206 = point_from_barycentrics(model, A, B, C, 0.23300471, 0.32875106, 0.43824423, ID="X_1206", classes=["center", "incident"])
    central_line(model, X_1, X_1206, 1, 1206, incident=True)
    return promote_point_to_top(model, X_1185)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1185 on the given reference triangle."""
    model = create_model('X_1185 = 2nd SARAGOSSA POINT OF X_31')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01185(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01185.json"))
    write_center_svg(
        model_acute,
        here / "x-01185.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

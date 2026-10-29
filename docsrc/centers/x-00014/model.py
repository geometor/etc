"""GEOMETOR construction model for X(14) = 2nd ISOGONIC CENTER."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    circumcircle,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    inner_equilateral_triangles,
    perspector,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00014(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(14) = 2nd ISOGONIC CENTER on reference triangle ABC."""
    circumcircle(model, A, B, C)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center"])
    central_line(model, X_6, X_13, 6, 13)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A + pi /3)', ID="X(15)", classes=["center"])
    central_line(model, X_2, X_15, 2, 15)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_18 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /6)', ID="X(18)", classes=["center"])
    central_line(model, X_3, X_18, 3, 18)
    Ea, Eb, Ec = inner_equilateral_triangles(model, A, B, C)
    X_14 = perspector(model, A, B, C, Ea, Eb, Ec, ID="X(14)", classes=["selected", "target"])
    return promote_point_to_top(model, X_14)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(14) on the given reference triangle."""
    model = create_model('X(14) = 2nd ISOGONIC CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00014(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00014.json"))
    write_center_svg(
        model_acute,
        here / "x-00014.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

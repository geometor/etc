"""GEOMETOR construction model for X(299) = ISOTOMIC CONJUGATE OF 2nd ISOGONIC CENTER."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00299(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(299) = ISOTOMIC CONJUGATE OF 2nd ISOGONIC CENTER on reference triangle ABC."""
    X_299 = eval_barycentric_point(model, A, B, C, 'csc(A)*sin(A - pi /3)', ID="X(299)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_13, X_76, 13, 76, incident=True)
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X(14)", classes=["center", "incident"])
    X_533 = point_from_barycentrics(model, A, B, C, 0.76482932, -0.13487259, -0.62995674, ID="X(533)", classes=["center", "incident"])
    central_line(model, X_14, X_533, 14, 533, incident=True)
    return promote_point_to_top(model, X_299)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(299) on the given reference triangle."""
    model = create_model('X(299) = ISOTOMIC CONJUGATE OF 2nd ISOGONIC CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00299(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00299.json"))
    write_center_svg(
        model_acute,
        here / "x-00299.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

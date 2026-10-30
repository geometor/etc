"""GEOMETOR construction model for X(641) = COMPLEMENT OF X(485)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00641(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(641) = COMPLEMENT OF X(485) on reference triangle ABC."""
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A - pi /4)', ID="X(485)", classes=["center"])
    X_488 = point_from_barycentrics(model, A, B, C, 0.48788658, 0.37148244, 0.14063098, ID="X(488)", classes=["center"])
    X_641 = midpoint(model, X_485, X_488, ID="X(641)", classes=["selected", "target"], guide=False)
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X(140)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_140, X_141, 140, 141, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A + pi /4)', ID="X(372)", classes=["center", "incident"])
    central_line(model, X_2, X_372, 2, 372, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_639 = point_from_barycentrics(model, A, B, C, 0.35035787, 0.32442401, 0.32521812, ID="X(639)", classes=["center", "incident"])
    central_line(model, X_3, X_639, 3, 639, incident=True)
    return promote_point_to_top(model, X_641)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(641) on the given reference triangle."""
    model = create_model('X(641) = COMPLEMENT OF X(485)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00641(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00641.json"))
    write_center_svg(
        model_acute,
        here / "x-00641.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

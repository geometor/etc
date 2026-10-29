"""GEOMETOR construction model for X(472) = X(62)-CROSS CONJUGATE OF X(303)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00472(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(472) = X(62)-CROSS CONJUGATE OF X(303) on reference triangle ABC."""
    X_466 = point_from_barycentrics(model, A, B, C, 0.46465913, 0.4148459, 0.12049497, ID="X(466)", classes=["center"])
    X_472 = anticomplement(model, A, B, C, X_466, ID="X(472)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center", "incident"])
    X_275 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*sec(B - C)', ID="X(275)", classes=["center", "incident"])
    central_line(model, X_13, X_275, 13, 275, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X(53)", classes=["center", "incident"])
    X_395 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 2*cos(A + pi /3)', ID="X(395)", classes=["center", "incident"])
    central_line(model, X_53, X_395, 53, 395, incident=True)
    return promote_point_to_top(model, X_472)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(472) on the given reference triangle."""
    model = create_model('X(472) = X(62)-CROSS CONJUGATE OF X(303)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00472(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00472.json"))
    write_center_svg(
        model_acute,
        here / "x-00472.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

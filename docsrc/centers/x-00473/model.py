"""GEOMETOR construction model for X(473) = X(61)-CROSS CONJUGATE OF X(302)."""

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


def construct_x_00473(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(473) = X(61)-CROSS CONJUGATE OF X(302) on reference triangle ABC."""
    X_465 = point_from_barycentrics(model, A, B, C, 0.41498319, 0.38401256, 0.20100425, ID="X(465)", classes=["center"])
    X_473 = anticomplement(model, A, B, C, X_465, ID="X(473)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X(14)", classes=["center", "incident"])
    X_275 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*sec(B - C)', ID="X(275)", classes=["center", "incident"])
    central_line(model, X_14, X_275, 14, 275, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X(53)", classes=["center", "incident"])
    X_396 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 2*cos(A - pi /3)', ID="X(396)", classes=["center", "incident"])
    central_line(model, X_53, X_396, 53, 396, incident=True)
    return promote_point_to_top(model, X_473)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(473) on the given reference triangle."""
    model = create_model('X(473) = X(61)-CROSS CONJUGATE OF X(302)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00473(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00473.json"))
    write_center_svg(
        model_acute,
        here / "x-00473.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_3733 = X_656com(TANGENTIAL TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03733(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3733 = X_656com(TANGENTIAL TRIANGLE) on reference triangle ABC."""
    X_3733 = eval_barycentric_point(model, A, B, C, 'a**(2)*(b - c)/(b + c)', ID="X_3733", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_36, X_238, 36, 238, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_798 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))', ID="X_798", classes=["center", "incident"])
    central_line(model, X_6, X_798, 6, 798, incident=True)
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center", "incident"])
    X_876 = point_from_barycentrics(model, A, B, C, 0.024662513, 1.0062305, -0.030893043, ID="X_876", classes=["center", "incident"])
    central_line(model, X_82, X_876, 82, 876, incident=True)
    return promote_point_to_top(model, X_3733)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3733 on the given reference triangle."""
    model = create_model('X_3733 = X_656com(TANGENTIAL TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03733(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03733.json"))
    write_center_svg(
        model_acute,
        here / "x-03733.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X(470) = X(15)-CROSS CONJUGATE OF X(298)."""

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
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00470(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(470) = X(15)-CROSS CONJUGATE OF X(298) on reference triangle ABC."""
    X_470 = eval_trilinear_point(model, A, B, C, 'sin(A + pi /3)*csc(2*A)', ID="X(470)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_18 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /6)', ID="X(18)", classes=["center", "incident"])
    X_275 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*sec(B - C)', ID="X(275)", classes=["center", "incident"])
    central_line(model, X_18, X_275, 18, 275, incident=True)
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X(264)", classes=["center", "incident"])
    X_301 = eval_barycentric_point(model, A, B, C, 'csc(A)*csc(A - pi /3)', ID="X(301)", classes=["center", "incident"])
    central_line(model, X_264, X_301, 264, 301, incident=True)
    return promote_point_to_top(model, X_470)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(470) on the given reference triangle."""
    model = create_model('X(470) = X(15)-CROSS CONJUGATE OF X(298)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00470(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00470.json"))
    write_center_svg(
        model_acute,
        here / "x-00470.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

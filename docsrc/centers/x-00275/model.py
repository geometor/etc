"""GEOMETOR construction model for X(275) = CEVAPOINT OF ORTHOCENTER AND SYMMEDIAN POINT."""

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
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00275(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(275) = CEVAPOINT OF ORTHOCENTER AND SYMMEDIAN POINT on reference triangle ABC."""
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X(216)", classes=["center"])
    X_275 = isogonal_conjugate(model, A, B, C, X_216, ID="X(275)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    central_line(model, X_4, X_54, 4, 54, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X(95)", classes=["center", "incident"])
    central_line(model, X_2, X_95, 2, 95, incident=True)
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center", "incident"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X(107)", classes=["center", "incident"])
    central_line(model, X_51, X_107, 51, 107, incident=True)
    return promote_point_to_top(model, X_275)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(275) on the given reference triangle."""
    model = create_model('X(275) = CEVAPOINT OF ORTHOCENTER AND SYMMEDIAN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00275(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00275.json"))
    write_center_svg(
        model_acute,
        here / "x-00275.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X(81) = CEVAPOINT OF INCENTER AND SYMMEDIAN POINT."""

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
    gergonne_point_of,
    incenter_of,
    incircle,
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
    tangential_triangle,
)
from geometor.etc.render import write_center_svg


def construct_x_00081(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(81) = CEVAPOINT OF INCENTER AND SYMMEDIAN POINT on reference triangle ABC."""
    incircle(model, A, B, C)
    tangential_triangle(model, A, B, C)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    central_line(model, X_2, X_6, 2, 6)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center"])
    central_line(model, X_1, X_21, 1, 21)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X(27)", classes=["center"])
    central_line(model, X_7, X_27, 7, 27)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center"])
    X_81 = isogonal_conjugate(model, A, B, C, X_37, ID="X(81)", classes=["selected", "target"])
    return promote_point_to_top(model, X_81)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(81) on the given reference triangle."""
    model = create_model('X(81) = CEVAPOINT OF INCENTER AND SYMMEDIAN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00081(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00081.json"))
    write_center_svg(
        model_acute,
        here / "x-00081.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X(20) = DE LONGCHAMPS POINT."""

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
    gergonne_point_of,
    incenter_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00020(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(20) = DE LONGCHAMPS POINT on reference triangle ABC."""
    circumcircle(model, A, B, C)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    central_line(model, X_1, X_7, 1, 7)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center"])
    central_line(model, X_8, X_40, 8, 40)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["selected", "target"])
    return promote_point_to_top(model, X_20)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(20) on the given reference triangle."""
    model = create_model('X(20) = DE LONGCHAMPS POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00020(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00020.json"))
    write_center_svg(
        model_acute,
        here / "x-00020.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

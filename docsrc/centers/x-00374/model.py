"""GEOMETOR construction model for X(374) = CENTROID OF THE PEDAL TRIANGLE OF X(9)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00374(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(374) = CENTROID OF THE PEDAL TRIANGLE OF X(9) on reference triangle ABC."""
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X(210)", classes=["center"])
    central_line(model, X_44, X_65, 44, 65)
    central_line(model, X_51, X_210, 51, 210)
    X_374 = intersect_lines(model, X_44, X_65, X_51, X_210, ID="X(374)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X(354)", classes=["center", "incident"])
    central_line(model, X_6, X_354, 6, 354, incident=True)
    return promote_point_to_top(model, X_374)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(374) on the given reference triangle."""
    model = create_model('X(374) = CENTROID OF THE PEDAL TRIANGLE OF X(9)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00374(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00374.json"))
    write_center_svg(
        model_acute,
        here / "x-00374.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

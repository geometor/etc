"""GEOMETOR construction model for X_3695 = X_580com(EXTOUCH TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    nine_point_center_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03695(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3695 = X_580com(EXTOUCH TRIANGLE) on reference triangle ABC."""
    X_3695 = eval_barycentric_point(model, A, B, C, '((b + c)**(2)*(b**(2) + c **(2) - a**(2)))', ID="X_3695", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_10, X_37, 10, 37, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_312 = eval_trilinear_point(model, A, B, C, '(b + c - a)*b**(2)*c**(2)', ID="X_312", classes=["center", "incident"])
    central_line(model, X_5, X_312, 5, 312, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_345 = eval_trilinear_point(model, A, B, C, '(csc(A))/(1 - sec(A))', ID="X_345", classes=["center", "incident"])
    central_line(model, X_3, X_345, 3, 345, incident=True)
    return promote_point_to_top(model, X_3695)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3695 on the given reference triangle."""
    model = create_model('X_3695 = X_580com(EXTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03695(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03695.json"))
    write_center_svg(
        model_acute,
        here / "x-03695.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

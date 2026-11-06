"""GEOMETOR construction model for X_3700 = X_661com(EXTOUCH TRIANGLE)."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03700(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3700 = X_661com(EXTOUCH TRIANGLE) on reference triangle ABC."""
    X_3700 = eval_barycentric_point(model, A, B, C, '((b + c - a)*(b**(2) - c**(2)))', ID="X_3700", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X_647", classes=["center", "incident"])
    central_line(model, X_37, X_647, 37, 647, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_1021 = eval_trilinear_point(model, A, B, C, '((cos(B) - cos(C))/(cos(B) + cos(C)))', ID="X_1021", classes=["center", "incident"])
    central_line(model, X_9, X_1021, 9, 1021, incident=True)
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    X_850 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))/a**(3)', ID="X_850", classes=["center", "incident"])
    central_line(model, X_321, X_850, 321, 850, incident=True)
    return promote_point_to_top(model, X_3700)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3700 on the given reference triangle."""
    model = create_model('X_3700 = X_661com(EXTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03700(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03700.json"))
    write_center_svg(
        model_acute,
        here / "x-03700.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

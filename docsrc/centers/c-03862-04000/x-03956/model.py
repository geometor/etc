"""GEOMETOR construction model for X_3956 = X_549com(EXTOUCH TRIANGLE)."""

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
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03956(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3956 = X_549com(EXTOUCH TRIANGLE) on reference triangle ABC."""
    X_3956 = eval_barycentric_point(model, A, B, C, '(a*(b + c)*(b**(2) + c**(2) - a**(2) + 5*b*c))', ID="X_3956", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    central_line(model, X_10, X_12, 10, 12, incident=True)
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    X_3740 = eval_barycentric_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*b - a*c + 4*b*c)', ID="X_3740", classes=["center", "incident"])
    central_line(model, X_519, X_3740, 519, 3740, incident=True)
    X_1962 = eval_trilinear_point(model, A, B, C, '(b + c)*(2*a + b + c)', ID="X_1962", classes=["center", "incident"])
    X_3293 = eval_trilinear_point(model, A, B, C, '((b + c)*((c + a)**(2) + (a + b)**(2) - (b + c)**(2)))', ID="X_3293", classes=["center", "incident"])
    central_line(model, X_1962, X_3293, 1962, 3293, incident=True)
    return promote_point_to_top(model, X_3956)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3956 on the given reference triangle."""
    model = create_model('X_3956 = X_549com(EXTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03956(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03956.json"))
    write_center_svg(
        model_acute,
        here / "x-03956.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

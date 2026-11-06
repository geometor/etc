"""GEOMETOR construction model for X_3988 = X_546com(EXTOUCH TRIANGLE)."""

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


def construct_x_03988(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3988 = X_546com(EXTOUCH TRIANGLE) on reference triangle ABC."""
    X_3988 = eval_barycentric_point(model, A, B, C, '(a*(b + c)*(3*b**(2) + 3*c**(2) - 3*a**(2) + b*c))', ID="X_3988", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    central_line(model, X_10, X_12, 10, 12, incident=True)
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    X_3636 = eval_trilinear_point(model, A, B, C, 'b*c*(6*a + b + c)', ID="X_3636", classes=["center", "incident"])
    central_line(model, X_518, X_3636, 518, 3636, incident=True)
    X_960 = eval_trilinear_point(model, A, B, C, '((b + c - a)*(b**(2) + c**(2) + a*b + a*c))', ID="X_960", classes=["center", "incident"])
    X_3635 = eval_trilinear_point(model, A, B, C, 'b*c*(6*a - b - c)', ID="X_3635", classes=["center", "incident"])
    central_line(model, X_960, X_3635, 960, 3635, incident=True)
    return promote_point_to_top(model, X_3988)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3988 on the given reference triangle."""
    model = create_model('X_3988 = X_546com(EXTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03988(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03988.json"))
    write_center_svg(
        model_acute,
        here / "x-03988.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

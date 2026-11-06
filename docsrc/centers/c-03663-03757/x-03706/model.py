"""GEOMETOR construction model for X_3706 = X_42com(EXTOUCH TRIANGLE)."""

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
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03706(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3706 = X_42com(EXTOUCH TRIANGLE) on reference triangle ABC."""
    X_3706 = eval_barycentric_point(model, A, B, C, '((b+c)*a+2*b*c) * (-a+b+c)', ID="X_3706", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    central_line(model, X_8, X_210, 8, 210, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center", "incident"])
    central_line(model, X_75, X_354, 75, 354, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_536 = eval_barycentric_point(model, A, B, C, '2*b*c - c*a - a*b', ID="X_536", classes=["center", "incident"])
    central_line(model, X_38, X_536, 38, 536, incident=True)
    return promote_point_to_top(model, X_3706)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3706 on the given reference triangle."""
    model = create_model('X_3706 = X_42com(EXTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03706(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03706.json"))
    write_center_svg(
        model_acute,
        here / "x-03706.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

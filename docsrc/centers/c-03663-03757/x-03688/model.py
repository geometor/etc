"""GEOMETOR construction model for X_3688 = X_75com(EXTOUCH TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03688(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3688 = X_75com(EXTOUCH TRIANGLE) on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    X_3688 = crosspoint(model, A, B, C, X_8, X_55, ID="X_3688", classes=["selected", "target"])
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X_219", classes=["center", "incident"])
    central_line(model, X_55, X_219, 55, 219, incident=True)
    X_314 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2)*(b + c - a)/(b + c))', ID="X_314", classes=["center", "incident"])
    central_line(model, X_8, X_314, 8, 314, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_674 = eval_trilinear_point(model, A, B, C, '(a*(b**(3) + c**(3) - a*(b**(2) + c**(2))))', ID="X_674", classes=["center", "incident"])
    central_line(model, X_37, X_674, 37, 674, incident=True)
    return promote_point_to_top(model, X_3688)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3688 on the given reference triangle."""
    model = create_model('X_3688 = X_75com(EXTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03688(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03688.json"))
    write_center_svg(
        model_acute,
        here / "x-03688.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

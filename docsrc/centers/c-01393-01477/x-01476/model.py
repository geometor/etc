"""GEOMETOR construction model for X_1476 = X_1222-BETH CONJUGATE OF X_1222."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01476(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1476 = X_1222-BETH CONJUGATE OF X_1222 on reference triangle ABC."""
    X_1476 = eval_trilinear_point(model, A, B, C, '1/(a**(2)*((sin(B/2))**(2) + (sin(C/2))**(2)))', ID="X_1476", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_8, X_56, 8, 56, incident=True)
    X_172 = eval_trilinear_point(model, A, B, C, 'a**(3) + a*b*c', ID="X_172", classes=["center", "incident"])
    X_294 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b**(2) + c**(2) - a*b - a*c))', ID="X_294", classes=["center", "incident"])
    central_line(model, X_172, X_294, 172, 294, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_496 = eval_trilinear_point(model, A, B, C, '2 - cos(B - C)', ID="X_496", classes=["center", "incident"])
    central_line(model, X_4, X_496, 4, 496, incident=True)
    return promote_point_to_top(model, X_1476)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1476 on the given reference triangle."""
    model = create_model('X_1476 = X_1222-BETH CONJUGATE OF X_1222')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01476(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01476.json"))
    write_center_svg(
        model_acute,
        here / "x-01476.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_1501 = TRILINEAR 5th POWER POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01501(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1501 = TRILINEAR 5th POWER POINT on reference triangle ABC."""
    X_1501 = eval_trilinear_point(model, A, B, C, 'a**(5)', ID="X_1501", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    central_line(model, X_6, X_22, 6, 22, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_32, X_184, 32, 184, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_697 = eval_trilinear_point(model, A, B, C, '(1/(a **(-5)*(b **(-3) + c **(-3)) - a **(-4)*(b **(-4) + c **(-4))))', ID="X_697", classes=["center", "incident"])
    central_line(model, X_101, X_697, 101, 697, incident=True)
    return promote_point_to_top(model, X_1501)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1501 on the given reference triangle."""
    model = create_model('X_1501 = TRILINEAR 5th POWER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01501(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01501.json"))
    write_center_svg(
        model_acute,
        here / "x-01501.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

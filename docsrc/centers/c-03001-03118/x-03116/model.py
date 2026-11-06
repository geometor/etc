"""GEOMETOR construction model for X_3116 = ISOGONAL CONJUGATE OF GtX(31)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03116(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3116 = ISOGONAL CONJUGATE OF GtX(31) on reference triangle ABC."""
    X_3113 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))/(a**(2)*(b**(6) - c**(6)))', ID="X_3113", classes=["center"])
    X_3116 = isogonal_conjugate(model, A, B, C, X_3113, ID="X_3116", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_31, X_48, 31, 48, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_38, X_75, 38, 75, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_723 = eval_trilinear_point(model, A, B, C, '(1/(a **(-4)*(b**(3) + c**(3)) - a**(2)*(b **(-3) + c **(-3))))', ID="X_723", classes=["center", "incident"])
    central_line(model, X_99, X_723, 99, 723, incident=True)
    return promote_point_to_top(model, X_3116)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3116 on the given reference triangle."""
    model = create_model('X_3116 = ISOGONAL CONJUGATE OF GtX(31)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03116(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03116.json"))
    write_center_svg(
        model_acute,
        here / "x-03116.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

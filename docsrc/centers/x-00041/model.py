"""GEOMETOR construction model for X(41) = -CEVA CONJUGATE OF X(31)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00041(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(41) = -CEVA CONJUGATE OF X(31) on reference triangle ABC."""
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center"])
    central_line(model, X_9, X_21, 9, 21)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center"])
    central_line(model, X_31, X_32, 31, 32)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center"])
    central_line(model, X_6, X_48, 6, 48)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["selected", "target"])
    return promote_point_to_top(model, X_41)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(41) on the given reference triangle."""
    model = create_model('X(41) = -CEVA CONJUGATE OF X(31)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00041(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00041.json"))
    write_center_svg(
        model_acute,
        here / "x-00041.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

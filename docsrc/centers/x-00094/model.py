"""GEOMETOR construction model for X(94) = ISOGONAL CONJUGATE OF X(50)."""

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
    nine_point_circle,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00094(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(94) = ISOGONAL CONJUGATE OF X(50) on reference triangle ABC."""
    nine_point_circle(model, A, B, C)
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X(49)", classes=["center"])
    X_93 = eval_trilinear_point(model, A, B, C, 'sec(3*A)', ID="X(93)", classes=["center"])
    central_line(model, X_49, X_93, 49, 93)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(23)", classes=["center"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center"])
    central_line(model, X_23, X_98, 23, 98)
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X(50)", classes=["center"])
    X_94 = isogonal_conjugate(model, A, B, C, X_50, ID="X(94)", classes=["selected", "target"])
    return promote_point_to_top(model, X_94)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(94) on the given reference triangle."""
    model = create_model('X(94) = ISOGONAL CONJUGATE OF X(50)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00094(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00094.json"))
    write_center_svg(
        model_acute,
        here / "x-00094.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

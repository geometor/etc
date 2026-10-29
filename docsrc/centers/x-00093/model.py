"""GEOMETOR construction model for X(93) = ISOGONAL CONJUGATE OF X(49)."""

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


def construct_x_00093(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(93) = ISOGONAL CONJUGATE OF X(49) on reference triangle ABC."""
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X(49)", classes=["center"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X(94)", classes=["center"])
    central_line(model, X_49, X_94, 49, 94)
    X_93 = isogonal_conjugate(model, A, B, C, X_49, ID="X(93)", classes=["selected", "target"])
    return promote_point_to_top(model, X_93)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(93) on the given reference triangle."""
    model = create_model('X(93) = ISOGONAL CONJUGATE OF X(49)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00093(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00093.json"))
    write_center_svg(
        model_acute,
        here / "x-00093.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

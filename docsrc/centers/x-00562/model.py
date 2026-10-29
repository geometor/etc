"""GEOMETOR construction model for X(562) = TRILINEAR QUOTIENT X(2)*X(50)/X(49)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00562(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(562) = TRILINEAR QUOTIENT X(2)*X(50)/X(49) on reference triangle ABC."""
    X_562 = eval_trilinear_point(model, A, B, C, 'csc(A)*tan(3*A)', ID="X(562)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_93 = eval_trilinear_point(model, A, B, C, 'sec(3*A)', ID="X(93)", classes=["center", "incident"])
    central_line(model, X_4, X_93, 4, 93, incident=True)
    return promote_point_to_top(model, X_562)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(562) on the given reference triangle."""
    model = create_model('X(562) = TRILINEAR QUOTIENT X(2)*X(50)/X(49)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00562(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00562.json"))
    write_center_svg(
        model_acute,
        here / "x-00562.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

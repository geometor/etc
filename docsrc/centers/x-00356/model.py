"""GEOMETOR construction model for X(356) = MORLEY CENTER."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00356(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(356) = MORLEY CENTER on reference triangle ABC."""
    X_356 = eval_trilinear_point(model, A, B, C, 'cos(A/3) + 2*cos(B/3)*cos(C/3)', ID="X(356)", classes=["selected", "target"])
    X_357 = eval_trilinear_point(model, A, B, C, 'sec(A/3)', ID="X(357)", classes=["center", "incident"])
    X_358 = eval_trilinear_point(model, A, B, C, 'cos(A/3)', ID="X(358)", classes=["center", "incident"])
    central_line(model, X_357, X_358, 357, 358, incident=True)
    return promote_point_to_top(model, X_356)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(356) on the given reference triangle."""
    model = create_model('X(356) = MORLEY CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00356(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00356.json"))
    write_center_svg(
        model_acute,
        here / "x-00356.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X(822) = CROSSDIFFERENCE OF X(1) AND X(29)."""

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


def construct_x_00822(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(822) = CROSSDIFFERENCE OF X(1) AND X(29) on reference triangle ABC."""
    X_822 = eval_trilinear_point(model, A, B, C, 'csc(B/2) - csc(C/2)', ID="X(822)", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    return promote_point_to_top(model, X_822)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(822) on the given reference triangle."""
    model = create_model('X(822) = CROSSDIFFERENCE OF X(1) AND X(29)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00822(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00822.json"))
    write_center_svg(
        model_acute,
        here / "x-00822.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

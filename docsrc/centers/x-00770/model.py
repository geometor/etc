"""GEOMETOR construction model for X(770) = POINT ACAMAR."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00770(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(770) = POINT ACAMAR on reference triangle ABC."""
    X_770 = point_from_barycentrics(model, A, B, C, 14.48, -40.752, 27.272, ID="X(770)", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    return promote_point_to_top(model, X_770)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(770) on the given reference triangle."""
    model = create_model('X(770) = POINT ACAMAR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00770(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00770.json"))
    write_center_svg(
        model_acute,
        here / "x-00770.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

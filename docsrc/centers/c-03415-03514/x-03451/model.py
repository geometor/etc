"""GEOMETOR construction model for X_3451 = 1st SARAGOSSA POINT OF X_9."""

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
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03451(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3451 = 1st SARAGOSSA POINT OF X_9 on reference triangle ABC."""
    X_3451 = eval_trilinear_point(model, A, B, C, '(a/ ((b + c - a)*(a*(b + c) + (b - c)**(2))))', ID="X_3451", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_604 = eval_trilinear_point(model, A, B, C, 'a*(1 - cos(A))', ID="X_604", classes=["center", "incident"])
    central_line(model, X_9, X_604, 9, 604, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_572 = eval_trilinear_point(model, A, B, C, '(cos(A - U))', ID="X_572", classes=["center", "incident"])
    central_line(model, X_55, X_572, 55, 572, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1604 = point_from_barycentrics(model, A, B, C, 0.93491407, 0.89942712, -0.83434118, ID="X_1604", classes=["center", "incident"])
    central_line(model, X_6, X_1604, 6, 1604, incident=True)
    return promote_point_to_top(model, X_3451)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3451 on the given reference triangle."""
    model = create_model('X_3451 = 1st SARAGOSSA POINT OF X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03451(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03451.json"))
    write_center_svg(
        model_acute,
        here / "x-03451.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

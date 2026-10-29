"""GEOMETOR construction model for X(366) = ISOGONAL CONJUGATE OF X(365)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00366(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(366) = ISOGONAL CONJUGATE OF X(365) on reference triangle ABC."""
    X_365 = eval_trilinear_point(model, A, B, C, 'a**(1/2)', ID="X(365)", classes=["center"])
    X_366 = isogonal_conjugate(model, A, B, C, X_365, ID="X(366)", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_364 = eval_trilinear_point(model, A, B, C, 'b**(1/2) + c**(1/2) - a**(1/2)', ID="X(364)", classes=["center", "incident"])
    central_line(model, X_9, X_364, 9, 364, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_367 = eval_trilinear_point(model, A, B, C, 'b**(1/2) + c**(1/2)', ID="X(367)", classes=["center", "incident"])
    central_line(model, X_2, X_367, 2, 367, incident=True)
    return promote_point_to_top(model, X_366)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(366) on the given reference triangle."""
    model = create_model('X(366) = ISOGONAL CONJUGATE OF X(365)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00366(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00366.json"))
    write_center_svg(
        model_acute,
        here / "x-00366.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

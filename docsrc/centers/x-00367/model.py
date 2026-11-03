"""GEOMETOR construction model for X_367 = CROSSPOINT OF X_1 AND X_366."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00367(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_367 = CROSSPOINT OF X_1 AND X_366 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_366 = eval_trilinear_point(model, A, B, C, 'a**(-1/2)', ID="X_366", classes=["center"])
    X_367 = crosspoint(model, A, B, C, X_1, X_366, ID="X_367", classes=["selected", "target"])
    X_364 = eval_trilinear_point(model, A, B, C, 'b**(1/2) + c**(1/2) - a**(1/2)', ID="X_364", classes=["center", "incident"])
    central_line(model, X_1, X_364, 1, 364, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_366, 2, 366, incident=True)
    return promote_point_to_top(model, X_367)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_367 on the given reference triangle."""
    model = create_model('X_367 = CROSSPOINT OF X_1 AND X_366')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00367(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00367.json"))
    write_center_svg(
        model_acute,
        here / "x-00367.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

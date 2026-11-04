"""GEOMETOR construction model for X_1286 = COLLINGS TRANSFORM OF X_22."""

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


def construct_x_01286(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1286 = COLLINGS TRANSFORM OF X_22 on reference triangle ABC."""
    X_1286 = point_from_barycentrics(model, A, B, C, 0.47412809, 1.0990863, -0.57321442, ID="X_1286", classes=["selected", "target"])
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_26", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_26, X_98, 26, 98, incident=True)
    return promote_point_to_top(model, X_1286)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1286 on the given reference triangle."""
    model = create_model('X_1286 = COLLINGS TRANSFORM OF X_22')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01286(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01286.json"))
    write_center_svg(
        model_acute,
        here / "x-01286.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

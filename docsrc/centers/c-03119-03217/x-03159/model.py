"""GEOMETOR construction model for X_3159 = X_1-CEVA CONJUGATE OF X_10."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03159(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3159 = X_1-CEVA CONJUGATE OF X_10 on reference triangle ABC."""
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center"])
    X_2901 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c)*(a**(3) + a**(2)*b + a**(2)*c - b**(2)*c - b*c**(2)))', ID="X_2901", classes=["center"])
    X_3159 = midpoint(model, X_72, X_2901, ID="X_3159", classes=["selected", "target"], guide=False)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_37, X_39, 37, 39, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_58, X_190, 58, 190, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_10, X_321, 10, 321, incident=True)
    return promote_point_to_top(model, X_3159)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3159 on the given reference triangle."""
    model = create_model('X_3159 = X_1-CEVA CONJUGATE OF X_10')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03159(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03159.json"))
    write_center_svg(
        model_acute,
        here / "x-03159.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

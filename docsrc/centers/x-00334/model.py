"""GEOMETOR construction model for X(334) = ISOTOMIC CONJUGATE OF X(238)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00334(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(334) = ISOTOMIC CONJUGATE OF X(238) on reference triangle ABC."""
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X(238)", classes=["center"])
    X_334 = isotomic_conjugate(model, A, B, C, X_238, ID="X(334)", classes=["selected", "target"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X(85)", classes=["center", "incident"])
    central_line(model, X_12, X_85, 12, 85, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_75, X_141, 75, 141, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_274 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c)', ID="X(274)", classes=["center", "incident"])
    central_line(model, X_10, X_274, 10, 274, incident=True)
    return promote_point_to_top(model, X_334)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(334) on the given reference triangle."""
    model = create_model('X(334) = ISOTOMIC CONJUGATE OF X(238)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00334(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00334.json"))
    write_center_svg(
        model_acute,
        here / "x-00334.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

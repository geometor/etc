"""GEOMETOR construction model for X_3775 = X_594com[INVERSE(nT(bc, c²))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
    reflection_in_point,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03775(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3775 = X_594com[INVERSE(nT(bc, c²))] on reference triangle ABC."""
    X_1100 = eval_trilinear_point(model, A, B, C, '2*a + b + c', ID="X_1100", classes=["center"])
    X_1125 = eval_trilinear_point(model, A, B, C, '(2*a+b+c)/a', ID="X_1125", classes=["center"])
    X_3775 = reflection_in_point(model, X_1100, X_1125, ID="X_3775", classes=["selected", "target"], guide=False)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center", "incident"])
    central_line(model, X_10, X_141, 10, 141, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_319 = eval_trilinear_point(model, A, B, C, '(1 + 2*cos(A))/a**(2)', ID="X_319", classes=["center", "incident"])
    central_line(model, X_1, X_319, 1, 319, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_1211 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c)*(b**(2) + c**(2) + a*b + a*c))', ID="X_1211", classes=["center", "incident"])
    central_line(model, X_11, X_1211, 11, 1211, incident=True)
    return promote_point_to_top(model, X_3775)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3775 on the given reference triangle."""
    model = create_model('X_3775 = X_594com[INVERSE(nT(bc, c²))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03775(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03775.json"))
    write_center_svg(
        model_acute,
        here / "x-03775.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

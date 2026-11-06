"""GEOMETOR construction model for X_3097 = INTERSECTION OF LINES X_1X_39 AND X_43X_63."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    reflection_in_point,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03097(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3097 = INTERSECTION OF LINES X_1X_39 AND X_43X_63 on reference triangle ABC."""
    X_1699 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A) + cos(B) + cos(C) - 1', ID="X_1699", classes=["center"])
    X_262 = eval_trilinear_point(model, A, B, C, 'sec(A -  omega  )', ID="X_262", classes=["center"])
    X_3097 = reflection_in_point(model, X_1699, X_262, ID="X_3097", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_1, X_39, 1, 39, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_43, X_63, 43, 63, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center", "incident"])
    central_line(model, X_10, X_194, 10, 194, incident=True)
    return promote_point_to_top(model, X_3097)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3097 on the given reference triangle."""
    model = create_model('X_3097 = INTERSECTION OF LINES X_1X_39 AND X_43X_63')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03097(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03097.json"))
    write_center_svg(
        model_acute,
        here / "x-03097.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

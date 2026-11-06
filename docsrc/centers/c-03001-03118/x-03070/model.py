"""GEOMETOR construction model for X_3070 = INTERSECTION OF X_4X_6 AND X_5X_372."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03070(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3070 = INTERSECTION OF X_4X_6 AND X_5X_372 on reference triangle ABC."""
    X_490 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 + csc(A)*sin(B)*sin(C)) - cos(B)*cos(C))', ID="X_490", classes=["center"])
    X_3070 = complement(model, A, B, C, X_490, ID="X_3070", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A +  pi  /4)', ID="X_372", classes=["center", "incident"])
    central_line(model, X_5, X_372, 5, 372, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A -  pi  /4)', ID="X_371", classes=["center", "incident"])
    central_line(model, X_30, X_371, 30, 371, incident=True)
    return promote_point_to_top(model, X_3070)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3070 on the given reference triangle."""
    model = create_model('X_3070 = INTERSECTION OF X_4X_6 AND X_5X_372')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03070(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03070.json"))
    write_center_svg(
        model_acute,
        here / "x-03070.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

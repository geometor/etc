"""GEOMETOR construction model for X_3093 = INTERSECTION OF LINES X_2X_1578 AND X_4X_6."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03093(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3093 = INTERSECTION OF LINES X_2X_1578 AND X_4X_6 on reference triangle ABC."""
    X_3093 = eval_trilinear_point(model, A, B, C, '(sin(A) - sec(A))', ID="X_3093", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A +  pi  /4)', ID="X_372", classes=["center", "incident"])
    central_line(model, X_25, X_372, 25, 372, incident=True)
    X_235 = eval_trilinear_point(model, A, B, C, 'sec(A) - cos(B - C)', ID="X_235", classes=["center", "incident"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A +  pi  /4)', ID="X_486", classes=["center", "incident"])
    central_line(model, X_235, X_486, 235, 486, incident=True)
    return promote_point_to_top(model, X_3093)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3093 on the given reference triangle."""
    model = create_model('X_3093 = INTERSECTION OF LINES X_2X_1578 AND X_4X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03093(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03093.json"))
    write_center_svg(
        model_acute,
        here / "x-03093.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

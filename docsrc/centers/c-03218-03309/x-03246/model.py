"""GEOMETOR construction model for X_3246 = MIDPOINT OF X_1 AND X_44."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03246(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3246 = MIDPOINT OF X_1 AND X_44 on reference triangle ABC."""
    X_3246 = eval_trilinear_point(model, A, B, C, '4*a**(2) + b**(2) + c**(2) - 4*b*c - c*a - a*b', ID="X_3246", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_88, X_105, 88, 105, incident=True)
    X_678 = eval_trilinear_point(model, A, B, C, '((b + c - 2*a)**(2))', ID="X_678", classes=["center", "incident"])
    X_899 = eval_trilinear_point(model, A, B, C, '1/b + 1/c - 2/a', ID="X_899", classes=["center", "incident"])
    central_line(model, X_678, X_899, 678, 899, incident=True)
    return promote_point_to_top(model, X_3246)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3246 on the given reference triangle."""
    model = create_model('X_3246 = MIDPOINT OF X_1 AND X_44')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03246(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03246.json"))
    write_center_svg(
        model_acute,
        here / "x-03246.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

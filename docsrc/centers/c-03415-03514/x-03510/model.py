"""GEOMETOR construction model for X_3510 = INTERSECTION OF LINES X_1X_76 AND X_6X_43."""

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


def construct_x_03510(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3510 = INTERSECTION OF LINES X_1X_76 AND X_6X_43 on reference triangle ABC."""
    X_3510 = eval_trilinear_point(model, A, B, C, '(b**(3)*c**(3) - a**(3)*b**(3) - a**(3)*c**(3) + a**(2)*b**(2)*c**(2))', ID="X_3510", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    central_line(model, X_6, X_43, 6, 43, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_1, X_76, 1, 76, incident=True)
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X_291", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_291, X_511, 291, 511, incident=True)
    return promote_point_to_top(model, X_3510)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3510 on the given reference triangle."""
    model = create_model('X_3510 = INTERSECTION OF LINES X_1X_76 AND X_6X_43')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03510(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03510.json"))
    write_center_svg(
        model_acute,
        here / "x-03510.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

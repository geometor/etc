"""GEOMETOR construction model for X_1027 = INTERSECTION OF LINES X_1X_514 AND X_6X_513."""

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
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01027(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1027 = INTERSECTION OF LINES X_1X_514 AND X_6X_513 on reference triangle ABC."""
    X_1026 = eval_trilinear_point(model, A, B, C, '((b**(2) + c**(2) - a*(b + c))/(b - c))', ID="X_1026", classes=["center"])
    X_1027 = isogonal_conjugate(model, A, B, C, X_1026, ID="X_1027", classes=["selected", "target"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    central_line(model, X_105, X_106, 105, 106, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_1, X_514, 1, 514, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_6, X_513, 6, 513, incident=True)
    return promote_point_to_top(model, X_1027)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1027 on the given reference triangle."""
    model = create_model('X_1027 = INTERSECTION OF LINES X_1X_514 AND X_6X_513')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01027(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01027.json"))
    write_center_svg(
        model_acute,
        here / "x-01027.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

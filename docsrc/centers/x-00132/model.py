"""GEOMETOR construction model for X(132) = X(2)X(107)∩X(4)X(32)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00132(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(132) = X(2)X(107)∩X(4)X(32) on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X(112)", classes=["center"])
    X_132 = midpoint(model, X_4, X_112, ID="X(132)", classes=["selected", "target"], guide=False)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    central_line(model, X_4, X_32, 4, 32, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X(107)", classes=["center", "incident"])
    central_line(model, X_2, X_107, 2, 107, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X(127)", classes=["center", "incident"])
    central_line(model, X_5, X_127, 5, 127, incident=True)
    return promote_point_to_top(model, X_132)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(132) on the given reference triangle."""
    model = create_model('X(132) = X(2)X(107)∩X(4)X(32)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00132(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00132.json"))
    write_center_svg(
        model_acute,
        here / "x-00132.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X(605) = INTERSECTION OF LINES X(371)X(602) AND X(372)X(601)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00605(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(605) = INTERSECTION OF LINES X(371)X(602) AND X(372)X(601) on reference triangle ABC."""
    X_605 = eval_trilinear_point(model, A, B, C, 'a*(1 + sin(A))', ID="X(605)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    central_line(model, X_6, X_31, 6, 31, incident=True)
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A - pi /4)', ID="X(371)", classes=["center", "incident"])
    X_602 = point_from_barycentrics(model, A, B, C, -0.21701389, 0.18844697, 1.0285669, ID="X(602)", classes=["center", "incident"])
    central_line(model, X_371, X_602, 371, 602, incident=True)
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A + pi /4)', ID="X(372)", classes=["center", "incident"])
    X_601 = point_from_barycentrics(model, A, B, C, 0.2783439, 0.34624094, 0.37541516, ID="X(601)", classes=["center", "incident"])
    central_line(model, X_372, X_601, 372, 601, incident=True)
    return promote_point_to_top(model, X_605)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(605) on the given reference triangle."""
    model = create_model('X(605) = INTERSECTION OF LINES X(371)X(602) AND X(372)X(601)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00605(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00605.json"))
    write_center_svg(
        model_acute,
        here / "x-00605.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

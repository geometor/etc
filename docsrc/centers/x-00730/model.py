"""GEOMETOR construction model for X(730) = EVEN (- 2, 1) INFINITY POINT."""

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
    intersect_lines,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00730(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(730) = EVEN (- 2, 1) INFINITY POINT on reference triangle ABC."""
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center"])
    central_line(model, X_10, X_39, 10, 39)
    central_line(model, X_1, X_76, 1, 76)
    X_730 = intersect_lines(model, X_10, X_39, X_1, X_76, ID="X(730)", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X(194)", classes=["center", "incident"])
    central_line(model, X_8, X_194, 8, 194, incident=True)
    return promote_point_to_top(model, X_730)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(730) on the given reference triangle."""
    model = create_model('X(730) = EVEN (- 2, 1) INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00730(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00730.json"))
    write_center_svg(
        model_acute,
        here / "x-00730.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

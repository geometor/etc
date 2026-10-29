"""GEOMETOR construction model for X(639) = COMPLEMENT OF X(371)."""

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
    intersect_lines,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00639(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(639) = COMPLEMENT OF X(371) on reference triangle ABC."""
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A - pi /4)', ID="X(371)", classes=["center"])
    central_line(model, X_5, X_141, 5, 141)
    central_line(model, X_2, X_371, 2, 371)
    X_639 = intersect_lines(model, X_5, X_141, X_2, X_371, ID="X(639)", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A - pi /4)', ID="X(485)", classes=["center", "incident"])
    central_line(model, X_69, X_485, 69, 485, incident=True)
    return promote_point_to_top(model, X_639)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(639) on the given reference triangle."""
    model = create_model('X(639) = COMPLEMENT OF X(371)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00639(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00639.json"))
    write_center_svg(
        model_acute,
        here / "x-00639.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

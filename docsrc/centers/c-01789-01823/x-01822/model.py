"""GEOMETOR construction model for X_1822 = ISOGONAL CONJUGATE OF X_2588."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01822(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1822 = ISOGONAL CONJUGATE OF X_2588 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center"])
    X_1113 = eval_trilinear_point(model, A, B, C, '(R - d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1113", classes=["center"])
    central_line(model, X_1, X_21, 1, 21)
    central_line(model, X_109, X_1113, 109, 1113)
    X_1822 = intersect_lines(model, X_1, X_21, X_109, X_1113, ID="X_1822", classes=["selected", "target"])
    return promote_point_to_top(model, X_1822)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1822 on the given reference triangle."""
    model = create_model('X_1822 = ISOGONAL CONJUGATE OF X_2588')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01822(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01822.json"))
    write_center_svg(
        model_acute,
        here / "x-01822.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

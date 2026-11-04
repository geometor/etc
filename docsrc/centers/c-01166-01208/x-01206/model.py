"""GEOMETOR construction model for X_1206 = 3rd SARAGOSSA POINT OF X_81."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01206(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1206 = 3rd SARAGOSSA POINT OF X_81 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center"])
    central_line(model, X_6, X_31, 6, 31)
    central_line(model, X_81, X_239, 81, 239)
    X_1206 = intersect_lines(model, X_6, X_31, X_81, X_239, ID="X_1206", classes=["selected", "target"])
    return promote_point_to_top(model, X_1206)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1206 on the given reference triangle."""
    model = create_model('X_1206 = 3rd SARAGOSSA POINT OF X_81')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01206(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01206.json"))
    write_center_svg(
        model_acute,
        here / "x-01206.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

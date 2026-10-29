"""GEOMETOR construction model for X(52) = ORTHOCENTER OF ORTHIC TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    orthic_triangle,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00052(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(52) = ORTHOCENTER OF ORTHIC TRIANGLE on reference triangle ABC."""
    orthic_triangle(model, A, B, C)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center"])
    central_line(model, X_5, X_51, 5, 51)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X(68)", classes=["center"])
    central_line(model, X_4, X_68, 4, 68)
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X(52)", classes=["selected", "target"])
    return promote_point_to_top(model, X_52)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(52) on the given reference triangle."""
    model = create_model('X(52) = ORTHOCENTER OF ORTHIC TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00052(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00052.json"))
    write_center_svg(
        model_acute,
        here / "x-00052.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

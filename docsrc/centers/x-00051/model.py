"""GEOMETOR construction model for X(51) = CENTROID OF ORTHIC TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    orthic_triangle,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00051(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(51) = CENTROID OF ORTHIC TRIANGLE on reference triangle ABC."""
    orthic_triangle(model, A, B, C)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center"])
    central_line(model, X_6, X_25, 6, 25)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X(52)", classes=["center"])
    central_line(model, X_5, X_52, 5, 52)
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["selected", "target"])
    return promote_point_to_top(model, X_51)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(51) on the given reference triangle."""
    model = create_model('X(51) = CENTROID OF ORTHIC TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00051(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00051.json"))
    write_center_svg(
        model_acute,
        here / "x-00051.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

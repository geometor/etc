"""GEOMETOR construction model for X(53) = SYMMEDIAN POINT OF ORTHIC TRIANGLE."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00053(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(53) = SYMMEDIAN POINT OF ORTHIC TRIANGLE on reference triangle ABC."""
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X(53)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_157 = point_from_barycentrics(model, A, B, C, 0.22698945, 0.13751531, 0.63549524, ID="X(157)", classes=["center", "incident"])
    central_line(model, X_25, X_157, 25, 157, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X(216)", classes=["center", "incident"])
    central_line(model, X_5, X_216, 5, 216, incident=True)
    return promote_point_to_top(model, X_53)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(53) on the given reference triangle."""
    model = create_model('X(53) = SYMMEDIAN POINT OF ORTHIC TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00053(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00053.json"))
    write_center_svg(
        model_acute,
        here / "x-00053.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

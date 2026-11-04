"""GEOMETOR construction model for X_1253 = ISOGONAL CONJUGATE OF X_1088."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01253(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1253 = ISOGONAL CONJUGATE OF X_1088 on reference triangle ABC."""
    X_1088 = eval_trilinear_point(model, A, B, C, '(sec(A/2))**(4)', ID="X_1088", classes=["center"])
    X_1253 = isogonal_conjugate(model, A, B, C, X_1088, ID="X_1253", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_6, X_31, 6, 31, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center", "incident"])
    central_line(model, X_35, X_255, 35, 255, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_294 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b**(2) + c**(2) - a*b - a*c))', ID="X_294", classes=["center", "incident"])
    central_line(model, X_9, X_294, 9, 294, incident=True)
    return promote_point_to_top(model, X_1253)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1253 on the given reference triangle."""
    model = create_model('X_1253 = ISOGONAL CONJUGATE OF X_1088')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01253(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01253.json"))
    write_center_svg(
        model_acute,
        here / "x-01253.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

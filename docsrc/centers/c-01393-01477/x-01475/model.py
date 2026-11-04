"""GEOMETOR construction model for X_1475 = X_1212-BETH CONJUGATE OF X_1212."""

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


def construct_x_01475(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1475 = X_1212-BETH CONJUGATE OF X_1212 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center"])
    central_line(model, X_6, X_41, 6, 41)
    central_line(model, X_39, X_42, 39, 42)
    X_1475 = intersect_lines(model, X_6, X_41, X_39, X_42, ID="X_1475", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    central_line(model, X_58, X_163, 58, 163, incident=True)
    return promote_point_to_top(model, X_1475)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1475 on the given reference triangle."""
    model = create_model('X_1475 = X_1212-BETH CONJUGATE OF X_1212')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01475(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01475.json"))
    write_center_svg(
        model_acute,
        here / "x-01475.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

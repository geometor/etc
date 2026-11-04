"""GEOMETOR construction model for X_1438 = X_294-BETH CONJUGATE OF X_294."""

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


def construct_x_01438(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1438 = X_294-BETH CONJUGATE OF X_294 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    central_line(model, X_1, X_41, 1, 41)
    central_line(model, X_32, X_56, 32, 56)
    X_1438 = intersect_lines(model, X_1, X_41, X_32, X_56, ID="X_1438", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    central_line(model, X_58, X_163, 58, 163, incident=True)
    return promote_point_to_top(model, X_1438)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1438 on the given reference triangle."""
    model = create_model('X_1438 = X_294-BETH CONJUGATE OF X_294')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01438(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01438.json"))
    write_center_svg(
        model_acute,
        here / "x-01438.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

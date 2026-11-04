"""GEOMETOR construction model for X_2317 = X_2-ISOCONJUGATE OF X_1389."""

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


def construct_x_02317(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2317 = X_2-ISOCONJUGATE OF X_1389 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center"])
    central_line(model, X_6, X_41, 6, 41)
    central_line(model, X_54, X_71, 54, 71)
    X_2317 = intersect_lines(model, X_6, X_41, X_54, X_71, ID="X_2317", classes=["selected", "target"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    central_line(model, X_163, X_284, 163, 284, incident=True)
    return promote_point_to_top(model, X_2317)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2317 on the given reference triangle."""
    model = create_model('X_2317 = X_2-ISOCONJUGATE OF X_1389')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02317(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02317.json"))
    write_center_svg(
        model_acute,
        here / "x-02317.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

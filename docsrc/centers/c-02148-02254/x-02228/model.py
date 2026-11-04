"""GEOMETOR construction model for X_2228 = X_2-ISOCONJUGATE OF X_713."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02228(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2228 = X_2-ISOCONJUGATE OF X_713 on reference triangle ABC."""
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    central_line(model, X_10, X_75, 10, 75)
    central_line(model, X_44, X_513, 44, 513)
    X_2228 = intersect_lines(model, X_10, X_75, X_44, X_513, ID="X_2228", classes=["selected", "target"])
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X_291", classes=["center", "incident"])
    X_320 = eval_trilinear_point(model, A, B, C, '(1 - 2*cos(A))/a**(2)', ID="X_320", classes=["center", "incident"])
    central_line(model, X_291, X_320, 291, 320, incident=True)
    return promote_point_to_top(model, X_2228)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2228 on the given reference triangle."""
    model = create_model('X_2228 = X_2-ISOCONJUGATE OF X_713')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02228(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02228.json"))
    write_center_svg(
        model_acute,
        here / "x-02228.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

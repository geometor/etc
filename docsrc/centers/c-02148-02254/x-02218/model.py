"""GEOMETOR construction model for X_2218 = X_2-ISOCONJUGATE OF X_579."""

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


def construct_x_02218(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2218 = X_2-ISOCONJUGATE OF X_579 on reference triangle ABC."""
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    central_line(model, X_10, X_55, 10, 55)
    central_line(model, X_37, X_41, 37, 41)
    X_2218 = intersect_lines(model, X_10, X_55, X_37, X_41, ID="X_2218", classes=["selected", "target"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_21, X_75, 21, 75, incident=True)
    return promote_point_to_top(model, X_2218)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2218 on the given reference triangle."""
    model = create_model('X_2218 = X_2-ISOCONJUGATE OF X_579')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02218(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02218.json"))
    write_center_svg(
        model_acute,
        here / "x-02218.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

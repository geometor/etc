"""GEOMETOR construction model for X_1101 = TRILINEAR SQUARE OF X_110."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01101(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1101 = TRILINEAR SQUARE OF X_110 on reference triangle ABC."""
    X_1101 = eval_trilinear_point(model, A, B, C, '((csc(B - C))**(2))', ID="X_1101", classes=["selected", "target"])
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X_59", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_59, X_60, 59, 60, incident=True)
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    X_798 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))', ID="X_798", classes=["center", "incident"])
    central_line(model, X_163, X_798, 163, 798, incident=True)
    X_656 = eval_trilinear_point(model, A, B, C, 'tan(B) - tan(C)', ID="X_656", classes=["center", "incident"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X_662", classes=["center", "incident"])
    central_line(model, X_656, X_662, 656, 662, incident=True)
    return promote_point_to_top(model, X_1101)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1101 on the given reference triangle."""
    model = create_model('X_1101 = TRILINEAR SQUARE OF X_110')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01101(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01101.json"))
    write_center_svg(
        model_acute,
        here / "x-01101.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

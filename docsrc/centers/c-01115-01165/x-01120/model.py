"""GEOMETOR construction model for X_1120 = X_2-BLAIKIE TRANSFORM OF X_1."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01120(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1120 = X_2-BLAIKIE TRANSFORM OF X_1 on reference triangle ABC."""
    X_1120 = eval_trilinear_point(model, A, B, C, '(b*c/(b**(2) + c**(2) + b*a + c*a - 4*b*c))', ID="X_1120", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_56, X_100, 56, 100, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_106, X_519, 106, 519, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_644 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b - c))', ID="X_644", classes=["center", "incident"])
    central_line(model, X_6, X_644, 6, 644, incident=True)
    return promote_point_to_top(model, X_1120)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1120 on the given reference triangle."""
    model = create_model('X_1120 = X_2-BLAIKIE TRANSFORM OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01120(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01120.json"))
    write_center_svg(
        model_acute,
        here / "x-01120.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

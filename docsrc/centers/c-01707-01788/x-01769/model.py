"""GEOMETOR construction model for X_1769 = MIMOSA TRANSFORM OF X_901."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01769(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1769 = MIMOSA TRANSFORM OF X_901 on reference triangle ABC."""
    X_1769 = eval_trilinear_point(model, A, B, C, '(b - c)*(a**(2)*(b + c) - 2*a*b*c - (b - c)**(2)*(b + c))', ID="X_1769", classes=["selected", "target"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    central_line(model, X_104, X_106, 104, 106, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_108, X_109, 108, 109, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_11, X_244, 11, 244, incident=True)
    return promote_point_to_top(model, X_1769)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1769 on the given reference triangle."""
    model = create_model('X_1769 = MIMOSA TRANSFORM OF X_901')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01769(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01769.json"))
    write_center_svg(
        model_acute,
        here / "x-01769.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

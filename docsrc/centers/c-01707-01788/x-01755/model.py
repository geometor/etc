"""GEOMETOR construction model for X_1755 = MIMOSA TRANSFORM OF X_287."""

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


def construct_x_01755(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1755 = MIMOSA TRANSFORM OF X_287 on reference triangle ABC."""
    X_1755 = eval_trilinear_point(model, A, B, C, 'a*cos(A + omega )', ID="X_1755", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    central_line(model, X_19, X_27, 19, 27, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_31, X_48, 31, 48, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    return promote_point_to_top(model, X_1755)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1755 on the given reference triangle."""
    model = create_model('X_1755 = MIMOSA TRANSFORM OF X_287')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01755(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01755.json"))
    write_center_svg(
        model_acute,
        here / "x-01755.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

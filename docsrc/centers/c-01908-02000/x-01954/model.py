"""GEOMETOR construction model for X_1954 = CROSSSUM OF PU(21)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01954(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1954 = CROSSSUM OF PU(21) on reference triangle ABC."""
    X_1954 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) + (sin(2*A))**(2))', ID="X_1954", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    X_1955 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))', ID="X_1955", classes=["center", "incident"])
    central_line(model, X_92, X_1955, 92, 1955, incident=True)
    return promote_point_to_top(model, X_1954)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1954 on the given reference triangle."""
    model = create_model('X_1954 = CROSSSUM OF PU(21)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01954(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01954.json"))
    write_center_svg(
        model_acute,
        here / "x-01954.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

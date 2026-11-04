"""GEOMETOR construction model for X_1956 = TRILINEAR POLE OF PU(21)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01956(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1956 = TRILINEAR POLE OF PU(21) on reference triangle ABC."""
    X_1955 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))', ID="X_1955", classes=["center"])
    X_1956 = isogonal_conjugate(model, A, B, C, X_1955, ID="X_1956", classes=["selected", "target"])
    X_293 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(A +  omega  )', ID="X_293", classes=["center", "incident"])
    X_1755 = eval_trilinear_point(model, A, B, C, 'a*cos(A +  omega  )', ID="X_1755", classes=["center", "incident"])
    central_line(model, X_293, X_1755, 293, 1755, incident=True)
    return promote_point_to_top(model, X_1956)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1956 on the given reference triangle."""
    model = create_model('X_1956 = TRILINEAR POLE OF PU(21)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01956(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01956.json"))
    write_center_svg(
        model_acute,
        here / "x-01956.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

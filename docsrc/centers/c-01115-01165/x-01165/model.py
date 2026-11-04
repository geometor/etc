"""GEOMETOR construction model for X_1165 = POINT ALTAIS."""

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


def construct_x_01165(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1165 = POINT ALTAIS on reference triangle ABC."""
    X_1165 = eval_trilinear_point(model, A, B, C, '(( area - a**(2))*(2*area + b**(2) + c**(2))/(a*(b**(2) + c**(2) - a**(2))))', ID="X_1165", classes=["selected", "target"])
    X_468 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cot(B) + cot(C) - 2*cot(A))', ID="X_468", classes=["center", "incident"])
    X_1164 = eval_trilinear_point(model, A, B, C, '(( area + a**(2))*(2*area - b**(2) - c**(2))/(a*(b**(2) + c**(2) - a**(2))))', ID="X_1164", classes=["center", "incident"])
    central_line(model, X_468, X_1164, 468, 1164, incident=True)
    return promote_point_to_top(model, X_1165)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1165 on the given reference triangle."""
    model = create_model('X_1165 = POINT ALTAIS')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01165(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01165.json"))
    write_center_svg(
        model_acute,
        here / "x-01165.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

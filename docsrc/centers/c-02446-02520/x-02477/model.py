"""GEOMETOR construction model for X_2477 = EXSIMILICENTER{INCIRCLE, SINE-TRIPLE-ANGLE CIRCLE}."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02477(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2477 = EXSIMILICENTER{INCIRCLE, SINE-TRIPLE-ANGLE CIRCLE} on reference triangle ABC."""
    X_2477 = eval_trilinear_point(model, A, B, C, '(a**(3)*(a**(2) - b**(2) - c**(2) - b*c)**(2)/(b + c - a))', ID="X_2477", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    central_line(model, X_1, X_49, 1, 49, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_11, X_54, 11, 54, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_12, X_110, 12, 110, incident=True)
    return promote_point_to_top(model, X_2477)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2477 on the given reference triangle."""
    model = create_model('X_2477 = EXSIMILICENTER{INCIRCLE, SINE-TRIPLE-ANGLE CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02477(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02477.json"))
    write_center_svg(
        model_acute,
        here / "x-02477.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

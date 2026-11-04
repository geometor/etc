"""GEOMETOR construction model for X_2611 = DIFFERENCE OF PU(71)."""

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
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02611(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2611 = DIFFERENCE OF PU(71) on reference triangle ABC."""
    X_1109 = eval_trilinear_point(model, A, B, C, '(sin(B - C))**(2)', ID="X_1109", classes=["center"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center"])
    X_2611 = reflection_in_point(model, X_1109, X_11, ID="X_2611", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_1, X_60, 1, 60, incident=True)
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_11, X_523, 11, 523, incident=True)
    X_2594 = eval_trilinear_point(model, A, B, C, '(cos(C- A) + cos(B - A))', ID="X_2594", classes=["center", "incident"])
    X_2599 = eval_trilinear_point(model, A, B, C, 'sec(C- A) + sec(B - A)', ID="X_2599", classes=["center", "incident"])
    central_line(model, X_2594, X_2599, 2594, 2599, incident=True)
    return promote_point_to_top(model, X_2611)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2611 on the given reference triangle."""
    model = create_model('X_2611 = DIFFERENCE OF PU(71)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02611(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02611.json"))
    write_center_svg(
        model_acute,
        here / "x-02611.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

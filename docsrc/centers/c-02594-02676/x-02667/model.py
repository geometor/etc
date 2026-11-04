"""GEOMETOR construction model for X_2667 = SUM OF PU(85)."""

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


def construct_x_02667(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2667 = SUM OF PU(85) on reference triangle ABC."""
    X_2667 = eval_trilinear_point(model, A, B, C, 'c*a/(c + a) + b*a/(b + a)', ID="X_2667", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_1, X_75, 1, 75, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    central_line(model, X_37, X_42, 37, 42, incident=True)
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X_192", classes=["center", "incident"])
    X_714 = eval_trilinear_point(model, A, B, C, '(a **(-4)*(b **(-1) + c **(-1)) - a **(-2)*(b **(-3) + c **(-3)))', ID="X_714", classes=["center", "incident"])
    central_line(model, X_192, X_714, 192, 714, incident=True)
    return promote_point_to_top(model, X_2667)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2667 on the given reference triangle."""
    model = create_model('X_2667 = SUM OF PU(85)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02667(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02667.json"))
    write_center_svg(
        model_acute,
        here / "x-02667.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

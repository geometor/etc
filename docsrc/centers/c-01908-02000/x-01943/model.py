"""GEOMETOR construction model for X_1943 = CROSSSUM OF PU(18)."""

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


def construct_x_01943(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1943 = CROSSSUM OF PU(18) on reference triangle ABC."""
    X_1943 = eval_trilinear_point(model, A, B, C, '(b*c*((cos(A))**(2) + cos(B)*cos(C)))', ID="X_1943", classes=["selected", "target"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    central_line(model, X_57, X_239, 57, 239, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_222 = eval_trilinear_point(model, A, B, C, 'cos(A)*tan(A/2)', ID="X_222", classes=["center", "incident"])
    central_line(model, X_75, X_222, 75, 222, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_278 = eval_trilinear_point(model, A, B, C, 'sec(A)*tan(A/2)', ID="X_278", classes=["center", "incident"])
    central_line(model, X_69, X_278, 69, 278, incident=True)
    return promote_point_to_top(model, X_1943)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1943 on the given reference triangle."""
    model = create_model('X_1943 = CROSSSUM OF PU(18)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01943(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01943.json"))
    write_center_svg(
        model_acute,
        here / "x-01943.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

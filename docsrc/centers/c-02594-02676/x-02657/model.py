"""GEOMETOR construction model for X_2657 = MIDPOINT OF PU(82)."""

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


def construct_x_02657(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2657 = MIDPOINT OF PU(82) on reference triangle ABC."""
    X_2657 = eval_trilinear_point(model, A, B, C, '((a*(sec(B) + sec(A)) + b*(sec(C) + sec(B)) + c*(sec(A) + sec(C)))*(sec(C) + sec(A)) + (a*(sec(C) + sec(A)) + b*(sec(A) + sec(B)) + c*(sec(B) + sec(C)))*(sec(B) + sec(A)))', ID="X_2657", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_2190 = eval_trilinear_point(model, A, B, C, 'sec(A)*sec(B - C)', ID="X_2190", classes=["center", "incident"])
    central_line(model, X_37, X_2190, 37, 2190, incident=True)
    X_652 = eval_trilinear_point(model, A, B, C, 'sec(B) - sec(C)', ID="X_652", classes=["center", "incident"])
    X_2654 = eval_trilinear_point(model, A, B, C, '2*sec(A) + sec(B) + sec(C)', ID="X_2654", classes=["center", "incident"])
    central_line(model, X_652, X_2654, 652, 2654, incident=True)
    return promote_point_to_top(model, X_2657)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2657 on the given reference triangle."""
    model = create_model('X_2657 = MIDPOINT OF PU(82)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02657(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02657.json"))
    write_center_svg(
        model_acute,
        here / "x-02657.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

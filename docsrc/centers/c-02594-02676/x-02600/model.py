"""GEOMETOR construction model for X_2600 = DIFFERENCE OF PU(69)."""

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


def construct_x_02600(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2600 = DIFFERENCE OF PU(69) on reference triangle ABC."""
    X_2600 = eval_trilinear_point(model, A, B, C, '(sec(C- A) - sec(B - A))', ID="X_2600", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_2599 = eval_trilinear_point(model, A, B, C, 'sec(C- A) + sec(B - A)', ID="X_2599", classes=["center", "incident"])
    X_2604 = eval_trilinear_point(model, A, B, C, '((a*sec(B - A) + b*sec(C - B) + c*sec(A - C))*sec(C - A) + (a*sec(C - A) + b*sec(A - B) + c*sec(B - C))*sec(B - A))', ID="X_2604", classes=["center", "incident"])
    central_line(model, X_2599, X_2604, 2599, 2604, incident=True)
    return promote_point_to_top(model, X_2600)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2600 on the given reference triangle."""
    model = create_model('X_2600 = DIFFERENCE OF PU(69)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02600(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02600.json"))
    write_center_svg(
        model_acute,
        here / "x-02600.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

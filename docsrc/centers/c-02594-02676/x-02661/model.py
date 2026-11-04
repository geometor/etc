"""GEOMETOR construction model for X_2661 = MIDPOINT OF PU(83)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02661(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2661 = MIDPOINT OF PU(83) on reference triangle ABC."""
    X_2661 = eval_trilinear_point(model, A, B, C, '((a/(sec(B) + sec(A)) + b/(sec(C) + sec(B)) + c/(sec(A) + sec(C)))/(sec(C) + sec(A)) + (a/(sec(C) + sec(A)) + b/(sec(A) + sec(B)) + c/(sec(B) + sec(C)))/(sec(B) + sec(A)))', ID="X_2661", classes=["selected", "target"])
    X_822 = eval_trilinear_point(model, A, B, C, '(sec(B))**(2) - (sec(C))**(2)', ID="X_822", classes=["center", "incident"])
    X_2658 = point_from_barycentrics(model, A, B, C, 0.32414957, 0.38052829, 0.29532214, ID="X_2658", classes=["center", "incident"])
    central_line(model, X_822, X_2658, 822, 2658, incident=True)
    return promote_point_to_top(model, X_2661)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2661 on the given reference triangle."""
    model = create_model('X_2661 = MIDPOINT OF PU(83)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02661(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02661.json"))
    write_center_svg(
        model_acute,
        here / "x-02661.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

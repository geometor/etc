"""GEOMETOR construction model for X_2719 = SR(X_100, X_107)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02719(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2719 = SR(X_100, X_107) on reference triangle ABC."""
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X_520", classes=["center"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    central_line(model, X_100, X_520, 100, 520)
    central_line(model, X_107, X_513, 107, 513)
    X_2719 = intersect_lines(model, X_100, X_520, X_107, X_513, ID="X_2719", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_822 = eval_trilinear_point(model, A, B, C, '(sec(B))**(2) - (sec(C))**(2)', ID="X_822", classes=["center", "incident"])
    central_line(model, X_101, X_822, 101, 822, incident=True)
    return promote_point_to_top(model, X_2719)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2719 on the given reference triangle."""
    model = create_model('X_2719 = SR(X_100, X_107)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02719(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02719.json"))
    write_center_svg(
        model_acute,
        here / "x-02719.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

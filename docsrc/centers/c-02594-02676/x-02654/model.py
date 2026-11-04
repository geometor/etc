"""GEOMETOR construction model for X_2654 = SUM OF PU(82)."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02654(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2654 = SUM OF PU(82) on reference triangle ABC."""
    X_2654 = eval_trilinear_point(model, A, B, C, '2*sec(A) + sec(B) + sec(C)', ID="X_2654", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_212 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(A))', ID="X_212", classes=["center", "incident"])
    X_405 = eval_trilinear_point(model, A, B, C, 'b*c*(a + b + c) + a*b*c*cos(A)', ID="X_405", classes=["center", "incident"])
    central_line(model, X_212, X_405, 212, 405, incident=True)
    X_201 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(B - C))', ID="X_201", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_201, X_517, 201, 517, incident=True)
    return promote_point_to_top(model, X_2654)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2654 on the given reference triangle."""
    model = create_model('X_2654 = SUM OF PU(82)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02654(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02654.json"))
    write_center_svg(
        model_acute,
        here / "x-02654.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

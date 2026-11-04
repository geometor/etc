"""GEOMETOR construction model for X_2643 = DIFFERENCE OF PU(79)."""

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


def construct_x_02643(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2643 = DIFFERENCE OF PU(79) on reference triangle ABC."""
    X_2643 = eval_trilinear_point(model, A, B, C, '1/(cot(C) - cot(A)) - 1/(cot(B) - cot(A))', ID="X_2643", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_560 = eval_trilinear_point(model, A, B, C, 'a**(4)', ID="X_560", classes=["center", "incident"])
    central_line(model, X_19, X_560, 19, 560, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X_662", classes=["center", "incident"])
    central_line(model, X_1, X_662, 1, 662, incident=True)
    X_267 = eval_trilinear_point(model, A, B, C, '1/(b**(3) + c**(3) - a**(3) + (b + c - a)*(b*c + c*a + a*b))', ID="X_267", classes=["center", "incident"])
    X_849 = eval_trilinear_point(model, A, B, C, '(a/(b + c))**(2)', ID="X_849", classes=["center", "incident"])
    central_line(model, X_267, X_849, 267, 849, incident=True)
    return promote_point_to_top(model, X_2643)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2643 on the given reference triangle."""
    model = create_model('X_2643 = DIFFERENCE OF PU(79)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02643(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02643.json"))
    write_center_svg(
        model_acute,
        here / "x-02643.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_2091 = 2nd STEVANOVIC PERSPECTOR."""

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


def construct_x_02091(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2091 = 2nd STEVANOVIC PERSPECTOR on reference triangle ABC."""
    X_2091 = eval_trilinear_point(model, A, B, C, '((1/(b + c - a))*(sin(B/2) + sin(C/2))*sec(A/2))', ID="X_2091", classes=["selected", "target"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_173 = eval_trilinear_point(model, A, B, C, 'cos(B/2) + cos(C/2) - cos(A/2)', ID="X_173", classes=["center", "incident"])
    central_line(model, X_57, X_173, 57, 173, incident=True)
    return promote_point_to_top(model, X_2091)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2091 on the given reference triangle."""
    model = create_model('X_2091 = 2nd STEVANOVIC PERSPECTOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02091(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02091.json"))
    write_center_svg(
        model_acute,
        here / "x-02091.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

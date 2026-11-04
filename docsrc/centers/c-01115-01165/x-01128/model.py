"""GEOMETOR construction model for X_1128 = 2nd DE VILLIERS POINT."""

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


def construct_x_01128(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1128 = 2nd DE VILLIERS POINT on reference triangle ABC."""
    X_1128 = eval_trilinear_point(model, A, B, C, '((sin(( pi  - A)/4))/sin(( pi  + 3*A)/4))', ID="X_1128", classes=["selected", "target"])
    X_164 = eval_trilinear_point(model, A, B, C, 'sin(B/2) + sin(C/2) - sin(A/2)', ID="X_164", classes=["center", "incident"])
    X_173 = eval_trilinear_point(model, A, B, C, 'cos(B/2) + cos(C/2) - cos(A/2)', ID="X_173", classes=["center", "incident"])
    central_line(model, X_164, X_173, 164, 173, incident=True)
    X_188 = eval_trilinear_point(model, A, B, C, 'csc(A/2)', ID="X_188", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_188, X_519, 188, 519, incident=True)
    X_258 = eval_trilinear_point(model, A, B, C, '1/(cos(B/2) + cos(C/2) - cos(A/2))', ID="X_258", classes=["center", "incident"])
    X_505 = eval_trilinear_point(model, A, B, C, '(1/(sin(B/2) + sin(C/2) - sin(A/2)))', ID="X_505", classes=["center", "incident"])
    central_line(model, X_258, X_505, 258, 505, incident=True)
    return promote_point_to_top(model, X_1128)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1128 on the given reference triangle."""
    model = create_model('X_1128 = 2nd DE VILLIERS POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01128(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01128.json"))
    write_center_svg(
        model_acute,
        here / "x-01128.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

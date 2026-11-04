"""GEOMETOR construction model for X_2290 = X_2-ISOCONJUGATE OF X_1141."""

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


def construct_x_02290(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2290 = X_2-ISOCONJUGATE OF X_1141 on reference triangle ABC."""
    X_2290 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*cos(B - C)', ID="X_2290", classes=["selected", "target"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_47, X_48, 47, 48, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X_50", classes=["center", "incident"])
    X_1399 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(2*A))', ID="X_1399", classes=["center", "incident"])
    central_line(model, X_50, X_1399, 50, 1399, incident=True)
    return promote_point_to_top(model, X_2290)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2290 on the given reference triangle."""
    model = create_model('X_2290 = X_2-ISOCONJUGATE OF X_1141')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02290(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02290.json"))
    write_center_svg(
        model_acute,
        here / "x-02290.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

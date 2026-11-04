"""GEOMETOR construction model for X_2222 = X_2-ISOCONJUGATE OF X_654."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02222(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2222 = X_2-ISOCONJUGATE OF X_654 on reference triangle ABC."""
    X_2222 = eval_barycentric_point(model, A, B, C, 'a*(a - b)*(a - c)*(a - b + c)*(a + b - c)*(a**(2) - b**(2) + c**(2) - a*c)*(a**(2) - c**(2) + b**(2) - a*b)', ID="X_2222", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_36, X_80, 36, 80, incident=True)
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X_59", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_59, X_110, 59, 110, incident=True)
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center", "incident"])
    central_line(model, X_74, X_484, 74, 484, incident=True)
    return promote_point_to_top(model, X_2222)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2222 on the given reference triangle."""
    model = create_model('X_2222 = X_2-ISOCONJUGATE OF X_654')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02222(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02222.json"))
    write_center_svg(
        model_acute,
        here / "x-02222.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

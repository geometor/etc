"""GEOMETOR construction model for X(337) = ISOTOMIC CONJUGATE OF X(242)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00337(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(337) = ISOTOMIC CONJUGATE OF X(242) on reference triangle ABC."""
    X_242 = point_from_barycentrics(model, A, B, C, -0.21362434, 0.01984127, 1.1937831, ID="X(242)", classes=["center"])
    X_337 = isotomic_conjugate(model, A, B, C, X_242, ID="X(337)", classes=["selected", "target"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X(85)", classes=["center", "incident"])
    central_line(model, X_12, X_85, 12, 85, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X(86)", classes=["center", "incident"])
    central_line(model, X_37, X_86, 37, 86, incident=True)
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X(72)", classes=["center", "incident"])
    X_295 = eval_trilinear_point(model, A, B, C, '(cos(A))/(a**(2) - b*c)', ID="X(295)", classes=["center", "incident"])
    central_line(model, X_72, X_295, 72, 295, incident=True)
    return promote_point_to_top(model, X_337)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(337) on the given reference triangle."""
    model = create_model('X(337) = ISOTOMIC CONJUGATE OF X(242)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00337(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00337.json"))
    write_center_svg(
        model_acute,
        here / "x-00337.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

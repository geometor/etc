"""GEOMETOR construction model for X(943) = ISOGONAL CONJUGATE OF X(942)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00943(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(943) = ISOGONAL CONJUGATE OF X(942) on reference triangle ABC."""
    X_942 = eval_trilinear_point(model, A, B, C, '2*a*b*c + (b + c)*(a - b + c)*(a + b -c)', ID="X(942)", classes=["center"])
    X_943 = isogonal_conjugate(model, A, B, C, X_942, ID="X(943)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_3, X_7, 3, 7, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center", "incident"])
    central_line(model, X_4, X_12, 4, 12, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X(72)", classes=["center", "incident"])
    central_line(model, X_21, X_72, 21, 72, incident=True)
    return promote_point_to_top(model, X_943)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(943) on the given reference triangle."""
    model = create_model('X(943) = ISOGONAL CONJUGATE OF X(942)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00943(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00943.json"))
    write_center_svg(
        model_acute,
        here / "x-00943.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X(967) = ISOGONAL CONJUGATE OF X(966)."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00967(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(967) = ISOGONAL CONJUGATE OF X(966) on reference triangle ABC."""
    X_966 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - 2*a*(b + c) - (b + c)**(2))', ID="X(966)", classes=["center"])
    X_967 = isogonal_conjugate(model, A, B, C, X_966, ID="X(967)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X(42)", classes=["center", "incident"])
    central_line(model, X_3, X_42, 3, 42, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    central_line(model, X_25, X_58, 25, 58, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X(63)", classes=["center", "incident"])
    central_line(model, X_37, X_63, 37, 63, incident=True)
    return promote_point_to_top(model, X_967)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(967) on the given reference triangle."""
    model = create_model('X(967) = ISOGONAL CONJUGATE OF X(966)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00967(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00967.json"))
    write_center_svg(
        model_acute,
        here / "x-00967.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

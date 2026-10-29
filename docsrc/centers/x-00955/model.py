"""GEOMETOR construction model for X(955) = ISOGONAL CONJUGATE OF X(954)."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00955(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(955) = ISOGONAL CONJUGATE OF X(954) on reference triangle ABC."""
    X_954 = eval_trilinear_point(model, A, B, C, 'a**(5) + (b + c)*(2*a**(2)*(b**(2) + c**(2) - a**(2) + b*c) - (b - c)**(2)*(2*b*c + a*b + a*c))', ID="X(954)", classes=["center"])
    X_955 = isogonal_conjugate(model, A, B, C, X_954, ID="X(955)", classes=["selected", "target"])
    X_278 = eval_trilinear_point(model, A, B, C, 'sec(A)*tan(A/2)', ID="X(278)", classes=["center", "incident"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X(354)", classes=["center", "incident"])
    central_line(model, X_278, X_354, 278, 354, incident=True)
    X_279 = eval_barycentric_point(model, A, B, C, '(a + b - c)**(2)*(a - b + c)**(2)', ID="X(279)", classes=["center", "incident"])
    X_942 = eval_trilinear_point(model, A, B, C, '2*a*b*c + (b + c)*(a - b + c)*(a + b -c)', ID="X(942)", classes=["center", "incident"])
    central_line(model, X_279, X_942, 279, 942, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_991 = eval_trilinear_point(model, A, B, C, 'a*(a**(3)*(b + c) - a**(2)*(b**(2) - b*c + c**(2)) - a*(b + c)*(b**(2) + c**(2)) + (b - c)*(b**(3) - c**(3)))', ID="X(991)", classes=["center", "incident"])
    central_line(model, X_57, X_991, 57, 991, incident=True)
    return promote_point_to_top(model, X_955)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(955) on the given reference triangle."""
    model = create_model('X(955) = ISOGONAL CONJUGATE OF X(954)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00955(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00955.json"))
    write_center_svg(
        model_acute,
        here / "x-00955.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

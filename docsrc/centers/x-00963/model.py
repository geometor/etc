"""GEOMETOR construction model for X(963) = ISOGONAL CONJUGATE OF X(962)."""

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


def construct_x_00963(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(963) = ISOGONAL CONJUGATE OF X(962) on reference triangle ABC."""
    X_962 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) + 2*a**(3)*(b + c) - 4*a**(2)*b*c - (b + c)*(b - c)**(2)*(2*a + b + c))', ID="X(962)", classes=["center"])
    X_963 = isogonal_conjugate(model, A, B, C, X_962, ID="X(963)", classes=["selected", "target"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    central_line(model, X_33, X_56, 33, 56, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_200 = eval_trilinear_point(model, A, B, C, '(cot(A/2))**(2)', ID="X(200)", classes=["center", "incident"])
    central_line(model, X_3, X_200, 3, 200, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center", "incident"])
    X_220 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)**(2)', ID="X(220)", classes=["center", "incident"])
    central_line(model, X_48, X_220, 48, 220, incident=True)
    return promote_point_to_top(model, X_963)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(963) on the given reference triangle."""
    model = create_model('X(963) = ISOGONAL CONJUGATE OF X(962)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00963(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00963.json"))
    write_center_svg(
        model_acute,
        here / "x-00963.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

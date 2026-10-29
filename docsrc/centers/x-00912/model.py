"""GEOMETOR construction model for X(912) = X(104)-CEVA CONJUGATE OF X(3)."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00912(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(912) = X(104)-CEVA CONJUGATE OF X(3) on reference triangle ABC."""
    X_912 = eval_trilinear_point(model, A, B, C, '(a**(2) - b**(2) - c**(2))*(a**(3)*(b + c) - a**(2)*(b**(2) + c**(2)) - a*(b - c)**(2)*(b + c) + (b**(2) - c**(2))**(2))', ID="X(912)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X(63)", classes=["center", "incident"])
    central_line(model, X_3, X_63, 3, 63, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_90 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A))', ID="X(90)", classes=["center", "incident"])
    central_line(model, X_1, X_90, 1, 90, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center", "incident"])
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X(68)", classes=["center", "incident"])
    central_line(model, X_65, X_68, 65, 68, incident=True)
    return promote_point_to_top(model, X_912)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(912) on the given reference triangle."""
    model = create_model('X(912) = X(104)-CEVA CONJUGATE OF X(3)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00912(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00912.json"))
    write_center_svg(
        model_acute,
        here / "x-00912.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X(245) = X(1)-LINE CONJUGATE OF X(110)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00245(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(245) = X(1)-LINE CONJUGATE OF X(110) on reference triangle ABC."""
    X_245 = eval_trilinear_point(model, A, B, C, '(csc(C - A))**(2) + csc(C - B)*(csc(C - A) -csc(B - A)) + (csc(A - B))**(2)', ID="X(245)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X(60)", classes=["center", "incident"])
    central_line(model, X_1, X_60, 1, 60, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X(125)", classes=["center", "incident"])
    central_line(model, X_115, X_125, 115, 125, incident=True)
    return promote_point_to_top(model, X_245)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(245) on the given reference triangle."""
    model = create_model('X(245) = X(1)-LINE CONJUGATE OF X(110)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00245(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00245.json"))
    write_center_svg(
        model_acute,
        here / "x-00245.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

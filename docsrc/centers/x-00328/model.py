"""GEOMETOR construction model for X(328) = ISOTOMIC CONJUGATE OF X(186)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00328(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(328) = ISOTOMIC CONJUGATE OF X(186) on reference triangle ABC."""
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X(186)", classes=["center"])
    X_328 = isotomic_conjugate(model, A, B, C, X_186, ID="X(328)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X(94)", classes=["center", "incident"])
    central_line(model, X_2, X_94, 2, 94, incident=True)
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X(95)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_95, X_99, 95, 99, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_265 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*csc(3*A)', ID="X(265)", classes=["center", "incident"])
    central_line(model, X_69, X_265, 69, 265, incident=True)
    return promote_point_to_top(model, X_328)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(328) on the given reference triangle."""
    model = create_model('X(328) = ISOTOMIC CONJUGATE OF X(186)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00328(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00328.json"))
    write_center_svg(
        model_acute,
        here / "x-00328.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

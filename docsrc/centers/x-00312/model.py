"""GEOMETOR construction model for X(312) = ISOTOMIC CONJUGATE OF X(57)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00312(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(312) = ISOTOMIC CONJUGATE OF X(57) on reference triangle ABC."""
    X_312 = eval_trilinear_point(model, A, B, C, '(b + c - a)*b**(2)*c**(2)', ID="X(312)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    central_line(model, X_2, X_37, 2, 37, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    central_line(model, X_29, X_33, 29, 33, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X(85)", classes=["center", "incident"])
    central_line(model, X_76, X_85, 76, 85, incident=True)
    return promote_point_to_top(model, X_312)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(312) on the given reference triangle."""
    model = create_model('X(312) = ISOTOMIC CONJUGATE OF X(57)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00312(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00312.json"))
    write_center_svg(
        model_acute,
        here / "x-00312.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

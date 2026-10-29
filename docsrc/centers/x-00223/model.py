"""GEOMETOR construction model for X(223) = X(2)-CEVA CONJUGATE OF X(57)."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00223(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(223) = X(2)-CEVA CONJUGATE OF X(57) on reference triangle ABC."""
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X(223)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    central_line(model, X_6, X_57, 6, 57, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X(77)", classes=["center", "incident"])
    central_line(model, X_2, X_77, 2, 77, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    X_221 = eval_trilinear_point(model, A, B, C, '(1 - cos(A))*(1 + cos(A) - cos(B) - cos(C))', ID="X(221)", classes=["center", "incident"])
    central_line(model, X_40, X_221, 40, 221, incident=True)
    return promote_point_to_top(model, X_223)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(223) on the given reference triangle."""
    model = create_model('X(223) = X(2)-CEVA CONJUGATE OF X(57)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00223(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00223.json"))
    write_center_svg(
        model_acute,
        here / "x-00223.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

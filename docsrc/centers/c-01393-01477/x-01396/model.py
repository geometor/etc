"""GEOMETOR construction model for X_1396 = X_27-BETH CONJUGATE OF X_27."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01396(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1396 = X_27-BETH CONJUGATE OF X_27 on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    central_line(model, X_7, X_27, 7, 27)
    central_line(model, X_28, X_34, 28, 34)
    X_1396 = intersect_lines(model, X_7, X_27, X_28, X_34, ID="X_1396", classes=["selected", "target"])
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_223", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    central_line(model, X_223, X_284, 223, 284, incident=True)
    return promote_point_to_top(model, X_1396)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1396 on the given reference triangle."""
    model = create_model('X_1396 = X_27-BETH CONJUGATE OF X_27')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01396(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01396.json"))
    write_center_svg(
        model_acute,
        here / "x-01396.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

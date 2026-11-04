"""GEOMETOR construction model for X_1047 = X_73-CEVA CONJUGATE OF X_1."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01047(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1047 = X_73-CEVA CONJUGATE OF X_1 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    central_line(model, X_1, X_29, 1, 29)
    central_line(model, X_43, X_46, 43, 46)
    X_1047 = intersect_lines(model, X_1, X_29, X_43, X_46, ID="X_1047", classes=["selected", "target"])
    return promote_point_to_top(model, X_1047)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1047 on the given reference triangle."""
    model = create_model('X_1047 = X_73-CEVA CONJUGATE OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01047(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01047.json"))
    write_center_svg(
        model_acute,
        here / "x-01047.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

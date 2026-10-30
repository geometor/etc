"""GEOMETOR construction model for X(208) = X(4)-CEVA CONJUGATE OF X(34)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00208(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(208) = X(4)-CEVA CONJUGATE OF X(34) on reference triangle ABC."""
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center"])
    central_line(model, X_25, X_34, 25, 34)
    central_line(model, X_4, X_57, 4, 57)
    X_208 = intersect_lines(model, X_25, X_34, X_4, X_57, ID="X(208)", classes=["selected", "target"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X(64)", classes=["center", "incident"])
    central_line(model, X_33, X_64, 33, 64, incident=True)
    return promote_point_to_top(model, X_208)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(208) on the given reference triangle."""
    model = create_model('X(208) = X(4)-CEVA CONJUGATE OF X(34)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00208(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00208.json"))
    write_center_svg(
        model_acute,
        here / "x-00208.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

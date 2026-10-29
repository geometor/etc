"""GEOMETOR construction model for X(728) = INTERSECTION OF LINES X(8)X(9) AND X(57)X(345)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00728(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(728) = INTERSECTION OF LINES X(8)X(9) AND X(57)X(345) on reference triangle ABC."""
    X_728 = eval_trilinear_point(model, A, B, C, '(b + c - a)**(3)', ID="X(728)", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    central_line(model, X_8, X_9, 8, 9, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_345 = eval_trilinear_point(model, A, B, C, '(csc(A))/(1 - sec(A))', ID="X(345)", classes=["center", "incident"])
    central_line(model, X_57, X_345, 57, 345, incident=True)
    X_200 = eval_trilinear_point(model, A, B, C, '(cot(A/2))**(2)', ID="X(200)", classes=["center", "incident"])
    X_220 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)**(2)', ID="X(220)", classes=["center", "incident"])
    central_line(model, X_200, X_220, 200, 220, incident=True)
    return promote_point_to_top(model, X_728)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(728) on the given reference triangle."""
    model = create_model('X(728) = INTERSECTION OF LINES X(8)X(9) AND X(57)X(345)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00728(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00728.json"))
    write_center_svg(
        model_acute,
        here / "x-00728.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

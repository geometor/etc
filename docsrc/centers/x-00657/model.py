"""GEOMETOR construction model for X(657) = CROSSDIFFERENCE OF X(1) AND X(7)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00657(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(657) = CROSSDIFFERENCE OF X(1) AND X(7) on reference triangle ABC."""
    X_657 = eval_trilinear_point(model, A, B, C, '(1 + cos(A))*(cos(B) - cos(C))', ID="X(657)", classes=["selected", "target"])
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X(59)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_59, X_101, 59, 101, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X(522)", classes=["center", "incident"])
    central_line(model, X_9, X_522, 9, 522, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    return promote_point_to_top(model, X_657)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(657) on the given reference triangle."""
    model = create_model('X(657) = CROSSDIFFERENCE OF X(1) AND X(7)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00657(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00657.json"))
    write_center_svg(
        model_acute,
        here / "x-00657.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X(242) = X(4)-LINE CONJUGATE OF X(71)."""

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
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00242(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(242) = X(4)-LINE CONJUGATE OF X(71) on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center"])
    central_line(model, X_4, X_9, 4, 9)
    central_line(model, X_25, X_92, 25, 92)
    X_242 = intersect_lines(model, X_4, X_9, X_25, X_92, ID="X(242)", classes=["selected", "target"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center", "incident"])
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X(87)", classes=["center", "incident"])
    central_line(model, X_34, X_87, 34, 87, incident=True)
    return promote_point_to_top(model, X_242)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(242) on the given reference triangle."""
    model = create_model('X(242) = X(4)-LINE CONJUGATE OF X(71)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00242(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00242.json"))
    write_center_svg(
        model_acute,
        here / "x-00242.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

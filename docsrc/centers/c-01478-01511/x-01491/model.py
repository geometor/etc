"""GEOMETOR construction model for X_1491 = CROSSDIFFERENCE OF X_1 AND X_32."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01491(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1491 = CROSSDIFFERENCE OF X_1 AND X_32 on reference triangle ABC."""
    X_659 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c)*(b - c)', ID="X_659", classes=["center"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center"])
    X_1491 = reflection_in_point(model, X_659, X_650, ID="X_1491", classes=["selected", "target"], guide=False)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_10, X_514, 10, 514, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_325, X_523, 325, 523, incident=True)
    return promote_point_to_top(model, X_1491)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1491 on the given reference triangle."""
    model = create_model('X_1491 = CROSSDIFFERENCE OF X_1 AND X_32')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01491(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01491.json"))
    write_center_svg(
        model_acute,
        here / "x-01491.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

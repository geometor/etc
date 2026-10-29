"""GEOMETOR construction model for X(926) = CROSSDIFFERENCE OF X(6) AND X(7)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00926(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(926) = CROSSDIFFERENCE OF X(6) AND X(7) on reference triangle ABC."""
    X_926 = eval_trilinear_point(model, A, B, C, 'a*(a - b - c)*(b - c)*(a*b + a*c - b**(2) - c**(2))', ID="X(926)", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    X_654 = eval_trilinear_point(model, A, B, C, 'cos(A - B) - cos(C - A)', ID="X(654)", classes=["center", "incident"])
    central_line(model, X_55, X_654, 55, 654, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    X_692 = eval_trilinear_point(model, A, B, C, 'a**(2)/(b - c)', ID="X(692)", classes=["center", "incident"])
    central_line(model, X_101, X_692, 101, 692, incident=True)
    return promote_point_to_top(model, X_926)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(926) on the given reference triangle."""
    model = create_model('X(926) = CROSSDIFFERENCE OF X(6) AND X(7)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00926(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00926.json"))
    write_center_svg(
        model_acute,
        here / "x-00926.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

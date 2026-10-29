"""GEOMETOR construction model for X(118) = MIDPOINT OF X(4) AND X(101)."""

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
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00118(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(118) = MIDPOINT OF X(4) AND X(101) on reference triangle ABC."""
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X(116)", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_118 = reflection_in_point(model, X_116, X_5, ID="X(118)", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X(103)", classes=["center", "incident"])
    central_line(model, X_2, X_103, 2, 103, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_4, X_101, 4, 101, incident=True)
    central_line(model, X_5, X_116, 5, 116, incident=True)
    return promote_point_to_top(model, X_118)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(118) on the given reference triangle."""
    model = create_model('X(118) = MIDPOINT OF X(4) AND X(101)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00118(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00118.json"))
    write_center_svg(
        model_acute,
        here / "x-00118.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

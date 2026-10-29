"""GEOMETOR construction model for X(120) = X(105)-OF-MEDIAL-TRIANGLE."""

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
    feuerbach_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00120(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(120) = X(105)-OF-MEDIAL-TRIANGLE on reference triangle ABC."""
    X_120 = eval_trilinear_point(model, A, B, C, 'b*c*(2*a*b*c - (b + c)*(a**(2) + (b - c)**(2)))*(b**(2) + c**(2) - a*b -a*c)', ID="X(120)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center", "incident"])
    central_line(model, X_2, X_11, 2, 11, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X(85)", classes=["center", "incident"])
    central_line(model, X_12, X_85, 12, 85, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X(116)", classes=["center", "incident"])
    central_line(model, X_10, X_116, 10, 116, incident=True)
    return promote_point_to_top(model, X_120)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(120) on the given reference triangle."""
    model = create_model('X(120) = X(105)-OF-MEDIAL-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00120(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00120.json"))
    write_center_svg(
        model_acute,
        here / "x-00120.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

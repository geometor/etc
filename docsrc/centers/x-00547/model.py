"""GEOMETOR construction model for X(547) = MIDPOINT OF X(2) AND X(5)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00547(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(547) = MIDPOINT OF X(2) AND X(5) on reference triangle ABC."""
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X(140)", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_547 = reflection_in_point(model, X_140, X_2, ID="X(547)", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_551 = eval_trilinear_point(model, A, B, C, '(4*a + b + c)/a', ID="X(551)", classes=["center", "incident"])
    X_952 = eval_trilinear_point(model, A, B, C, 'b*c*(2*a**(4) - 2*a**(3)*(b + c) - a**(2)*(b**(2) - 4*b*c + c**(2)) + (2*a - b - c)*(b - c)*(b**(2) - c**(2)))', ID="X(952)", classes=["center", "incident"])
    central_line(model, X_551, X_952, 551, 952, incident=True)
    return promote_point_to_top(model, X_547)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(547) on the given reference triangle."""
    model = create_model('X(547) = MIDPOINT OF X(2) AND X(5)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00547(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00547.json"))
    write_center_svg(
        model_acute,
        here / "x-00547.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

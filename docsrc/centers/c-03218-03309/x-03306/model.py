"""GEOMETOR construction model for X_3306 = INTERSECTION OF LINES X_1X_88 AND X_2X_7."""

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
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03306(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3306 = INTERSECTION OF LINES X_1X_88 AND X_2X_7 on reference triangle ABC."""
    X_3306 = eval_trilinear_point(model, A, B, C, '(2 - cos(A))*csc(A)', ID="X_3306", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    central_line(model, X_1, X_88, 1, 88, incident=True)
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    X_658 = eval_trilinear_point(model, A, B, C, '1/((1 + cos(A))*(cos(B) - cos(C)))', ID="X_658", classes=["center", "incident"])
    central_line(model, X_85, X_658, 85, 658, incident=True)
    return promote_point_to_top(model, X_3306)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3306 on the given reference triangle."""
    model = create_model('X_3306 = INTERSECTION OF LINES X_1X_88 AND X_2X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03306(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03306.json"))
    write_center_svg(
        model_acute,
        here / "x-03306.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

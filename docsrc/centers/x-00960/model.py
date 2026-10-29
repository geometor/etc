"""GEOMETOR construction model for X(960) = INTERSECTION OF LINES X(1)X(6) AND X(5)X(10)."""

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
    incenter_of,
    midpoint,
    nine_point_center_of,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00960(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(960) = INTERSECTION OF LINES X(1)X(6) AND X(5)X(10) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X(72)", classes=["center"])
    X_960 = midpoint(model, X_1, X_72, ID="X(960)", classes=["selected", "target"], guide=False)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    central_line(model, X_5, X_10, 5, 10, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center", "incident"])
    central_line(model, X_2, X_65, 2, 65, incident=True)
    return promote_point_to_top(model, X_960)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(960) on the given reference triangle."""
    model = create_model('X(960) = INTERSECTION OF LINES X(1)X(6) AND X(5)X(10)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00960(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00960.json"))
    write_center_svg(
        model_acute,
        here / "x-00960.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

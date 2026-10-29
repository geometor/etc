"""GEOMETOR construction model for X(117) = MIDPOINT OF X(4) AND X(109)."""

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
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00117(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(117) = MIDPOINT OF X(4) AND X(109) on reference triangle ABC."""
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X(102)", classes=["center"])
    central_line(model, X_11, X_65, 11, 65)
    central_line(model, X_2, X_102, 2, 102)
    X_117 = intersect_lines(model, X_11, X_65, X_2, X_102, ID="X(117)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    central_line(model, X_4, X_109, 4, 109, incident=True)
    return promote_point_to_top(model, X_117)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(117) on the given reference triangle."""
    model = create_model('X(117) = MIDPOINT OF X(4) AND X(109)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00117(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00117.json"))
    write_center_svg(
        model_acute,
        here / "x-00117.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

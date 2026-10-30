"""GEOMETOR construction model for X(976) = INTERSECTION OF LINES X(1)X(2) AND X(3)X(38)."""

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
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00976(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(976) = INTERSECTION OF LINES X(1)X(2) AND X(3)X(38) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X(38)", classes=["center"])
    central_line(model, X_1, X_2, 1, 2)
    central_line(model, X_3, X_38, 3, 38)
    X_976 = intersect_lines(model, X_1, X_2, X_3, X_38, ID="X(976)", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["center", "incident"])
    central_line(model, X_37, X_41, 37, 41, incident=True)
    return promote_point_to_top(model, X_976)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(976) on the given reference triangle."""
    model = create_model('X(976) = INTERSECTION OF LINES X(1)X(2) AND X(3)X(38)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00976(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00976.json"))
    write_center_svg(
        model_acute,
        here / "x-00976.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

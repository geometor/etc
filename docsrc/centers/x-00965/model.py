"""GEOMETOR construction model for X(965) = INTERSECTION OF LINES X(2)X(6) AND X(3)X(9)."""

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
    intersect_lines,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00965(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(965) = INTERSECTION OF LINES X(2)X(6) AND X(3)X(9) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    central_line(model, X_2, X_6, 2, 6)
    central_line(model, X_3, X_9, 3, 9)
    X_965 = intersect_lines(model, X_2, X_6, X_3, X_9, ID="X(965)", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X(78)", classes=["center", "incident"])
    central_line(model, X_37, X_78, 37, 78, incident=True)
    return promote_point_to_top(model, X_965)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(965) on the given reference triangle."""
    model = create_model('X(965) = INTERSECTION OF LINES X(2)X(6) AND X(3)X(9)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00965(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00965.json"))
    write_center_svg(
        model_acute,
        here / "x-00965.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

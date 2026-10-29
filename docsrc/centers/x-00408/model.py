"""GEOMETOR construction model for X(408) = EULER LINE INTERCEPT OF LINE X(73)X(228)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00408(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(408) = EULER LINE INTERCEPT OF LINE X(73)X(228) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X(73)", classes=["center"])
    X_228 = eval_trilinear_point(model, A, B, C, '(sin(2*A))*(sin(B) + sin(C))', ID="X(228)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_73, X_228, 73, 228)
    X_408 = intersect_lines(model, X_2, X_3, X_73, X_228, ID="X(408)", classes=["selected", "target"])
    return promote_point_to_top(model, X_408)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(408) on the given reference triangle."""
    model = create_model('X(408) = EULER LINE INTERCEPT OF LINE X(73)X(228)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00408(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00408.json"))
    write_center_svg(
        model_acute,
        here / "x-00408.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_1817 = INVERSE MIMOSA TRANSFORM OF X_1249."""

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


def construct_x_01817(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1817 = INVERSE MIMOSA TRANSFORM OF X_1249 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_57, X_77, 57, 77)
    X_1817 = intersect_lines(model, X_2, X_3, X_57, X_77, ID="X_1817", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_306 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2))*(b + c)*cos(A)', ID="X_306", classes=["center", "incident"])
    central_line(model, X_100, X_306, 100, 306, incident=True)
    return promote_point_to_top(model, X_1817)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1817 on the given reference triangle."""
    model = create_model('X_1817 = INVERSE MIMOSA TRANSFORM OF X_1249')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01817(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01817.json"))
    write_center_svg(
        model_acute,
        here / "x-01817.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

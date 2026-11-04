"""GEOMETOR construction model for X_2004 = ORTHOCORRESPONDENT OF X_61."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02004(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2004 = ORTHOCORRESPONDENT OF X_61 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center"])
    X_61 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /6)', ID="X_61", classes=["center"])
    central_line(model, X_2, X_13, 2, 13)
    central_line(model, X_51, X_61, 51, 61)
    X_2004 = intersect_lines(model, X_2, X_13, X_51, X_61, ID="X_2004", classes=["selected", "target"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_2005 = point_from_barycentrics(model, A, B, C, 0.35631767, 0.24069977, 0.40298257, ID="X_2005", classes=["center", "incident"])
    central_line(model, X_32, X_2005, 32, 2005, incident=True)
    return promote_point_to_top(model, X_2004)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2004 on the given reference triangle."""
    model = create_model('X_2004 = ORTHOCORRESPONDENT OF X_61')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02004(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02004.json"))
    write_center_svg(
        model_acute,
        here / "x-02004.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

"""GEOMETOR construction model for X_2073 = INVERSE-IN-CIRCUMCIRCLE OF X_27."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02073(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2073 = INVERSE-IN-CIRCUMCIRCLE OF X_27 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center"])
    X_270 = eval_trilinear_point(model, A, B, C, '(sec(A))/(1 + cos(B - C))', ID="X_270", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_35, X_270, 35, 270)
    X_2073 = intersect_lines(model, X_2, X_3, X_35, X_270, ID="X_2073", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_916 = point_from_barycentrics(model, A, B, C, 0.80066716, -0.26177284, -0.53889432, ID="X_916", classes=["center", "incident"])
    central_line(model, X_110, X_916, 110, 916, incident=True)
    return promote_point_to_top(model, X_2073)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2073 on the given reference triangle."""
    model = create_model('X_2073 = INVERSE-IN-CIRCUMCIRCLE OF X_27')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02073(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02073.json"))
    write_center_svg(
        model_acute,
        here / "x-02073.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

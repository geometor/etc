"""GEOMETOR construction model for X_2002 = ORTHOCORRESPONDENT OF X_33."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02002(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2002 = ORTHOCORRESPONDENT OF X_33 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center"])
    central_line(model, X_2, X_7, 2, 7)
    central_line(model, X_19, X_77, 19, 77)
    X_2002 = intersect_lines(model, X_2, X_7, X_19, X_77, ID="X_2002", classes=["selected", "target"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    X_653 = eval_trilinear_point(model, A, B, C, '1/(sec(B) - sec(C))', ID="X_653", classes=["center", "incident"])
    central_line(model, X_85, X_653, 85, 653, incident=True)
    return promote_point_to_top(model, X_2002)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2002 on the given reference triangle."""
    model = create_model('X_2002 = ORTHOCORRESPONDENT OF X_33')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02002(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02002.json"))
    write_center_svg(
        model_acute,
        here / "x-02002.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

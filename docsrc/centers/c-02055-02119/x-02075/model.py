"""GEOMETOR construction model for X_2075 = INVERSE-IN-CIRCUMCIRCLE OF X_29."""

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


def construct_x_02075(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2075 = INVERSE-IN-CIRCUMCIRCLE OF X_29 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center"])
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X_162", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_36, X_162, 36, 162)
    X_2075 = intersect_lines(model, X_2, X_3, X_36, X_162, ID="X_2075", classes=["selected", "target"])
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X_250", classes=["center", "incident"])
    X_1101 = eval_trilinear_point(model, A, B, C, '((csc(B - C))**(2))', ID="X_1101", classes=["center", "incident"])
    central_line(model, X_250, X_1101, 250, 1101, incident=True)
    return promote_point_to_top(model, X_2075)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2075 on the given reference triangle."""
    model = create_model('X_2075 = INVERSE-IN-CIRCUMCIRCLE OF X_29')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02075(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02075.json"))
    write_center_svg(
        model_acute,
        here / "x-02075.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

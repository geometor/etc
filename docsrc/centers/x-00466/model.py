"""GEOMETOR construction model for X(466) = EULER LINE INTERCEPT OF LINE X(216)X(396)."""

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


def construct_x_00466(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(466) = EULER LINE INTERCEPT OF LINE X(216)X(396) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X(216)", classes=["center"])
    X_396 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 2*cos(A - pi /3)', ID="X(396)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_216, X_396, 216, 396)
    X_466 = intersect_lines(model, X_2, X_3, X_216, X_396, ID="X(466)", classes=["selected", "target"])
    X_395 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 2*cos(A + pi /3)', ID="X(395)", classes=["center", "incident"])
    X_577 = eval_trilinear_point(model, A, B, C, 'cos(A)*(tan(A) + tan(B) + tan(C)) - sin(A)', ID="X(577)", classes=["center", "incident"])
    central_line(model, X_395, X_577, 395, 577, incident=True)
    return promote_point_to_top(model, X_466)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(466) on the given reference triangle."""
    model = create_model('X(466) = EULER LINE INTERCEPT OF LINE X(216)X(396)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00466(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00466.json"))
    write_center_svg(
        model_acute,
        here / "x-00466.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

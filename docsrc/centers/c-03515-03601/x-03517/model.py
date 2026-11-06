"""GEOMETOR construction model for X_3517 = EULER LINE INTERCEPT OF LINE X_154X_389."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03517(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3517 = EULER LINE INTERCEPT OF LINE X_154X_389 on reference triangle ABC."""
    X_3517 = eval_trilinear_point(model, A, B, C, '(3*cos(A) - 2*sec(A))', ID="X_3517", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_154 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(B)*cos(C))*a**(2)', ID="X_154", classes=["center", "incident"])
    X_389 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(2*A)*cos(B - C)', ID="X_389", classes=["center", "incident"])
    central_line(model, X_154, X_389, 154, 389, incident=True)
    X_231 = eval_trilinear_point(model, A, B, C, '(cos(B))*(4*(sin(C))**(2) - 1)*(cos(A)*sin(B) - sin(A)*cos(B)) - (cos(C))*(4*(sin(B))**(2) - 1)*(cos(C)*sin(A) - sin(C)*cos(A))', ID="X_231", classes=["center", "incident"])
    X_1609 = eval_trilinear_point(model, A, B, C, 'a*((cos(B))**(2) + (cos(C))**(2) - (cos(A))**(2))', ID="X_1609", classes=["center", "incident"])
    central_line(model, X_231, X_1609, 231, 1609, incident=True)
    return promote_point_to_top(model, X_3517)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3517 on the given reference triangle."""
    model = create_model('X_3517 = EULER LINE INTERCEPT OF LINE X_154X_389')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03517(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03517.json"))
    write_center_svg(
        model_acute,
        here / "x-03517.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

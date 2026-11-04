"""GEOMETOR construction model for X_2074 = INVERSE-IN-CIRCUMCIRCLE OF X_28."""

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
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02074(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2074 = INVERSE-IN-CIRCUMCIRCLE OF X_28 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center"])
    X_912 = eval_trilinear_point(model, A, B, C, '(a**(2) - b**(2) - c**(2))*(a**(3)*(b + c) - a**(2)*(b**(2) + c**(2)) - a*(b - c)**(2)*(b + c) + (b**(2) - c**(2))**(2))', ID="X_912", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_110, X_912, 110, 912)
    X_2074 = intersect_lines(model, X_2, X_3, X_110, X_912, ID="X_2074", classes=["selected", "target"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    X_935 = eval_barycentric_point(model, A, B, C, '1/((b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2)))', ID="X_935", classes=["center", "incident"])
    central_line(model, X_105, X_935, 105, 935, incident=True)
    return promote_point_to_top(model, X_2074)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2074 on the given reference triangle."""
    model = create_model('X_2074 = INVERSE-IN-CIRCUMCIRCLE OF X_28')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02074(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02074.json"))
    write_center_svg(
        model_acute,
        here / "x-02074.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

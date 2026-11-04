"""GEOMETOR construction model for X_1303 = COLLINGS TRANSFORM OF X_389."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01303(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1303 = COLLINGS TRANSFORM OF X_389 on reference triangle ABC."""
    X_389 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(2*A)*cos(B - C)', ID="X_389", classes=["center"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center"])
    X_1303 = cevapoint(model, A, B, C, X_389, X_512, ID="X_1303", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_130 = eval_trilinear_point(model, A, B, C, '((sin(A))*(sin(2*B) + sin(2*C))*((sin(2*B) - sin(2*C))**(2))*((sin(2*A))**(2) + sin(2*B)*sin(2*C)))', ID="X_130", classes=["center", "incident"])
    central_line(model, X_2, X_130, 2, 130, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_129 = point_from_barycentrics(model, A, B, C, 0.22802261, -0.036048578, 0.80802596, ID="X_129", classes=["center", "incident"])
    central_line(model, X_4, X_129, 4, 129, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center", "incident"])
    central_line(model, X_98, X_185, 98, 185, incident=True)
    return promote_point_to_top(model, X_1303)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1303 on the given reference triangle."""
    model = create_model('X_1303 = COLLINGS TRANSFORM OF X_389')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01303(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01303.json"))
    write_center_svg(
        model_acute,
        here / "x-01303.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

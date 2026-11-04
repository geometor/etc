"""GEOMETOR construction model for X_1889 = ZOSMA TRANSFORM OF X_968."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01889(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1889 = ZOSMA TRANSFORM OF X_968 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1836 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) + 2*cos(B)*cos(C)', ID="X_1836", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_6, X_1836, 6, 1836)
    X_1889 = intersect_lines(model, X_2, X_3, X_6, X_1836, ID="X_1889", classes=["selected", "target"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    X_1824 = eval_trilinear_point(model, A, B, C, '(b + c)*tan(A)', ID="X_1824", classes=["center", "incident"])
    central_line(model, X_518, X_1824, 518, 1824, incident=True)
    return promote_point_to_top(model, X_1889)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1889 on the given reference triangle."""
    model = create_model('X_1889 = ZOSMA TRANSFORM OF X_968')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01889(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01889.json"))
    write_center_svg(
        model_acute,
        here / "x-01889.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

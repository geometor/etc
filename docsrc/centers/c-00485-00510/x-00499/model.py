"""GEOMETOR construction model for X_499 = {X_1,X_2}-HARMONIC CONJUGATE OF X_498."""

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
    feuerbach_point_of,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00499(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_499 = {X_1,X_2}-HARMONIC CONJUGATE OF X_498 on reference triangle ABC."""
    X_499 = eval_trilinear_point(model, A, B, C, '1 - 2*sin(B)*sin(C)', ID="X_499", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_3, X_11, 3, 11, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    central_line(model, X_4, X_36, 4, 36, incident=True)
    return promote_point_to_top(model, X_499)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_499 on the given reference triangle."""
    model = create_model('X_499 = {X_1,X_2}-HARMONIC CONJUGATE OF X_498')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00499(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00499.json"))
    write_center_svg(
        model_acute,
        here / "x-00499.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

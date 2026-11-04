"""GEOMETOR construction model for X_35 = {X_1,X_3}-HARMONIC CONJUGATE OF X_36."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00035(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_35 = {X_1,X_3}-HARMONIC CONJUGATE OF X_36 on reference triangle ABC."""
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_10, X_21, 10, 21, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    central_line(model, X_12, X_30, 12, 30, incident=True)
    return promote_point_to_top(model, X_35)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_35 on the given reference triangle."""
    model = create_model('X_35 = {X_1,X_3}-HARMONIC CONJUGATE OF X_36')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00035(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00035.json"))
    write_center_svg(
        model_acute,
        here / "x-00035.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

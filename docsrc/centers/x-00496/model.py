"""GEOMETOR construction model for X(496) = {X(1),X(5)}-HARMONIC CONJUGATE OF X(495)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00496(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(496) = {X(1),X(5)}-HARMONIC CONJUGATE OF X(495) on reference triangle ABC."""
    X_496 = eval_trilinear_point(model, A, B, C, '2 - cos(B - C)', ID="X(496)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    central_line(model, X_30, X_56, 30, 56, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X(140)", classes=["center", "incident"])
    central_line(model, X_55, X_140, 55, 140, incident=True)
    return promote_point_to_top(model, X_496)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(496) on the given reference triangle."""
    model = create_model('X(496) = {X(1),X(5)}-HARMONIC CONJUGATE OF X(495)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00496(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00496.json"))
    write_center_svg(
        model_acute,
        here / "x-00496.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

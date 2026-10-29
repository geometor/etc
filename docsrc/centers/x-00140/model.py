"""GEOMETOR construction model for X(140) = MIDPOINT OF X(3) AND X(5)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00140(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(140) = MIDPOINT OF X(3) AND X(5) on reference triangle ABC."""
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_140 = complement(model, A, B, C, X_5, ID="X(140)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A + pi /3)', ID="X(15)", classes=["center", "incident"])
    X_18 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /6)', ID="X(18)", classes=["center", "incident"])
    central_line(model, X_15, X_18, 15, 18, incident=True)
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A- pi /3)', ID="X(16)", classes=["center", "incident"])
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /6)', ID="X(17)", classes=["center", "incident"])
    central_line(model, X_16, X_17, 16, 17, incident=True)
    return promote_point_to_top(model, X_140)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(140) on the given reference triangle."""
    model = create_model('X(140) = MIDPOINT OF X(3) AND X(5)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00140(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00140.json"))
    write_center_svg(
        model_acute,
        here / "x-00140.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

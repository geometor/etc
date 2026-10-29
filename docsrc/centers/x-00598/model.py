"""GEOMETOR construction model for X(598) = ISOGONAL CONJUGATE OF X(574)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00598(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(598) = ISOGONAL CONJUGATE OF X(574) on reference triangle ABC."""
    X_574 = eval_trilinear_point(model, A, B, C, 'a*(a**(2) - 2*b**(2) - 2*c**(2))', ID="X(574)", classes=["center"])
    X_598 = isogonal_conjugate(model, A, B, C, X_574, ID="X(598)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    central_line(model, X_2, X_187, 2, 187, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_262 = eval_trilinear_point(model, A, B, C, 'sec(A - omega )', ID="X(262)", classes=["center", "incident"])
    central_line(model, X_30, X_262, 30, 262, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X(381)", classes=["center", "incident"])
    central_line(model, X_98, X_381, 98, 381, incident=True)
    return promote_point_to_top(model, X_598)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(598) on the given reference triangle."""
    model = create_model('X(598) = ISOGONAL CONJUGATE OF X(574)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00598(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00598.json"))
    write_center_svg(
        model_acute,
        here / "x-00598.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

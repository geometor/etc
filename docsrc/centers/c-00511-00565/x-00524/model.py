"""GEOMETOR construction model for X_524 = ISOGONAL CONJUGATE OF X_111."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00524(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_524 = ISOGONAL CONJUGATE OF X_111 on reference triangle ABC."""
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center"])
    X_524 = isogonal_conjugate(model, A, B, C, X_111, ID="X_524", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    X_317 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)*(csc(A))**(2)', ID="X_317", classes=["center", "incident"])
    central_line(model, X_53, X_317, 53, 317, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_524)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_524 on the given reference triangle."""
    model = create_model('X_524 = ISOGONAL CONJUGATE OF X_111')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00524(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00524.json"))
    write_center_svg(
        model_acute,
        here / "x-00524.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

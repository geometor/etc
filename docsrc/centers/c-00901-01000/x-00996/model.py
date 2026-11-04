"""GEOMETOR construction model for X_996 = INTERSECTION OF LINES X_8X_58 AND X_10X_56."""

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
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00996(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_996 = INTERSECTION OF LINES X_8X_58 AND X_10X_56 on reference triangle ABC."""
    X_995 = eval_trilinear_point(model, A, B, C, 'a*(a*b + a*c - b*c + b**(2) + c**(2))', ID="X_995", classes=["center"])
    X_996 = isogonal_conjugate(model, A, B, C, X_995, ID="X_996", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    central_line(model, X_8, X_58, 8, 58, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_10, X_56, 10, 56, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    central_line(model, X_2, X_106, 2, 106, incident=True)
    return promote_point_to_top(model, X_996)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_996 on the given reference triangle."""
    model = create_model('X_996 = INTERSECTION OF LINES X_8X_58 AND X_10X_56')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00996(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00996.json"))
    write_center_svg(
        model_acute,
        here / "x-00996.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

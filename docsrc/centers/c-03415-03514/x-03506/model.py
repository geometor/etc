"""GEOMETOR construction model for X_3506 = INTERSECTION OF LINES X_2X_98 AND X_32X_694."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03506(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3506 = INTERSECTION OF LINES X_2X_98 AND X_32X_694 on reference triangle ABC."""
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X_385", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_3506 = ceva_conjugate(model, A, B, C, X_385, X_32, ID="X_3506", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_2, X_98, 2, 98, incident=True)
    X_694 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) - b**(2)*c**(2))', ID="X_694", classes=["center", "incident"])
    central_line(model, X_32, X_694, 32, 694, incident=True)
    X_648 = eval_trilinear_point(model, A, B, C, '1/(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2)))', ID="X_648", classes=["center", "incident"])
    X_1974 = eval_trilinear_point(model, A, B, C, 'a**(4)*cos(B)*cos(C)', ID="X_1974", classes=["center", "incident"])
    central_line(model, X_648, X_1974, 648, 1974, incident=True)
    return promote_point_to_top(model, X_3506)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3506 on the given reference triangle."""
    model = create_model('X_3506 = INTERSECTION OF LINES X_2X_98 AND X_32X_694')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03506(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03506.json"))
    write_center_svg(
        model_acute,
        here / "x-03506.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

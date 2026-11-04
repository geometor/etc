"""GEOMETOR construction model for X_1585 = POINT CAPH I."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01585(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1585 = POINT CAPH I on reference triangle ABC."""
    X_1585 = eval_trilinear_point(model, A, B, C, '(csc(A) + sec(A))', ID="X_1585", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    X_590 = eval_trilinear_point(model, A, B, C, '(a**(2) + 4*area )/a', ID="X_590", classes=["center", "incident"])
    central_line(model, X_53, X_590, 53, 590, incident=True)
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center", "incident"])
    X_491 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 - csc(A)*sin(B)*sin(C)) + cos(B)*cos(C))', ID="X_491", classes=["center", "incident"])
    central_line(model, X_264, X_491, 264, 491, incident=True)
    return promote_point_to_top(model, X_1585)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1585 on the given reference triangle."""
    model = create_model('X_1585 = POINT CAPH I')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01585(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01585.json"))
    write_center_svg(
        model_acute,
        here / "x-01585.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

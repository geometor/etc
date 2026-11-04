"""GEOMETOR construction model for X_1975 = CROSSSUM OF PU(39)."""

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
    midpoint,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01975(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1975 = CROSSSUM OF PU(39) on reference triangle ABC."""
    X_489 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 - csc(A)*sin(B)*sin(C)) - cos(B)*cos(C))', ID="X_489", classes=["center"])
    X_490 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 + csc(A)*sin(B)*sin(C)) - cos(B)*cos(C))', ID="X_490", classes=["center"])
    X_1975 = midpoint(model, X_489, X_490, ID="X_1975", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_3, X_76, 3, 76, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    central_line(model, X_20, X_64, 20, 64, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center", "incident"])
    central_line(model, X_6, X_194, 6, 194, incident=True)
    return promote_point_to_top(model, X_1975)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1975 on the given reference triangle."""
    model = create_model('X_1975 = CROSSSUM OF PU(39)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01975(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01975.json"))
    write_center_svg(
        model_acute,
        here / "x-01975.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

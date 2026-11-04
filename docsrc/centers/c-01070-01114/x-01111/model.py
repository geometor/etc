"""GEOMETOR construction model for X_1111 = TRILINEAR SQUARE OF X_514."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01111(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1111 = TRILINEAR SQUARE OF X_514 on reference triangle ABC."""
    X_1110 = eval_trilinear_point(model, A, B, C, '((a/(b - c))**(2))', ID="X_1110", classes=["center"])
    X_1111 = isogonal_conjugate(model, A, B, C, X_1110, ID="X_1111", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    central_line(model, X_1, X_85, 1, 85, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_7, X_80, 7, 80, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_334 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(a**(2) - b*c)', ID="X_334", classes=["center", "incident"])
    central_line(model, X_76, X_334, 76, 334, incident=True)
    return promote_point_to_top(model, X_1111)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1111 on the given reference triangle."""
    model = create_model('X_1111 = TRILINEAR SQUARE OF X_514')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01111(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01111.json"))
    write_center_svg(
        model_acute,
        here / "x-01111.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

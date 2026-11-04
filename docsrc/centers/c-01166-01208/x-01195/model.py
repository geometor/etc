"""GEOMETOR construction model for X_1195 = 3rd SARAGOSSA POINT OF X_19."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01195(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1195 = 3rd SARAGOSSA POINT OF X_19 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center"])
    X_1195 = crosspoint(model, A, B, C, X_19, X_284, ID="X_1195", classes=["selected", "target"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    central_line(model, X_41, X_71, 41, 71, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_43, X_165, 43, 165, incident=True)
    X_208 = eval_trilinear_point(model, A, B, C, '((1 - sec(A))*(cos(B) + cos(C) - cos(A) - 1))', ID="X_208", classes=["center", "incident"])
    central_line(model, X_19, X_208, 19, 208, incident=True)
    return promote_point_to_top(model, X_1195)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1195 on the given reference triangle."""
    model = create_model('X_1195 = 3rd SARAGOSSA POINT OF X_19')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01195(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01195.json"))
    write_center_svg(
        model_acute,
        here / "x-01195.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

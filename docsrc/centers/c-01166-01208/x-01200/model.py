"""GEOMETOR construction model for X_1200 = 3rd SARAGOSSA POINT OF X_55."""

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


def construct_x_01200(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1200 = 3rd SARAGOSSA POINT OF X_55 on reference triangle ABC."""
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_1200 = crosspoint(model, A, B, C, X_55, X_57, ID="X_1200", classes=["selected", "target"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_41, X_55, 41, 55, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_43, X_165, 43, 165, incident=True)
    X_279 = eval_trilinear_point(model, A, B, C, 'csc(A)*(tan(A/2))**(2)', ID="X_279", classes=["center", "incident"])
    central_line(model, X_57, X_279, 57, 279, incident=True)
    return promote_point_to_top(model, X_1200)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1200 on the given reference triangle."""
    model = create_model('X_1200 = 3rd SARAGOSSA POINT OF X_55')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01200(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01200.json"))
    write_center_svg(
        model_acute,
        here / "x-01200.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

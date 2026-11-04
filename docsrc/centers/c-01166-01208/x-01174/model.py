"""GEOMETOR construction model for X_1174 = 1st SARAGOSSA POINT OF X_57."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01174(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1174 = 1st SARAGOSSA POINT OF X_57 on reference triangle ABC."""
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center"])
    X_1174 = isogonal_conjugate(model, A, B, C, X_142, ID="X_1174", classes=["selected", "target"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_41, X_57, 41, 57, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_218 = eval_trilinear_point(model, A, B, C, '((cos(A/2))**(2)*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4)))', ID="X_218", classes=["center", "incident"])
    central_line(model, X_55, X_218, 55, 218, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center", "incident"])
    central_line(model, X_101, X_354, 101, 354, incident=True)
    return promote_point_to_top(model, X_1174)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1174 on the given reference triangle."""
    model = create_model('X_1174 = 1st SARAGOSSA POINT OF X_57')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01174(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01174.json"))
    write_center_svg(
        model_acute,
        here / "x-01174.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

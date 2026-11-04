"""GEOMETOR construction model for X_1190 = 2nd SARAGOSSA POINT OF X_55."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01190(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1190 = 2nd SARAGOSSA POINT OF X_55 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    central_line(model, X_6, X_57, 6, 57)
    central_line(model, X_41, X_55, 41, 55)
    X_1190 = intersect_lines(model, X_6, X_57, X_41, X_55, ID="X_1190", classes=["selected", "target"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    X_218 = eval_trilinear_point(model, A, B, C, '((cos(A/2))**(2)*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4)))', ID="X_218", classes=["center", "incident"])
    central_line(model, X_165, X_218, 165, 218, incident=True)
    return promote_point_to_top(model, X_1190)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1190 on the given reference triangle."""
    model = create_model('X_1190 = 2nd SARAGOSSA POINT OF X_55')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01190(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01190.json"))
    write_center_svg(
        model_acute,
        here / "x-01190.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

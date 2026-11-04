"""GEOMETOR construction model for X_1170 = 1st SARAGOSSA POINT OF X_41."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01170(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1170 = 1st SARAGOSSA POINT OF X_41 on reference triangle ABC."""
    X_1170 = eval_trilinear_point(model, A, B, C, '1/((a - b - c)*(a*(b + c) - (b - c)**(2)))', ID="X_1170", classes=["selected", "target"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_41, X_57, 41, 57, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_65, X_105, 65, 105, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_220 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)**(2)', ID="X_220", classes=["center", "incident"])
    central_line(model, X_2, X_220, 2, 220, incident=True)
    return promote_point_to_top(model, X_1170)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1170 on the given reference triangle."""
    model = create_model('X_1170 = 1st SARAGOSSA POINT OF X_41')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01170(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01170.json"))
    write_center_svg(
        model_acute,
        here / "x-01170.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

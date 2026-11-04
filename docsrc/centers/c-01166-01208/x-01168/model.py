"""GEOMETOR construction model for X_1168 = 1st SARAGOSSA POINT OF X_36."""

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


def construct_x_01168(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1168 = 1st SARAGOSSA POINT OF X_36 on reference triangle ABC."""
    X_214 = eval_trilinear_point(model, A, B, C, '(b + c - 2*a)*(b**(2) + c**(2) - a**(2) - b*c)', ID="X_214", classes=["center"])
    X_1168 = isogonal_conjugate(model, A, B, C, X_214, ID="X_1168", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    central_line(model, X_36, X_88, 36, 88, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_44, X_517, 44, 517, incident=True)
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_80, X_519, 80, 519, incident=True)
    return promote_point_to_top(model, X_1168)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1168 on the given reference triangle."""
    model = create_model('X_1168 = 1st SARAGOSSA POINT OF X_36')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01168(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01168.json"))
    write_center_svg(
        model_acute,
        here / "x-01168.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

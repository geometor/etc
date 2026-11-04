"""GEOMETOR construction model for X_2970 = 4th MACBEATH POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02970(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2970 = 4th MACBEATH POINT on reference triangle ABC."""
    X_847 = eval_trilinear_point(model, A, B, C, 'sec(A)*sec(2*A)', ID="X_847", classes=["center"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center"])
    X_2970 = ceva_conjugate(model, A, B, C, X_847, X_523, ID="X_2970", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X_94", classes=["center", "incident"])
    central_line(model, X_4, X_94, 4, 94, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_25, X_98, 25, 98, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_135 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sin(2*B))/(sec(2*C) - sec(2*A)) + (sin(2*C))/(sec(2*A) - sec(2*B)))', ID="X_135", classes=["center", "incident"])
    central_line(model, X_115, X_135, 115, 135, incident=True)
    return promote_point_to_top(model, X_2970)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2970 on the given reference triangle."""
    model = create_model('X_2970 = 4th MACBEATH POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02970(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02970.json"))
    write_center_svg(
        model_acute,
        here / "x-02970.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

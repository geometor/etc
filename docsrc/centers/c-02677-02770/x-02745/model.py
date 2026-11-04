"""GEOMETOR construction model for X_2745 = SR(X_104, X_108)."""

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
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02745(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2745 = SR(X_104, X_108) on reference triangle ABC."""
    X_2720 = point_from_barycentrics(model, A, B, C, -0.17241379, 0.49655172, 0.67586207, ID="X_2720", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2745 = reflection_in_point(model, X_2720, X_3, ID="X_2745", classes=["selected", "target"], guide=False)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center", "incident"])
    central_line(model, X_104, X_521, 104, 521, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_108, X_517, 108, 517, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_1309 = eval_trilinear_point(model, A, B, C, '(csc(2*A))/(4*((sin(B))**(2) - (sin(C))**(2))*cos(B)*cos(C) + (sin(B))**(2)*cos(B) - (sin(C))**(2)*cos(C))', ID="X_1309", classes=["center", "incident"])
    central_line(model, X_8, X_1309, 8, 1309, incident=True)
    return promote_point_to_top(model, X_2745)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2745 on the given reference triangle."""
    model = create_model('X_2745 = SR(X_104, X_108)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02745(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02745.json"))
    write_center_svg(
        model_acute,
        here / "x-02745.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

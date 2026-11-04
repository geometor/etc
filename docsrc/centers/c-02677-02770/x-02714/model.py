"""GEOMETOR construction model for X_2714 = SR(X_99, X_108)."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02714(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2714 = SR(X_99, X_108) on reference triangle ABC."""
    X_2707 = point_from_barycentrics(model, A, B, C, 1.0414086, 0.22924055, -0.27064911, ID="X_2707", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2714 = reflection_in_point(model, X_2707, X_3, ID="X_2714", classes=["selected", "target"], guide=False)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center", "incident"])
    central_line(model, X_99, X_521, 99, 521, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_108, X_512, 108, 512, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_810 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*((cos(B))**(2) - (cos(C))**(2))', ID="X_810", classes=["center", "incident"])
    central_line(model, X_109, X_810, 109, 810, incident=True)
    return promote_point_to_top(model, X_2714)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2714 on the given reference triangle."""
    model = create_model('X_2714 = SR(X_99, X_108)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02714(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02714.json"))
    write_center_svg(
        model_acute,
        here / "x-02714.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

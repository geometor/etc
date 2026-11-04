"""GEOMETOR construction model for X_2708 = SR(X_98, X_109)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02708(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2708 = SR(X_98, X_109) on reference triangle ABC."""
    X_2701 = eval_trilinear_point(model, A, B, C, '(a/((b - c)*(a**(3) + b**(3) + c**(3) - 2*a**(2)*b - 2*a**(2)*c + a*b*c)))', ID="X_2701", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2708 = reflection_in_point(model, X_2701, X_3, ID="X_2708", classes=["selected", "target"], guide=False)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A +  omega  )', ID="X_240", classes=["center", "incident"])
    central_line(model, X_108, X_240, 108, 240, incident=True)
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    X_415 = eval_barycentric_point(model, A, B, C, '(a + b) * (a + c) * (a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2)) * (a**(3) - 2*a**(2)*b + b**(3) - 2*a**(2)*c + a*b*c + c**(3))', ID="X_415", classes=["center", "incident"])
    central_line(model, X_107, X_415, 107, 415, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center", "incident"])
    central_line(model, X_99, X_515, 99, 515, incident=True)
    return promote_point_to_top(model, X_2708)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2708 on the given reference triangle."""
    model = create_model('X_2708 = SR(X_98, X_109)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02708(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02708.json"))
    write_center_svg(
        model_acute,
        here / "x-02708.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

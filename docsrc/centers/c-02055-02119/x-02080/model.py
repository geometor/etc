"""GEOMETOR construction model for X_2080 = INVERSE-IN-CIRCUMCIRCLE OF X_182."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02080(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2080 = INVERSE-IN-CIRCUMCIRCLE OF X_182 on reference triangle ABC."""
    X_2080 = eval_trilinear_point(model, A, B, C, '2*cos(A) - cos(A - 2*omega  )', ID="X_2080", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_30, X_98, 30, 98, incident=True)
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center", "incident"])
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    central_line(model, X_83, X_140, 83, 140, incident=True)
    return promote_point_to_top(model, X_2080)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2080 on the given reference triangle."""
    model = create_model('X_2080 = INVERSE-IN-CIRCUMCIRCLE OF X_182')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02080(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02080.json"))
    write_center_svg(
        model_acute,
        here / "x-02080.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

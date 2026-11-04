"""GEOMETOR construction model for X_2948 = EXCENTRAL-ISOGONAL CONJUGATE OF X_30."""

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
    incenter_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02948(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2948 = EXCENTRAL-ISOGONAL CONJUGATE OF X_30 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center"])
    X_2948 = reflection_in_point(model, X_1, X_110, ID="X_2948", classes=["selected", "target"], guide=False)
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_1, X_60, 1, 60, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_191 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(b*c + c*a + a*b) + b**(3) + c**(3) - a**(3)', ID="X_191", classes=["center", "incident"])
    central_line(model, X_3, X_191, 3, 191, incident=True)
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_74, X_165, 74, 165, incident=True)
    return promote_point_to_top(model, X_2948)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2948 on the given reference triangle."""
    model = create_model('X_2948 = EXCENTRAL-ISOGONAL CONJUGATE OF X_30')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02948(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02948.json"))
    write_center_svg(
        model_acute,
        here / "x-02948.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

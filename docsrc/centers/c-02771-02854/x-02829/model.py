"""GEOMETOR construction model for X_2829 = ISOGONAL CONJUGATE OF X_2745."""

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
    feuerbach_point_of,
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02829(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2829 = ISOGONAL CONJUGATE OF X_2745 on reference triangle ABC."""
    X_2745 = point_from_barycentrics(model, A, B, C, 1.0404693, 0.29511494, -0.33558429, ID="X_2745", classes=["center"])
    X_2829 = isogonal_conjugate(model, A, B, C, X_2745, ID="X_2829", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_4, X_11, 4, 11, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_20, X_100, 20, 100, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_119 = eval_trilinear_point(model, A, B, C, '(csc(A))*(-1 + cos(B) + cos(C))*(sin(2*B) + sin(2*C) + 2*(-1 + cos(A))*(sin(B) + sin(C)))', ID="X_119", classes=["center", "incident"])
    central_line(model, X_3, X_119, 3, 119, incident=True)
    return promote_point_to_top(model, X_2829)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2829 on the given reference triangle."""
    model = create_model('X_2829 = ISOGONAL CONJUGATE OF X_2745')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02829(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02829.json"))
    write_center_svg(
        model_acute,
        here / "x-02829.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )

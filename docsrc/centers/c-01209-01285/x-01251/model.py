"""GEOMETOR construction model for X_1251 = ISOGONAL CONJUGATE OF X_1082."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01251(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1251 = ISOGONAL CONJUGATE OF X_1082 on reference triangle ABC."""
    X_1082 = eval_trilinear_point(model, A, B, C, '(sec(A/2))*sin(A/2 - pi /3)', ID="X_1082", classes=["center"])
    X_1251 = isogonal_conjugate(model, A, B, C, X_1082, ID="X_1251", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A + pi /3)', ID="X_15", classes=["center", "incident"])
    central_line(model, X_1, X_15, 1, 15, incident=True)
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X_13", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_13, X_80, 13, 80, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_199 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) - a**(4) + (b**(2) + c**(2) - a**(2))*(b*c + c*a + a*b)))', ID="X_199", classes=["center", "incident"])
    central_line(model, X_55, X_199, 55, 199, incident=True)
    return promote_point_to_top(model, X_1251)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1251 on the given reference triangle."""
    model = create_model('X_1251 = ISOGONAL CONJUGATE OF X_1082')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01251(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01251.json"))
    write_center_svg(
        model_acute,
        here / "x-01251.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
